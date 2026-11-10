import json


def export_flow(labels, path):
    with open(path, 'w') as fh:
        json.dump(labels, fh, indent=2)
