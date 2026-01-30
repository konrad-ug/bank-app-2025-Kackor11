[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IwJY4g24)
# Bank-app

## Author:
name: Kacper

surname: Korzekwa

group: II

## How to start the app

python -m flask --app app/api.py run

## How to execute tests

python3 -m pytest app/api_tests/account_crud.py
python3 -m coverage run --source=src -m pytest 