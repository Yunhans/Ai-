import random
from urllib.parse import parse_qsl, parse_qs
from line_chatbot_api import *

roma = ['a','i','u','e','o','ka','ki','ku','ke','ko','sa','shi','su','se','so','ta','chi','tsu','te','to','na','ni','nu','ne','no','ha','hi','fu','he','ho','ma','mi','mu','me','mo','ya','yu','yo','ra','ri','ru','re','ro','wa','wo','n']


def hiragana_test(event):
    hiragana = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん']
    key = random.randint(0,45)
    messages=[]
    messages.append(AudioSendMessage(original_content_url='https://31fb-2001-b400-e33a-dae0-3569-cc0d-75d6-a1c2.ngrok.io/audio/{}.mp3'.format(roma[key]),duration=1000))
    messages.append(TextSendMessage(text=f"[{roma[key]}]的平假名怎麼寫？",quick_reply=QuickReply(items=[QuickReplyButton(action=URIAction(label='打開白板寫寫看', uri='https://liff.line.me/1657646010-mWYvBkxr'))])))
    line_bot_api.reply_message(event.reply_token, messages)
    return [hiragana[key],key] # return the answer and key

def get_hiragana_rate(hiragana, hiragana0):
    hiragana_rate=0
    hiragana_rate_list=[]
    for i in range(46):
        if hiragana[i] != 0:
            hiragana_rate_list.append(hiragana0[i]/hiragana[i])
        else:
            hiragana_rate_list.append(0)
    print(hiragana_rate_list)
    for i in range(46):
        if hiragana_rate_list[i]>=0.6:
            hiragana_rate+=1
    hiragana_rate=hiragana_rate/46
    print('hiragana_rate:{:.0%}'.format(hiragana_rate))  
    return hiragana_rate

def get_hiragana_wrong(hiragana, hiragana0):
    hiragana_list = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん']
    hiragana_rate_list=[]
    hiragana_wrong=''
    for i in range(46):
        if hiragana[i] != 0:
            hiragana_rate_list.append(hiragana0[i]/hiragana[i])
        else:
            hiragana_rate_list.append(2)
    print(hiragana_rate_list)
    for i in range(3):
        word_rate = min(hiragana_rate_list)
        if word_rate < 1:
            index = hiragana_rate_list.index(word_rate)
            hiragana_wrong += '' if hiragana_wrong=='' else ' , '
            hiragana_wrong += hiragana_list[index] 
            hiragana_rate_list.pop(index)
            hiragana_list.pop(index)
    if hiragana_wrong == '':
        hiragana_wrong = '統計中'
    print(hiragana_wrong)
    return hiragana_wrong
            

# def katakana_test(event):
#     katakana = dict(a='ア',i='イ',u='ウ',e='エ',o='オ',
#                     ka='カ',ki='キ',ku='ク',ke='ケ',ko='コ',
#                     sa='サ',shi='シ',su='ス',se='セ',so='ソ',
#                     ta='タ',chi='チ',tsu='ツ',te='テ',to='ト',
#                     na='ナ',ni='ニ',nu='ヌ',ne='ネ',no='ノ',
#                     ha='ハ',hi='ヒ',fu='フ',he='ヘ',ho='ホ',
#                     ma='マ',mi='ミ',mu='ム',me='メ',mo='モ',
#                     ya='ヤ',yu='ユ',yo='ヨ',
#                     ra='ラ',ri='リ',ru='ル',re='レ',ro='ロ',
#                     wa='ワ',wo='ヲ',n='ン')
#     key = random.choice(list(katakana.keys()))
    # messages=[]
#     messages.append(TextSendMessage(text=f"[{key}]的片假名怎麼寫？",quick_reply=QuickReply(items=[
#                                                                 QuickReplyButton(action=CameraAction(label="開啟相機辨識")),
#                                                                 QuickReplyButton(action=CameraRollAction(label="相機膠卷")),
#                                                                 ])))
#     line_bot_api.reply_message(event.reply_token, messages)
#     return katakana[key] # return the answer

def end_test(event):
    messages=[]
    i = random.randint(0,7)
    j = random.randint(1,2)
    sticker=[['446','2022','2023'],
            ['789','10876','10890'],
            ['6325','10979907','10979914'],
            ['6362','11087923','11087930'],
            ['8515','16581252','16581259'],
            ['8525','16581300','16581307'],
            ['11537','52002757','52002761'],
            ['11539','52114120','52114121']]
    messages.append(StickerSendMessage(package_id=sticker[i][0],sticker_id=sticker[i][j]))
    messages.append(TextSendMessage(text='辛苦了！'))
    line_bot_api.reply_message(event.reply_token, messages)
