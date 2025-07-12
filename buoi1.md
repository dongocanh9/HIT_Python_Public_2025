Bài 1 

Ngôn ngữ thông dịch là ngôn ngữ mà mã nguồn được thực thi trực tiếp bởi trình thông dịch (interpreter) mà không cần biên dịch thành mã máy trước.

    Khi chương trình chạy:

Trình thông dịch đọc từng dòng mã nguồn, dịch và thực thi ngay.

Nếu có lỗi, chương trình sẽ báo lỗi tại dòng đó và dừng lại luôn.

Ngôn ngữ biên dịch là ngôn ngữ mà mã nguồn phải được biên dịch thành mã máy (machine code) nhờ một trình biên dịch (compiler) trước khi chạy.

    Khi chương trình chạy:

Trình biên dịch dịch toàn bộ mã nguồn sang file thực thi (.exe/.out).

Sau đó chạy file thực thi mà không cần đến mã nguồn nữa.

    Sơ đồ cơ chế hoạt động Python

Mã nguồn Python (.py) =>Trình thông dịch Python (Interpreter)
=>Dịch sang Bytecode (.pyc trong __pycache__)
=>Python Virtual Machine (PVM)
=>Chạy trên máy tính (hiển thị kết quả)

    Do Python sử dụng trình thông dịch (Interpreter) để thực thi mã nguồn trực tiếp, không biên dịch thành file thực thi độc lập, nên Python được xếp vào nhóm ngôn ngữ thông dịch.
BÀI 2

1.Các liểu dữ liệu trong python 

int : lưu trữ số nguyên, không có phần thập phân.

 Ví dụ: 1, 25, -7

float : lưu số thực (có dấu thập phân).

 Ví dụ: 3.14, -0.5, 2.75

complex : số phức, gồm phần thực và phần ảo (ký hiệu j đại diện cho căn bậc hai của -1).

 Ví dụ: 3+4j, -1+2j

str : chuỗi ký tự nằm trong dấu nháy đơn hoặc nháy kép.

 Ví dụ: "Hello", 'Python'

list : danh sách chứa nhiều giá trị (có thể khác kiểu), thứ tự được giữ nguyên và có thể thay đổi.

 Ví dụ: [1, 2, "Python", 4.5]

tuple : giống list nhưng không thể thay đổi giá trị sau khi tạo (immutable).

Ví dụ: (1, 2, "Python", 4.5)

dict : lưu trữ dữ liệu dưới dạng cặp khóa — giá trị (key: value).

 Ví dụ: {"name": "John", "age": 30}

set : tập hợp các giá trị duy nhất, không có thứ tự và không trùng lặp.

Ví dụ: {1, 2, 3, 4, 5}
2.Các toán tử trong python 

    Toán tử số học:
Dùng để thực hiện các phép tính cơ bản như:

+ : Cộng

- : Trừ

* : Nhân

/ : Chia

% : Chia lấy dư

** : Lũy thừa

// : Chia lấy phần nguyên

Ví dụ:
a = 10, b = 3
a + b = 13, a % b = 1, a // b = 3

    Toán tử so sánh (quan hệ):
Dùng để so sánh hai giá trị, trả về True/False.
Gồm: ==, !=, >, <, >=, <=

Ví dụ:
10 > 5 → True, 3 == 4 → False

Lưu ý: Python 3 không dùng <>, chỉ dùng !=

    Toán tử gán:
Gán giá trị cho biến, có thể kết hợp với phép toán.
Ví dụ:

= : phép gán bằng 

+= : phép gán cộng 

-= : phép gán trừ 

*= : phép gán nhân 

/= : phép gán chia lấy phần nguyên 

%= : phép gán chia lấy phần dư 

**= : phép gán lũy thừa 

//= : phép gán chia floor

Ví dụ:
a = 5; a += 3 → a = 8

    Toán tử logic:
Dùng để kết hợp các điều kiện logic.

and : Cả hai đều đúng → True

or : Một trong hai đúng → True

not : Phủ định kết quả

Ví dụ:

(a > 9 and b > 19) là true

(a > 9 or b > 100) is true.

Not(a > 9) là false

    Toán tử membership:
Kiểm tra một giá trị có thuộc vào danh sách không.

in : Trả về true nếu tìm thấy biến a trong tập các giá trị sau in, ngược lại trả về false.

not in : Trả về false nếu tìm thấy biến a trong tập các giá trị sau in, ngược lại trả về false.

Ví dụ:
3 in [1,2,3] → True

    Toán tử identity (nhận dạng):
So sánh vị trí bộ nhớ (xem hai biến có cùng trỏ đến một đối tượng không).

is : Trả về true nếu 2 biến cùng trỏ về 1 đối tượng giống nhau.

is not : Trả về False nếu hai biến ở hai bên toán tử trỏ đến cùng một đối tượng, và trả về True nếu không.

Ví dụ:\
x = "hello"
y = "hello"

print(x is y)       # True, vì Python lưu 2 chuỗi giống nhau tại cùng 1 chỗ
print(x is not y)   # False, vì x và y cùng vị trí bộ nhớ

    Toán tử thao tác bit 
Thao tác trên từng bit của số nguyên.

& : Sao chép một bit tới kết quả nếu bit này tồn tại trong cả hai toán hạng

| : Sao chép một bit tới kết quả nếu bit này tồn tại trong bất kỳ toán hạng nào

^ : 	Sao chép bit nếu nó được set (chỉ bit 1) chỉ trong một toán hạng

~ : Đây là toán tử một ngôi, được sử dụng để đảo ngược bit

<< : Toán tử dịch trái nhị phân. Giá trị của toán hạng trái được dịch chuyển sang trái một số lượng bit đã được xác định bởi toán hạng phải
 
>> : Toán tử dịch phải nhị phân. Giá trị của toán hạng trái được dịch chuyển sang phải một số lượng bit đã được xác định bởi toán hạng phải

Ví dụ:
Giả sử:

a = 60 → 0011 1100

b = 13 → 0000 1101

Kết quả:

a & b → 0000 1100 (12)

a | b → 0011 1101 (61)

a ^ b → 0011 0001 (49)

~a → 1100 0011 (-61)

a << 2 → 1111 0000 (240)

a >> 2 → 0000 1111 (15)

    Thứ tự ưu tiên toán tử:
Python thực hiện phép tính theo thứ tự từ cao xuống thấp:
Ngoặc () → Lũy thừa ** → Âm - → Nhân/Chia * / // % → Cộng/Trừ + - → So sánh → Logic → Gán

3 Mệnh đề điều kiện vòng lặp

    if
Kiểm tra điều kiện đúng (True) thì thực thi lệnh.

number = 8

if number % 2 == 0:

print("Even number")

    if...elif...else
Dùng khi có nhiều trường hợp.

time = 10

if time < 10:

print("Good morning")

elif time < 20:

print("Good day")

else:
print("Good evening")

 Vòng lặp

    while
Lặp khi điều kiện còn đúng.

x = 0

while x < 5:

print(x)

x += 1

while...else: thực thi else khi thoát vòng lặp.

    for
Lặp qua từng phần tử trong chuỗi, danh sách, hoặc theo chỉ số.

for letter in 'abc':

print(letter)

for...else: thực thi else khi kết thúc vòng lặp bình thường.

    Câu lệnh điều khiển vòng lặp
break: thoát vòng lặp ngay lập tức.

continue: bỏ qua phần còn lại của lần lặp hiện tại, sang vòng tiếp.

Ví dụ:\
for i in range(5):

if i == 3:
break
print(i)

for i in range(5):

if i == 3:
continue
print(i)
4. Kiểu dữ liệu true , false trong python

Là kiểu boolean (bool) — chỉ có 2 giá trị:

True (đúng)

False (sai)

Dùng chủ yếu trong câu lệnh điều kiện và vòng lặp.

