from datetime import datetime

def days_between(data_str1, data_str2):

    d1 = datetime.strptime(data_str1, "%Y-%m-%d")
    d2 = datetime.strptime(data_str2, "%Y-%m-%d")
    return abs((d2 - d1).days)