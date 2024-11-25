try:
    a = 5
    b = int(input("ใส่ตัวเลข : "))
    if b == 0:
        raise ZeroDivisionError ()
    else:
        c = a*b
    print(c)
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except:
    print("ห้ามใส่ 0")   