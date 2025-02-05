from abc import ABC, abstractmethod
from typing import final
from enum import Enum

class Workable(ABC):

    @abstractmethod
    def work(self) -> str:
        pass

class RolesOfEmployee(Enum):
    associate_engineer: int = 1
    interns: int = 2
    hr_associate: int = 3
    senior_developer: int = 4
    team_leads: int = 5
    project_manager: int = 6



class Employee(ABC):
    MINIMUM_WORKING_HOURS: final = 8.5

    def __init__(self, name: str, id: int, age: int, salary: float, role: RolesOfEmployee):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary
        self.role = role

    @abstractmethod
    def showDetails(self) -> None:
        pass

    
    def workingHours(self) -> None:
        print(F'{Employee.MINIMUM_WORKING_HOURS}') 
    
    @abstractmethod
    def showSalary(self):
        pass

class Interns(Employee,Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 6000
    
    def work(self):
        return 'your work is learning and assisting to senior developer..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}, Role: {self.role}')

class AssociateEngineer(Employee, Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 60000
    
    def work(self):
        return 'your work is to develop and build the solutions for the bussiness or clients..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')

class HrAssociate(Employee, Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 45000
    
    def work(self):
        return 'your work is to manage employee relations and do recuritment..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')

    
class SeniorDeveloper(Employee, Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 80000
    
    def work(self):
        return 'your work is to guide all the intern and develop the bussiness solutions..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')

class Teamlead(Employee, Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 100000
    
    def work(self):
        return 'your work is to manage and lead the team..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')

class ProjectManager(Employee, Workable):
    def __init__(self, name, id, age, salary, role):
        super().__init__(name, id, age, salary, role)

    def showSalary(self):
        return 200000
    
    def work(self):
        return 'your work is to deal with all the clients..'
    
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}, Age: {self.age}')


def main() -> None:
    harsh = Interns("Harsh Dadiya", 168, 21, 6000, RolesOfEmployee.interns)
    harsh.showDetails()
    print(f"Salary: {harsh.showSalary()}")
    print(harsh.work())
    print()


    hitesh = AssociateEngineer("Hitesh Kumar", 100, 25, 60000,RolesOfEmployee.associate_engineer)
    hitesh.showDetails()
    print(f"Salary: {hitesh.showSalary()}")
    print(hitesh.work())
    print()

    dhruv = AssociateEngineer("Dhruv Bhavsar", 101, 25, 60000, RolesOfEmployee.associate_engineer)
    dhruv.showDetails()
    print(f"Salary: {dhruv.showSalary()}")
    print(dhruv.work())
    print()

    dhruvansh = AssociateEngineer("Dhruvansh", 105, 25, 60000, RolesOfEmployee.associate_engineer)
    dhruvansh.showDetails()
    print(f"Salary: {dhruvansh.showSalary()}")
    print(dhruvansh.work())
    print()

    arbas = AssociateEngineer("Arbas", 106, 25, 60000, RolesOfEmployee.associate_engineer)
    arbas.showDetails()
    print(f"Salary: {arbas.showSalary()}")
    print(arbas.work())
    print()

    komal = HrAssociate("Komal Dangi", 102, 27, 45000, RolesOfEmployee.hr_associate)
    komal.showDetails()
    print(f"Salary: {komal.showSalary()}")
    print(komal.work())
    print()

    jaldip = Teamlead("Jaldip Patel", 100, 35, 100000, RolesOfEmployee.team_leads)
    jaldip.showDetails()
    print(f"Salary:{jaldip.showSalary()}")
    print(jaldip.work())


if __name__ == '__main__':

    main()




    






    

    