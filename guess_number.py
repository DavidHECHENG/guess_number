import random
r = random.randint(1,100)
time = 1 
while True :
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
    time = time + 1