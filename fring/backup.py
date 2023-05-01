import os
import shutil
import datetime

import config
import console

from rich.progress import Progress, SpinnerColumn, TextColumn

def start_backup():
    console.info('Starting backup...')
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    zip_name = f'backup-{dt}'

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description='Zipping...', total=None)

        shutil.make_archive(zip_name, 'zip', config.get('backup_folder'))

    console.success('Successfully backed up!')

if __name__ == '__main__':
    start_backup()
