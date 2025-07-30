#bai1
N = int(input("Nhập N: "))
lst = list(map(int, input(f"Nhập {N} số nguyên, cách nhau bởi khoảng trắng: ").split()))
lst = lst[:N]
print("List:", lst)

X = int(input("Nhập X: "))
print("Số lần", X, "xuất hiện:", lst.count(X))

lst[1:7] = [8, 5, 4, 0, 1, 3]
print("List sau thay thế:", lst)

print("Max:", max(lst))
print("Min:", min(lst))

Y = int(input("Nhập Y: "))
lst.insert(0, Y)
print("List sau chèn Y:", lst)

if lst == sorted(lst):
    print("TĂNG")
elif lst == sorted(lst, reverse=True):
    print("GIẢM")
else:
    print("NO")

#bai2
k = int(input("Nhập k: "))
a = list(map(int, input(f"Nhập {k} số nguyên (cách nhau bởi khoảng trắng): ").split()))[:k]
n, m = map(int, input("Nhập n m: ").split())
if n * m > k:
    print("NO")
else:
    X = []
    need = n * m
    b = a[:need]
    for i in range(n):
        X.append(b[i*m:(i+1)*m])
    print(X)
#bai3
s1 = input("s1 = ")
s2 = input("s2 = ")
print("Đảo ngược s1:", s1[::-1])

a = int(input("a = "))
b = int(input("b = "))
if 1 <= a < b <= len(s2):
    start = a - 1
    s2_new = s2[:start] + s2[start:b][::-1] + s2[b:]
    print("s2 sau khi đảo đoạn a..b:", s2_new)
else:
    print("a, b không hợp lệ")
s3 = s1[::2]
print("s3:", s3)
min_len = min(len(s1), len(s2))
s4 = ""
for i in range(min_len):
    s4 += s1[i] + s2[i]
s4 += s1[min_len:] + s2[min_len:]
print("s4:", s4)
# bai4
s = input("Nhập họ tên: ")
a = " ".join(s.strip().split()).title()
print(a)
