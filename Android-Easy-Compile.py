#!/usr/bin/python  
# -*- coding: utf-8 -*- 

import os
column_ = 45
os.system('title = Android-Easy-Compile   v0.01   by Aaron Feng')

while True:
	print('-'*column_)
	print(' 借助ADB对安卓手机的APP进行本地编译优化')
	print('')
	print(' 适用于安卓版本高于Android 7的安卓智能手机')
	print('')
	print(' 使用前先进入 开发者选项 启用 USB调试')
	print('-'*column_)
	print(' 1. 检查连接状态')
	print('')
	print(' 2. 对所有应用进行 Everything 编译')
	print('')
	print(' 3. 对所有应用进行 Speed 编译')
	print('')
	print(' 4. 如何在设备上启用 adb 调试')
	print('-'*column_)
	print('( 1 / 2 / 3 / 4 )')
	choice_ = input().strip(' ')
	
	if choice_ == '1':
		os.system('cls')
		os.system('adb devices -l')
		print('\n按 Enter 键以继续.')
		input()
		os.system('cls')
	
	elif choice_ == '2':
		os.system('cls')
		
		Commands = [
			'cmd package compile -m everything -f -a'
		]
		with open('Everything.txt','w+') as f:
			f.writelines(Commands)
		
		print('编译中, 请耐心等待....')
		os.system('adb shell < Everything.txt')
		os.system('cls')
		print('')
		print('编译完成!!')
		print('按 Enter 键以继续.')
		input()
		os.system('cls')
	
	elif choice_ == '3':
		os.system('cls')
		
		Commands = [
			'cmd package compile -m speed -f -a'
		]
		with open('Speed.txt','w+') as f:
			f.writelines(Commands)
		print('编译中, 请耐心等待....')
		os.system('adb shell < Speed.txt')
		os.system('cls')
		print('')
		print('编译完成!!')
		print('按 Enter 键以继续.')
		input()
		os.system('cls')
	
	elif choice_ == '4':
		os.system('cls')
		print('''
在设备上启用 adb 调试 :

要在通过 USB 连接的设备上使用 adb，您必须在设备的系统设置中启用 USB 调试（位于开发者选项下）。

在搭载 Android 4.2 及更高版本的设备上，“开发者选项”屏幕默认情况下处于隐藏状态。
如需将其显示出来，请依次转到设置 > 关于手机，然后点按版本号七次。返回上一屏幕，在底部可以找到开发者选项。

在某些设备上，“开发者选项”屏幕所在的位置或命名方式可能有所不同。

现在，您已经可以通过 USB 连接设备。您可以在主菜单选项 "1. 检查连接状态"，验证设备是否已连接。
如果已连接，您将看到设备名称以“设备”形式列出。
		''')
		print('')
		print('按 Enter 键以继续.')
		input()
		os.system('cls')
	
	else:
		os.system('cls')
		print('输入无效,请重试.')
		print('按 Enter 键以继续.')
		input()
		os.system('cls')


