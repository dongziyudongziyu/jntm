import time
import keyboard
import sys
import os
import sys
import pygame
pygame.init()
pygame.mixer.init()
# Global variables
last_press_time = None
exit_key = 'esc'
press_count = 0
last_press_time = None
if getattr(sys, 'frozen', False):
    # 如果是打包后的可执行文件
    base_path = sys._MEIPASS
else:
    # 如果是普通的 Python 脚本
    base_path = os.path.abspath(".")
sounds = {
    "j": pygame.mixer.Sound(os.path.join(base_path, "sounds\\j.mp3")),
    "n": pygame.mixer.Sound(os.path.join(base_path, "sounds\\n.mp3")),
    "t": pygame.mixer.Sound(os.path.join(base_path, "sounds\\t.mp3")),
    "m": pygame.mixer.Sound(os.path.join(base_path, "sounds\\m.mp3")),
    "q": pygame.mixer.Sound(os.path.join(base_path, "sounds\\quanminzhizuoren.mp3")),
    "a": pygame.mixer.Sound(os.path.join(base_path, "sounds\\aha.mp3")),
    "l": pygame.mixer.Sound(os.path.join(base_path, "sounds\\lanqiu.mp3")),
}

def play_sound(pygameMusic):
    print("play sound")
    pygameMusic.play()
    # global sound_dir
    # sound_path = os.path.join("./", sound_file)
    # if os.path.exists(sound_path) :
    #     print("file path:", sound_path)
    #     playsound(sound_path)
    #     # audio = AudioSegment.from_file(sound_path)
    #     # play(audio)

def on_key_event(e):
    global sounds
    if e.event_type == "down":
        key_name = e.name
        current_time = time.time()
        print("key:", key_name)
        if key_name == exit_key :
            exit_process(key_name)
        if key_name in sounds.keys() and sounds[key_name] is not None :
            play_sound(sounds[key_name])
        else:
            None

def exit_process(key_name):
    global press_count, last_press_time
    if key_name == exit_key:
        current_time = time.time()
        
        if last_press_time is not None:
            elapsed_time = current_time - last_press_time
            if elapsed_time <= 1.0:
                print("连续按两次，退出程序")
                exit(0)
            else:
                # 重置计数器
                press_count = 1
        else:
            press_count = 1
        
        last_press_time = current_time
    else:
        # 清除计数器和时间戳
        press_count = 0
        last_press_time = None

def main():
    keyboard.hook(on_key_event)
    # atexit.register(save_data_on_exit)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    # finally:
        # save_data_on_exit()
        
main()