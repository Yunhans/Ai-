from line_chatbot_api import *
from keras.models import load_model
import numpy as np
import random
from PIL import Image, ImageOps
from actions.access_data import *
import shutil

# Load the model
sound_model = load_model('model/katakana.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def katakana_notify(event, answer, user_id):
    key=read_key(user_id)
    if event.message.content_provider.type == 'line':
        message_content = line_bot_api.get_message_content(event.message.id)  # 只能接收使用者傳出的圖片 liff.sendMessages不行
        with open('temp_image.png', 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
        image = Image.open('temp_image.png')
    elif event.message.content_provider.type == 'external': # 圖片由liff.sendMessages送出時
        imgName = event.message.content_provider.original_content_url[-36:]
        image = Image.open(f'static/imgs/{imgName}')

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    # run the inference
    prediction_options=('ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','サ','シ','ス','セ','ソ','タ','チ','ツ','テ','ト','ナ','ニ','ヌ','ネ','ノ','ハ','ヒ','フ','ヘ','ホ','マ','ミ','ム','メ','モ','ヤ','ユ','ヨ','ラ','リ','ル','レ','ロ','ワ','ヲ','ン')
    prediction = sound_model.predict(data)

    # Calculate the confidence of the model's predictions
    confidence = np.max(prediction)
    print('confidence score: '+str(confidence))

    prediction_int_result = prediction.argmax()
    prediction_string_result = prediction_options[prediction_int_result]
    messages=[]
    messages.append(TextSendMessage(text=f"你寫的字是[{prediction_string_result}]"))

    # 答題數+1
    list=read_katakana(user_id)
    list[key]+=1
    print(list)
    update_katakana(user_id,list)

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
                                                                QuickReplyButton(action=MessageAction(label="繼續下一題",text="片假名")),
                                                                ])))
        # 答對題數+1
        list0=read_katakana0(user_id)
        list0[key]+=1
        print(list0)
        update_katakana0(user_id,list0)

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
                                                                QuickReplyButton(action=MessageAction(label="繼續下一題",text="片假名")),
                                                                ])))

    # move staitc/imgs to class_imgs
    shutil.move(f'static/imgs/{imgName}', f'class_imgs/katakana/{prediction_string_result}/{imgName}')

    # 回傳訊息給使用者
    line_bot_api.reply_message(event.reply_token, messages)
