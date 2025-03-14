from django.db import models

import re
import phonenumbers
from datetime import datetime
from tinydb import TinyDB, Query


db = TinyDB('db.json')
field = ['name', 'date', 'phone', 'email']


def validEmail(email: str) -> bool: 
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None


def validPhone(phone: str) -> bool: 
    try:
        phone_number_obj = phonenumbers.parse(phone, "RU")
    except:
        return False
    
    return phonenumbers.is_possible_number(phone_number_obj)


def valiDate(date_text: str) -> bool: 
    # DD.MM.YYYY or YYYY-MM-DD
    res = False
    try:
        res = bool(datetime.strptime(date_text, "%Y-%m-%d"))
    except ValueError:
        try:
            res = bool(datetime.strptime(date_text, "%d.%m.%Y"))
        except ValueError:
            res = False
    return res


def searchQuery(name: str, date: str, phone: str, email: str) -> str:
    user = Query()
    tables = db.tables()
    for each in tables:
        table = db.table(each)
        result = table.search( (user.name == name) & (user.date == date) & (user.phone == phone) & (user.email == email))
        if len(result) != 0:
            return each
    
    return "Undefined"
