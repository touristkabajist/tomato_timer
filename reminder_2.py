###
#app reminder 0.1.1
import tkinter as tk
import tkinter.font as tkFont
from threading import Timer

class CustomDialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        top.title("弹窗番茄钟")  # Set window title
        top.attributes('-topmost', True)  # Make the window always stay on top
        
         # Make the window appear in the center of the screen
        window_width = top.winfo_reqwidth()
        window_height = top.winfo_reqheight()
        position_right = int(top.winfo_screenwidth()/2 - window_width/2)
        position_down = int(top.winfo_screenheight()/2 - window_height/2)
        top.geometry("+{}+{}".format(position_right, position_down))
        
        tk.Label(top, text="休息时间到啦！站起来走走吧QwQ\n是否进入30分钟倒计时?", font=tkFont.Font(family="Lucida Grande", size=32)).pack()
        button_frame = tk.Frame(top)
        button_frame.pack(fill="x", ipadx=5, ipady=5)
        
        tk.Button(button_frame, text="确认", command=self.ok, font=tkFont.Font(family="Lucida Grande", size=32)).pack(side="left", padx=10)
        tk.Button(button_frame, text="取消", command=self.cancel, font=tkFont.Font(family="Lucida Grande", size=32)).pack(side="right", padx=10)
        self.result = False

    def ok(self):
        self.result = True
        self.top.destroy()

    def cancel(self):
        self.result = False
        self.top.destroy()

class CountdownWindow:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        top.title("弹窗番茄钟")  # Set window title
        self.label = tk.Label(top, text="", font=tkFont.Font(family="Lucida Grande", size=32))
        self.label.pack()
        
    def update(self, text):
        self.label.config(text=text)

class App:
    def __init__(self, root):
        self.root = root
        self.countdown = None
        self.countdown_window = None
        self.root.withdraw()
        self.ask()

    def ask(self):
        dialog = CustomDialog(self.root)
        self.root.wait_window(dialog.top)
        if dialog.result:
            self.countdown = 30*60 # 30 minutes in seconds 30*60
            self.countdown_window = CountdownWindow(self.root)
            self.update_timer()
        else:
            self.root.destroy()

    def update_timer(self):
        if self.countdown:
            self.countdown -= 1
            minutes, seconds = divmod(self.countdown, 60)
            self.countdown_window.update(f"剩余时间: {minutes} 分 {seconds} 秒")
            self.root.after(1000, self.update_timer)  # Call this method after 1 second.
        else:
            self.countdown_window.top.destroy()
            self.countdown_window = None
            self.ask()  # Restart the countdown

root = tk.Tk()
root.attributes('-topmost', True)
root.geometry('500x500')  # Adjust the size according to your content and font size.

app = App(root)

root.mainloop()
