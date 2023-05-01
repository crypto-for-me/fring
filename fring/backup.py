import os
import io
import shutil
import datetime
import rich.progress

import console

def start_backup():
    console.info('Starting backup...')
    dt = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    zip_name = f'backup-{dt}'
    zip_path = os.path.join(os.getcwd(), f'{zip_name}.zip')

    with rich.progress.open(zip_path, 'w') as writer:
        shutil.make_archive(zip_name, 'zip', os.getcwd(), writer=writer)

    console.success('Successfully backed up!')

if __name__ == '__main__':
    start_backup()
