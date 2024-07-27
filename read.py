import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='vansheel',
                             password='vansheel@1111',
                             database='AIWR',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

data = {}  # Dictionary to store the fetched data

try:
    with connection.cursor() as cursor:
        # Select all records from the table
        sql = "SELECT * FROM articles"
        cursor.execute(sql)
        
        # Fetch all records
        rows = cursor.fetchall()
        
        # Store fetched data in the dictionary
        for row in rows:
            title = row['title']
            content = row['content']
            data[title] = content

finally:
    # Close the connection
    connection.close()

# Print the fetched data
for title, content in data.items():
    print("Title:", title)
    print("Content:", content)
    print()
