import json


def dict_from_proto_list(obj_list):
    d = dict()
    for item in obj_list:
        d[item.key] = json.loads(item.value_json)
    return d
