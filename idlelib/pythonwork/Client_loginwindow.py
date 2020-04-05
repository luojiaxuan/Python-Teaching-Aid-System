import tkinter as tk
import tkinter.ttk as ttk


class LoginWindow():

    def __init__(self):
        self.frame=tk.Tk()

        # 设置界面的基本属性
        self.frame.title("登录界面")
        self.frame.geometry("600x400+500+300")
        self.frame["bg"] = "RoyalBlue"
        self.frame.resizable(0,0)

        self.design_ui()

    def design_ui(self):

        from PIL import Image, ImageTk

        # 先定义需要的样式style
        self.frame.Style_01 = ttk.Style()
        self.frame.Style_01.configure("text_01",font=("微软雅黑",16,"bold"),foreground="white",background="RoyalBlue")

        # 创建一个Label展示图片,photpimage仅仅只能支持gif格式
        self.frame.login_image = Image.open("D:\\毕业设计3-13\\idlelib\\pythonwork\\python_login2.gif")
        self.frame.login_photo = ImageTk.PhotoImage(self.frame.login_image)
        self.frame.image_label = tk.Label(self.frame, image=self.frame.login_photo)
        self.frame.image_label.pack()

        # 创建两个文本输入框，分别输入学号userid和密码password
        self.frame.Label_userid = tk.Label(self.frame,text="学号",font=("微软雅黑",14,"bold"),foreground="white",background="RoyalBlue").pack(side=tk.LEFT,padx=20)
        self.frame.Value_userid = tk.StringVar()
        self.frame.Entry_userid = tk.Entry(self.frame,width="10",textvariable=self.frame.Value_userid).pack(side=tk.LEFT,padx=20)
        self.frame.Label_password = tk.Label(self.frame,text="密码",font=("微软雅黑",14,"bold"),foreground="white",background="RoyalBlue").pack(side=tk.LEFT,padx=20)
        self.frame.Value_password = tk.StringVar()
        self.frame.Entry_password = tk.Entry(self.frame, width="10",textvariable=self.frame.Value_password,show="·").pack(side=tk.LEFT,padx=20)


        # 创建按钮 登录 和 退出 , 并为按钮捆绑onclick函数(注意不要加小括号)
        self.frame.Button_login = tk.Button(self.frame,text="登录",command=self.send_loginmsg).pack(side=tk.LEFT,padx=20)
        self.frame.Button_return = tk.Button(self.frame,text="退出").pack(side=tk.LEFT,padx=20)

    def show(self):
        self.frame.mainloop()

    def send_loginmsg(self):
        # 获取输入的用户名和密码
        userid = self.frame.Value_userid.get()
        password = self.frame.Value_password.get()

        self.open_IDLEwindow()

    # 获取输入的用户名和密码
    def get_userid(self):
        return self.frame.Value_userid.get()

    def get_password(self):
        return self.frame.Value_password.get()

    def open_IDLEwindow(self):

        # 删除旧的窗体
        self.frame.destroy()

        # 加载新的窗体
        try:
            # modify by luojiaxuan
            import sys
            sys.path.append("../")
            import pyshell
        except ImportError:
            # IDLE is not installed, but maybe pyshell is on sys.path:
            from . import pyshell
            import os
            idledir = os.path.dirname(os.path.abspath(pyshell.__file__))
            if idledir != os.getcwd():
                # We're not in the IDLE directory, help the subprocess find run.py
                pypath = os.environ.get('PYTHONPATH', '')
                if pypath:
                    os.environ['PYTHONPATH'] = pypath + ':' + idledir
                else:
                    os.environ['PYTHONPATH'] = idledir
            pyshell.main()
        else:
            # modify by luojiaxuan
            pyshell.main(self.get_userid())
            # idlelib.PyShell.main(self.get_userid())




if __name__ == "__main__":
    this_login = LoginWindow()
    this_login.show()





