
import time
import pandas as pd

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x[0] < pivot[0]]
    middle = [x for x in arr if x[0] == pivot[0]]
    right = [x for x in arr if x[0] > pivot[0]]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    df = pd.read_csv("tambol.csv")
    data = df.values.tolist()
    start_time = time.time()
    sorted_data = quick_sort(data)
    end_time = time.time()
    print(f"Quick Sort Time: {round(end_time - start_time, 5)} seconds")
