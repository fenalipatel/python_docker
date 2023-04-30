import docker
import pymysql
import pandas as pd


# Connect to Docker container
client = docker.from_env()
container = client.containers.get('my-mysql')
container.start()

# Check if container is connected
if container.status == 'running':
    print('Docker container connected.')
else:
    print('Error: Docker container not connected.')

# Connect to the MySQL server
try:
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="my-secret-pw"
    )
except pymysql.err.OperationalError as e:
    print("Error connecting to database:", e)
    exit()

# Create a new database
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
existing_databases = cursor.fetchall()

if ('pydb',) not in existing_databases:
    try:
        cursor.execute("CREATE DATABASE pydb")
        print("Database created")
    except pymysql.err.OperationalError as e:
        print("Error creating database:", e)
        exit()
else:
    print("Database already exists")

# Switch to the new database
cursor.execute("USE pydb")

# Define the table schema
table1_schema = (
    "CREATE TABLE IF NOT EXISTS table1 ("
    "FNAME VARCHAR(255),"
    "LNAME VARCHAR(255),"
    "AGE INT,"
    "TF INT)"
)


# Drop table1 if it already exists
try:
    cursor.execute("DROP TABLE IF EXISTS table1")
except pymysql.err.OperationalError as e:
    print("Error dropping table:", e)
    exit()

# Create the table
try:
    cursor.execute(table1_schema)
except pymysql.err.OperationalError as e:
    print("Error creating table:", e)
    exit()

# Load data from CSV file
try:
    table1_data = pd.read_csv("Book1.csv", header=0)
except pd.errors.EmptyDataError as e:
    print("Error reading CSV file:", e)
    exit()

# Insert data into table1
for i, row in table1_data.iterrows():
    insert_query = "INSERT INTO table1 (FNAME,LNAME,AGE,TF) VALUES (%s,%s, %s,%s)"
    data = (row['FNAME'], row['LNAME'],row['AGE'],row["TF"])
    try:
        cursor.execute(insert_query, data)
    except pymysql.err.OperationalError as e:
        print("Error inserting data:", e)
        exit()

# Commit changes to the database
try:
    conn.commit()
    print("Data inserted successfully!")
except pymysql.err.OperationalError as e:
    print("Error committing changes:", e)
    exit()

# Retrieve data from table1
select_query = "SELECT * FROM table1"
try:
    cursor.execute(select_query)
    rows = cursor.fetchall()
    print("Total rows:", len(rows))
    for row in rows:
        print(row)
except pymysql.err.OperationalError as e:
    print("Error retrieving data:", e)

# Close the database connection
conn.close()