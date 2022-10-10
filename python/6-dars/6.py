# while loops -- cheksiz takrorlash operatori

# 1-usul
# raqam  = input("Raqam kiriting: ")

# while raqam == "":
#     raqam  = input("Raqam kiriting: ")
#     print(raqam)

# 2-usul
# raqam  = ""

# while len(raqam) == 0:
#     raqam  = input("Raqam kiriting: ")
#     print(raqam)

# 3-usul
# while True:
#     raqam = input("Raqam kiriting: ")
#     print(raqam)
#     if raqam != "" :
#         break

# continue -> biz hozlagan narsalarni tashlab ketadi 
# telefon = "998-90-755-21-77"
# for x in telefon:
#     if x == "-":
#         continue
#     print(x, end="")

# for i in range(1,11):
#     if i == 6:
#         pass
#     else:
#         print(i)

# import time
# from traceback import print_list
# havo_1 = int(input("Havo harorati qanaqa: "))
# if havo_1 >= 20 and havo_1 <= 30:
#     print("Men ishga chiqaman")
#     time.sleep(1)
#     print("Chunki bugun havo yaxshi")
    
# elif havo_1 >= 30 and havo_1 <= 60:
#     print("Men bugun uydaman")
#     time.sleep(1)
#     print("Chunki havo issiq")
# elif havo_1 >= 60 and havo_1 <= 100:
#     print("Men ishga bormiman ")
#     time.sleep(1)
#     print("Chunki kun issiq")
# elif havo_1 >= -20 and havo_1 <= 0:
#     print("Bugun havo juda ham sovuq")
#     time.sleep(1)
#     print("Men kochaga chiqa olmiman")

for x in range(1, 11):
    if x == 3 or x == 4 or x == 7:
        continue
    print(x)
    
    