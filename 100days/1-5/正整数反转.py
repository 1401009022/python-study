"""
在求水仙花数中，我们通过整除和求模运算分别找出了一个三位数的个位、十位和百位，
这种小技巧在实际开发中还是常用的。用类似的方法，我们还可以实现将一个正整数反转，
例如：将12345变成54321，代码如下所示。
"""
num = int(input('请输入一个正整数：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

