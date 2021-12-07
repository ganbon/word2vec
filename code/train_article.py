from dataset import word_list, cutsentence, text_data
from wd2vec import word2vc
path = "../text/"
article_df = text_data(path)
sentences = []
wd2data = []
for i, data in enumerate(article_df['本文']):
    s = cutsentence(data)
    sentences[len(sentences):len(sentences)] = s
for sentence in sentences:
    word = word_list(sentence)
    list_word = [x[0] for x in word]
    wd2data.append(list_word)
word2vc(wd2data)