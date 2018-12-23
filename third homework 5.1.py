import random, time, heapq
import matplotlib.pyplot as plt
 
class MinMaxQuickSort(object):
 
    def __init__(self):
        self.content = []
        pass
    def partition(arr,low,high):
        i = ( low-1 )         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low , high):
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
                
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )
    
    
    def quicksort(arr,low,high):
        if low < high:
            pi = partition(arr,low,high)
            quicksort(arr, low, pi-1)
            quicksort(arr, pi+1, high)

    def measurethis(self, size):
        mylist = []
        for i in range(size):
            mylist.append(random.randint(0,size))



class treenode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key=key
        self.payload=value
        self.leftchild=left
        self.rightchild=right
        self.parent=parent

    def hasleftchild(self):
        return self.leftchild

    def hasrightchild(self):
        return self.rightchild

    def hasanychild(self):
        return self.rightchild or self.leftchild

    def hasbothchild(self):
        return self.rightchild and self.leftchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild == self

    def isrightchild(self):
        return self.parent and self.parent.rightchild == self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not (self.rightchild or self.leftchild)

    def replacenodedata(self,key,value,leftc,rightc):
        self.key=key
        self.payload=value
        self.leftchild = leftc
        self.rightchild = rightc

        if self.hasleftchild():
            self.leftchild.parent = self
        if self.hasrightchild():
            selfrightchild.parent=self

class binarytree:
    def __init__(self):
        self.content = []

    def add(self, value):
        self.content.append(value)
        self.content.sort()

    def getmin(self):
        return self.content[0]

    def getmax(self):
        return self.content[-1]


class MinMaxHeap(object):
 
    def __init__(self):
        self.content_min = []
        self.content_max = []
        #heapq.heapify(self.content_min)
        #heapq.heapify(self.content_max)
 
    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)
 
    def get_min(self):
        if len(self.content_min) > 0:
            return self.content_min[0]
 
    def get_max(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]
 
 
class MinMaxBubble(object):
 
    def __init__(self):
        self.content = []
 
    def bubble_sort(self):
        for passnum in range(len(self.content) - 1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i + 1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp
 
    def add(self, value):
        self.content.append(value)
        self.bubble_sort()
 
    def get_min(self):
        return self.content[0]
 
    def get_max(self):
        return self.content[-1]
 
 
def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0
 
    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)
 
        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)
 
        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)
 
    return tot_time_add, tot_time_min, tot_time_max




if __name__ == '__main__' :
    a = MinMaxQuickSort()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())
 
    a = binarytree()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())
 
    a = MinMaxHeap()
    a.add(5)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(7)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(3)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
    a.add(9)
    print(a.content_min, a.content_max, a.get_min(), a.get_max())
 
    a = MinMaxBubble()
    a.add(5)
    print(a.content, a.get_min(), a.get_max())
    a.add(7)
    print(a.content, a.get_min(), a.get_max())
    a.add(3)
    print(a.content, a.get_min(), a.get_max())
    a.add(9)
    print(a.content, a.get_min(), a.get_max())
 
    repetitions = 3
    max_operations = 800
    step = 200
 
    values_quicksort_add, values_quicksort_min, values_quicksort_max = [], [], []
    values_binarytree_add, values_binarytree_min, values_binarytree_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []
 
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 1000))
 
        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxQuickSort()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax
 
        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions
 
        values_quicksort_add.append(tot_time_add * 1000)
        values_quicksort_min.append(tot_time_min * 1000)
        values_quicksort_max.append(tot_time_max * 1000)
 
        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = binarytree()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax
 
        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions
 
        values_binarytree_add.append(tot_time_add * 1000)
        values_binarytree_min.append(tot_time_min * 1000)
        values_binarytree_max.append(tot_time_max * 1000)
 
        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = MinMaxHeap()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax
 
        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5
 
        values_heap_add.append(tot_time_add * 1000)
        values_heap_min.append(tot_time_min * 1000)
        values_heap_max.append(tot_time_max * 1000)
 
        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxBubble()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax
 
        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions
 
        values_bubble_add.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)
 
    xlabels = range(step, max_operations, step)
 
    plt.plot(xlabels, values_binarytree_add, label='Add')
    plt.plot(xlabels, values_binarytree_min, label='Get Min')
    plt.plot(xlabels, values_binarytree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Binary Tree Solution")
    plt.show()
 
    plt.plot(xlabels, values_quicksort_add, label='Add')
    plt.plot(xlabels, values_quicksort_min, label='Get Min')
    plt.plot(xlabels, values_quicksort_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Quicksort Solution")
    plt.show()
 
    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()
 
    plt.plot(xlabels, values_bubble_add, color='b', linestyle='-', label='Add')
    plt.plot(xlabels, values_bubble_min, color='b', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_bubble_max, color='b', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Bubble Sort")
    plt.show()
 
    plt.plot(xlabels, values_binarytree_add, color='g', linestyle='-', label='Vittoria Add')
    plt.plot(xlabels, values_quicksort_add, color='r', linestyle='-', label='QuickSort Add')
    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Add")
    plt.show()
 
    plt.plot(xlabels, values_binarytree_min, color='g', linestyle='--', label='Vittoria Get Min')
    plt.plot(xlabels, values_quicksort_min, color='r', linestyle='--', label='QuickSort Get Min')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Min")
    plt.show()
 
    plt.plot(xlabels, values_binarytree_max, color='g', linestyle='-.', label='Vittoria Get Max')
    plt.plot(xlabels, values_quicksort_max, color='r', linestyle='-.', label='QuickSort Get Max')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Max")
    plt.show()
 
    plt.plot(xlabels, values_binarytree_add, color='g', linestyle='-', label='Vittoria Add')
    plt.plot(xlabels, values_binarytree_min, color='g', linestyle='--', label='Vittoria Get Min')
    plt.plot(xlabels, values_binarytree_max, color='g', linestyle='-.', label='Vittoria Get Max')
    plt.plot(xlabels, values_bubble_add, color='y', linestyle='-', label='Heap Add')
 
    plt.plot(xlabels, values_quicksort_add, color='r', linestyle='-', label='Matteo Add')
    plt.plot(xlabels, values_quicksort_min, color='r', linestyle='--', label='Matteo Get Min')
    plt.plot(xlabels, values_quicksort_max, color='r', linestyle='-.', label='Matteo Get Max')
    plt.plot(xlabels, values_bubble_min, color='y', linestyle='--', label='Heap Get Min')
 
    plt.plot(xlabels, values_heap_add, color='b', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_heap_min, color='b', linestyle='--', label='Heap Get Min')
    plt.plot(xlabels, values_heap_max, color='b', linestyle='-.', label='Heap Get Max')
    plt.plot(xlabels, values_bubble_max, color='y', linestyle='-.', label='Heap Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of the Binary Tree, QuickSort, Heap solutions")
    plt.show()

