import PySimpleGUI as sg

# from Servlet import UserServlet


# 初始化登录窗体
def login_init():
    sg.theme("DarkAmber")
    layout = [
        [sg.Text("Username"), sg.InputText()],
        [sg.Text("Password"), sg.InputText()],
        [sg.Button("Login"), sg.Button("Cancel")],
    ]
    return sg.Window("User", layout, finalize=True)


# 登录测试
def login_test():
    login_window = login_init()
    window, event, value = sg.read_all_windows()

    while True:
        window, event, value = sg.read_all_windows()
        if event == "Login":
            username = value[0]
            password = value[1]

            print("username:" + username)
            print("password:" + password)
            result = 1
            # result = us.login(username, password)
            if result != None:
                sg.popup(title="Login Success")

        elif event == "Cancel":
            break

    window.close()


login_test()
