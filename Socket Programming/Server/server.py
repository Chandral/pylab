import socket
import helper.logger as logger
import helper.db as db
import helper.s_helper as help

IP = "127.0.0.1"
PORT = 2021

logger.create_logs_directory()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows to use the same IP/Port on server restart
s.bind((IP, PORT))
s.listen(5)
logger.log(logger.INFO, "Listening for incoming connections at {}:{}".format(IP, PORT))

while True:
    client_socket, address = s.accept()
    logger.log(logger.SUCCESS, "Established incoming connection from {}".format(address))
    data = client_socket.recv(1024).decode("utf-8")
    logger.log(logger.SUCCESS, "Decoded data received from {}".format(address))
    logger.log(logger.INFO, data)
    data = help.change_data_to_dict(data)
    if data:
        db_entry = db.enter_data_in_db(data)
        if db_entry[0]:
            logger.log(logger.SUCCESS, "Saved data received from {}".format(address))
        elif not db_entry[0]:
            logger.log(logger.ERROR, "Failed to save data received from {}".format(address))
            logger.log(logger.ERROR, db_entry[1])
    else:
        logger.log(logger.WARNING, "Client request does not contain appropriate data")
