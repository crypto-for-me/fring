import os
import yaml

import console

CONFIG_FILE_PATH = os.path.join(os.path.expanduser('~'), '.config', 'crying', 'crying.yml')
DEFAULTS = {
    'python_call': 'python',
    'pip_call': 'python -m pip'
}

def get(key: str=None):
    with open(CONFIG_FILE_PATH, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    if not key:
        if not config:
            return {}

        return config
    return config[key]

def edit(key: str, value: str=None) -> None:
    try:
        config = get()
    except FileNotFoundError:
        config = {}

    if not value:
        config = key
    else:
        config[key] = value

    with open(CONFIG_FILE_PATH, 'w') as f:
        yaml.dump(config, f)

def init() -> None:
    console.info(f'Initializing config file at "{CONFIG_FILE_PATH}"')

    os.makedirs(os.path.dirname(CONFIG_FILE_PATH), exist_ok=True)

    for k, v in DEFAULTS.items():
        edit(k, v)

if not os.path.exists(CONFIG_FILE_PATH):
    console.warning(f'Configuration file not found. If this is your first time running Crying, you can safely ignore this message.')
    init()
else:
    for k in DEFAULTS:
        if k not in get():
            console.warning(f'Configuration at "{CONFIG_FILE_PATH}" seems out to date, as some keys don\'t exist Re-initializing...')
            init()
            break

if __name__ == '__main__':
    pass
