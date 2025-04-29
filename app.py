import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Підключення до бази через секрети
db_user = st.secrets["DB_USER"]
db_pass = st.secrets["DB_PASS"]
db_host = st.secrets["DB_HOST"]
db_port = st.secrets["DB_PORT"]
db_name = st.secrets["DB_NAME"]

# SQLAlchemy engine
engine = create_engine(f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}')

# SQL-запит
query = "SELECT * FROM users"  # Назва таблиці в Supabase
df = pd.read_sql(query, engine)

# Вивід у Streamlit
st.title("Дані з Supabase PostgreSQL")
st.dataframe(df)
