
import matplotlib.pyplot as plt
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield arr
        if not swapped:
            break


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swapped = True
        yield arr
        if not swapped:
            break



def insertion_sort(arr):
    for i in range(1, len(arr)):
        swapped = False
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        swapped = True
        yield arr
        if not swapped:
            break




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        yield arr  




def quick_sort(arr):
    if len(arr) <= 1:
        yield arr
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    yield from quick_sort(left)  
    yield middle
    yield from quick_sort(right)  


    arr[:] = left + middle + right
    yield arr



def animate_sorting(sort_func, arr):
    start_time = time.time()  
    fig, ax = plt.subplots()
    ax.set_title('Sorting Animation')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    bars = ax.bar(range(len(arr)), arr)

    for updated_arr in sort_func(arr):
        for bar, height in zip(bars, updated_arr):
            bar.set_height(height)
        plt.pause(0.1)
        plt.draw()
    
    end_time = time.time()
    print("Time taken for sorting:", end_time - start_time, "seconds")


x=1
while x!= 0:
   
    array_input = input("Enter the array elements separated by space: ")

    array = list(map(int, array_input.split()))

    print("Array elements entered: ", array)

    sort =int(input("chose the sorting algo (1=bubble, 2=selection, 3=insertion, 4=merge, 5=quick):"))
    
    if sort == 1:
        animate_sorting(bubble_sort, array)
       
    elif sort == 2:
        animate_sorting(selection_sort, array)
        
    elif sort == 3:
        animate_sorting(insertion_sort, array)
        
    elif sort == 4:
        animate_sorting(merge_sort, array)
        
    elif sort == 5:
        animate_sorting(quick_sort, array)
        
    else:
        print("Wrong input")
    
    
    x = int(input("Do you want to continue? (1=yes, 0=no): "))
    plt.close('all')

