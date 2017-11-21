# -*- coding: utf-8 -*-
# 直接选择排序基本思想：
# 第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
# 第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
# 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
def  cdSort(numbers):
	# 直接选择的实现
	count = len(numbers)
	for i in range(0, count):
		min = i
		for j in range(i+1, count):
			if numbers[min] > numbers[j]:
				min = j
		numbers[min], numbers[i] = numbers[i], numbers[min]
		print(numbers)
			
def main():
	#主函数
	numbers = [23, 12, 9, 15,6]
	cdSort(numbers)

if __name__ == '__main__':
	main()		