setup:
	# Create python virtualenv & source it
	# source ~/.scooter/bin/activate
	python3 -m venv ~/.scooter

install:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt


all: install lint 