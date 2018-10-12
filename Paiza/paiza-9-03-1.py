# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:39:20 2018

@author: WATARU TANISHIMA
"""
右のコードには、Greetingクラスに、say_helloメソッドが定義されており、
Greetingクラスを継承したHelloクラスが定義されています。

このHelloクラスで、say_helloメソッドをオーバーライドして、メソッド呼び出しの引数をターゲットとして表示してください。
たとえば、引数に「python」を渡した場合、「hello python」と表示します。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
hello python

class Greeting:
	def __init(self):
		self.msg = "hello"
		self.target = "paiza"

	def say_hello(self):
		print(self.msg + " " + self.target)

class Hello(Greeting):
	#ここにオーバーライドするメソッドを記述する
	def __init__(self):
	    
		self.msg = "hello"
	
	def say_hello(self,newtarget):
		
		print(self.msg + " " + newtarget)

player = Hello()
player.say_hello("python")
