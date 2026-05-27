import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def selection_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):

        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(lista):
    arr = lista.copy()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menor_pivot = [x for x in arr[1:] if x <= pivot]
        mayor_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(menor_pivot) + [pivot] + quick_sort(mayor_pivot)

tamaños = [100, 200, 400, 800, 1000]

tiempos_bubble = []
tiempos_selection = []
tiempos_insertion = []
tiempos_quick_sort = []

for tamaño in tamaños:

    lista = [random.randint(1, 10000) for _ in range(tamaño)]

    inicio = time.time()
    bubble_sort(lista)
    fin = time.time()
    tiempos_bubble.append(fin - inicio)

    inicio = time.time()
    selection_sort(lista)
    fin = time.time()
    tiempos_selection.append(fin - inicio)

    inicio = time.time()
    insertion_sort(lista)
    fin = time.time()
    tiempos_insertion.append(fin - inicio)

    inicio = time.time()
    quick_sort(lista)
    fin = time.time()
    tiempos_quick_sort.append(fin - inicio)

plt.plot(tamaños, tiempos_bubble, marker="o", label="Bubble Sort")
plt.plot(tamaños, tiempos_selection, marker="o", label="Selection Sort")
plt.plot(tamaños, tiempos_insertion, marker="o", label="Insertion Sort")
plt.plot(tamaños, tiempos_quick_sort, marker="o", label="Quick Sort")
plt.title("Sorting Algorithms Comparison")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.show()