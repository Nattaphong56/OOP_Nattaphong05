try:  
    num = int(input("ใส่ยอด : "))  
    if num == 0:
        raise ZeroDivisionError()
    elif num < 0 :
        raise Exception()
    elif num >= 5000:
        nine =  num * 0.2
        nine1 = num - nine
        print(f"20% Discount = {nine} num = {nine1}")
    elif num >= 2000:
        nine =  num * 0.1
        nine1 = num - nine
        print(f"10% Discount = {nine} num = {nine1}")
    else:
        print("คุณไม่ได้รับส่วนลด")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")