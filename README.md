# Fintechracy interview assignment
Fintechracy is an IT company that aims to end paper receipts, as part of their selction process they have asked me to complete this assignment.

## Setup
follow this instructions to setup the project on your local machine

- clone this repo 
```bash
git clone https://github.com/bouzenaali/Fintechracy-interview-assignment.git
```
- create a virtual environment
```bash
python3 -m venv env
```

- activate the virtual environment: <br>
for `windows`
```bash
env\Scripts\activate
``` 
&emsp; for a `linux` and `mac`
```bash
source env/bin/activate
```

- install the requirements
```bash
pip install -r requirements.txt
```

- run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

- run the server
```bash
python manage.py runserver
```
