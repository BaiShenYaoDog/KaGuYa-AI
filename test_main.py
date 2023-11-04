import utils

utils.Debug = True
utils.Live = False
utils.ChatGLMinit()

def Chat():
    InputText = input()
    if (InputText.isspace() == False):
        print(utils.get_resp(InputText))
    Chat()
Chat()