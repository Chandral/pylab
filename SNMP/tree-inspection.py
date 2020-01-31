from pysnmp.smi import builder, view, compiler, error

mibBuilder = builder.MibBuilder()
mibBuilder.addMibSources(builder.DirMibSource('/home/chandral/MyGithub/projects/pylab/SNMP/MIB Files'))
mibBuilder.loadModules('ORION-BASE-MIB')
mibView = view.MibViewController(mibBuilder)


print('MIB symbol name lookup by OID: '),
oid, label, suffix = mibView.getNodeName((1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 1))
print(oid, label, suffix)
