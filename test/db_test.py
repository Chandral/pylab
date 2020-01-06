import mysql.connector
import yaml

config_data = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)

def connection_1():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="test",
        passwd="Orion@123",
        database="socketTestDB"
    )
    c = conn.cursor()
    return c, conn

def connection_2():
    conn = mysql.connector.connect(
        host=config_data["host"],
        user=config_data["user"],
        passwd=config_data["password"],
        database=config_data["database"]
    )
    c = conn.cursor()
    return c, conn

print(connection_1())
print(connection_2())
