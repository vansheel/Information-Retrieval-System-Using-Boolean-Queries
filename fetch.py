import mysql.connector
from mysql.connector import Error

# Assuming your connection setup from the sample code
connection = mysql.connector.connect(
    host="localhost",
    user="vansheel",
    password="vansheel@1111",
    database="AIWR"
)

def retrieve_documents():
    cursor = connection.cursor()
    retrieve_query = """
    SELECT doc_id, doc_name, body FROM articles
    """
    cursor.execute(retrieve_query)
    records = cursor.fetchall()
    
    for record in records:
        print("Doc ID:", record[0])
        print("Doc Name:", record[1])
        print("Body:", record[2])
        print("-----\n")

    cursor.close()

# Call the function to retrieve and print documents
retrieve_documents()
