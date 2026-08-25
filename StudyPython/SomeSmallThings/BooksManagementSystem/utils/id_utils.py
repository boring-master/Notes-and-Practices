import random
from datetime import datetime


def generate_id():
    ts = int(datetime.now().strftime("%Y%m%d%H%M%S"))
    rand = random.randint(0, 999)
    return f'{ts*1000+rand}'

def generate_member_id():
    return f'M{generate_id()}'

def generate_book_id():
    return f'B{generate_id()}'