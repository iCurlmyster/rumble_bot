# RumbleBot

- [Commands](#commands)
- [Building](#building)
- [Running](#running)

A Discord bot that will simulate fights between the caller and someone else in a server.

## Commands

All commands are preceded with a `!`

- [rumble](#rumble)
- [lift](#lift)
- [rumble_info](#rumble-info)
- [rumble_src](#rumble_src)

### rumble

This command takes one argument, a user's name. Can be `john` or `john#0001`.

This will start a rumble between the caller and the other user referenced.

The result will be logged to the chat once the simulation is done.

### lift

This command takes no arguments.

Running this will allow you to possibly increase your strength by 1, 2 if you get lucky, or decrease your strength by 1 if you are unlucky and injury yourself.

#### rumble_info

This command takes 1 optional argument. A user's name. Can be `john` or `john#0001`.

No arguments given, this command spits out the stat summary of the calling user.
With an argument this command spits out the stat summary of the given user.

The stat summary includes the user's strength and last time worked out (using the `lift` command).

#### rumble_src

This command takes no arguments.

This command spits out the link to this project's github.com repo.


## Building

This project requires:

OS packages:
- sqlite3
- python 3.7+
- docker (optional)

Python packages(with pip):
- discord.py
- peewee
- python-dotenv

You can install all of the dependencies yourself or you can build the Docker image and run it with docker.

The program pulls in to environment variables that should be set in a `.env` file.

- DISCORD_TOKEN this is your discord token for the bot
- RUMBLE_DB this is the database name which should be set to `rumble.db`. If this is changed make sure to update the `load_db.sh` file

## Running

If you pull in the dependencies yourself run the `run.sh` file which calls the `load_db.sh` if the db has not been created and then runs `python main.py`.

Running with docker requires you to run the `build_docker.sh` file and then run the `run_docker.sh` file. The docker image is called `rumble_docker`, the container is `rumble_bot`.

