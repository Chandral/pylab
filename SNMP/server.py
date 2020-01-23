from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv

snmpEngine = engine.SnmpEngine()
TrapAgentAddress = '0.0.0.0'  # Trap listener address
Port = 8000  # trap listener port
print("Agent is listening SNMP Trap on " + TrapAgentAddress+" , Port : " + str(Port))
print('~'*50)
config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode((TrapAgentAddress, Port))
)

#  Configure community here
config.addV1System(snmpEngine, 'my-area', 'public')


def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    print("Received new Trap message")
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))


ntfrcv.NotificationReceiver(snmpEngine, cbFun)
snmpEngine.transportDispatcher.jobStarted(1)

try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise
