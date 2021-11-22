import time 
start = time.time()

def insertion(vector):
    trocas = 0
    for j in range(1, len(vector)):
        key = vector[j]
        i = j - 1

        while i >= 0 and vector[i] > key:
            vector[i + 1] = vector[i]
            i = i - 1

            trocas+=1
            print(f'{trocas} trocas')

        vector[i + 1] = key 
        print(f'\n{vector}\n')
    print(f'{(time.time() - start):.4f} segundos\n')
    
    return vector