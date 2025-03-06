worked_hour = float(input("Enter hours worked: "))
your_salary = float(input("Enter your salary per hour: "))
gio_tieu_chuan = 40
gio_vuot_chuan = max(0,worked_hour - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * your_salary + gio_vuot_chuan * your_salary * 1.5
print('Your salary is', thuc_linh)