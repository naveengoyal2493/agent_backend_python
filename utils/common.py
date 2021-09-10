import os
import datetime
import re


def get_env_var(var_name):
    return os.environ[var_name]


def is_valid_date(date_string, format):
    try:
        datetime.datetime.strptime(date_string, format)
        return True
    except:
        return False


def is_valid_email(email):
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))


def is_string_size_less_then_length(string, value):
    if not type(string) == str:
        raise TypeError(f"Expected a string type value not {string}")
    if not type(value) == int:
        raise TypeError(f"Expected an integer type value not {value}")
    return True if len(string) < value else False
        

def does_string_exist_in_list(string, values):
    if not type(values) == list:
        raise TypeError(f"Expected {values} to be a list")
    if not type(string) == str:
        raise TypeError(f"Expected {string} to be a string")
    return True if string in values else False