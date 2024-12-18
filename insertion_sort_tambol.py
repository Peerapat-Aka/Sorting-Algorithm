import timeit
start_time = timeit.default_timer()

def lnsertion_sort_revers(a_list):
    n = len(a_list)
    for i in range(1, n):
        temp = a_list[i]
        hole = i
        while hole > 0 and a_list[hole - 1] < temp:
            a_list[hole] = a_list[hole - 1]
            hole -= 1
        a_list[hole] = temp
    return a_list

file = 'tambol'
list_file = []
with open(f'Sorting-Algorithm/data_txt/tambol.txt', 'r', encoding='utf-8') as files:
    for line in files:
        list_file.append(line.strip())
        
#เริ่ม
list_reversed = lnsertion_sort_revers(list_file)
# แสดงผล
output_file = f'Sorting-Algorithm/output_data_txt/tambol_insertion.txt'
with open(output_file, 'w', encoding='utf-8') as write_province:
    for row in list_reversed:
        write_province.write(f"{row}\n")
        
elapsed = timeit.default_timer() - start_time
print(f"{elapsed} seconds")