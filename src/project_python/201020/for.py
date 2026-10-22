# for num in range (3):
#     print(num)

for i in range(0, 9, 3):
        print()
#     print(f"1*{i+1} = {1*{i+1}}")
        for j in range(9):
                print(f"{i+1}*{j+1} = {(i+1)*(j+1)} ", end="\t")
                print(f"{i+2}*{j+1} = {(i+2)*(j+1)} ", end="\t")
                print(f"{i+3}*{j+1} = {(i+3)*(j+1)} ", end="\t")
                print(f"{i+4}*{j+1} = {(i+4)*(j+1)} ", end="\t")
                print(f"{i+5}*{j+1} = {(i+5)*(j+1)} ", end="\t")
                print()
# 外層迴圈控制筆數，內層迴圈控制欄位筆數

# while True:
#         print("1")

count = 0
while count < 5:
        print(f"count 小於5, {count}")
        count = count + 1 #控制條件的變