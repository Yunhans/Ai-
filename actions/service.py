import random
from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *

def hiragana_test(event):
    hiragana = dict(a='あ',i='い',u='う',e='え',o='お',
                    ka='か',ki='き',ku='く',ke='け',ko='こ',
                    sa='さ',si='し',su='す',se='せ',so='そ',
                    ta='た',ti='ち',tu='つ',te='て',to='と',
                    na='な',ni='に',nu='ぬ',ne='ね',no='の',
                    ha='は',hi='ひ',hu='ふ',he='へ',ho='ほ',
                    ma='ま',mi='み',mu='む',me='め',mo='も',
                    ya='ya',yu='ゆ',yo='よ',
                    wa='わ',wo='を',n='ん')
    key = random.choice(list(hiragana.keys()))
    messages=[]
    messages.append(TextSendMessage(text=f"請寫出{key}"))
    line_bot_api.reply_message(event.reply_token, messages)
    

def katakana_test(event):
    katakana = dict(a='ア',i='イ',u='ウ',e='エ',o='オ',
                    ka='カ',ki='キ',ku='ク',ke='ケ',ko='コ',
                    sa='サ',si='シ',su='ス',se='セ',so='ソ',
                    ta='タ',ti='チ',tu='ツ',te='テ',to='ト',
                    na='ナ',ni='ニ',nu='ヌ',ne='ネ',no='ノ',
                    ha='ハ',hi='ヒ',hu='フ',he='ヘ',ho='ホ',
                    ma='マ',mi='ミ',mu='ム',me='メ',mo='モ',
                    ya='ヤ',yu='ユ',yo='ヨ',
                    wa='ワ',wo='ヲ',n='ン')
    key = random.choice(list(katakana.keys()))
    messages=[]
    messages.append(TextSendMessage(text=f"請寫出{key}"))
    line_bot_api.reply_message(event.reply_token, messages)
    
