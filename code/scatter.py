from gensim.models import word2vec
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
##TSNEで次元の削減
tsne = TSNE(n_components=2, random_state=0)
#モデルの読み込み
model = word2vec.Word2Vec.load("../word2vec_model/article_cbow_1_1.model")
#モデル内にある単語を全て取得
words = model.wv.index_to_key
key=input()#キー単語
words_label = []
vector = []
for w in range(len(words)):
    words_label.append(words[w])
    #単語のベクトルを取得
    word_vector = model.wv.get_vector(words[w])
    vector.append(word_vector)
#ベクトルを2次元ベクトルに変換
vector = tsne.fit_transform(vector)
x_vector = [x[0] for x in vector]#ｘ座標
y_vector = [x[1] for x in vector]#y座標
#日本語表示のためのフォント指定
plt.rcParams['font.family'] = "MS Gothic"
fig, ax = plt.subplots()
#散布図作成
sc = plt.scatter(x=x_vector, y=y_vector, s=5)
for i in range(len(words_label)):
    #キー単語のみ点の色を赤に変更する
    if key==words_label[i]:
        ax.scatter(x_vector[i],y_vector[i],c="red")
#単語ラベル表示の設定
annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
#通常は隠しておく
annot.set_visible(False)
#マウスイベント
def update_annot(ind):
    i = ind["ind"][0]
    pos = sc.get_offsets()[i]
    annot.xy = pos
    text = words_label[i]
    annot.set_text(text)
#マウスが対象の座標を指しているか判定
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()
#マウスイベント
fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()
