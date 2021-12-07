from gensim.models import word2vec
import matplotlib.pyplot as plt
#モデルファイルの読み込み
model = word2vec.Word2Vec.load("../word2vec_model/article_sg_3.model")
#モデル内のすべての単語を取得
words = model.wv.index_to_key
pro = []
x_label = [x for x in range(10)]
#対象単語入力
key = input()
for w in words:
    if w == key:
        continue
    #対象単語との近さの割合を検出
    similer_percent = model.wv.similarity(key, w)*100
    pro.append((w, similer_percent))
#上から順になるように並び替え
re = sorted(pro, reverse=True, key=lambda x: x[1])
#ラベルの作成
word_labels = [x[0] for x in re]
height = [x[1] for x in re]
#日本語表示のためのフォント指定
plt.rcParams['font.family'] = "MS Gothic"
#棒グラフの作成
#上位10個を表示
plt.bar(x_label, height[:10], width=0.5)
plt.xticks(x_label, word_labels[:10], fontsize=5)
plt.show()
