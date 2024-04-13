# # n = int(input())
# # check = True
# # for i in range(2,n):
# #     if n%i == 0:
# #         check = False
# #         break
# # if check :
# #     print("so nguyen to")
# # else:
# #     print("khong phai so nguyen to")
# n = int(input())
# count = 0
# for i in range(2,n+1):
#     check = True
#     for j in range(2,i):
#         if i%j == 0:
#             check = False
#     if check == True:
#         count = count + 1
# print(count)
point = 0
print("Câu 1: Python được phát hành vào năm nào?", "A. 1991", "B. 1989", "C. 2000", "D. 1995")
answer = input()
if answer == "a" or answer == "A":
    point = point + 1
    print("Dung")
else:
    print("sai")
print("Ai là người tạo ra Python?", "A. Guido van Rossum", "B. Dennis Ritchie", "C. James Gosling", "D. Bjarne Stroustrup")
answer = input()
if answer == "a" or answer == "A":
    point = point + 1
    print("Dung")
else:
    print("sai")
print("Câu lệnh nào dùng để hiển thị dữ liệu ra màn hình trong Python?", "A. print()", "B. cout<<", "C. System.out.println()"," D. echo")
answer = input()
if answer == "a" or answer == "A":
    point = point + 1
    print("Dung")
else:
    print("sai")
print(point)