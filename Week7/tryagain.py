Shop = 0  
while True:
    try:
        num = input("ใส่ราคาสินค้า (หรือพิมพ์ 'exit' เพื่อสิ้นสุด): ")
        if num == "exit":
            break  
        num = int(num)  
        if num == 0:  
            raise ZeroDivisionError
        elif num < 0:
            raise Exception
        else:
            Shop += num 
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากกว่า 0 ")
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ ")
print(f"ยอดขายรวมทั้งหมด: {Shop} บาท")

