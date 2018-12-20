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
           a = MinMaxTree()
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

    plt.plot(xlabels, values_tree_add, label='Add')
    plt.plot(xlabels, values_tree_min, label='Get Min')
    plt.plot(xlabels, values_tree_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of BinaryTree's Solution")
    plt.show()

    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap's Solution")
    plt.show()

    plt.plot(xlabels, values_bubble_add, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_bubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Bubble's Solution")
    plt.show()

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