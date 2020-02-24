import logging

logging.basicConfig(filename="test2.log", level=logging.DEBUG,
                    format="%(asctime)s|%(levelname)s|%(message)s")

logging.debug("Testing log")

print(__name__)