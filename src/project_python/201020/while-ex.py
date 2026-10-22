# #設計客服系統
# #1.呼叫客服
# #2文字聯繫
# #3.留下資料
# #4.離開系統
# #5.輸入1~4選擇功能或按q離開

"""
產生系統選單
"""
def print_menu():
    print("歡迎使用客服系統")
    print("1.呼叫客服")
    print("2.文字聯繫")
    print("3.留下資訊")
    print("4.離開系統")


while True :
    print_menu()

    num=input("請選擇數字:")

    if num == "1":
        print("客服呼叫中")
    elif num == "2":
        mes=input("請留下您的訊息:")
        print(f"已收到您的訊息, {mes}")
    elif num == "3":
        mes2=input("請留下您的資訊:")
        print(f"已收到您的訊息, {mes2}")
    elif num == "4":
        print("已離開系統")
        break
    elif num == "g":
        print("滾")
        break
    else:
        print("滾")

# # for vaule in (1, 2, 3):
# #     if vaule ==2:
# #         continue
# #     print(vaule)

# name = "  小明  "
# clean_name = name.strip()