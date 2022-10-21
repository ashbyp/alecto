# Basic config for now, replace with hydra possibly
from os import path
import json


BASE = "resources/"

PUBLIC = [
    BASE + "config.json"
]

PRIVATE = [
    BASE + "secrets/keys.json"
]


def _find_prefix() -> str:
    if path.exists(BASE):
        return ""
    if path.exists(f'../{BASE}'):
        return '../'
    if path.exists(f'../../{BASE}'):
        return '../../'
    raise FileNotFoundError('Cannot find resources folder')


def get() -> dict:
    prefix = _find_prefix()

    public_dict = {}
    for file in PUBLIC:
        with open(prefix + file, "r") as f:
            public_dict.update(json.load(f))

    private_dict = {}
    for file in PRIVATE:
        with open(prefix + file, "r") as f:
            private_dict.update(json.load(f))

    return {"public": public_dict, "private": private_dict}


if __name__ == '__main__':
    import pprint
    pprint.pprint(get())
