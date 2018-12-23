import random, time, heapq


class MinMaxQuick(object):

    def __init__(self):
        self.content = []

    def partition(arr, low, high):
        i = (low - 1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quick_Sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_Sort(arr, low, pi - 1)
            quick_Sort(arr, pi + 1, high)

    def add(self, value):
        self.content.append(value)


    def get_min(self):
        return min(self.content)

    def get_max(self):
        return max(self.content)



class MinMaxTree(object):

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = MinMaxTree(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = MinMaxTree(data)
                else:
                    self.right.add(data)
            else:
                self.data = data

    def get_min(self):
        if self.left:
            self.left.get_min()
        else:
            return self.data


    def get_max(self):
        if self.right:
            self.right.get_max()
        else:
            return self.data

class MinMaxHeap(object):

    def __init__(self):
        self.content_min = []
        self.content_max = []

    def add(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)

    def get_min(self):
            return self.content_min[0]

    def get_max(self):
        return self.content_max[0]


class MinMaxBubble(object):
    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content)-1, 0, -1):
            for i in range(passnum):
                if self.content[i] > self.content[i+1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i+1]
                    self.content[i+1] = temp

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


if __name__ == '__main__':

    repetitions = 3
    max_operations = 1000
    data = random.randint(0,1000)

    values_quick_add, values_quick_min, values_quick_max = [], [], []
    values_tree_add, values_tree_min, values_tree_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []
    for rounds in range(100, max_operations, 100):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 1000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxQuick()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        print('QuickSort add:', tot_time_add, 'QuickSort min:', tot_time_min, 'QuickSort max:', tot_time_max)

        values_quick_add.append(tot_time_add * 1000)
        values_quick_min.append(tot_time_min * 1000)
        values_quick_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
           a = MinMaxTree(data)
           myadd, mymin, mymax = measure_time(a, this_list)
           tot_time_add += myadd
           tot_time_min += mymin
           tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        print('BinaryTree add:', tot_time_add, 'BinaryTree min:', tot_time_min, 'BinaryTree max:', tot_time_max)

        values_tree_add.append(tot_time_add * 1000)
        values_tree_min.append(tot_time_min * 1000)
        values_tree_max.append(tot_time_max * 1000)

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(repetitions):
            a = MinMaxHeap()
            myadd, mymin, mymax = measure_time(a, this_list)
            tot_time_add += myadd
            tot_time_min += mymin
            tot_time_max += mymax

        tot_time_add /= repetitions
        tot_time_min /= repetitions
        tot_time_max /= repetitions

        print('Heap add:', tot_time_add, 'Heap min:', tot_time_min, 'Heap max:', tot_time_max)

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

        print('BubbleSort add:', tot_time_add, 'BubbleSort min:', tot_time_min, 'BubbleSort max:', tot_time_max)

        values_bubble_add.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)

    import matplotlib.pyplot as plt

    xlabels = range(100, max_operations, 100)

    plt.plot(xlabels, values_quick_add, label='Add')
    plt.plot(xlabels, values_quick_min, label='Get Min')
    plt.plot(xlabels, values_quick_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of QuickSort's Solution")
    plt.show()
    plt.savefig('QUicksort solution')

    plt.plot(xlabels, values_tree_add, label='Add')
    plt.plot(xlabels, values_tree_min, label='Get Min')
    plt.plot(xlabels, values_tree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of BinaryTree's Solution")
    plt.show()
    plt.savefig('Binary Tree solution')


    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap's Solution")
    plt.show()
    plt.savefig('Heap solution')

    plt.plot(xlabels, values_bubble_add, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_bubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble's Solution")
    plt.show()
    plt.savefig(' Bubble solution')

    plt.plot(xlabels, values_quick_add, label='Add(quick)')
    plt.plot(xlabels, values_quick_min, label='Get Min(quick)')
    plt.plot(xlabels, values_quick_max, label='Get Max(quick)')
    plt.plot(xlabels, values_tree_add, label='Add(BynTree)')
    plt.plot(xlabels, values_tree_min, label='Get Min(BynTree)')
    plt.plot(xlabels, values_tree_max, label='Get Max(BynTree)')
    plt.plot(xlabels, values_heap_add, label='Add(heap)')
    plt.plot(xlabels, values_heap_min, label='Get Min(heap)')
    plt.plot(xlabels, values_heap_max, label='Get Max(heap)')
    plt.plot(xlabels, values_bubble_add, label='Add(bubble)')
    plt.plot(xlabels, values_bubble_min, label='Get Min(bubble)')
    plt.plot(xlabels, values_bubble_max, label='Get Max(bubble)')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of all solutions")
    plt.show()
    plt.savefig(' All solutions')


