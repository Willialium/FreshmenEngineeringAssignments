def decimalToBinary(n):
    if n == 0:
        return ''
    else:
        return decimalToBinary(n // 2) + str(n % 2)


print(decimalToBinary(15))
