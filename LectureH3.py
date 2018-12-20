import random, time, heapq

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
        return self.content_max[100]


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

class Quicksort(object):

    def __init__(self):
        self.content = []

    def partition(arr, low, high):
        i = (low -1)
        pivot = arr [high]
        for j in range(low, high):
            if arr [j] <= pivot:
                i = i +1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quick_sort(arr, low, high):
        if low < high:
            pi= partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    def add(self, value):
        self.content.append(value)

    def get_min(self):
        return min(self.content)

    def get_max(self):
        return max(self.content)


class BinaryTre(object):

    def __init__(self):
        self.content = []

        class Node:
            def __init__(self, val):
                self.l =  None
                self.r = None
                self.v = val

        class Tree:
            def __init__(self):
                self.root = None

            def getroot(self):
                return self.root

            def add(self, val):
                if (self.root == Node):
                    self.root = Node(val)
                else:
                    self._add(val, self.root)

            def _add(self, val, node):
                if (val < node.v):
                    if (node.l != None):
                        self._add(val, node.l)
                    else:
                        node.l = Node(val)
                else:
                    if (node.r != None):
                        self._add(val, node.r)
                    else:
                        node.r = Node(val)

            def find(self,val):
                if (self.root != None):
                    return self._find(val, self.root)
                else:
                    return None

            def _find(self,val, node):
                if (val == node.v):
                    return node
                elif (val < node.v and node.l  != None):
                    self._find(val, node.l)
                elif (val > node.v and node.r  != None):
                    self._find(val, node.r)

            def deleteTree(self):
                self.root = None

            def printTre(self):
                if (self.root!= None):
                    self._printTree(self.root)

            def _printTree(self, node):
                if (node != Node):
                    self._printTree(self.root)
                    print (str(node.v) + ' ')
                    self._printTree(node.r)

            def add(self,value):
                self.content.append(value)

            def get_min(self):
                return min(self.content)

            def get_max(self):
                return max(self.content)

