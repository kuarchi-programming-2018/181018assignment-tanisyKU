# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:38:39 2018

@author: WATARU TANISHIMA
"""
右のコードエリアで、forを使って、次のような2次元リストを作成して、print関数で出力してください。

・要素数は、5個
・[7,7,7,7]というリストを要素にする

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
[[7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7], [7, 7, 7, 7]]

#2次元リストを作成してみよう
list = [7 for i in range(4)]
numbers = [list for j in range(5)]
print(numbers)
