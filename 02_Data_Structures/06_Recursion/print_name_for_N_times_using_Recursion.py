def Print_name(n):
    if n == 0:
        return
    print("XYZ")
    Print_name(n-1)
    
Print_name(5)