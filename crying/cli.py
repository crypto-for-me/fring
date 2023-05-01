import typer

import backup
import prepare
import console
import config
import production

app = typer.Typer()

@app.command()
def start():
    """Pushes the current folder to production."""
    console.info('Creating backup...')
    backup.start()

    console.info('STARTING UPDATES')
    prepare.update_packages()

    console.info('PUSHING TO PRODUCTION')
    production.to_prod()

    console.success('Done!')

@app.command()
def settings(k: str=None, v: str=None):
    """Change a setting using --k and --v, or run without arguments to see the path to the config file."""

    if not k:
        console.info(f'The config file is located at "{config.CONFIG_FILE_PATH}".')
        console.info('Use --k (key) and --v (value) to change a setting.')
        console.info('Use "quotes" if the value contains spaces.')
        return

    config.edit(k, v)

main = app

if __name__ == '__main__':
    main()
