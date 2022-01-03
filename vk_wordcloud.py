# Python functions for creation
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from tkinter import filedialog, Tk
from PIL import Image
from os import path, getcwd
from wordcloud import WordCloud

from textproc import cleanse_text
from htmlproc import html_text_extract, html_audio_extract


# vk.com data archive export messages to cloud of words
# You should select path to folder that contains .html messages
def vk_message_wordcloud(path2folder=None, mask=None, contour=None):

    # 1. Import masks:
    np_mask = None

    if mask:
        d = path.dirname(__file__) if "__file__" in locals() else getcwd()
        if mask == "cloud":
            np_mask = np.array(Image.open(path.join(d, "./masks/cloud.png")))
        if mask == "snowflake":
            # source: https://pixabay.com/vectors/snowflake-crystal-symmetry-winter-153108/
            np_mask = np.array(Image.open(path.join(d, "./masks/snowflake.png")))
        if mask == "butterfly":
            np_mask = np.array(Image.open(path.join(d, "./masks/butterfly.png")))
        if mask == "turd":
            np_mask = np.array(Image.open(path.join(d, "./masks/turd.png")))
        if mask == "christmas_ball":
            np_mask = np.array(Image.open(path.join(d, "./masks/christmas_ball.png")))

    if contour:
        contour_width = contour
    else:
        contour_width = 0

    # 2. Import folder with all .html files:
    if not path2folder:
        root = Tk()
        path2folder = filedialog.askdirectory(initialdir="./", title="Select folder")
        root.destroy()
    datafiles = glob(path2folder + "/*.html")

    clean_words = ""
    stopwords = ""

    n_datafiles = len(datafiles)
    clean_text = ""

    # 3. Open and process all .html textfiles:
    for file_i in range(n_datafiles):
        with open(datafiles[file_i], mode="r", encoding='cp1251', errors='ignore') as f:
            filetext_list = f.readlines()

        clean_words_buffer = cleanse_text(html_text_extract(filetext_list))
        clean_words += clean_words_buffer.replace('   ', ' ')

    # Import stop words:
    with open('stop_words.txt', mode="r", encoding='utf-8', errors='ignore') as f:
        stopwords = f.read()

    stopwords = set(stopwords.split("\n"))

    wc = WordCloud(width=1600, height=1200, max_words=2000,
                   background_color="white", mask=np_mask,
                   stopwords=stopwords, contour_width=contour_width, contour_color=contour)  # "steelblue"

    # Generate a word cloud image
    wc.generate(clean_words)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()



# vk.com data archive export messages to cloud of words
# You should select path to folder that contains .html messages
def vk_music_wordcloud(path2folder=None, mask=None, contour=None):

    # 1. Import masks:
    np_mask = None

    if mask:
        d = path.dirname(__file__) if "__file__" in locals() else getcwd()
        if mask == "cloud":
            np_mask = np.array(Image.open(path.join(d, "./masks/cloud.png")))
        if mask == "snowflake":
            # source: https://pixabay.com/vectors/snowflake-crystal-symmetry-winter-153108/
            np_mask = np.array(Image.open(path.join(d, "./masks/snowflake.png")))
        if mask == "butterfly":
            np_mask = np.array(Image.open(path.join(d, "./masks/butterfly.png")))
        if mask == "turd":
            np_mask = np.array(Image.open(path.join(d, "./masks/turd.png")))
        if mask == "christmas_ball":
            np_mask = np.array(Image.open(path.join(d, "./masks/christmas_ball.png")))

    if contour:
        contour_width = contour
    else:
        contour_width = 0

    # 2. Import folder with all .html files:
    if not path2folder:
        root = Tk()
        path2folder = filedialog.askdirectory(initialdir="./", title="Select folder")
        root.destroy()
    datafiles = glob(path2folder + "/*.html")

    clean_words = ""
    stopwords = ""

    n_datafiles = len(datafiles)
    clean_text = ""
    filetext_list = []
    # 3. Open and process all .html textfiles:
    for file_i in range(n_datafiles):
        with open(datafiles[file_i], mode="r", encoding='cp1251', errors='ignore') as f:
            filetext_list += f.readlines()

    [band_name, song_name, duration] = html_audio_extract(filetext_list)


    wc = WordCloud(width=1600, height=1200, max_words=2000,
                   background_color="black", mask=np_mask,
                   contour_width=contour_width, contour_color=contour)  # "steelblue"

    # band_name_wc = set(band_name)
    band_name_wc = '\n'.join(band_name)
    # band_name_wc = '\r\n'.join(band_name)
    band_name_wc = band_name_wc.replace(' ', "_")

    # Generate a word cloud image
    wc.generate(band_name_wc)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()