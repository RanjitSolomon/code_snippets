import numpy as np 
import pandas as pd
# 1. Chain Transformations with assign()

## Creating new columns or modifying existing ones is a core part 
## of data transformation. Instead of creating intermediate variables 
## or breaking the process into multiple steps, .assign() method lets 
## you chain transformations.

df = (df.assign(total_sales=lambda x: x['units_sold'] * x['unit_price'])
      .assign(log_sales=lambda x: np.log1p(x['total_sales'])))

## Here, we create a new column total_sales by multiplying units_sold with unit_price, 
## and then create another column log_sales with the log of total sales. 


# 2. Fill Missing Values with a Dict in fillna()

## Handling missing values is one of the first and most frequent data prep tasks. 
## Instead of writing individual fill statements for each column, you can fill multiple columns using fillna().

df.fillna({'price': 0, 'category': 'Unknown'}, inplace=True)

## This approach gives you full control over how each column is filled. For example, you can replace missing 
## prices with 0 and fill missing category labels with a string like “Unknown”.

# 3. Flatten List Columns with explode()

## Many datasets (e.g., JSON, nested CSVs) include columns with list-like data. .explode() function is a tool 
## for flattening those into individual rows while keeping other columns intact.

df.explode('tags')

## This function transforms each item in the list into its own row while keeping the rest of the data intact. It’s 
# useful for handling one-to-many relationships where each row can relate to multiple tags.

# 4. Readable Filtering with query()

## Filtering data with logical conditions can get messy, especially when chaining multiple conditions. .query() 
## offers a much more readable way to filter rows using SQL-like expressions.

df.query('region == "West" and sales > 5000')

## This makes it easy to apply filters without deeply nested brackets. You can write complex conditions 
## that are still easy to understand at a glance.

# 5. Named Aggregations with groupby().agg()

## Summarizing your data is a crucial part of the analysis process. Instead of using default aggregation names, 
## you can assign custom names to each metric using named aggregations in the .agg() method.

df.groupby('category').agg(
    avg_sales=('sales', 'mean'),
    max_discount=('discount', 'max')
)

## This way, your resulting DataFrame has meaningful column names like avg_sales 
## and max_discount instead of just sales or discount.

# 6. Date Parsing with pd.to_datetime()

## Dealing with messy date formats? Use pd.to_datetime() to convert strings to proper date objects. 
## This makes it easy to work with date-based operations later.

df['date'] = pd.to_datetime(df['date'], errors='coerce')

## Setting errors='coerce' tells Pandas to turn bad date strings into NaT (Not a Time), which avoids errors during parsing

# 7. Modular Workflows with pipe()

## As data transformations become increasingly complex, your code can become more difficult to follow. .pipe() 
## helps you build modular, reusable pipelines by chaining custom functions.

def clean_prices(df):
    return df.assign(price=lambda x: x['price'].fillna(0))

def add_sales_tax(df, rate=0.1):
    return df.assign(final_price=lambda x: x['price'] * (1 + rate))

# Example usage
df = (
    df
    .pipe(clean_prices)
    .pipe(add_sales_tax, rate=0.08)
)

## By using this function, you pass the DataFrame through a sequence of custom functions. 
## Each function takes the DataFrame as its first argument and returns a modified version.

# With just a few Pandas tricks, you can drastically improve your data preparation speed and clarity. 
# Here’s a quick recap:

# Trick             # Purpose
# assign()          Chain column creation and transforations
# fillno(dict)      Fill missing values by column
# explode()         Normalize list-based columns into rows
# query()           Simplify complex filtering 
# groupby().agg()   Create named aggregations for clear summaries
# pd.to_datetime()  Parse and sanitize date columns 
# pipe()            Build modular transformaiton pipelines

