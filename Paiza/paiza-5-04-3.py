# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 22:35:33 2018

@author: WATARU TANISHIMA
"""
�E�̃R�[�h�ɂ́Apoints�Ƃ��������ɁA�e�X�g�̓_�����������Ă��܂��B
���̎����̒l�̍��v���v�Z���ďo�͂��Ă��������B

�v���O���������s���āA�������o�͂����Ή��K�ۑ�N���A�ł��I

 ���҂���o�͒l
157

# ���[�v�ō��v���v�Z���悤


points = {"����" : 70, "�Z��" : 35, "�p��" : 52}

sum = 0

# ���̉��ŁA�����̒l�̍��v�����[�v�Ōv�Z���Ă݂悤


for score in points:
	sum = sum + points[score]
print(int(sum))

