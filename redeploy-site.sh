#!/bin/bash

#Store and run this file in the same directory where this git repository is stored

tmux kill-server || echo "No tmux server to kill"

cd ~/flask-personal-portfolio

git fetch && git reset origin/main --hard

source python3-virtualenv/bin/activate
pip3 install -r requirements.txt

tmux new-session -d -s myportfolio 'source python3-virtualenv/bin/activate && \
export FLASK_ENV=development && flask run --host=0.0.0.0'
