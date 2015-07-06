# REST API Scaffold

This project is intended to use as a directories structure to build a RestFul API using Python Flask Famework.

## Requirements

* Python 2.7+
* pip: sudo apt-get install python-pip
* virtualenv: sudo apt-get install python-virtualenv

## Configuration File:

You must copy api/instance/iconfig.py.default to api/instance/iconfig.py. This file contains specific configurations and is ignored by Git, so you can add passwords and sensitive data. The settings can vary depending your needs.

## How to start

* Clone this repo
* Install dependencies:
	1. Create virtual environment: virtualenv venv
	2. Load virtual environment: source venv/bin/activate
	3. Install modules: pip install -r requirements.txt
* To access: http://127.0.0.1:5000/0.0.1/. 0.0.1 is the version. To versioning we use Blueprints, so each version is modularized and is independent to any another. In that way, the API can provide backward compatibility.
* Start to code

## Contributing

Anyone and everyone is welcome to contribute. Please feel free to contribute with new issues, pull requests, code fixes or new features.