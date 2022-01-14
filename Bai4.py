name = input("Hãy nhập tên của bạn: ")
msv = input("Hãy nhập msv của bạn: ")
print(name + msv)

l=(name + msv).split(",")
t=tuple(l)
print (l)
print (t)

# Kết Quả
# Hãy nhập tên của bạn: Linh
# Hãy nhập msv của bạn: 1351020067
# Linh1351020067     
# ['Linh1351020067'] 
# ('Linh1351020067',)
