# 員工類別
class Employee:
    # 構造函數，初始化員工屬性
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name 
        self.emp_salary = emp_salary
        self.emp_department = emp_department 

    # 方法用於計算工作時數；如果超過50小時，則計算加班並將其添加到薪水中
    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            salary = self.emp_salary + (overtime * (self.emp_salary / 50))
            return salary
        else:
            salary = self.emp_salary
            return salary

    # 方法用於分配工作內容
    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    # 方法用於打印員工詳細信息
    def print_employee_details(self):
        print(f"員工編號: {self.emp_id}")
        print(f"員工姓名: {self.emp_name}")
        print(f"員工薪水: ${self.emp_salary}")
        print(f"工作內容: {self.emp_department}")

# 飲料的基類
class Drink:
    # 構造函數，初始化飲料屬性
    def __init__(self, drinks_id, drinks_price):
        self.drinks_id = drinks_id
        self.drinks_price = drinks_price

# 冷飲的子類
class Cold(Drink):
    def __init__(self, drinks_id, drinks_price, name, field, temperature):
        super().__init__(drinks_id, drinks_price)  # 使用飲料ID和價格初始化飲料對象。
        self._field = field
        self._temperature = temperature
        self._name = name

    @property
    def cold_field(self):
        return self._field

    @property
    def cold_temperature(self):
        return self._temperature

    @property
    def cold_name(self):
        return self._name

    def practice(self):
        print("冷飲")

    def describe(self):
        print(f"飲料ID: {self.drinks_id}")
        print(f"飲料名稱: {self.cold_name}")
        print(f"飲料價格: ${self.drinks_price}")
        print(f"飲料類別: {self.practice()}")
        print(f"飲料製作區域: {self.cold_field}")
        print(f"飲料溫度: {self.cold_temperature} °C")

# 員工的示例數據
employee1 = Employee("E7876", "ADAMS", 50000, "櫃台")
employee2 = Employee("E7499", "JONES", 45000, "調飲")
employee3 = Employee("E7900", "MARTIN", 50000, "外送")
employee4 = Employee("E7698", "SMITH", 55000, "營運")

# 更改部門的示例
employee1.emp_assign_department("冷飲作業")
employee1.print_employee_details()

# 根據總工作時間計算薪水的示例
total_salary_employee2 = employee2.calculate_emp_salary(55)
print(f"{employee2.emp_name}的總薪水: ${total_salary_employee2}")

# 創建冷飲的示例
cold_drink1 = Cold("D001", 5.99, "Iced Coffee", "Coffee Bar", 4)
cold_drink1.describe()
