import random
from urllib.parse import parse_qsl, parse_qs
from line_chatbot_api import *

def hiragana_test(event):
    # hiragana = dict(a='あ',i='い',u='う',e='え',o='お',
    #                 ka='か',ki='き',ku='く',ke='け',ko='こ',
    #                 sa='さ',si='し',su='す',se='せ',so='そ',
    #                 ta='た',chi='ち',tsu='つ',te='て',to='と',
    #                 na='な',ni='に',nu='ぬ',ne='ね',no='の',
    #                 ha='は',hi='ひ',hu='ふ',he='へ',ho='ほ',
    #                 ma='ま',mi='み',mu='む',me='め',mo='も',
    #                 ya='や',yu='ゆ',yo='よ',
    #                 wa='わ',wo='を',n='ん')
    hiragana = dict(a='あ',i='い',u='う',e='え',o='お',
                    ka='か',ki='き',ku='く',ke='け',ko='こ',
                    sa='さ',shi='し',su='す',se='せ',so='そ',
                    ta='た',chi='ち',tsu='つ',te='て',to='と',
                    na='な',ni='に',nu='ぬ',ne='ね',no='の',
                    ha='は',hi='ひ',fu='ふ',he='へ',ho='ほ',
                    ma='ま',mi='み',mu='む',me='め',mo='も',)
    key = random.choice(list(hiragana.keys()))
    messages=[]
    messages.append(TextSendMessage(text=f"[{key}]的平假名怎麼寫？",quick_reply=QuickReply(items=[
                                                                # QuickReplyButton(action=CameraAction(label="開啟相機辨識")),
                                                                # QuickReplyButton(action=CameraRollAction(label="相機膠卷")),
                                                                QuickReplyButton(action=URIAction(label="打開白板寫寫看", uri='https://liff.line.me/1657646010-mWYvBkxr')),
                                                                ])))
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
#                     wa='ワ',wo='ヲ',n='ン')
#     key = random.choice(list(katakana.keys()))
    # messages=[]
#     messages.append(TextSendMessage(text=f"[{key}]的片假名怎麼寫？",quick_reply=QuickReply(items=[
#                                                                 QuickReplyButton(action=CameraAction(label="開啟相機辨識")),
#                                                                 QuickReplyButton(action=CameraRollAction(label="相機膠卷")),
#                                                                 ])))
#     line_bot_api.reply_message(event.reply_token, messages)
#     return katakana[key] # return the answer