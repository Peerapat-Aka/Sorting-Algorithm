
import time
import pandas as pd

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    df = pd.read_csv("tambol.csv")
    data = df.values.tolist()
    start_time = time.time()
    insertion_sort(data)
    end_time = time.time()
    print(f"Insertion Sort Time: {round(end_time - start_time, 5)} seconds")
