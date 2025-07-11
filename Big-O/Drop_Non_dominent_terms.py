def print_items(n):              #|
    for i in range(n):           #|...................O(N)    |
        for j in range(n):       #|...................O(N)    |
            print(f"( {i} , {j} )")  #| 

    for k in range(n):
        print(k)

print_items(10)