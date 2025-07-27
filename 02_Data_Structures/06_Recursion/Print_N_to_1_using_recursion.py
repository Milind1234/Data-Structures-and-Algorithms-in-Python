def Print_Number(n):
    if n == 0 :
        return 0
    print(n)
    Print_Number(n-1)

Print_Number(5)