def merge_sort(data):
  
    if len(data) > 1:
        mid = len(data) // 2
        firstHalf = data[:mid]
        secondHalf = data[mid:]
        
        merge_sort(firstHalf)
        merge_sort(secondHalf)
        
        leftIndex = 0
        rightIndex = 0
        arrayIndex = 0
        
        while leftIndex < len(firstHalf) and rightIndex < len(secondHalf):
            if data[leftIndex] <= data[rightIndex]:
                data[arrayIndex] = firstHalf[leftIndex]
                leftIndex += 1
            else:
                data[arrayIndex] = secondHalf[rightIndex]
                rightIndex += 1
            arrayIndex += 1
        while(leftIndex < len(firstHalf)):
            data[arrayIndex] = firstHalf[leftIndex]
            leftIndex += 1
            arrayIndex += 1
        while(rightIndex < len(secondHalf)):
            data[arrayIndex] = secondHalf[rightIndex]
            rightIndex += 1
            arrayIndex += 1

def main():
    data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
    merge_sort(data)
    print(data)
    
if __name__ == '__main__':
    main()