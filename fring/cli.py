import os
import typer

import backup
import prepare
import console
import config
import production

from rich import print

app = typer.Typer()

@app.command()
def start():
    """Pushes the current folder to production."""
    console.info('Creating backup...')
    backup.start_backup()

    console.info('STARTING UPDATES')
    prepare.update_packages()

    console.info('PUSHING TO PRODUCTION')
    production.to_prod()

    console.success('Done!')

@app.command()
def settings(k: str=None, v: str=None, show: bool=False):
    """Change a setting using --k and --v, or run without arguments to see the path to the config file."""

    if show:
        console.info(f'Settings located at "{config.CONFIG_FILE_PATH}":')
        print(config.get())
        return
        
    if v is None:
        console.info(f'The config file is located at "{config.CONFIG_FILE_PATH}".')
        console.info('Use --k (key) and --v (value) to change a setting.')
        console.info('Use --show to see all settings.')
        console.info('Use "quotes" if the value contains spaces.')
        return

    config.edit(k, v)
    console.success('Done.')

@app.command()
def folder(path: str):
    """Change the project folder of Fring.
    Creates the folders they don't exist.
    This will also change the location where backups etc. will be stored.
    """

    console.info(f'Changing project folder to "{path}"...')

    os.makedirs(path, exist_ok=True)

    for folder_name in ['projects', 'backups']:
        folder_path = os.path.join(path, folder_name)

        if not os.path.isdir(folder_path):
            console.info(f'Creating "{folder_path}"...')

        os.makedirs(folder_path, exist_ok=True)
        config.edit(f'{folder_name}_folder', folder_path)

    console.success('Done.')

@app.command()
def new(name: str, port: int=5000):
    """Initialize a new project.
    Make sure to read the docs before using this command.
    """

    name = name.lower()
    new_name = ''
    for char in name:
        if not char.isalnum():
            new_name += '_'
        else:
            new_name += char

    c = config.get()

    if new_name in c['projects']:
        console.error(f'A project with the name "{new_name}" already exists.')
        return

    c['projects'][new_name] = {
        'port': port,
        'dev_path': os.getcwd(),
        'prod_path': os.path.join(config.get('projects_folder'), new_name),
        'backup_path': os.path.join(config.get('backups_folder'), new_name)
    }

    config.edit('projects', c['projects'])

    console.success(f'Project "{new_name}" created.')

main = app

if __name__ == '__main__':
    main()
