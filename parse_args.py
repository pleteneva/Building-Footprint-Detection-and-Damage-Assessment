import argparse
import yaml
from typing import Optional

def parse_args(args):
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('--config', help='path to config', default="config.yml")
    config = yaml_parser(parser.parse_args(args).config)
    return config


def yaml_parser(
    path: Optional[str] = None,
    data: Optional[str] = None,
    loader: yaml.SafeLoader = yaml.SafeLoader
) -> dict:
    if path:
        with open(r"{}".format(path)) as file:
            return yaml.load(file, Loader=loader)
    elif data:
        return yaml.load(data, Loader=loader)

    raise ValueError('Either a path or data should be defined as input')
