import re


def validate_account_id(account_id,length=11):
    return len(account_id) == length and account_id.isdigit()

def validate_password(password, min_length=8, max_length=64):
    return (max_length >= len(password) >= min_length and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'[0-9]', password)
            )

def validate_name(name):
    """检验名字是否为纯中文"""
    pattern = r'^[\u4e00-\u9fff\u3400-\u4dbf\U00020000-\U0002a6df]+$'
    return bool(re.fullmatch(pattern, name))