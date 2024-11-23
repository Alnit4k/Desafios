while True:
    try:  
        a, b = [int(x) for x in input("Enter 2 numbers >>> ").split()]

        print(a^b)

    except EOFError:
            break