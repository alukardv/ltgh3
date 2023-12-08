# luxoft_techground_hackathon_3
## Setup
### Install pyenv
#### Link for pyenv
```
https://github.com/pyenv/pyenv
```
#### Install python 3.12 version
```bash
pyenv install 3.12
```
### Install poetry
#### Link for poetry
```
https://python-poetry.org/docs/#installation
```
### Create project with poetry
```bash
git clone git@github.com:alukardv/ltgh3.git
cd ltgh3
```
#### Create virtual environments
```bash
pyenv local 3.12
```
#### Install requirements
```bash
poetry install
```
### Create project with venv
```bash
git clone git@github.com:alukardv/ltgh3.git
cd ltgh3
```
#### Create virtual environments
```bash
pyenv local 3.12
```
#### Create virtual environments and activate
```bash
python3 -m venv venv
source venv/bin/activate
```
#### Install requirements
```bash
pip3 install -r requirements.txt
```

## DB migrate
### with virtual environments 
```bash
python3 manage.py migrate 
```
### with poetry
```bash
poetry run python manage.py migrate
```

## Load initial data
### with virtual environments 
```bash
./manage.py load_initial_region initial_data/region.txt
./manage.py load_initial_type_of_users initial_data/type_of_user.csv
./manage.py load_initial_veterans_assistant initial_data/veterans_assistant.csv
./manage.py load_initial_user_tg initial_data/user_tg.csv
./manage.py load_initial_question initial_data/question.csv

```
### with poetry
```bash
poetry run python manage.py load_initial_region initial_data/region.txt
poetry run python manage.py load_initial_type_of_users initial_data/type_of_user.csv
poetry run python manage.py load_initial_veterans_assistant initial_data/veterans_assistant.csv
poetry run python manage.py load_initial_user_tg initial_data/user_tg.csv
poetry run python manage.py load_initial_question initial_data/question.csv
```
