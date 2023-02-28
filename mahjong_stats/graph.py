import matplotlib.pyplot as plt
import base64
from io import BytesIO

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph(x,y):
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	values=range(len(x))
	plt.plot(values,y)                     #グラフ作成
	plt.xticks(values,x,rotation=45)          #X軸値を45度傾けて表示
	#plt.title("totalpoint")    #グラフタイトル
	plt.xlabel("Date")               #xラベル
	plt.ylabel("totalpoint")             #yラベル
	plt.tight_layout()
	plt.grid(True)               #レイアウト
	for i in range(len(y)):
		plt.text(i, y[i],'({t})'.format(t=round(y[i],2)),fontsize=10,ha="left",va="top")
	graph = Output_Graph()           #グラフプロット
	return graph