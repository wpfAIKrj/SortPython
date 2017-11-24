# -*- coding: utf-8 -*-
# 堆排序
def  adjustHeap(numbers, i, size):
	lchild = 2*i + 1
	rchild = 2*i + 2
	max = i
	if i < size / 2:
		if lchild < size and numbers[lchild] > numbers[max]:
			max = lchild
		if rchild < size and numbers[rchild] > numbers[max]:
			max = rchild
		if max != i:
			numbers[max], numbers[i] = numbers[i], numbers[max]
			print(numbers)
			adjustHeap(numbers, max, size)

def buildHeap(numbers, size):
	for i in range(0, (size/2))[::-1]:
		adjustHeap(numbers, i, size)

def heapSort(numbers):
	size = len(numbers)
	buildHeap(numbers, size)
	for i in range(0, size)[::-1]:
		numbers[0], numbers[i] = numbers[i], numbers[0]
		adjustHeap(numbers, 0, i)
			
def main():
	#主函数
	numbers = [23, 12, 9, 15,6,45,76,84,13,24]
	heapSort(numbers)
	

if __name__ == '__main__':
	main()		