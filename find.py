import os
import re
import time
import datetime

today = datetime.date.today()
today_da = today.strftime('%Y.%m.%d')


def find_by_name(path='/Users', namef=''):
    res = []
    file_v = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            try:
                if namef.lower() in os.path.join(address, name).lower():
                    res.append(str((str(os.path.join(address, name)),
                                    datetime.datetime.strftime(
                                        datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(address, name))),
                                        '%Y.%m.%d'),
                                    str(os.path.getsize(os.path.join(address, name))) + ' б')))
                    file_v += os.path.getsize(os.path.join(address, name))
            except FileNotFoundError:
                pass
    res.append(str(file_v) + ' б ~= ' + str(file_v//1024) + ' кб ~=' + str(file_v//1024//1024) + ' мб ~=' + str(file_v//1024//1024//1024) + ' гб' )
    return res


def find_by_time(path='/Users', start_time=0.0, end_time=time.time()):
    res = []
    file_v = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            try:
                if start_time <= os.path.getctime(os.path.join(address, name)) <= end_time:
                    res.append(str((str(os.path.join(address, name)),
                                    datetime.datetime.strftime(
                                        datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(address, name))),
                                        '%Y.%m.%d'),
                                    str(os.path.getsize(os.path.join(address, name))) + ' б')))
                    file_v += os.path.getsize(os.path.join(address, name))
            except FileNotFoundError:
                pass
    res.append(str(file_v) + ' б ~= ' + str(file_v//1024) + ' кб ~=' + str(file_v//1024//1024) + ' мб ~=' + str(file_v//1024//1024//1024) + ' гб' )
    return res


def find_by_date(path='/Users', first_date='1970.01.01', second_date=today_da):
    stamp1 = datetime.datetime.strptime(first_date, '%Y.%m.%d').timestamp()
    stamp2 = datetime.datetime.strptime(second_date, '%Y.%m.%d').timestamp() + 86400
    return find_by_time(path, stamp1, stamp2)


def size_tr(size):
    if size == float('inf'):
        res = size
    else:
        if size[-2:].lower() == ' б':
            res = int(size[:-2]) * 8
        elif size[-2:].lower() == 'кб':
            res = int(size[:-2]) * 1024
        elif size[-2:].lower() == 'мб':
            res = int(size[:-2]) * 1024 * 1024
        elif size[-2:].lower() == 'гб':
            res = int(size[:-2]) * 1024 * 1024 * 1024
        else:
            res = int(size[:-2]) * 1024 * 1024 * 1024 * 1024
    return res


def find_by_size(path='/Users', min_size='0 б', max_size='10000000000 тб'):
    min_size_b = size_tr(min_size)
    max_size_b = size_tr(max_size)
    res = []
    file_v = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            try:
                if min_size_b <= os.path.getsize(os.path.join(address, name)) <= max_size_b:
                    res.append(str((str(os.path.join(address, name)),
                                    datetime.datetime.strftime(
                                        datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(address, name))),
                                        '%Y.%m.%d'),
                                    str(os.path.getsize(os.path.join(address, name))) + ' б')))
                    file_v += os.path.getsize(os.path.join(address, name))
            except FileNotFoundError:
                pass
    res.append(str(file_v) + ' б ~= ' + str(file_v//1024) + ' кб ~=' + str(file_v//1024//1024) + ' мб ~=' + str(file_v//1024//1024//1024) + ' гб' )
    return res


def find_by_regex(path='/Users', regex=''):
    res = []
    file_v = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            try:
                if re.search(regex, os.path.join(address, name)):
                    res.append(str((str(os.path.join(address, name)),
                                    datetime.datetime.strftime(
                                        datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(address, name))),
                                        '%Y.%m.%d'),
                                    str(os.path.getsize(os.path.join(address, name))) + ' б')))
                    file_v += os.path.getsize(os.path.join(address, name))
            except FileNotFoundError:
                pass
    res.append(str(file_v) + ' б ~= ' + str(file_v//1024) + ' кб ~=' + str(file_v//1024//1024) + ' мб ~=' + str(file_v//1024//1024//1024) + ' гб' )
    return res
