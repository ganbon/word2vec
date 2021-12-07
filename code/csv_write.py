from gensim.models import word2vec
import pandas as pd
model=word2vec.Word2Vec.load("article2.model")
a=model.wv.index_to_key
a.sort()
word_df=pd.DataFrame(a,columns=["word"])
word_df.to_csv("../text/article_model2.csv") 
