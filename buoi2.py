#bai1
def so_ngay_trong_thang(thang,nam):
    if thang in (1,3,5,7,8,10,12):
        return 31
    elif thang in (4,6,9,11):
        return 30
    elif thang in(2,):
        if (nam % 400 == 0) or (nam % 4==0 and nam % 100 !=0):
           return 29
        else :
            return 28
    else :
        return("Tháng ko hợp lệ ")

print(so_ngay_trong_thang(10,2020))
print(so_ngay_trong_thang(2,2024))
print(so_ngay_trong_thang(2,2025))
print(so_ngay_trong_thang(11,1921))
#bai2
n=int(input("Lương của bạn là bao nhiêu ?"))
if n==15000000:
   thuethunhap=0.3*n
elif 7000000<=n<15000000:
    thuethunhap=0.2*n
else :
    thuethunhap=0.1*n
luongrong=n-thuethunhap
print(f"Thuế : {thuethunhap} Thu nhập : {luongrong}")
#bai3
n=int(input(""))
x=len(str(abs(n)))
z=sum(int(ch)for ch in str(abs(n)))
print(f"Số chữ số : {x} Tổng chữ số :{z}")
#bai4
N=int(input(""))
x=28
chaimua=N//x
vo=chaimua
tongchai=chaimua
while vo>=3:
    chaidoi=vo//3
    tongchai+=chaidoi
    vo=vo%3+chaidoi
print(f"Sốc chai bia có thể mua được là : {tongchai} ")




