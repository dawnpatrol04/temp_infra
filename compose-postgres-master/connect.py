import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
user = 'postgres'
password = 'changeme'
host = 'localhost'
port = '5432'
database = 'postgres'

# Create an SQLAlchemy engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# SQL query
sql_query = 'SELECT * FROM s1.test'

# Use pandas to read the SQL query
df = pd.read_sql(sql_query, con=engine)

# Now, df contains the data fetched from your database
print(df.head())