# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:39:20 2018

@author: WATARU TANISHIMA
"""
�E�̃R�[�h�ɂ́AGreeting�N���X�ɁAsay_hello���\�b�h����`����Ă���A
Greeting�N���X���p������Hello�N���X����`����Ă��܂��B

����Hello�N���X�ŁAsay_hello���\�b�h���I�[�o�[���C�h���āA���\�b�h�Ăяo���̈������^�[�Q�b�g�Ƃ��ĕ\�����Ă��������B
���Ƃ��΁A�����Ɂupython�v��n�����ꍇ�A�uhello python�v�ƕ\�����܂��B

�v���O���������s���āA�������o�͂����Ή��K�ۑ�N���A�ł��I

 ���҂���o�͒l
hello python

class Greeting:
	def __init(self):
		self.msg = "hello"
		self.target = "paiza"

	def say_hello(self):
		print(self.msg + " " + self.target)

class Hello(Greeting):
	#�����ɃI�[�o�[���C�h���郁�\�b�h���L�q����
	def __init__(self):
	    
		self.msg = "hello"
	
	def say_hello(self,newtarget):
		
		print(self.msg + " " + newtarget)

player = Hello()
player.say_hello("python")
