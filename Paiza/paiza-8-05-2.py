# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:39:02 2018

@author: WATARU TANISHIMA
"""
右のコードは、学生の国語と算数のテストの点数を保持するクラスです。
このクラスに、テストの合計点数を計算するsumメソッドを記述してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
合計は113点です

# coding: utf-8

# 学生メソッドを作る


class Gakusei:

	def __init__(self, kokugo, sansu):

        	self.kokugo = kokugo

        	self.sansu  = sansu

    
	# この下に、合計得点を戻り値として返すsumメソッドを記述する


	def sum(self):
		return self.kokugo + self.sansu
	

yamada = Gakusei(70, 43)

print("合計は" + str(yamada.sum()) + "点です")
