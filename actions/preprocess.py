import librosa
import os
from keras.utils import to_categorical
import numpy as np
from sklearn.preprocessing import StandardScaler

DATA_PATH = "./data/"

# Input: Folder Path
# Output: Tuple (Label, Indices of the labels, one-hot encoded labels)
def get_labels(path=DATA_PATH):
    labels = os.listdir(path)
    if '.DS_Store' in labels: 
        labels.remove('.DS_Store')
    label_indices = np.arange(0, len(labels))
    return labels, label_indices, to_categorical(label_indices)

labels = os.listdir(DATA_PATH)
print(labels)

# Handy function to convert wav2mfcc
def wav2mfcc(file_path, max_pad_len=11):
    wave, sr = librosa.load(file_path, mono=True, sr=None)
    wave = wave[::3]
    
    # michael added to cut my audio file
    i=0
    # 訓練資料的長度
    wav_length=5334
    # 聲音檔過長，擷取片段
    if len(wave) > wav_length:
        # 尋找最大聲的點，取前後各半
        i=np.argmax(wave)
        if i > (wav_length):
            wave = wave[i-int(wav_length/2):i+int(wav_length/2)]
        else:
            # 聲音檔過長，取前面
            wave = wave[0:wav_length]
    
    mfcc = librosa.feature.mfcc(wave, sr=16000)
    pad_width = max_pad_len - mfcc.shape[1]
    if pad_width < 0:
        pad_width = 0
        mfcc = mfcc[:,:11]
    mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
    return mfcc
