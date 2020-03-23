FROM python:3.7-slim

RUN apt-get update
RUN apt-get install -y sudo \
	wget \
	sqlite3

RUN pip install -U discord.py python-dotenv peewee

WORKDIR /rumble_bot

COPY . /rumble_bot

CMD ./run.sh
