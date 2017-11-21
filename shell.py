# -*- coding: utf-8 -*-
# 希尔排序，
def  insertSort(numbers):
	# 希尔排序的实现
	count = len(numbers)
	step = 2
	group = count/step
	while group > 0:
		for i in range(0, group):
			j = i + group
			while j < count:
				k = j - group
				key = numbers[j]
				while k >= 0:
					if numbers[k] > key:
						numbers[k + group] = numbers[k]
						numbers[k] = key
					k -= group
				j += group
				print(numbers)
		group /= step
			
def main():
	#主函数
	numbers = [23, 12, 9, 15,6]
	insertSort(numbers)

if __name__ == '__main__':
	main()		