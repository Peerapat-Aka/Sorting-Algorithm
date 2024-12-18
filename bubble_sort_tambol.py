
import time
import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    df = pd.read_csv("tambol.csv")
    data = df.values.tolist()
    start_time = time.time()
    bubble_sort(data)
    end_time = time.time()
    print(f"Bubble Sort Time: {round(end_time - start_time, 5)} seconds")
