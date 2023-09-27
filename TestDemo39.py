F0 = 0 (n=0)
F1 = 1 (n=1)
Fn = F[n-1]+F[n-2](n=>2)
 

要求一：输出第10个斐波那契数列

方法一：

def fib(n):
    a,b = 1,1
 for i in range(n-1):
        a,b = b,a+b
 return a

 方法二：使用递归方法来解救这个问题。

def fib(n):
 if n==1 or n==2:
 return 1
 return fib(n-1)+fib(n-2)
结果为55，这里就先不演示了。

要求二：问题的要求改为：需要输出指定个数的斐波那契数列，要怎么来解决呢？我们往下看。

def fib(n):
 if n == 1:
 return [1]
 if n == 2:
 return [1, 1]
    fibs = [1, 1]
 for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
 return fibs