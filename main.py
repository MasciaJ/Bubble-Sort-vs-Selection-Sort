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

tamaños = [100, 200, 400, 800, 1000]

tiempos_bubble = []
tiempos_selection = []

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

plt.plot(tamaños, tiempos_bubble, marker="o", label="Bubble Sort")
plt.plot(tamaños, tiempos_selection, marker="o", label="Selection Sort")
plt.title("Bubble Sort vs Selection Sort")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.show()