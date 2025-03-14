<div align="center">
  <h1>DjangoTest</h1>
</div>

One page is available that accepts parameters. Searches for a user across all data from two tables

## Getting Started

- download archive
- install packages: pip install -r requirements.txt
- start server: py manage.py runserver
- go to the page by url: 'http://127.0.0.1:8000/get_form'

## Testing page

Testing was done using the "unittest" package

tested:
- open other URLs
- valid parameters
- the result is available in the tables
- result not available in tables

## Output data

find user: table name

no find user: Undefined

no valid parameter:
    name : text halo,
    date : date YYYY-MM-DD | DD.MM.YYYY 2024-10-12,
    phone : phone +79999999999,
    email : email example@yandex.ru
