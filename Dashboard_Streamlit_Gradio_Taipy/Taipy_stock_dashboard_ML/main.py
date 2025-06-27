# WSL
# https://docs.rapids.ai/install/
# conda create -n rapids-25.06 -c rapidsai -c conda-forge -c nvidia  cudf=25.06 python=3.12 'cuda-version>=12.0,<=12.8'

# Requirements 
#plotly==5.24.1
#scikit-learn==1.5.2
#taipy==4.0.0
#tensorflow==2.18.0
# https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks


import taipy as tp
import taipy.gui.builder as tgb
from taipy.gui import Icon
from taipy import Config
import datetime 
import cudf.pandas
cudf.pandas.install()
import pandas as pd 
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from tensorflow.keras import models
from tensorflow.keras import layers

stock_data = pd.read_csv("data/sp500_stocks.csv")
#print(stock_data.loc[0])

company_data = pd.read_csv("data/sp500_companies.csv")
#print(company_data.loc[0])

country_names = company_data["Country"].unique().tolist()
country_names = [(name, Icon("images/flags/" + name + ".png", name)) for name in country_names]

company_names = company_data[["Symbol", "Shortname"]].sort_values("Shortname").values.tolist() # .values to convert to numpy array
#print(country_names)
#print(company_names)

dates = [
    stock_data["Date"].min(),
    stock_data["Date"].max()
]

country = "United States"
company = ["GOOG"]

lin_pred = 0
knn_pred = 0
rnn_pred = 0

graph_data = None
figure = None

# create page
with tgb.Page() as page: 
    # Center the text
    with tgb.part("text-center"):
        tgb.image("images/icons/logo.png", width="10vw")        # Image width - viewport width
        tgb.text("# S&P 500 Stock Value Over Time", mode="md")
        tgb.date_range("{dates}", label_start="Start Date", label_end="End Date")   # Date Range
        with tgb.layout("20 80"):   # Country, company row
            tgb.selector(label="country", class_name="fullwidth", value="{country}", lov="{country_names}", dropdown=True, value_by_id=True)
            tgb.selector(label="company", class_name="fullwidth", value="{company}", lov="{company_names}", dropdown=True, value_by_id=True, multiple=True)
        tgb.chart(figure="{figure}")
        with tgb.part("text-left"):
            with tgb.layout("4 72 4 4 4 4 4 4"): 
                tgb.image("images/icons/id-card.png", width="3vw")
                tgb.text("{company[-1]} | {company_data['Shortname'][company_data['Symbol'] == company[-1]].values[0]}", mode="md")
                tgb.image("images/icons/lin.png", width="3vw")
                tgb.text("{lin_pred}", mode="md")
                tgb.image("images/icons/knn.png", width="3vw")
                tgb.text("{knn_pred}", mode="md")
                tgb.image("images/icons/rnn.png", width="3vw")
                tgb.text("{rnn_pred}", mode="md")


def build_company_names(country): 
    company_names = company_data[["Symbol", "Shortname"]][
        company_data["Country"] == country
    ].sort_values("Shortname").values.tolist()
    return company_names

def build_graph_data(dates, company):
    #print("---------------------")
    #print(dates, company)

    temp_data = stock_data[["Date", "Adj Close", "Symbol"]][
        #(stock_data["Symbol"] == company) & 
        (stock_data["Date"] > str(dates[0])) &
        (stock_data["Date"] < str(dates[1]))
    ]
    graph_data = pd.DataFrame()
    graph_data["Date"] = temp_data["Date"].unique()

    for i in company:
         graph_data[i] = temp_data["Adj Close"][temp_data["Symbol"] == i].values

    # graph_data = graph_data.rename(columns={"Adj Close": company})

    print(graph_data)

    return graph_data

def display_graph(graph_data): 
    figure = go.Figure()
    symbols = graph_data.columns[1:]

    for i in symbols: 
        figure.add_trace(go.Scatter(
            x=graph_data["Date"],
            y=graph_data[i],
            name=i,
            showlegend=True
        ))

    figure.update_layout(
        xaxis_title="Date",
        yaxis_title="Stock Value"
    )

    return figure

def split_data(stock_data, dates, symbol):
    temp_data = stock_data[
    (stock_data["Symbol"] == symbol) & 
    (stock_data["Date"] > str(dates[0])) &
    (stock_data["Date"] < str(dates[1]))
    ].drop(["Date", "Symbol"], axis=1)

    eval_features = temp_data.values[-1]
    eval_features = eval_features.reshape(1, -1)
    features = temp_data.values[:-1]
    targets = temp_data["Adj Close"].shift(-1).values[:-1]

    #temp_data["Targets"] = targets
    #print(temp_data)

    mean = features.mean(axis=0)
    std = features.std(axis=0)

    features -= mean
    features /= std

    eval_features -= mean
    eval_features /= std

    return features, targets, eval_features

# split_data(stock_data, dates, "GOOG")

def get_lin(dates, company): 
    X, y, eval_X = split_data(stock_data, dates, company[-1])

    lin_model.fit(X, y)
    lin_pred = lin_model.predict(eval_X)

    return round(lin_pred[0],3)

def get_knn(dates, company): 
    X, y, eval_X = split_data(stock_data, dates, company[-1])
    
    knn_model.fit(X, y)
    knn_pred = knn_model.predict(eval_X)

    return round(knn_pred[0],3)

def get_rnn(dates, company): 
    X, y, eval_X = split_data(stock_data, dates, company[-1])

    rnn_model.fit(X, y, batch_size=32, epochs=10, verbose=0)
    rnn_pred = rnn_model.predict(eval_X)

    return round(float(rnn_pred[0][0]),3)

# Scenarios - based on input selection, output selection changes --------------
country_cfg = Config.configure_data_node(id="country")

company_names_cfg = Config.configure_data_node(id="company_names")

dates_cfg = Config.configure_data_node(id="dates")

company_cfg = Config.configure_data_node(id="company")

graph_data_cfg = Config.configure_data_node(id="graph_data")

lin_pred_cfg = Config.configure_data_node(id="lin_pred")

knn_pred_cfg = Config.configure_data_node(id="knn_pred")

rnn_pred_cfg = Config.configure_data_node(id="rnn_pred")

get_lin_cfg = Config.configure_task(
    input = [dates_cfg, company_cfg],
    output = lin_pred_cfg,
    function = get_lin,
    id="get_lin",
    skippable=True
)

get_knn_cfg = Config.configure_task(
    input = [dates_cfg, company_cfg],
    output = knn_pred_cfg,
    function = get_knn,
    id="get_knn",
    skippable=True
)

get_rnn_cfg = Config.configure_task(
    input = [dates_cfg, company_cfg],
    output = rnn_pred_cfg,
    function = get_rnn,
    id="get_rnn",
    skippable=True
)

build_graph_data_cfg = Config.configure_task(
    input = [dates_cfg, company_cfg],
    output = graph_data_cfg,
    function = build_graph_data,
    id="build_graph_data",
    skippable=True
)

build_company_names_cfg = Config.configure_task(
    input = country_cfg,
    output = company_names_cfg,
    function = build_company_names,
    id = "build_company_names",
    skippable=True
)

scenario_cfg = Config.configure_scenario(
    task_configs=[
    build_company_names_cfg, 
    build_graph_data_cfg, 
    get_lin_cfg,
    get_knn_cfg,
    get_rnn_cfg
    ],
    id="scenario")
#============================================================================

def on_init(state): 
    state.scenario.country.write(state.country)
    state.scenario.dates.write(state.dates)
    state.scenario.company.write(state.company)
    state.scenario.submit(wait=True)
    state.graph_data = state.scenario.graph_data.read()
    state.company_names = state.scenario.company_names.read()
    state.lin_pred = state.scenario.lin_pred.read()
    state.knn_pred = state.scenario.knn_pred.read()
    state.rnn_pred = state.scenario.rnn_pred.read()


# Fetch Selection
def on_change(state, name, value):
    if name == "country":
        print(name, "was modified", value)
        #print("-----------------------------")
        #print("state.country", state.country)
        #print("counttry", country)
        #print("----------------------------")
        state.scenario.country.write(state.country)
        state.scenario.submit(wait=True)
        state.company_names = state.scenario.company_names.read()
        #print("-----------------------------")
        #print("state.country", state.country)
        #print("country", country)
        #print("----------------------------")
    if name == "company" or name == "dates":
        print(name, "was modified", value)
        state.scenario.dates.write(state.dates)
        state.scenario.company.write(state.company)
        state.scenario.submit(wait=True)
        state.graph_data = state.scenario.graph_data.read()
        state.lin_pred = state.scenario.lin_pred.read()
        state.knn_pred = state.scenario.knn_pred.read()
        state.rnn_pred = state.scenario.rnn_pred.read()

    if name == "graph_data": 
        state.figure = display_graph(state.graph_data)

def build_RNN(n_features):
    model = models.Sequential()
    model.add(layers.Dense(64, activation = 'relu', input_shape=(n_features, )))
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(1, activation = 'linear'))
    model.compile(optimizer = 'rmsprop', loss = 'mse', metrics = ['mae'])
    return model

if __name__ == "__main__": 
    lin_model = LinearRegression() 
    knn_model = KNeighborsRegressor()
    rnn_model = build_RNN(6)

    tp.Orchestrator().run()
    scenario = tp.create_scenario(scenario_cfg)
    gui = tp.Gui(page)
    gui.run(title = "Data Science Dashboard", use_reloader=True)
