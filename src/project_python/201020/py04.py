a = 30
b = 20
if  a<b :
    print("a < b")
    print("區塊語法都會被執行")
else:
    print("條件不成立")

if a > b:
    print("a > b 成立")
elif a == b:
    print("a == b 成立")
elif a > b:
    print("a > b 不成立")
else:
    print("都不成立")

if a < b and a == 30 and b == 5:
    print("複合條件")

if a > b :
    if a ==30 :
        print("巢狀式條件")
