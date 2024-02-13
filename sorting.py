class SortAlgorithm:
    def __init__(self, arr):
        self.arr = arr

    def bubbleSort2(self):
        swapped = False
        for i in range(len(self.arr)):
            for j in range(0, len(self.arr)-i-1):
                if self.arr[j] > self.arr[j+1]:
                    temp = self.arr[j]
                    self.arr[j] = self.arr[j+1]
                    self.arr[j+1] = temp
                    swapped = True
            if not swapped:
                break

    def selectionSort1(self):
        for i in range(len(self.arr)):
            low_index = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[low_index]:
                    low_index = j
            
            self.arr[i], self.arr[low_index] = self.arr[low_index], self.arr[i]
        
        return self.arr

    def selectionSort2(self):
        for i in range(len(self.arr)):
            high_index = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] > self.arr[high_index]:
                    high_index = j
            
            self.arr[i], self.arr[high_index] = self.arr[high_index], self.arr[i]
        
        return self.arr
    
            
    def insertionSort1(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j = j - 1
            
            self.arr[j + 1] = key
    
    def insertionSort2(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            
            while j >= 0 and key > self.arr[j]:  # Modified condition for descending order
                self.arr[j + 1] = self.arr[j]
                j = j - 1
            
            self.arr[j + 1] = key


def test_list_1():
    list1 = [9, 1, 11, 7, 3, 13, 5]
    sortAlgorithm = SortAlgorithm(list1)
    sortAlgorithm.bubbleSort2()
    
    assert list1 == [1,3,5,7,9,11,13]
    
def test_list_2():
    list2 = [10,4,14,8,12,6]
    sortAlgorithm = SortAlgorithm(list2)
    sortAlgorithm.selectionSort2()
    
    assert list2 == [14,12,10,8,6,4]

def test_list_3():
    list3 = ['John', 'Jack', 'Jane', 'Jill']
    sortAlgorithm = SortAlgorithm(list3)
    sortAlgorithm.insertionSort1()
    
    assert list3 == ['Jack', 'Jane', 'Jill', 'John']

def test_list_4():
    list4 = ['A', 'a', 'Z', 'z', '1', '10']
    sortAlgorithm = SortAlgorithm(list4)
    sortAlgorithm.insertionSort2()
    print(list4)
    
    
test_list_1()
test_list_2()
test_list_3()
test_list_4()