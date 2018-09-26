__author__ = 'Daniel Garcia Alonso'


def decimalABinario(decimal):
    if decimal == 0:
        return 0

    binario=''
    decimal2 = int(decimal)
    while (decimal2 > 0):
        binario+= str(decimal2%2)
        decimal = int(decimal2/2)

    return binario[::-1]

print(decimalABinario(212))

