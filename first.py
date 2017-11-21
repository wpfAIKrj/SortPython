# -*- coding: utf-8 -*-
# 冒泡排序
def  bubbleSort(numbers):
	# 冒泡算法的实现
	for j in range(len(numbers)-1,-1,-1):

		for i in range(j):
			if numbers[i] > numbers[i+1]:
				#把数字大的放到后面
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
			print(numbers)
			
def main():
	#主函数
	numbers = [23, 12, 9, 15,6]
	bubbleSort(numbers)

if __name__ == '__main__':
	main()		