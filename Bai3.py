def ho_ten(number):
    str1 = str(number);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;

ho = input("Hãy nhập họ của bạn: ")
dem = input("Hãy nhập tên đệm của bạn: ")
ten = input("Hãy nhập tên của bạn: ")
print("Tên đầy đủ của bạn là: ",ho +" "+dem+" " + ten)

dem1=len(ten)
dem2=len(dem)
dem3=len(ho)
number=dem1+dem2+dem3

print(number ,"là", ho_ten(number))