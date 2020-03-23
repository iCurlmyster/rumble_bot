#!/bin/bash

if [ ! -f "rumble.db" ]; then
	bash load_db.sh
fi

python main.py
