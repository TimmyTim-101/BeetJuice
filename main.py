from LogUtil import print_double_separate_line, print_info
from SimulationLoop import SimulationLoop

if __name__ == '__main__':
    print_info('开始启动 }Beet Juice{')
    sl = SimulationLoop()
    print_info('截图根文件夹：' + sl.screenshot_folder)
    print_info('截图间隔时间：' + str(int(sl.sleep_time * 1000)) + 'ms')
    print_info('是否处于游玩中：' + str(sl.is_play_state))
    print_double_separate_line()
    sl.run()
    print_info('结束启动 }Beet Juice{')
    print_double_separate_line()
    pass
