print("โปรแกรมคำนวณค่า BMI")
a = float(input("ใส่ค่าส่วนสูง (เซนติเมตร): "))  
b = float(input("ใส่ค่าน้ำหนัก (กิโลกรัม): "))  
m = b / 100 
bmi = a / (m** 2)  
print(f"BMI ของคุณคือ: {bmi:.2f}")  
 