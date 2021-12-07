from gensim.models import word2vec
import matplotlib.pyplot as plt
import numpy as np
word1=input()
word2=input()
model = word2vec.Word2Vec.load("../word2vec_model/article_cbow_2.model")
words = model.wv.most_similar(positive=[word1,word2])
for word in words:
    print(word)