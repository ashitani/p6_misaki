# P6_Misaki

PC6001(初代32K) で美咲フォントを使った文章を表示します。
OSXでしか確認していません。

!(screenshot)[https://user-images.githubusercontent.com/5352510/114544053-12899a00-9c95-11eb-8d7c-4426a24f2192.png]

# requirement

- (XSM)[https://github.com/garymsx/xsm]　アセンブル
- (z88dk)[https://github.com/z88dk/z88dk]　CASファイル作成など
- (8x8DotJPFont)[https://github.com/emutyworks/8x8DotJPFont]
- python フォント/テキストデータの変換
- java XSMの実行のため

# 使い方

```
> git clone https://github.com/garymsx/xsm.git
> git clone --recursive https://github.com/ashitani/p6_misaki.git
> cd p6_misaki
> make
```
でmain.casが出来ます。うまく行かない場合はMakefile内のパスを適宜設定してください。

```
> make run
```
でエミュレータ(デフォルトではPC6001VX)が起動します。

```
How many pages? 1
cload
run
```

で実行できます。


# 好きなテキストに差し替え

text/text_data.txtを編集してmakeすれば好きな文章を表示できます。現状はすべて全角のutf-8を仮定しています。
