tenDem = input("Hãy nhập tên đệm của bạn: ")
print("Tên đệm của bạn là:", tenDem)

def timNtheoTenDem(hoVaTen):
    array = hoVaTen.split(" ")
    nString = ""
    for i in range(0, len(array)):
        doDai = len(array[i])
        nString = nString + str(doDai)
    return int(nString)

n = int(timNtheoTenDem(tenDem))
print("Số nguyên n theo tên đệm của bạn là:", n)

def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;

print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));