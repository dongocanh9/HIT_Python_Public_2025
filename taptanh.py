#string
first_name = "Bro"
food = " pizza"
print (f"Hello {first_name}")
print (f"I like{food}")
#integer
age = 25
print (f"you are {age} years old")
#float
gpa = 3.25
print(f"i want to more {gpa}")
#boolean
is_student = True
if is_student :
    print("you are a student")
else :
    print("you are not a student")
# typecasting ; chuyển đổi kiểu dữ liệu str(). int (), float(), bool()
gpa = 3.2
name ="Ánh"
window = 10
is_student = True

gpa=str(gpa)
print(gpa)
name=bool(name)
print(name)
window=float(window)
print(window)
#input()
name = input("what is your name ? ")
gpa=float(input("gpa của cậu là bao nhiêu ?"))
gpa=int(gpa)
print(gpa)
gpa=gpa+1
print(f"Hello {name}!")
print(f"gpa của tớ là {gpa}")
#bài tập 1 ; TÍNH DIỆN TÍCH HÌNH CHỮ NHẬT
chieudai = float(input("chiều dài của cái hộp là bao nhiêu ?"))
chieurong = float(input("chiều rộng của cái hộp là bao nhiêu ?"))
dientich=chieudai*chieurong
print (f"tổng diện tích sẽ là {dientich} cm\u00B2")
#bài tập 2 : tính tiền lương nhân viên
name = str(input("tên của nhân viên ? : "))
day=int(input("số ngày (name) làm việc ?"))
money = float(input("lương/ngày" ))
cong=day*money
print(f"nhân viên {name} có tổng lương là {cong}đồng")
#bài tập 2 : tính tiền lương nhân viên
name = str(input("tên của nhân viên ? : "))
day=int(input(f"số ngày {name} làm việc ?"))
money = float(input("lương/ngày " ))
cong=day*money
print(f"nhân viên {name} có tổng lương là {cong} đồng")
#bài tập 3 : tính số phút đã sống
age =int(input("How old are u ?"))
day=age*365
phut=day*1440
print(f"Bạn đã sống khoảng {day} ngày tương đương khoảng {phut} phút ")

