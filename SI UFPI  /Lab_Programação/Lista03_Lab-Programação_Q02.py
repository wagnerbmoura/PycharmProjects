def func_div(num):
    if num%2 == 0 and num%3 ==0:
        return 'SIM'
    else:
        return 'NÃO'

num = 26
result = func_div(num)
print(result)