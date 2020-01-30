from pysnmp.smi import builder, view, compiler
import os
mibBuilder = builder.MibBuilder()
compiler.addMibCompiler(mibBuilder, sources=[os.getcwd() + "/MIB Files"])
mibBuilder.loadModules('IF-MIB', 'INET-ADDRESS-MIB', 'SNMPv2-MIB', 'ORION-BASE-MIB')
mibView = view.MibViewController(mibBuilder)

oid, label, suffix = mibView.getNodeName((1,3,6,1,2,1,31,1,1,1,6))
[print(i) for i in (oid, label, suffix)]