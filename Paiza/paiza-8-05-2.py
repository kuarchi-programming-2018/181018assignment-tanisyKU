# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:39:02 2018

@author: WATARU TANISHIMA
"""
�E�̃R�[�h�́A�w���̍���ƎZ���̃e�X�g�̓_����ێ�����N���X�ł��B
���̃N���X�ɁA�e�X�g�̍��v�_�����v�Z����sum���\�b�h���L�q���Ă��������B

�v���O���������s���āA�������o�͂����Ή��K�ۑ�N���A�ł��I

 ���҂���o�͒l
���v��113�_�ł�

# coding: utf-8

# �w�����\�b�h�����


class Gakusei:

	def __init__(self, kokugo, sansu):

        	self.kokugo = kokugo

        	self.sansu  = sansu

    
	# ���̉��ɁA���v���_��߂�l�Ƃ��ĕԂ�sum���\�b�h���L�q����


	def sum(self):
		return self.kokugo + self.sansu
	

yamada = Gakusei(70, 43)

print("���v��" + str(yamada.sum()) + "�_�ł�")
