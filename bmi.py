print("歡迎使用bmi計算系統")
height = float(input("請輸入您的身高(公分): "))
weight = float(input("請輸入您的體重(公斤): "))
float_height = height / 100
bmi = weight / (float_height ** 2)
print("您的BMI值為: {:.2f}".format(bmi))
print("BMI分類結果:")
if bmi < 18.5:
    print("體重過輕")
elif 18.5 <= bmi < 24:
    print("體重正常")
elif 24 <= bmi < 27:
    print("體重過重")
elif 27 <= bmi < 30:
    print("輕度肥胖")
elif 30 <= bmi < 35:
    print("中度肥胖")
else:
    print("重度肥胖")