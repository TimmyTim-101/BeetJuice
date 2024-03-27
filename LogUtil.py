import time


def print_separate_line():
    print('-' * 66)
    pass


def print_double_separate_line():
    print('=' * 66)
    pass


def print_info(msg):
    s_time = time.time()
    print('[INFO] - ' + str(time.strftime("%Y-%m-%d %H:%M:%S.", time.localtime(s_time))) + format(int(s_time * 1000) % 1000, '03d') + ' -> ' + msg)
    pass
