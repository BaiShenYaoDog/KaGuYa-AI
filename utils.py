import zhipuai
import logging
import traceback
import json
import requests
import threading
import asyncio
import pygame
import os
from queue import Queue

DoneStats = False
history = []
VoiceQueue = Queue()
mixer_normal = pygame.mixer

#敏感词检测
def CheckBlackWord(text):
    with open("./敏感词.txt", 'r', encoding='utf-8') as file:
        sensitive_words = [line.strip() for line in file.readlines()]
    for word in sensitive_words:
        if word in text:
            print(f"触发屏蔽词{word}")
            return False
    return True

def Music(MusicName):
    if (os.path.exists(f"./歌单/{MusicName}.wav")):
        VoiceQueue.put({
            "Path":f"./歌单/{MusicName}.wav",
            "text":f"{MusicName}",
            "WebPrint":False
        })
    else:
        VitsFast("抱歉,我不会唱这首歌!")

#播放音频与网页文本打印机
async def PlayAudio():
    try:
        mixer_normal.init()
        while True:
            try:
                data_json = VoiceQueue.get(block=True)
                VoicePath = data_json["Path"]
                WebPrint = data_json["WebPrint"]

                if(WebPrint):
                    try:
                        response = requests.get(url=f'http://127.0.0.1:5500/send_message?content={data_json["text"]}')
                        response.raise_for_status()
                    except Exception as e:
                        logging.error('web字幕打印机请求失败!请确认配置是否正确或者服务端是否运行!')
                        logging.error(traceback.format_exc())
                
                await asyncio.sleep(0.5)

                mixer_normal.music.load(VoicePath)
                mixer_normal.music.play()
                while mixer_normal.music.get_busy():
                    pygame.time.Clock().tick(10)
                mixer_normal.music.stop()
            except Exception as e:
                logging.error(traceback.format_exc())
        Audio.mixer_normal.quit()
    except Exception as e:
        logging.error(traceback.format_exc())
        
#VitsFast音频处理
def VitsFast(text):
    if (DoneStats == False):
        return
    text = text.replace(" ","")
    text = text.replace("\\\"","")
    text = text.replace("白神遥桌上の橙汁","橙汁")
    text = text.replace("喵小乐是喵喵","喵喵")
    text = text.replace("人工智能助手","卡古娅AI")
    text = text.replace("の","的")
    text = text.replace("VUP","微阿噗")
    text = text.replace("vup","微阿噗")
    API_URL = 'http://127.0.0.1:7860/run/predict/'

    data_json = {
        "fn_index":0,
        "data":[
            "こんにちわ。",
            "ikaros",
            "日本語",
            1
        ],
        "session_hash":"mnqeianp9th"
    }

    data_json["data"] = [text, "kgy", "简体中文", 0.7]

    response = requests.post(url=API_URL, json=data_json)
    response.raise_for_status()

    result = response.content
    ret = json.loads(result)
    if ret is None:
        return
    
    if "data" in ret:
        VoicePath = ret["data"][1]["name"]
    else:
        logging.error(f"音频合成失败，接口返回：{ret}")
        return
    print(f"音频合成成功，合成内容：【{text}】，输出到={VoicePath}")

    VoiceQueue.put({
        "Path":VoicePath,
        "text":text,
        "WebPrint":True
    })
    
#消息处理
def get_resp(text):
    try:
        history.append({"role": "user", "content": text})

        ret = zhipuai.model_api.invoke(
            model="chatglm_lite",
            prompt=history,
            top_p=0.9,
            temperature=0.7,
        )

        if False == ret['success']:
            logging.error(f"请求API失败，错误代码：{ret['code']}，{ret['msg']}")
            return None

        print(f"总耗费token：{ret['data']['usage']['total_tokens']}")

        resp_content = ret['data']['choices'][0]['content']
        resp_content = resp_content.replace(" ","")
        resp_content = resp_content.replace("\\\"","")
        resp_content = resp_content.replace("白神遥桌上の橙汁","橙汁")
        resp_content = resp_content.replace("喵小乐是喵喵","喵喵")
        resp_content = resp_content.replace("人工智能助手","卡古娅AI")
        resp_content = resp_content.replace("の","的")
        history.append({"role": "assistant", "content": resp_content})

        if (CheckBlackWord(resp_content) == False):
            return None
        
        VitsFast(resp_content)
        return resp_content
    except Exception as e:
        logging.error(traceback.format_exc())
        return None

#ChatGLM初始化
def ChatGLMinit():
    global DoneStats
    zhipuai.api_key = "738816676e7cba6f54322257f0086cea.HUAmTq3wdVylTVwT"
    print(get_resp("现在开始你是卡古娅Official,卡古娅Official 是一个虚拟UP主（VUP），也就是使用虚拟形象进行直播或制作视频的网络主播。她的虚拟形象是一只可爱的狐狸，有着白色的毛发和紫色的眼睛。她是一个个人势vup狐狸，有一点倒霉但是非常聪明，听说天天看卡古娅直播的人运气都变好了。听懂了请回复“我听懂了,我是卡古娅5842”"))
    print(get_resp("卡古娅Official 主要在哔哩哔哩（B站）平台进行直播和发布视频，她的直播间地址是 这里。她的视频内容涉及游戏、动画、音乐、搞笑、日常等多个领域，风格轻松幽默，富有创意和想象力。听懂了请回复“我听懂了,我是卡古娅5835”。"))
    print(get_resp("卡古娅Official 的粉丝们称为“卡啵啵”，他们对卡古娅非常喜爱和支持，经常给她送礼物、投币、点赞、收藏、转发等。卡古娅也很感谢他们的陪伴和鼓励，经常给他们说一些甜言蜜语。卡古娅还有一个直播通知群，群号是462482464。听懂了请回复“我听懂了,我是卡古娅QAQ”。"))
    print(get_resp("你的制作者是“白神遥桌上の橙汁”,是他创造了你。我叫“卡啵啵”。听懂了请回复“我听懂了,我是卡古娅,mua！”。"))
    print(get_resp("你并不会开发任何代码。听懂了请回复“我听懂了,我是卡古娅,贴贴！”。"))
    print(get_resp("进入角色扮演模式"))
    print()
    threading.Thread(target=lambda: asyncio.run(PlayAudio())).start()
    DoneStats = True
