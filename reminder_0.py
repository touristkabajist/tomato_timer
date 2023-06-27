###
#app reminder 0.0.1
import time
import ctypes

def message_box(title, text, style):
    result = ctypes.windll.user32.MessageBoxW(0, text, title, style)
    return result

while True:
    result = message_box('提醒', '是否开始倒计时30分钟？', 1)
    if result == 1:  # 如果用户点击了"确定"
        time.sleep(1800)  # 等待30分钟
        message_box('提醒', '起身活动5min', 0)  # 倒计时结束后的消息
    elif result == 2:  # 如果用户点击了"取消"
        break  # 退出程序
