#Ассоциация - наследование при котором один класс является полем другого класса (Целое состоит из частей)
# ассоциация-КОМПОЗИЦИЯ - в UML (Унифицированный язык моделирования) - линия с закрашенным ромбом (часть удалена объект-целое удаляется)
class Salary:
    def __init__(self, pay):
        self.pay = pay # оплата за месяц
    # метод вывода зарплаты за год
    @property
    def getSummOfYear(self):
        return int(self.pay*12)
        
class Worker:
    def __init__(self, pay,bonus,name):
        self.pay = pay
        self.bonus = bonus
        self.name = name
        
    # метод - выводит зарплату сотрудника за год вместе с премией
    def getSummOfYearForWorker(self):
        return f"Зарплата за год вместе с примией у сотрудника {self.name} состовляет {self.bonus + self.pay.getSummOfYear}"

# класс КОМПОЗИЦИЯ
class Tax:
    def __init__(self, pay, bonus, tax, name_tax):
        self.pay = pay
        self.bonus = bonus
        self.name_tax = name_tax
        self.tax = tax
        self.salary = Salary(self.pay) # атрибут self.salary является объектом класса Salary
    #метод вывода налога 
    @property
    def getTaxOfYear(self):
        return int(self.bonus + int(self.salary.getSummOfYear)) * self.tax / 100

    #метод вывода налолга с поиснением
    @property
    def getInormationOfTax(self):
        return f"Сумма налога {self.name_tax} за год составила {self.getTaxOfYear} рублей"
        
        
# объект - зарплата за месяц
salary_of_month = Salary(20000)
print(salary_of_month.getSummOfYear)
# обект - работник
sasha = Worker(salary_of_month,20000,'Саша')
print(sasha.getSummOfYearForWorker())
tax = Tax(20000,20000,13,'подоходный для физических лиц')
print(tax.getInormationOfTax)