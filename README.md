# QR5 Server [![Build Status](https://travis-ci.org/mbasanta/QR5Server.svg)](https://travis-ci.org/mbasanta/QR5Server)

## Requirments

Make sure you have the basics installed

- Python
- Pip
- VirtualEnv (recommended)

## Install Dependencies

- Create a virtual enviroment
- Install Pip requirments `sudo pip install -r requirements/dev.txt`

## Database Setup

Create and upgrade database

```bash
$ ./db_create.py
$ ./db_upgrade.py
...
$
```

## Run the application locally

```bash
$ ./runserver.py
```

