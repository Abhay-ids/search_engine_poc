import pandas as pd
import psycopg2
from psycopg2 import sql
import json

# Load the CSV file
file_path = 'AU20240224-55.csv'
csv_data = pd.read_csv(file_path)

# Database connection details
db_host = 'localhost'
db_port = '5432'
db_name = 'australia'
db_user = 'postgres'
db_password = 'Login@#6009'

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
cur = conn.cursor()

# Create table query
create_table_query = """
CREATE TABLE IF NOT EXISTS trademarks (
    applicationNumber BIGINT,
    applicationDate DATE,
    registrationNumber BIGINT,
    expiryDate DATE,
    disclaimer TEXT,
    colors TEXT,
    markFeature TEXT,
    verbalElements TEXT,
    comments TEXT,
    validation_errors TEXT,
    priorities_date DATE,
    priorities_country TEXT,
    publicationEvents_publicationNumber BIGINT,
    publicationEvents_publicationDate DATE,
    publicationEvents_sectionName TEXT,
    publicationEvents_description TEXT,
    publicationEvents_eventDetail TEXT,
    classifications_niceClass TEXT,
    classifications_localClass TEXT,
    classifications_goodServiceDescription TEXT
);
"""

# Execute the create table query
cur.execute(create_table_query)
conn.commit()

# Function to convert NaN to None
def nan_to_none(value):
    if pd.isna(value):
        return None
    return value

# Function to handle lists of dates, returning the first date in the list
def handle_date_list(value):
    if isinstance(value, str):
        try:
            # Convert string representation of list to actual list
            date_list = json.loads(value.replace("'", '"'))
            if isinstance(date_list, list) and len(date_list) > 0:
                return date_list[0]  # Return the first date in the list
        except json.JSONDecodeError:
            pass
    return nan_to_none(value)

# Insert data into the table
for index, row in csv_data.iterrows():
    row['applicationDate'] = handle_date_list(row['applicationDate'])
    row['expiryDate'] = handle_date_list(row['expiryDate'])
    row['priorities_date'] = handle_date_list(row['priorities_date'])
    row['publicationEvents_publicationDate'] = handle_date_list(row['publicationEvents_publicationDate'])
    
    row['verbalElements'] = json.dumps(nan_to_none(row['verbalElements']))
    row['validation_errors'] = json.dumps(nan_to_none(row['validation_errors']))
    row['publicationEvents_sectionName'] = json.dumps(nan_to_none(row['publicationEvents_sectionName']))
    row['publicationEvents_eventDetail'] = json.dumps(nan_to_none(row['publicationEvents_eventDetail']))
    row['classifications_niceClass'] = json.dumps(nan_to_none(row['classifications_niceClass']))
    row['classifications_goodServiceDescription'] = json.dumps(nan_to_none(row['classifications_goodServiceDescription']))

    insert_query = sql.SQL("""
    INSERT INTO trademarks (
        applicationNumber, applicationDate, registrationNumber, expiryDate,
        disclaimer, colors, markFeature, verbalElements, comments, validation_errors,
        priorities_date, priorities_country, publicationEvents_publicationNumber,
        publicationEvents_publicationDate, publicationEvents_sectionName,
        publicationEvents_description, publicationEvents_eventDetail,
        classifications_niceClass, classifications_localClass,
        classifications_goodServiceDescription
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    
    cur.execute(insert_query, (
        nan_to_none(row['applicationNumber']), nan_to_none(row['applicationDate']), nan_to_none(row['registrationNumber']), nan_to_none(row['expiryDate']),
        nan_to_none(row['disclaimer']), nan_to_none(row['colors']), nan_to_none(row['markFeature']), row['verbalElements'], nan_to_none(row['comments']), row['validation_errors'],
        nan_to_none(row['priorities_date']), nan_to_none(row['priorities_country']), nan_to_none(row['publicationEvents_publicationNumber']),
        nan_to_none(row['publicationEvents_publicationDate']), row['publicationEvents_sectionName'],
        nan_to_none(row['publicationEvents_description']), row['publicationEvents_eventDetail'],
        row['classifications_niceClass'], nan_to_none(row['classifications_localClass']),
        row['classifications_goodServiceDescription']
    ))

# Commit the transaction
conn.commit()

# Close the database connection
cur.close()
conn.close()