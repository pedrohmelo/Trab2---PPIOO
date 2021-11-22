import time 
start = time.time()

def selection(vector):
    trocas = 0
    for i in range(len(vector)):
        min = i
        for j in range(i+1, len(vector)):
            if vector[min] > vector[j]:
                min = j

        print(f'{vector}\n')
        if i != min:
            vector[i], vector[min] = vector[min], vector[i]
            trocas+=1
            print(f'{trocas} trocas\n')

    print(f'{(time.time() - start):.4f} segundos\n')
    print(f'Total de trocas: {trocas} \n')
    
    return vector