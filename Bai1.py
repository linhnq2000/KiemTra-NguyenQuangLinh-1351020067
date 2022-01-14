name = input("Hãy nhập tên của bạn: ")
print("Tên của bạn là: ", name)

n = len(str(name))
print("Độ dài tên của bạn là: ",n)
 
d = dict()
for i in range(1, n + 1):
    d[i] = i * i
 
print (d)