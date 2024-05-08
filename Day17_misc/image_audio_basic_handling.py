# -*- coding: utf-8 -*-
"""image_audio_basic_handling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zqVwBEq8jdCvW8gGnLgkbxvxBHrI7KAB

# Image Processing

Libraries Supporting Image Processing

- pillow
- opencv
- scipy.ndimage
- skimage
- matplotlib.pyplot

And many more

All these libraries load image as an array of multidimensional values

2D Color Image is having 3 Dims : height, width and color

2D grayscale image is having 2 dims : height and width

Video is 4 dim : 3 dims of color image and then video is containing multiple images on time axis

## Image processing using Pillow

reference : https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
"""

!python3 -m pip install --upgrade Pillow

import PIL

from PIL import Image

img = Image.open("/content/index.jpg" )

img.size

img.format

import matplotlib.pyplot as plt
plt.imshow(img)

rot_img = img.rotate(-90)

plt.imshow(rot_img)

"""## Filter Image with prebuilt filters

ImageFilter class Filters

The current version of the library provides the following set of predefined image enhancement filters:

    BLUR

    CONTOUR

    DETAIL

    EDGE_ENHANCE

    EDGE_ENHANCE_MORE

    EMBOSS

    FIND_EDGES

    SHARPEN

    SMOOTH

    SMOOTH_MORE

"""

from PIL import ImageFilter
img_out = img.filter(ImageFilter.SHARPEN)

plt.imshow(img_out)

"""## Split the image"""

r,g,b = img.split()

r.size

g.size

b.size



"""## Image Peocessing using OpenCV

further reference :https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
"""

import cv2

img_arr = cv2.imread("index.jpg")

img_arr.shape

import matplotlib.pyplot as plt
plt.imshow(img_arr)

"""### Rotate Image using openCV"""

center = (img_arr.shape[0]//2, img_arr.shape[1]//2)
rot_mat = cv2.getRotationMatrix2D( center, 45 ,0.5)
img_rotate_dst = cv2.warpAffine(img_arr, rot_mat, (img_arr.shape[1], img_arr.shape[0]))

plt.imshow(img_rotate_dst)

"""# Audio Processing

Libraries supporting audio processing

- scipy.io
- librosa ( mostly used )

and many more

Audio is sequence of values (int / float) which represent the audio signal at perticular sampling frequency

Every value is one digital sample from the actual audio signal which is analog.

Higher sampling rate gives better quality audio.

## Audio processing with Librosa

Librosa library used default 22050 sampling rate
"""

import librosa
data, samplerate = librosa.load('/content/file_example_MP3_700KB.mp3')

samplerate

data

import soundfile as sf

sf.write('sample_file.wav', data, samplerate, subtype='PCM_24')

"""## Advanced Processing using Libriosa

further reading : https://www.kaggle.com/code/jaseemck/audio-processing-using-librosa-for-beginners

### Generate Mel Frequency Cepstral Coefficients (MFCCs)

It is most imp for audio classification
"""

mfccs = librosa.feature.mfcc(y=data, sr=samplerate)

print(mfccs.shape)

import librosa.display
librosa.display.specshow(mfccs, sr=sr, x_axis='time')

"""## Audio file handling using Scipy.io

Can ONLY handle wav files
"""

from scipy.io import wavfile

samplerate, data = wavfile.read('sample_file.wav')

samplerate

data
