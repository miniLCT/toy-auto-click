import pyautogui
from pynput import keyboard
import time

stop_program = False


# Key press handler
def on_press(key):
    global stop_program
    try:
        if key.char == 'q':  # Stop the auto-click when 'q' is pressed
            stop_program = True
            return False  # Stop listener
    except AttributeError:
        pass


# 连点器函数
def auto_click(x, y, interval=0.1):
    print("开始连点, 按 'q' 键中断")
    n = 0
    while not stop_program:
        pyautogui.click(x, y)  # 点击指定坐标
        time.sleep(interval)
        n += 1
        if n % 10 == 0:
            pyautogui.click(697, 587)  # 防止上面遮住下面，取不到
            time.sleep(interval)
            pyautogui.click(697, 587)  # 防止上面遮住下面，取不到
            # time.sleep(interval)
            pyautogui.click(697, 587)  # 防止上面遮住下面，取不到
            # time.sleep(interval)
        if n % 17 == 0:
            pyautogui.click(818, 699)  # 取炸弹
            time.sleep(0.5)
            pyautogui.click(697, 587)  # 炸上面一块
            time.sleep(interval)
            pyautogui.click(690, 539)
            time.sleep(interval)
        if n % 2101 == 0:
            time.sleep(interval*2)
            pyautogui.click(633, 705)  # 取锁头
            time.sleep(0.5)
            pyautogui.click(700, 334)  # 从上到下
            time.sleep(0.5)
        # 主函数


def main():
    # 等待用户确认准备开始连点
    print("请按 's' 键开始连点")

    # Wait for 's' key press
    with keyboard.Events() as events:
        for event in events:
            if isinstance(event, keyboard.Events.Press) and event.key.char == 's':
                break

    # 651, 635
    # (683, 645)
    click_x = 683
    click_y = 645

    # 开始自动点击
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    auto_click(click_x, click_y)
    listener.join()


if __name__ == "__main__":
    main()
