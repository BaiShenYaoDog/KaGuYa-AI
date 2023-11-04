import utils

utils.Live = False
utils.ChatGLMinit()

def Chat():
    InputText = input()
    print(utils.get_resp(InputText))
    Chat()
Chat()