def bubbleSort(vector):
    n = len(vector)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]

    print(f'\n{vector}\n')

    return vector
            