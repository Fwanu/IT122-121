#By Clark Daryll B. OMASDANG
#IT1R13
#fibonacci sequence 
def fibonacci(nibba):
    sequence = [1, 1]
    for i in range(2, nibba):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[-1]

def main():
    nibba = int(input("Enter an Index: "))
    fib_number = fibonacci(nibba)
    print("The Fibonacci number at index", nibba, "is:", fib_number)

if __name__ == "__main__":
    main()




    