from gensim.models import word2vec


def word2vc(word_list):
    #word2vecの引数
    #sg(=0の時CoBW=1の時Skit-gram),sentense(学習させる文章),vecter_size(次元数),min_count(最小単語回数),epochs(学習率)
    model = word2vec.Word2Vec(sg=1,sentences=word_list,vector_size=200,min_count=5, window=5, epochs=200)
    #学習モデルをファイルに保存
    model.save("../word2vec_model/article_sg.model")
    
