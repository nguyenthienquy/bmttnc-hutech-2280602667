# Nhập các dòng từ người dùng
print("Nhập các dòng từ văn bản (Nhập 'done' để kết thúc ): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
# Chuyển các dòng thành chữ in hoa và in ra màn hình
print("\n Các dòng đẫ nhập sau khi chuyển thành chữ in hoa: ")
for line in lines:
    print(line.upper())