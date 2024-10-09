# ================================================================ #
#                                                                  #
# Alfred Santa Molison, 8814921, PROG8850 - Fall 2024 - Section 1  #
#                                                                  #
# ================================================================ #

# importing OS library for executing commands as if in terminal
import os
# importing pymysql library for enabling connection with mysql
import pymysql
# importing logging library to enable logging in console or file
import logging
# importing sys library for reading arguments
import sys

# creating the log handle
logger = logging.getLogger()
# setting the log level as info in the root level
logger.setLevel(logging.INFO)

# logging to console output
log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(logging.INFO)
# composing the format of log message
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)


# Creating the connection parameters object
# argv[1] takes the first argument, argv[2] takes the second argument, etc.
# ssl={"fake_flag_to_enable_tls":True} creates a dummy ssl which enables database connection in case if there is no real ssl file
connection = pymysql.connect(
    host=sys.argv[1],
    user=sys.argv[2],
    password=sys.argv[3],
    database=sys.argv[4],
    ssl={"fake_flag_to_enable_tls":True}
)

# Path to the SQL script file
sql_file_path = 'add_departments.sql'

# Read the SQL script file in read mode and create a file handle named sql_script
with open(sql_file_path, 'r') as file:
    sql_script = file.read()

# try - catch mode is implemented to handle exceptions
try:
# Create a cursor (SQL handle) object to execute SQL queries
    with connection.cursor() as cursor:
    
# The split function will create an array from string, by specifying a delimiter character (here ;)
# The for loop will iterate through each SQL statement
        for statement in sql_script.split(';'):
# The if - strip() is used to check if the element of array is empty or not
            if statement.strip():
# Logging the SQL query for information
                logger.info(f"Executing statement: {statement}")
# Execute the SQL statement using the cursor created
                cursor.execute(statement)

# call the commit function finally to permanently save the database changes        
        connection.commit()

# Check if there is any exception and logging if any
except Exception as e:
    logging.error(f"An error occurred: {e}")

# Close the connection to database after use
connection.close()

logger.info('SQL execution completed successfully')
