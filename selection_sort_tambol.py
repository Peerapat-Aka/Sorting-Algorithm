
import time
import pandas as pd

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    df = pd.read_csv("tambol.csv")
    data = df.values.tolist()
    start_time = time.time()
    selection_sort(data)
    end_time = time.time()
    print(f"Selection Sort Time: {round(end_time - start_time, 5)} seconds")
