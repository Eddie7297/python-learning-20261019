hours_per_day = 2
days = 5
total_hours = hours_per_day * days
A = 10
a = 20
#盡量不要用中文
chinese_type = 120
print(total_hours)
print(chinese_type)
# 井字號為註解符號
# 單行註解指令為  ctrl+/
# 多行註解 三個雙引號開頭，三個雙引號結尾 """"""

# if a>10:
#     print("a > 10")
#     print("a > 10")

number1 = int(input("請輸入整數:"))
number2 = int(input("請輸入另一個整數:"))
x = input("請輸入+、-、*、/、%其中一個運算符號:")

if x == "+":
    print(number1 + number2)
elif x == "-":
    print(number1 - number2)
elif x == "*":
    print(number1 * number2)
elif x == "/":
    print(number1 / number2)
elif x == "%":
    print(number1 % number2)
