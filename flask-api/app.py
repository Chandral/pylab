import json
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


@app.route("/")
def hello():
	try:
		c, conn = connection()
		c.execute("SELECT * FROM V_TEE_sites")
		data = c.fetchall()
		print("c----->>", data)
		# print(jsonify(data))
		response_body = {
			"message": "JSON received!",
			"sender": "name"
		}

		res = make_response(jsonify(response_body), 200)

		return jsonify(data)
	except Exception as e:
		return str(e)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8000)
