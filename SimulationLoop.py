import os.path
import subprocess
import time

import cv2
import keyboard
import uiautomator2

from LogUtil import print_info


class SimulationLoop:

    def __init__(self):
        self.screenshot_folder = os.path.dirname(os.path.abspath(__file__)) + '/Screenshots/'
        self.sleep_time_long = 1
        self.sleep_time_short = 0.1
        self.sleep_time = self.sleep_time_long
        self.is_play_state = False
        self.sub_folder_name = str(int(time.time() * 1000))
        self.adb_device = '127.0.0.1:7555'
        pass

    def do_screen_shot(self):
        this_screen_shot_path = self.screenshot_folder
        if self.is_play_state:
            this_screen_shot_path += self.sub_folder_name + '/'
            pass
        if os.path.exists(this_screen_shot_path) is False:
            os.mkdir(this_screen_shot_path)
            pass
        this_screen_shot_path += str(int(time.time() * 1000)) + '.png'
        command = ["adb", "-d", "shell", "screencap -p /storage/emulated/0/temp.png"]
        subprocess.run(command)
        command = ["adb", "-d", "pull", "/storage/emulated/0/temp.png", this_screen_shot_path]
        subprocess.run(command)
        pass

    def judge_play_state(self):
        return False

    def run(self):
        while True:
            try:
                print_info('在main_loop中循环')
                if keyboard.is_pressed('z'):
                    print_info('检测到按下z键，将退出循环')
                    break
                    pass
                # 截图
                self.do_screen_shot()
                # 分析是不是在游戏中
                current_play_state = self.judge_play_state()
                if current_play_state != self.is_play_state:
                    if current_play_state:
                        # 进入到模拟状态
                        self.is_play_state = current_play_state
                        self.sleep_time = self.sleep_time_short
                        self.sub_folder_name = str(int(time.time() * 1000))
                        print_info('^^游戏状态变为模拟状态，截图频率调整为' + str(self.sleep_time))
                        pass
                    else:
                        # 模拟状态结束
                        self.is_play_state = current_play_state
                        self.sleep_time = self.sleep_time_long
                        print_info('^^游戏状态变为待机状态，截图频率调整为' + str(self.sleep_time))
                        pass
                    pass
                if self.is_play_state:
                    # 是的话开始模拟手打
                    pass
                else:
                    # 不是的话处于待机状态
                    pass
                time.sleep(self.sleep_time)
                pass
            except KeyboardInterrupt:
                break
            pass
        pass

    pass
