import random
start = input('選一個開始值：')
end = input('選一個結束值：')
start = int(start)
end = int(end)

count = 0
r = random. randint(start, end)
while True:
	count = count +1
	num = input('猜個數字：')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count,'次')

