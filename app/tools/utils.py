"""
Create by yy on 2020/3/10
"""
from tool_yy import get_date_time, get_now_time_stamp


def get_file_name():
    return "{file_name}.log".format(file_name=get_date_time(get_now_time_stamp(), "%Y-%m-%d"))
