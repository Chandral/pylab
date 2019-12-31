import mysql.connector

# Database connection object
mysql_db = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="Orion@123",
  database="socketTestDB"
)


def connection():
    """
    Simply returns a cursor object of the database connection
    :return: MYSQL DB cursor object
    """
    return mysql_db.cursor()


def enter_data_in_db(data):
    """
        Takes in a dictionary as a parameter, extracts dictionary keys as DB column names and the values as column's data.
        Saves the data in the database and returns
        :param data: Dictionary object which is the data received from the client
        :return: A tuple with the two values 'True' and the data received if data saved successfully or a tuple with
        one more additional value, string of Exception occurred if data submission failed.
    """
    fields = ""  # Empty string for fields to be used in SQL query
    values = ""  # Empty string for field values to be used in SQL query

    # Loop iterates over each key in the dictionary, modifies it as the pre-defined column name in DB and appends it to
    # the local variable 'fields'. It also appends the value of the dictionary key to the local variable 'values'
    for key in data:
        fields += str(key) + ', '
        values += str(data[key]) + ', '

    fields = fields.replace('.', '_')  # Replaces '.' with '_' as per the pre-defined column names in the database
    fields = fields.strip()[:-1]  # Removes the extra ',' appended to the string on the last iteration
    values = values.strip()[:-1]  # Removes the extra ',' appended to the string on the last iteration

    try:
        connection().execute("INSERT INTO clientData ({}) VALUES ({})".format(fields, values))  # SQL query to insert
        mysql_db.commit()  # Committing changes to the DB
        return True, "Data Saved"
    except Exception as E:
        return False, str(E)
