# uv init llm_text_to_sql 
# cd llm_text_to_sql 
# uv venv  or uv sync
# .venv\Scripts\activate
# uv add ollama pg8000 python-dotenv   
# uv run ollama_txt_to_sql.py

# .env file ---------------------
# DB_HOST="localhost"
# DB_NAME="students_db"
# DB_USER="postgres"
# DB_PASSWORD="your password"
# DB_PORT="5432"
#================================

# ------Postgres database -----students_db------
#   id      name    major       email    
#   1       John    Math        john@gmail.com
#   2       Jane    Chemistry   jane@gmail.com
#   3       Smith   Physics     smith@gmail.com
#================================================



import ollama
from db import get_connection
import pg8000

def text_to_sql(user_query):
    prompt = f"""
    Convert the following natural language query into an SQL statement for PySQL:

    Query: "{user_query}"

    Ensure the query is syntactically correct and does not contain harmful operations.
    Only return the SQL query without any explanation.
    """

    # Update the model name to 'llama3.2:latest'
    response = ollama.chat(model="gpt-oss:latest", messages=[{"role": "user", "content": prompt}])
    sql_query = response['message']['content'].strip()
    return sql_query


# Uncomment this section if you wish to connect with PySQL and fill out your credentials in db.py
def execute_sql_query(user_query):
    sql_query = text_to_sql(user_query)

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        result = cursor.fetchall()
    except pg8000.connector.Error as e:
        return {"error": f"PySQL Error: {e}"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()  # Ensure connection is closed even if an error occurs

    return result

# Example usage
if __name__ == "__main__":
    user_input = "Show me all students whose name starts with the letter J in the name column"
    sql_query = (text_to_sql(user_input))
    print(sql_query)
    result = execute_sql_query(sql_query)
    print(result)