class Parking_Garage(): 

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets # list
        self.parkingSpaces = parkingSpaces # list
        self.currentTicket = {'Paid': False} # dictionary

    def take_ticket(self):
        num_tickets = list(range(1,21))
        self.tickets = num_tickets
        num_tickets = num_tickets[:-1]
        self.tickets = num_tickets
        print(f'There are {self.tickets[-1]} tickets left.')


    # Decrease the amount of tickets available by 1
    # Decrease the amount of parking spots available by 1
        
    def pay_for_parking(self):     
        # Displays an input that waits for  an amount from the user and store it in a variable
        payment = float(input("Please pay $10.00 for your parking ticket: "))

        # If the payment variable is not empty then (meaning the ticket has been paid) -> 
        # display a message to the user that their ticket has been paid and they have 15mins to leave
        while True:
            if payment == 10.00:
                print('Your ticket has been paid. You have 15 minutes to exit the garage.')
                this_ticket = self.currentTicket
                # Update the 'currentTicket' dictionary key 'paid' to True
                this_ticket['Paid'] == True
                self.currentTicket = this_ticket
                break
            # Need an else statement that will start this loop from beginning if payment does not equal 10.00
                
                
    def leave_garage(self):
    # If ticket has been paid, display 'Thank you, have a nice day'
        if self.currentTicket['Paid']==True:
            print('Thank you, have a nice day')
        else:
            self.pay_for_parking()
    # If ticket hasn't been paid, display an input prompt for payment
    # Once paid display, 'Thank you, have a nice day'
    # Update parkingSpaces list to increase by 1
        self.tickets.append(self.tickets[-1]+1)
    # Update tickets list to increase by 1
        self.parkingSpaces.append(self.parkingSpaces[-1]+1)


num_tickets = []
num_spots = []
var = Parking_Garage(num_tickets, num_spots, False)
var.take_ticket()