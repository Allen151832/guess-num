# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複猜數字
# 猜對印出 "答對了!"
# 猜錯要告訴他比答案大或小

import random

r = random.randint(1,100)
while True:
	num = input ("請猜數字: ")
	num = int(num)
	if num == r:
		print("猜對了!")
		break
	elif num > r:
		print("猜錯了,比答案大")
	elif num < r:
		print("猜錯了,比答案小")
