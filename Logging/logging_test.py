import test
# import Logging
#
# """
#     There are 5 separate Logging levels
#     DEBUG       Detailed info typically for diagnosing problem
#     INFO        Confirmation that things work as expected
#     WARNING     Something unexpected happened or a potential issue (e.g. low disk space)
#     ERROR       The app as a whole is working fine but a feature failed to work as expected
#     CRITICAL    A serious error where the program itself may not be able to function
#     By default it won't log DEBUG & INFO
# """
#
logging.basicConfig(filename="test.log", level=logging.DEBUG,
                    format="%(asctime)s|%(name)s|%(levelname)s|%(message)s")

logging.debug("Testing log")

