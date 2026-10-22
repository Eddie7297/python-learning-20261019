"""
IF練習

1.設計一個程式接收使用者輸入考試分數(0~100分)
2.每10分一個級距 A級為90分以上(包含90)，B級為80分以上，以此類推至E級
    輸出分數轉換後的等級
3.不滿E級就輸出不及格
4.使用IF完成
"""
score = input("請輸入您的分數:")
if int(score) >= 0 and int(score) <= 100:
    print("輸入的分數格式正確，進行轉換")
    #設定一個變數接下型別轉換後的SCORE
    intScore = int(score)
    if intScore >= 90:
        print("A級")
    elif intScore >= 80:
        print("B級")
    elif intScore >= 70:
        print("C級")
    elif intScore >= 60:
        print("D級")
    elif intScore >= 50:
        print("E級")
    else:
          print("不及格")
else:
    print("輸入的數字不符合，程式將結束")

