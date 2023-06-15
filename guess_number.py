import random

min = input('請輸入隨機範圍最小值：')
max = input('請輸入隨機範圍最大值：')
min = int(min)
max = int(max)

r = random.randint(min,max)
time = 0 
while True :
    time = time + 1
    guess = input('請輸入您猜的數字：')
    guess = int(guess)
    if r == guess : 
        print('恭喜您答對了')
        print('您總共猜了',time,'次')
        break
    elif r > guess : 
        print('您猜的數字比答案案還要小喔！')
    else  :
        print('您猜的數字比答案案還要大喔！')
    print('您總共猜了',time,'次')
    