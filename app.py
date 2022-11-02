# import flask related
from flask import Flask, request, abort, url_for
from urllib.parse import parse_qsl, parse_qs
import random
from linebot.models import events
from line_chatbot_api import *
from actions.service import *

from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# create flask server
app = Flask(__name__)

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

answer = ''
@handler.add(MessageEvent)
def handle_something(event):
    if event.message.type=='text':
        global answer
        answer = ''
        recrive_text=event.message.text
        # print(recrive_text)
        if '使用說明' in recrive_text:
            messages=[]
            messages.append(TextSendMessage(text='歡迎使用AIあイ'))
            messages.append(TextSendMessage(text='以下是使用說明的影片'))
            line_bot_api.reply_message(event.reply_token, messages)  
        elif '50音表' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://imgur.com/FRkwLch.png', preview_image_url='https://imgur.com/FRkwLch.png'))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '答案卷' in recrive_text:
            messages=[]
            messages.append(ImageSendMessage(original_content_url='https://imgur.com/0I7lHKR.png', preview_image_url='https://imgur.com/0I7lHKR.png'))
            line_bot_api.reply_message(event.reply_token, messages)
        elif '回饋表單' in recrive_text:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此功能準備中'))
        elif '平假名測驗' in recrive_text:
            answer=hiragana_test(event)
        elif '片假名測驗' in recrive_text:
            # messages=[]
            # messages.append(TextSendMessage(text='下載此答案卷\n請寫在方框內'))
            # messages.append(ImageSendMessage(original_content_url='https://imgur.com/0I7lHKR.png', preview_image_url='https://imgur.com/0I7lHKR.png'))
            # answer=katakana_test(event, messages)
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='此功能準備中'))
        else:
            messages=[]
            messages.append(StickerSendMessage(package_id=789, sticker_id=10882))
            messages.append(TextSendMessage(text='抱歉我聽不懂你說的意思~'))
            messages.append(TextSendMessage(text='可以用其他方式再說一次嗎?'))
            line_bot_api.reply_message(event.reply_token, messages)
    elif event.message.type=='sticker':
        receive_sticker_id=event.message.sticker_id
        receive_package_id=event.message.package_id
        line_bot_api.reply_message(event.reply_token, StickerSendMessage(package_id=receive_package_id, sticker_id=receive_sticker_id))
    elif event.message.type=='image':
        message_content = line_bot_api.get_message_content(event.message.id)
        with open('temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)

        # Replace this with the path to your image
        image = Image.open('temp_image.png')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        # run the inference
        prediction_options=('あ', 'い', 'う', 'え', 'お','か','き','く','け','こ')
        prediction = model.predict(data)
        prediction_int_result = prediction.argmax()
        prediction_string_result = prediction_options[prediction_int_result]
        messages=[]
        messages.append(TextSendMessage(text=f"你寫的字是：{prediction_string_result}"))

        if(answer==prediction_string_result):
            messages.append(TextSendMessage(text='答對了！'))
        else:
            messages.append(TextSendMessage(text=f"答錯了\n是{answer}才對喔！"))
        
        # 回傳訊息給使用者
        line_bot_api.reply_message(event.reply_token, messages)


# run app
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5566, debug=True)