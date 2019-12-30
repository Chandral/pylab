import mysql.connector

# Configuration data
mysql_db = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="Orion@123",
  database="socketTestDB"
)


def connection():
    return mysql_db.cursor()


def enter_data_in_db(data):
    fields = ""
    values = ""

    for key in data:
        if '.' in key:
            fields += key.replace('.', '_') + ', '
        else:
            fields += key + ", "
        values += str(data[key]) + ', '

    fields = fields.strip()[:-1]
    values = values.strip()[:-1]
    print(fields)
    print(values)
    input()
    connection().execute("INSERT INTO clientData ({}) VALUES ({})".format(fields, values))
    mysql_db.commit()

