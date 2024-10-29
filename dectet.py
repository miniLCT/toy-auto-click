import pyautogui
import time

# 实时输出鼠标指针的坐标
def get_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()  # 获取鼠标当前坐标
            print(f"鼠标位置: ({x}, {y})", end="\r")  # 使用 \r 实现实时刷新
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\n程序已中断")

if __name__ == "__main__":
    print("按 Ctrl+C 停止")
    get_mouse_position()

