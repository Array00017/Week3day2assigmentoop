#Exercise 1 - Class Inheritance
#Create an Employee class that sets an employee's first name, last name, job title, salary, and email. The Employee class should have a class attribute for the raise amount set to 5% (1.05). Create a method that will apply the raise to an employee's salary.

class employee:
    
    raiseamount = 1.05
    
    def __init__(self,firstname,lastname,jobtitle,salary,email):
        self.firstname = firstname 
        self.lastname = lastname 
        self.jobtitle = jobtitle 
        self.salary = salary 
        self.email = email
    
    
    def __salaryraise__(self,salary):
        if self.salary == salary
        print(f"New salary"{self.salary}*{raiseamount})
        
print [(employee{self.firstname} = "Michael" {self.lastname} = "Rayburn" {self.jobtitle} = "Doctor" {self.salary} = 200,000 {self.email} = "doctorrayburn@gmail.com")]
     