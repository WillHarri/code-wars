def time_convert(time):
    time1 = int(time / 60)
    time2 = time % 60
    print (f'{time1}:{time2}')

time_convert(139)