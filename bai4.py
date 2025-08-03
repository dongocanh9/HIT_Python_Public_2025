#bai1
a=("1","2","3","4","5","6","7","8")
b=tuple(int(x) for x in a)
if len(b)>0 :
    average = sum (b)/len(b)
else :
    average =0
print(f"tupe ban đầu :{a} ")
print(f"tupe mới :{b} ")
print(f"trung bình cộng :{average} ")
#bai2
A={200,201,202,203,204,205}
B={203,204,207,208}
print(f"Bàn 1= {A}")
print(f"Bàn 2= {B}")
c=int(input("Nhập mã sinh viên : "))
C=A.intersection(B)
if c in C :
    print("Có ")
else :
    print("Không")
E=A.union(B)
D = A.difference(B)
print(f"Danh sách tổng hợp sinh viên đăng ký của 2 bàn :{E}")
print(f"Danh sách sinh viên đăng ký tại bàn 1 mà không đăng ký tại bàn 2 : {D}")
#bai3
n,m = map(int, input("Nhập số và giữa mỗi số có dấu cách ").split())
a=list(map(int,input("Nhập số và giữa mỗi số có dấu cách").split()))
A=set(map(int,input("Nhập số và giữa mỗi số có dấu cách").split()))
B=set(map(int,input('Nhập số và giữa mỗi số có dấu cách').split()))
happiness=0
for x in a :
    if x in A :
        happiness+=1
    elif x in B :
        happiness-=1
    else :
        pass
print (happiness)
#bai4
n=int(input("Nhập số phần tử n : "))
a=(input(f"Nhập phần tử thứ {i+1}:") for i in range (n))
b=tuple(a)
count=sum( 1 for x in b if x.isdigit())
print(count)
