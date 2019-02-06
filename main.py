'''
File: main.py
Developer: Jonathan Martinez
Date last modified: 12/16/2017
Description: A simple payroll manager that reads in employee data and prints out their info
Email: jonathanmartineztek@gmail.com
'''
import csv

class Employee:
  def __init__(self,num,name):
    self.number = num
    self.name = name
    
class ProductionWorker(Employee):
  def __init__(self,num,name,shift,rate,hrs):
    Employee.__init__(self,num,name)
    self.shift = shift
    self.rate = rate
    self.hours = hrs
    self.pay = float(rate) * float(hrs)

class ShiftManager():
  def __init__(self):
    self.employees = {}
  
  def add_employee(self, em):
    self.employees[em.name] = em

  def print_report(self):
    print('Number |Name\t\t|shift\t\t|Payrate\t|HourlyWorked\t|Pay')
    for key in self.employees:
      
      em = self.employees[key]
      print("%s\t%s\t%s\t\t%s\t\t%s\t\t%s" %(em.number, em.name, em.shift, em.rate , em.hours, em.pay))

worker = ShiftManager()
csvfile = open("employee.csv", newline = "")
reader = csv.reader(csvfile,delimiter=",")


for row in reader:
  worker.add_employee(ProductionWorker(row[0], row[1], row[2], row[3], row[4]))

worker.print_report()
