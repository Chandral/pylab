from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from Logging import logger
import threading

logger.create_logs_directory()
snmpEngine = engine.SnmpEngine()
IP = '0.0.0.0'  # Trap listener address
PORT = 8000  # trap listener port
config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode((IP, PORT))
)

#  Configure community here
config.addV1System(snmpEngine, 'my-area', 'public')


def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    logger.log(logger.INFO, "Received new trap")
    for name, val in varBinds:
        logger.log(logger.INFO, '%s = %s' % (name.prettyPrint(), val.prettyPrint()))


ntfrcv.NotificationReceiver(snmpEngine, cbFun)
snmpEngine.transportDispatcher.jobStarted(1)
logger.log(logger.INFO, "Listening for Traps at {}:{}".format(IP, PORT))


def listen_threaded():
    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except:
        snmpEngine.transportDispatcher.closeDispatcher()
        raise


listen_threaded()
t1 = threading.Thread(target=listen_threaded)
t1.start()
t1.join()
