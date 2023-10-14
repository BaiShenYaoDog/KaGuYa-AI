import logging
import traceback
import os
import utils
import datetime
from bilibili_api import live, sync, login

def start():
    #登录
    try:
        credential = login.login_with_qrcode()
        room = live.LiveDanmaku(21854213, credential=credential)
    except Exception as e:
        logging.error(traceback.format_exc())

    #弹幕
    @room.on('DANMU_MSG')
    async def _(event):
        content = event["data"]["info"][1]
        if ("[" in content and "]" in content):
            return
        user_name = event["data"]["info"][2][1]
        print(f"[{user_name}]: {content}")
        utils.VitsFast(content)
        print(utils.get_resp(content))

    #礼物
    @room.on('SEND_GIFT')
    async def _(event):
        gift_name = event["data"]["data"]["giftName"]
        user_name = event["data"]["data"]["uname"]
        num = event["data"]["data"]["num"]
        print(f"{user_name} 赠送 {num} 个 {gift_name}")
        text = f"感谢{user_name}的{num}个{gift_name}! 老板大气! 啵啵!"
        utils.VitsFast(text)

    #大航海
    @room.on('GUARD_BUY')
    async def _(event):
        print(event)
        user_name = event["data"]["data"]["username"]
        gift_name = event["data"]["data"]["gift_name"]
        text = f"感谢{user_name}的{gift_name}! 老板大气!"
        utils.VitsFast(text)

    #SC
    @room.on('SUPER_CHAT_MESSAGE')
    async def _(event):
        message = event["data"]["data"]["message"]
        user_name = event["data"]["data"]["user_info"]["uname"]
        price = event["data"]["data"]["price"]
        print(f"{user_name} 发送 {price}元 SC：{message}")
        text = f"感谢{user_name}的{price}元SC! 老板大气! 啵啵!"
        utils.VitsFast(text)

    #进入直播间
    @room.on('INTERACT_WORD')
    async def _(event):
        user_name = event["data"]["data"]["uname"]
        print(f"{user_name} 进入直播间")
        text = "欢迎"+user_name
        if (datetime.datetime.now().hour >= 6 and datetime.datetime.now().hour <= 10):
            text = f"上午好!{user_name}!啵啵!"
        if (datetime.datetime.now().hour >= 11 and datetime.datetime.now().hour <= 12):
            text = f"中午好!{user_name}!啵啵!"
        if (datetime.datetime.now().hour >= 13 and datetime.datetime.now().hour <= 17):
            text = f"下午好!{user_name}!啵啵!"
        if (datetime.datetime.now().hour >= 18 and datetime.datetime.now().hour <= 23):
            text = f"晚上好!{user_name}!啵啵!"
        if (datetime.datetime.now().hour >= 0 and datetime.datetime.now().hour <= 5):
            text = f"晚上好!{user_name}!啵啵!"
        utils.VitsFast(text)

    #启动 Bilibili 直播间连接
    try:
        sync(room.connect())
    except KeyboardInterrupt:
        logging.warning('程序被强行退出')
    finally:
        logging.warning('关闭连接...')
        os._exit(0)