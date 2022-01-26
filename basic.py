# 알고리즘

def fib_tab(n):
    fib_list = [0, 1, 1]
    i = 3
    while i <= n:
        fib_list.append(fib_list[i-1] + fib_list[i-2])
        i += 1
    return fib_list[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))