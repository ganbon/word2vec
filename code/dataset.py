import pandas as pd
import os
import glob
import pathlib
import re
from janome.tokenizer import Tokenizer


def text_data(path):
    p_temp = pathlib.Path(path)
    article_list = []
    # フォルダ内のテキストファイルを全てサーチ
    for p in p_temp.glob('**/*.txt'):
        # 第二階層フォルダ名がニュースサイトの名前になっているので、それを取得
        pathname = os.path.split(p)
        media = pathname[0]
        file_name = pathname[1]
    # テキストファイルを読み込む
        with open(p, 'r', encoding='utf-8') as f:
            # テキストファイルの中身を一行ずつ読み込み、リスト形式で格納
            article = f.readlines()
            # 不要な改行等を置換処理
            article = [re.sub(r'[\n \u3000]', '', i) for i in article]
        # ニュースサイト名・記事タイトル・本文の並びでリスト化
        article_list.append([media,article[2], ''.join(article[3:])])
    article_df = pd.DataFrame(article_list, columns=['名前', 'タイトル', '本文'])
    return article_df

def cutsentence(s):
    #全角スペースなどを削除
    s.strip()
    #半角数字,半角英字、全角英字を削除
    s=re.sub(r'[0-9]','',s)
    s=re.sub(r'[a-z]','',s)
    s=re.sub(r'[A-Z]','',s)
    s=re.sub(r'[Ａ-Ｚ]','',s)
    s=re.sub(r'[ａ-ｚ]','',s)
    #不要な記号を削除
    code_regex = re.compile('[!"#$%&\'\\\\()*+,-./:;<=>?дД⇒┐‾♯@[\\]^○◯♂♡♪■〝〟，．┃┗┏━_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥★¥±°–—•″⇔∀∞≒≪≫①②③④⑤│┌＾]')
    s = code_regex.sub('', s)
    #一文ずつ取り出してリスト化
    text_data = s.split('。')
    return text_data

def word_list(word):
    t = Tokenizer()
    word_data = []
    #形態素解析で単語ごとに分解する
    for token in t.tokenize(word):
        surface = token.surface #単語
        speech = token.part_of_speech.split(',')[0] #品詞
        if speech != '接続詞' and speech != '記号':
            #取り出した単語と品詞をリスト化
            word_data.append([surface, speech])
    return word_data
