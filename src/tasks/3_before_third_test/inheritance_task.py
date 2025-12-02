print()
class Ticket:
    """
    Represents a standard ticket with a base price and an MVA fee.
    Provides functionality to calculate and display the final ticket price.
    """
    
    def __init__(self, price: float):
        """
        Initialize a Ticket instance.

        Parameters:
            price (float): The base price of the ticket.

        Sets:
            self.price: The base ticket price.
            self.mva: The MVA tax rate applied to the ticket.
        """
        self.mva = 0.12
        self.price = price

    def calculate_price(self):
        """
        Calculate the final ticket price including MVA fees.

        Returns:
            float: The base ticket price plus the MVA fee.
        """
        return self.price + (self.price * self.mva)

    def show_info(self):
        """
        Print the final calculated price of the ticket.
        """
        print(f"Ticket price: {self.calculate_price()} kr")


class Kids_Ticket(Ticket):
    """
    A ticket type for children. Inherits from Ticket and applies a discount before fees.
    """
    
    def __init__(self, price):
        """
        Initialize a Kids_Ticket instance.

        Parameters:
            price (float): The base price before discount.

        Sets:
            self.discount_rate: Discount applied to children's tickets.
        """
        super().__init__(price)
        self.discount_rate = 0.5

    def calculate_price(self):
        """
        Calculate the final ticket price for a child, 
        applying the child discount and MVA fee.

        Returns:
            float: Discounted price including MVA.
        """
        discounted_price = self.price * self.discount_rate
        return discounted_price + (discounted_price * self.mva)


class Conscripts_Ticket(Ticket):
    """
    A ticket type for conscripts (military service). 
    Applies a specific discount before calculating MVA.
    """
    
    def __init__(self, price):
        """
        Initialize a Conscripts_Ticket instance.

        Parameters:
            price (float): The base price before discount.

        Sets:
            self.discount_rate: Discount applied to conscript tickets.
        """
        super().__init__(price)
        self.discount_rate = 0.9
    
    def calculate_price(self):
        """
        Calculate the final ticket price for a conscript,
        applying the conscript discount and MVA fee.

        Returns:
            float: The final rounded ticket price.
        """
        discounted_price = self.price * self.discount_rate
        return round(discounted_price + (discounted_price * self.mva), 2)


class Week_Ticket(Ticket):
    """
    Represents a weekly ticket calculated from a daily price.
    Applies a weekly rate and MVA fees.
    """
    
    def __init__(self, price):
        """
        Initialize a Week_Ticket instance.

        Parameters:
            price (float): The daily price before weekly calculation.
        """
        super().__init__(price)
        
    def calculate_price(self):
        """
        Calculate the total weekly ticket price, 
        using 20% of the 7-day total price and adding MVA.

        Returns:
            float: The final rounded weekly ticket price.
        """
        week_price = (self.price * 7) * 0.2
        return round(week_price + (week_price * self.mva), 2)

Ticket(450).show_info()
Kids_Ticket(450).show_info()
Conscripts_Ticket(450).show_info()
Week_Ticket(450).show_info()

