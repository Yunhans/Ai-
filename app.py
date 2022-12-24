# import flask related
from flask import Flask, request, abort, render_template, make_response, url_for, Response
from PIL import Image, ImageOps
#new
from flask_bootstrap import Bootstrap
import os
import uuid
import base64
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)

#end new
from linebot.models import events
from line_chatbot_api import *
from actions.service import *
from actions.hiragana_notify import *
from actions.katakana_notify import *
from actions.admin import *
from actions.access_data import *

# create flask server
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def do_get():
    return render_template('index.html')

@app.route('/saveimage', methods=['POST'])
def saveimage():
    event = request.form.to_dict()
    dir_name = 'static/imgs'
    img_name = uuid.uuid4().hex

    # Saving image in the 'imgs' folder temporarily. Should be deleted after a certain period of time
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(os.path.join(dir_name, '{}.png'.format(img_name)), 'wb') as img:
        img.write(base64.b64decode(event['image'].split(",")[1]))
    return make_response(img_name, 200)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


# answer = ''
@handler.add(MessageEvent)
def handle_something(event):
    user_id=read_user_id(event.source.user_id)
    if event.message.type=='text':
        # global answer
        # answer = ''
        receive_text=event.message.text
        # print(recrive_text)
        if '使用說明' in receive_text:
            messages=[]
            # messages.append(TextSendMessage(text='歡迎使用AIあイ'))
            # messages.append(TextSendMessage(text='以下是使用說明的影片'))
            messages.append(TextSendMessage(text='此功能準備中'))
            line_bot_api.reply_message(event.reply_token, messages)  
        elif '50音表' in receive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://imgur.com/FRkwLch.png', preview_image_url='https://imgur.com/FRkwLchl.png'))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '假名測驗' in receive_text:
            flex(event, user_id)
        elif '平假名' in receive_text:
            hiragana_test(event, user_id)
        elif '片假名' in receive_text:
            katakana_test(event, user_id)
            # line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此功能準備中'))
        elif '我累了' in receive_text:
            end_test(event)
        elif 'Admin' in receive_text:
            admin_menu(event)
        else:
            messages=[]
            messages.append(StickerSendMessage(package_id=789, sticker_id=10882))
            messages.append(TextSendMessage(text='抱歉我聽不懂你說的意思~'))
            messages.append(TextSendMessage(text='可以用其他方式再說一次嗎?'))
            line_bot_api.reply_message(event.reply_token, messages)
    elif event.message.type=='image':
        answer=read_answer(user_id)
        hiragana = ['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん']
        katakana = ['ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン']
        if answer in hiragana:
            hiragana_notify(event, answer, user_id)
        elif answer in katakana:
            katakana_notify(event, answer, user_id)
        elif answer == 'collect':
            collect(event, user_id) # 繼續收集樣本
    elif event.message.type=='audio':
        filename_wav=f'static/user_voice/{user_id}.wav'
        filename_aac=f'static/user_voice/{user_id}.aac'
        # filename_mp3=f'static/user_voice/{user_id}.mp3'
        message_content = line_bot_api.get_message_content(event.message.id)
        with open(filename_aac, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        fd.close()
        # convert mp3 to wav                  
        os.system(f'ffmpeg -y -i {filename_aac} {filename_wav} -loglevel quiet')
        # shutil.move(filename_wav, f'class_imgs/hiragana/{prediction_string_result}/{imgName}')
        os.rename(filename_wav,f'static/user_voice/{uuid.uuid4().hex}.wav')

        # text = predict(filename_wav)
        # print(text)
        # messages=[]
        # messages.append(TextSendMessage(text=text))
        # line_bot_api.reply_message(event.reply_token, messages)



@handler.add(PostbackEvent)
def handle_postback(event):
    user_id=read_user_id(event.source.user_id)
    if event.postback.data == '收集樣本':
        collect(event, user_id)
    elif event.postback.data == 'flex':
        flex(event, user_id)

# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)