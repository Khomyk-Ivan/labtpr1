def read_file():
    with open('D:\\L1.txt', 'r') as f:
        arr1 = [[int(num) for num in line.split(' ')] for line in f]
    print('Your text : ', arr1)
    return arr1

def valds_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(min(array1[i]))
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)

def laplas_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(round(sum(array1[i])/3, 1))
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)

def gurvic_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(min(array1[i])*0.1+max(array1[i])*0.9)
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)

def baes_laplas_method(array1, array2, best_option):
    arr = []
    for i in range(len(array1)):
        array2[i].append(array1[i][0]*0.55 + array1[i][1] * 0.3 + array1[i][2] * 0.15)
        arr.append(array2[i][-1])
    best_option.append(arr.index(max(arr))+1)
    print(best_option)
    print(array2)

array1 = read_file()
array2 = read_file()
best_option = []
valds_method(array1, array2, best_option)
laplas_method(array1, array2, best_option)
gurvic_method(array1, array2, best_option)
baes_laplas_method(array1, array2, best_option)

