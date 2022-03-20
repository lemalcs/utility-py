import time

def fibonacci_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter+=1
            yield n1
        elif counter == 1:
            counter+=1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter+=1
            if aux<=max:
                yield aux
            else:
                return

            

if __name__ == "__main__":
    result = fibonacci_gen(144)
    for element in result:
        print(element)
        time.sleep(0.5)