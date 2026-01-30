import json
import yaml


def load_data(filepath):
    '''
    Reads a json file and returns a dictionary.
    :param filepath:
    :return: dictionary
    '''
    with open(filepath) as fh:
        data = json.load(fh)
    return data


def convert_to_yaml(data):
    '''
    Converts a dict to a clean YAML string for visualization purposes.
    :param data: dictionary
    :return: yaml string
    '''
    return yaml.dump(data, sort_keys=False, default_flow_style=False)
