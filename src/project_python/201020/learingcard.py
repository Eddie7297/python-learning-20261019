# 課堂練習：學習資料卡
name = input("請輸入您的尊姓大名:")
x = input("您本期最想完成甚麼作品?:")
hours = float(input("每天學習幾小時?: "))
days = input("每週學習幾天?:")
weeks = input("預計學習幾週?:")

# print(f"我叫{name}, 我這期最想完成的作品是{x}, 我每天學習{round(hours, 2)}小時, 我一週學習{days}天， 我預計學習{weeks}週。")
print(f"我叫{name}, 我這期最想完成的作品是{x}, 我每天學習{hours}小時, 我一週學習{days}天， 我預計學習{weeks}週。")
