print()
from datetime import datetime, date

class Person:
    
    """
    Docstring for Person
    
    A Person class meant to create details of people
    """
    
    def __init__(self, first_name: str, last_name: str, birth_date: str) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param first_name: Description
        :type first_name: str
        :param last_name: Description
        :type last_name: str
        :param birth_date: Description
        :type birth_date: int
        
        Initialize a Person instance.
        """
        
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
        
    def calculate_age(self) -> int:
        
        """
        Docstring for calculate_age
        
        :param self: Description
        :return: Description
        :rtype: int
        
        Calculate the person's current age.
        """
        
        today = date.today()
        age = today.year - self.birth_date.year
        
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        
        return age
    
    
    def show_info(self) -> None:
        
        """
        Docstring for show_info
        
        :param self: Description
        :return: Description
        :rtype: str
        
        Display formatted person information.
        """
        
        birth_date_str = self.birth_date.strftime("%A %d %B %Y")
        
        
        print(f"First Name: {self.first_name:^10} | Last Name: {self.last_name:^10} | Age: {self.calculate_age():^10} | Birth Date: {birth_date_str:^10}")
        

p1 = Person("Jimmy", "Devold", "07-01-2008") 
p2 = Person("Max", "Timmy", "03-12-2030")
p3 = Person("Jimmy", "Newtron", "11-04-1955")

person_list = [p1, p2, p3]

for person in person_list:
    person.show_info()

