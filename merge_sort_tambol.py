
import time
import pandas as pd

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    df = pd.read_csv("tambol.csv")
    data = df.values.tolist()
    start_time = time.time()
    merge_sort(data)
    end_time = time.time()
    print(f"Merge Sort Time: {round(end_time - start_time, 5)} seconds")
