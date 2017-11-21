# -*- coding: utf-8 -*-
# 快速排序通过一趟排序将要排序的数据分割成独立的两部分，
# 其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，
# 整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def  fastSort(numbers, left, right):
	# 快速排序的实现
	if left >= right:
		return numbers
	key = numbers[left]
	low = left
	high = right
	while left < right:
		while left < right and numbers[right] >= key:
			right -= 1
		numbers[left] = numbers[right]
		while left < right and numbers[left] <= key:
			left += 1
		numbers[right] = numbers[left]
	numbers[right] = key
	print(numbers)
	fastSort(numbers, low, left - 1)
	fastSort(numbers, left +1, high)
			
def main():
	#主函数
	numbers = [23, 12, 9, 15,6,44,17,1,98]
	fastSort(numbers, 0, len(numbers)-1)

if __name__ == '__main__':
	main()		