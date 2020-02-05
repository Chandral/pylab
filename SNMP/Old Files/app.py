from pysnmp import hlapi

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value


def construct_object_types(list_of_oids):
    object_types = []
    for oid in list_of_oids:
        object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types


def fetch(handler, count):
    result = []
    for i in range(count):
        try:
            error_indication, error_status, error_index, var_binds = next(handler)
            if not error_indication and not error_status:
                items = {}
                for var_bind in var_binds:
                    items[str(var_bind[0])] = cast(var_bind[1])
                result.append(items)
            else:
                raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
        except StopIteration:
            break
    return result


def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]


<<<<<<< HEAD:SNMP/Old Files/app.py
a = get('demo.snmplabs.com', ['1.3.6.1.2.1.1.2.0'], hlapi.CommunityData('public'))

g = construct_object_types(a[i] for i in a)
print(g[0].prettyPrint())


def get_bulk(target, oids, credentials, count, start_from=0, port=161, engine=hlapi.SnmpEngine(),
             context=hlapi.ContextData()):
    handler = hlapi.bulkCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        start_from, count,
        *construct_object_types(oids)
    )
    return fetch(handler, count)
=======
print(get('10.0.0.1', ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData('ICTSHORE')))
>>>>>>> b8a3076860c8cf1a7d4b2b236269687764731d4c:SNMP/app.py
