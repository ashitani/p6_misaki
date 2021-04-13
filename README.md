# P6_Misaki

PC6001(初代32K) で美咲フォントを使った文章を表示します。

# requirement

- (XSM)[https://github.com/garymsx/xsm]　アセンブル
- (z88dk)[https://github.com/z88dk/z88dk]　CASファイル作成など
- (8x8DotJPFont)[https://github.com/emutyworks/8x8DotJPFont]
- python フォント/テキストデータの変換
- java XSMの実行のため

# 使い方

Makefile内のパスを適宜設定したのちに

```
> make
```
でmain.casが出来ます。

```
> make run
```
でエミュレータ(デフォルトではPC6001VX)が起動します。

# 好きなテキストに差し替え

text/text_data.txt
を編集してmake。現状はすべて全角のutf-8を仮定しています。
