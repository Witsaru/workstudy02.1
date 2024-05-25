import matplotlib.pyplot as plt
import csv

# อ่านข้อมูลจากไฟล์ CSV และแยกข้อมูลออกเป็นสองลิสต์
all_time = []
time_poor = []

with open('csv_data/Test_02B/all_Time_Test_02B_11.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] != '0':  # ตรวจสอบเพื่อหลีกเลี่ยงข้อมูลที่เป็น 0
            all_time.append(float(row[1]))

with open('csv_data/Test_02B/time_poor_Test_02B_11.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[1] != '0':  # ตรวจสอบเพื่อหลีกเลี่ยงข้อมูลที่เป็น 0
            time_poor.append(float(row[1]))

# สร้างกราฟวงกลม
plt.figure(figsize=(10, 6))

labels = ['All Time', 'Time Poor']
sizes = [sum(all_time), sum(time_poor)]
colors = ['#66b3ff','#ff9999']
print(sizes)

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Total Time vs Time Poor Time is Test_02')
plt.axis('equal')  # ทำให้กราฟเป็นวงกลมแท้

# แสดงกราฟ
plt.show()
