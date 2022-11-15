from line_chatbot_api import *

def collect(event,answer):
    messages=[]
    messages.append(TextSendMessage(text='管理員功能：收集樣本',quick_reply=QuickReply(items=[
                                                                QuickReplyButton(action=URIAction(label="打開白板寫寫看", uri='https://liff.line.me/1657646010-mWYvBkxr')),
                                                                ])))
    line_bot_api.reply_message(event.reply_token, messages)
    answer='collect'
    return answer