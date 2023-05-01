import colorama
import subprocess

from typing import List, Union

colorama.init(autoreset=True)

def run(command: Union[str, List[str]]):
    if isinstance(command, str):
        command = command.split()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as err:
        err = err.output.decode('utf-8').strip()
        raise Exception(f"""{colorama.Fore.RED}ERROR
The command {colorama.Fore.YELLOW}{" ".join(command)}{colorama.Fore.RED}
failed with the following output:
{colorama.Fore.YELLOW}{err}
""")

def info(message: str):
    print(f'{colorama.Fore.BLUE}{message}')

def success(message: str):
    print(f'{colorama.Fore.GREEN}{message}')

def error(message: str):
    print(f'{colorama.Fore.RED}{message}')

def warning(message: str):
    print(f'{colorama.Fore.YELLOW}{message}')
