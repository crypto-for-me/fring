# `$ fring`
📅 Named after [Gustavo Fring](https://en.wikipedia.org/wiki/Gus_Fring), Fring is a tool for managing Flask web servers and deploying them to production with ease.

*Because a developer provides for their server uptime.*

## Support
### OS
- Linux (Debian)

## Web frameworks
- Flask

## Installation
```bash
pip install fring
```

You can also use `fring` manually by cloning this repository, installing the requirements
and running commands like this:

```bash
python fring --help
```

Next, install the following package:
```bash	
sudo apt install screen
```

`screen` is a terminal multiplexer, which allows you to run multiple terminals in one window. It is required to run the production server in the background, because otherwise the server would stop running as soon as you close the terminal.

After that, you need to specify the folder where your projects are located. This can be done by running:

```bash
fring folder /home/fring/projects
```

If the folder does not exist, it will be created, but make sure to give the
script the proper permissions to do so.

To check your settings, run:

```bash
fring settings --show
```

You can change a settings like so:

```bash
fring settings --k python_call --v "python3"
```

## Project setup
Before you can start a project, you need to make sure your folder has a file called `app.py` in the **current directory**. This file has to contain the function `create_app()`, which should return the `flask.Flask` object used for running your web server.

Here's a simple example of what your `app.py` file could look like:

```python
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'We are not the same.'

    return app
```


Once you have everything set up, go to the directory of your development project and set the name for your new project (in this example "gus"). You will also need to specify the port you want to use for your **production** server. Both can be done by running:

```bash
fring new --name gus --port 1234
```

From now on, you don't *have* to be in the same directory as your `app.py` file, as everything is set up.

To start the production server, run:

```bash
fring start gus
```

And you should be good to go!

## Usage

You can access your terminal multiplexer by running:

```bash
fring show gus
```

To stop the production server, run:

```bash
fring stop gus
```

This will stop the production server.

## Configuration
The default file path of the configuration file is `/root/.config/fring/fring.conf`.
