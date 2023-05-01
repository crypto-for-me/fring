import config
import console

def update_packages():
    console.info('Updating pip...')
    console.run(f'{config.get("pip_call")} install --upgrade pip pipreqs')

    console.info('Updating requirements...')
    console.run(f'{config.get("python_call")} -m pipreqs.pipreqs --force .')

    console.info('Updating packages...')
    console.run(f'{config.get("pip_call")} install --upgrade -r requirements.txt')

    console.success('Successfully updated packages!')

if __name__ == '__main__':
    update_packages()
