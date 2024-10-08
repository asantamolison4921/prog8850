# ================================================================ #
#                                                                  #
# Alfred Santa Molison, 8814921, PROG8850 - Fall 2024 - Section 1  #
#                                                                  #
# ================================================================ #

# importing pymysql library for enabling connection with mysql
import pymysql

# Create the database connection directly
connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'),
    ssl={"fake_flag_to_enable_tls":True}
)

# Path to the SQL file
sql_file_path = 'update_projects_schema.sql'

# Read the SQL script from the file
with open(sql_file_path, 'r') as file:
    sql_script = file.read()

try:
# Create a cursor object to execute SQL queries
    with connection.cursor() as cursor:
    
        # Execute each SQL statement individually (split by semicolon)
        for statement in sql_script.split(';'):
            if statement.strip():  # Execute only non-empty statements
                cursor.execute(statement)
        
        connection.commit()  # Commit all changes at once

except Exception as e:
    logging.error(f"An error occurred: {e}")
    
connection.close()  # Close the connection

print("Execution completed successfully")
