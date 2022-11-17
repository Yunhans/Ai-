from line_chatbot_api import *
from keras.models import load_model
import numpy as np
import random
from PIL import Image, ImageOps

# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def hiragana_notify(event, answer):
    if event.message.content_provider.type == 'line':
        message_content = line_bot_api.get_message_content(event.message.id)  # 只能接收使用者傳出的圖片 liff.sendMessages不行
        with open('temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        image = Image.open('temp_image.png')
    elif event.message.content_provider.type == 'external': # 圖片由liff.sendMessages送出時
        urlName = event.message.content_provider.original_content_url
        print(urlName[-36:])
        image = Image.open('imgs/{}'.format(urlName[-36:]))

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    # run the inference
    prediction_options=('あ','い','う','え','お',
                        'か','き','く','け','こ',
                        'さ','し','す','せ','そ',
                        'た','ち','つ','て','と',
                        'な','に','ぬ','ね','の',
                        'は','ひ','ふ','へ','ほ',
                        'ま','み','む','め','も',
                        'や','ゆ','よ',
                        'ら','り','る','れ','ろ',
                        'わ','を','ん')
    prediction = model.predict(data)
    prediction_int_result = prediction.argmax()
    prediction_string_result = prediction_options[prediction_int_result]
    messages=[]
    messages.append(TextSendMessage(text=f"你寫的字是[{prediction_string_result}]"))

    if(answer==prediction_string_result):
        i = random.randint(0,3)
        j = random.randint(1,5)
        sticker=[['446','1989','1993','1998','1991','1992'],
                ['789','10855','10857','10859','10863','10891'],
                ['11537','52002734','52002735','52002736','52002748','52002752'],
                ['11539','52114117','52114123','52114125','52114131','52114118']]
        messages.append(StickerSendMessage(package_id=sticker[i][0],sticker_id=sticker[i][j]))
        messages.append(TextSendMessage(text='答對了！',quick_reply=QuickReply(items=[
                                                                QuickReplyButton(action=MessageAction(label="結束測驗",text="我累了")),
                                                                QuickReplyButton(action=MessageAction(label="繼續下一題",text="平假名")),
                                                                ])))
    else:
        i = random.randint(0,3)
        j = random.randint(1,5)
        sticker=[['11538','51626510','51626497','51626524','51626529','51626531'],
                ['11539','52114114','52114127','52114137','52114138','52114141'],
                ['789','10860','10879','10881','10885','10887'],
                ['11537','52002749','52002750','52002758','52002765','52002770']]
        messages.append(StickerSendMessage(package_id=sticker[i][0],sticker_id=sticker[i][j]))
        messages.append(TextSendMessage(text=f"答錯了！是[{answer}]才對喔",quick_reply=QuickReply(items=[
                                                                QuickReplyButton(action=MessageAction(label="結束測驗",text="我累了")),
                                                                QuickReplyButton(action=MessageAction(label="繼續下一題",text="平假名")),
                                                                ])))
    # 回傳訊息給使用者
    line_bot_api.reply_message(event.reply_token, messages)
