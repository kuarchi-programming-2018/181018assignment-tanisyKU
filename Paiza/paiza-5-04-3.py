# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:35:33 2018

@author: WATARU TANISHIMA
"""
右のコードには、pointsという辞書に、テストの点数が代入されています。
この辞書の値の合計を計算して出力してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
157

# ループで合計を計算しよう


points = {"国語" : 70, "算数" : 35, "英語" : 52}

sum = 0

# この下で、辞書の値の合計をループで計算してみよう


for score in points:
	sum = sum + points[score]
print(int(sum))

