from pysnmp.smi import builder, view, compiler

mibBuilder = builder.MibBuilder()
mibBuilder.addMibSources(builder.DirMibSource('/home/chandral/MyGithub/projects/pylab/SNMP/MIB Files'))
mibBuilder.loadModules('ORION-BASE-MIB')
mibView = view.MibViewController(mibBuilder)

sysDescr_OID = (1, 3, 6, 1, 2, 1, 1, 1, 0)
systemInfoGroup = (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 1)

oid, label, suffix = mibView.getNodeName(sysDescr_OID)
print(oid, label, suffix)
# Prints
oid, label, suffix = mibView.getNodeName(systemInfoGroup)
print(oid, label, suffix)
# Prints

# compiler.addMibCompiler(mibBuilder, sources=["/home/chandral/MyGithub/projects/pylab/SNMP/MIB Files"])
# mibBuilder.loadModules('IF-MIB', 'INET-ADDRESS-MIB', 'SNMPv2-MIB')