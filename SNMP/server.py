from pysnmp.smi import builder, view, rfc1902

mibBuilder = builder.MibBuilder()
mibView = view.MibViewController(mibBuilder)
mibVar = rfc1902.ObjectIdentity('SNMPv2-MIB', 'sysDescr')
mibVar.resolveWithMib(mibView)
OID = tuple(mibVar)
print(OID)  # Prints >> (1, 3, 6, 1, 2, 1, 1, 1)
mibVar = rfc1902.ObjectIdentity(OID).resolveWithMib(mibView)
print(mibVar.prettyPrint())  # Prints >> SNMPv2-MIB::sysDescr
