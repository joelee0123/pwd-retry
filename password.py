password = 'a123456'
i = 3 # 剩餘次數
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 跳出迴圈
	else:
		print('密碼錯誤')
		if i > 0:
			print('你還有', i,'機會')