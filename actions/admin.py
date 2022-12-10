from line_chatbot_api import *
from actions.service import *
from actions.access_data import *

def admin_menu(event):
    messages=[]
    messages.append(TextSendMessage(text='管理員功能',quick_reply=QuickReply(items=[
                                                    QuickReplyButton(action=PostbackAction(label="收集樣本",data='收集樣本')),
                                                    QuickReplyButton(action=PostbackAction(label="flex",data='flex')),
                                                    ])))
    line_bot_api.reply_message(event.reply_token, messages)

def collect(event, user_id):
    messages=[]
    messages.append(TextSendMessage(text='管理員功能：收集樣本',quick_reply=QuickReply(items=[QuickReplyButton(action=URIAction(label="打開白板寫寫看", uri='https://liff.line.me/1657646010-mWYvBkxr'))])))
    line_bot_api.reply_message(event.reply_token, messages)
    update_answer(user_id, 'collect')

def flex(event, user_id):
    hiragana=read_hiragana(user_id)
    hiragana0=read_hiragana0(user_id)
    hiragana_rate=get_hiragana_rate(hiragana, hiragana0)
    hiragana_wrong=get_hiragana_wrong(hiragana, hiragana0)
    messages=[]
    messages.append(FlexSendMessage(
    alt_text='假名測驗',
    contents=
    {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "size": "nano",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "分類",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "lg",
                    "gravity": "center"
                },
                {
                    "type": "text",
                    "text": "學習率(%)",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "xs",
                    "gravity": "center",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        }
                        ],
                        "width": "40%",
                        "backgroundColor": "#0D8186",
                        "height": "6px"
                    }
                    ],
                    "backgroundColor": "#9FD8E36E",
                    "height": "6px",
                    "margin": "sm"
                }
                ],
                "backgroundColor": "#27ACB2",
                "paddingTop": "19px",
                "paddingAll": "12px",
                "paddingBottom": "16px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "最常錯的字",
                        "color": "#8C8C8C",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    }
                    ],
                    "flex": 1
                }
                ],
                "spacing": "md",
                "paddingAll": "12px"
            },
            "styles": {
                "footer": {
                "separator": False
                }
            }
            },
            {
            "type": "bubble",
            "size": "nano",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "平假名",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "lg",
                    "gravity": "center"
                },
                {
                    "type": "text",
                    "text": "{:.0%}".format(hiragana_rate),
                    "color": "#ffffff",
                    "align": "start",
                    "size": "xs",
                    "gravity": "center",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        }
                        ],
                        "width": "{:.0%}".format(hiragana_rate),
                        "backgroundColor": "#DE5658",
                        "height": "6px"
                    }
                    ],
                    "backgroundColor": "#FAD2A76E",
                    "height": "6px",
                    "margin": "sm"
                }
                ],
                "backgroundColor": "#FF6B6E",
                "paddingTop": "19px",
                "paddingAll": "12px",
                "paddingBottom": "16px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": f"{hiragana_wrong}",
                        "color": "#8C8C8C",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    }
                    ],
                    "flex": 1
                }
                ],
                "spacing": "md",
                "paddingAll": "12px"
            },
            "styles": {
                "footer": {
                "separator": False
                }
            }
            },
            {
            "type": "bubble",
            "size": "nano",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "片假名",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "lg",
                    "gravity": "center"
                },
                {
                    "type": "text",
                    "text": "0%",
                    "color": "#ffffff",
                    "align": "start",
                    "size": "xs",
                    "gravity": "center",
                    "margin": "lg"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "filler"
                        }
                        ],
                        "width": "0%",
                        "backgroundColor": "#7D51E4",
                        "height": "6px"
                    }
                    ],
                    "backgroundColor": "#9FD8E36E",
                    "height": "6px",
                    "margin": "sm"
                }
                ],
                "backgroundColor": "#A17DF5",
                "paddingTop": "19px",
                "paddingAll": "12px",
                "paddingBottom": "16px"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "功能準備中",
                        "color": "#8C8C8C",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    }
                    ],
                    "flex": 1
                }       
                ],
                "spacing": "md",
                "paddingAll": "12px"
            },
            "styles": {
                "footer": {
                "separator": False
                }
            }
            }
        ]
    }
    ))
    messages.append(TextSendMessage(text='想測驗什麼呢？',quick_reply=QuickReply(items=[
                                                    QuickReplyButton(action=MessageAction(label='平假名測驗',text='平假名')),                                                                
                                                    QuickReplyButton(action=MessageAction(label='片假名測驗',text='片假名')),
                                                    ])))
    line_bot_api.reply_message(event.reply_token, messages)