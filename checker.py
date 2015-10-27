# -*- coding: utf-8 -*-

data_file = open('data_zhuanyeke', 'r')

step = 0
begin = 0
while True:
    step += 1
    data = data_file.readline()
    data_arr = data.split(',')
    if step < begin or len(data_arr) < 11 or not data_arr[7] or not data_arr[8]:
        continue
    if not data:
        break
    if data_arr[4].split('-')[0] and data_arr[4].split('-')[1]:
        try:
            a = int(data_arr[4].split('-')[0])
            b = int(data_arr[4].split('-')[1])
        except:
            print data_arr
            break
    print step
