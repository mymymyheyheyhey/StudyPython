# 변수 라이프 스코프
a = 10 # global variable

def vartest(x):
    x += 1 # local variable
    return x

a = vartest(a)
print(a)



