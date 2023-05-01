# crying
📅 "Crying" = "Crypto" + "Staging" | A simple, but efficient development and production workflow manager, so you can focus on developing instead of crying

## Support
### OS
- Linux (Debian)

## Web frameworks
- Flask

## Installation
```bash
pip install crying
```

Next, install the following package:
```bash	
sudo apt install screen
```

`screen` is a terminal multiplexer, which allows you to run multiple terminals in one window. 
It is required to run the production server in the background, because otherwise the server would stop running as soon as you close the terminal.

After that, you need to specify the path of your projects.
Use quotes in the value (`--v`) if the path contains spaces.

```bash
crying settings --k projects --v /home/tears
```

If you want to, you can also specify

## Project setup
Once you have everything installed, go to the directory of your development project and set the name for your new project:

```bash
crying init demo
```

To start the production server, run:

```bash
crying start demo
```

And you should be good to go!

## Usage

You can access your terminal multiplexer by running:

```bash
crying show demo
```

To stop the production server, run:

```bash
crying stop demo
```

This will stop the production server.

## Configuration
The default file path of the configuration file is `/root/.config/crying/crying.conf`.
