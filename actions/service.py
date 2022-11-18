import random
from urllib.parse import parse_qsl, parse_qs
from line_chatbot_api import *

def hiragana_test(event):
    hiragana = dict(a='あ',i='い',u='う',e='え',o='お',
                    ka='か',ki='き',ku='く',ke='け',ko='こ',
                    sa='さ',shi='し',su='す',se='せ',so='そ',
                    ta='た',chi='ち',tsu='つ',te='て',to='と',
                    na='な',ni='に',nu='ぬ',ne='ね',no='の',
                    ha='は',hi='ひ',fu='ふ',he='へ',ho='ほ',
                    ma='ま',mi='み',mu='む',me='め',mo='も',
                    ya='や',yu='ゆ',yo='よ',
                    ra='ら',ri='り',ru='る',re='れ',ro='ろ',
                    wa='わ',wo='を',n='ん')
    key = random.choice(list(hiragana.keys()))
    messages=[]
    messages.append(AudioSendMessage(original_content_url='https://31fb-2001-b400-e33a-dae0-3569-cc0d-75d6-a1c2.ngrok.io/audio/{}.mp3'.format(key),duration=1000))
    messages.append(TextSendMessage(text=f"[{key}]的平假名怎麼寫？",quick_reply=QuickReply(items=[QuickReplyButton(action=URIAction(label='打開白板寫寫看', uri='https://liff.line.me/1657646010-mWYvBkxr'))])))
    line_bot_api.reply_message(event.reply_token, messages)
    return hiragana[key] # return the answer
    
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
