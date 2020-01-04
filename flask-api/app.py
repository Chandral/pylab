import json, yaml
import mysql.connector
from flask import Flask, jsonify, make_response

server_config = json.load(open('config.json'))


def connection():
	conn = mysql.connector.connect(
		host=server_config["host"],
		user=server_config["user"],
		passwd=server_config["password"],
		database=server_config["database"]
	)
	c = conn.cursor()
	return c, conn


app = Flask(__name__)
columns_query = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='socketTestDB' AND `TABLE_NAME`='V_TEE_sites';"


@app.route("/")
def hello():
	try:
		c, conn = connection()
		c.execute(columns_query)
		column_names = [(column_record[0]) for column_record in c.fetchall()]
		if server_config["last_record_id"]:
			c.execute("SELECT * FROM Products WHERE AccID > {};".format(server_config["last_record_id"]))
		else:
			c.execute("SELECT * FROM V_TEE_sites")
		raw_data = c.fetchall()
		list_of_record_dict = [dict(zip(column_names, record)) for record in raw_data]
		last_id = list_of_record_dict[-1]["AccID"]
		a = """{"last_record_id": {}}""".format(str(last_id))
		last = json.loads(a)
		print("~"*20, last["last_record_id"])

		response_body = {
			"message": "JSON received!",
			"sender": "name",
			"data": list_of_record_dict
		}

		res = make_response(jsonify(response_body), 200)
		return res
	except Exception as e:
		return str(e)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)
