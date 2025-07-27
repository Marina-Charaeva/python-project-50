import json


def format_json(diff):
    def convert(node):
        result = {}
        for key, value in sorted(node.items()):
            if value['type'] == 'nested':
                result[key] = {
                    'type': 'nested',
                    'children': convert(value['children'])
                }
            elif value['type'] == 'added':
                result[key] = {'type': 'added', 'value': value['value']}
            elif value['type'] == 'removed':
                result[key] = {'type': 'removed', 'value': value['value']}
            elif value['type'] == 'changed':
                result[key] = {
                    'type': 'changed',
                    'old_value': value['old_value'],
                    'new_value': value['new_value']
                }
            else:
                result[key] = {'type': 'unchanged', 'value': value['value']}
        return result
    return json.dumps(convert(diff), indent=2, sort_keys=False)

