
from prettytable import PrettyTable

machine_resources={
    'water':300,
    'coffe_powder':100,
    'milk':200

}

class Menu:
    def __init__(self,item: str,cost: int,ingredients):
        self.item=item
        self.cost=cost
        self.ingredients=ingredients

    def print_report(self,machine_resources):
        print("remaining resources of machine")
        x=PrettyTable()
        x.add_column("water",[machine_resources['water']])
        x.add_column("milk",[machine_resources['milk']])
        x.add_column("coffe powder",[machine_resources['coffe_powder']])
        x.align="l"
        print(x)
    def order_a_coffe(self):
        global available,is_cash_minimum

        #set varibles as false for further use
        is_cash_minimum=False
        available=False


        if machine_resources['water'] >= self.ingredients['water'] and machine_resources['coffe_powder'] >= self.ingredients['water'] and machine_resources['milk'] >= self.ingredients['milk'] :
            available=True

        if available == True:
            cash = int(input(f"enter cost of {self.item}: {self.cost}rs: "))
            if cash < self.cost:
                print(f"you dont have enough money: cost is {self.cost} rs and you have: {cash} rs")
                print(" ")
                #if you have cash minimum then it will true se varible which will we use to continue to progrem
                is_cash_minimum=True

            if cash >= self.cost:
                print(f"Here is Your{'☕'} {self.item} sir ")
                machine_resources['water'] = machine_resources['water'] - self.ingredients['water']
                machine_resources['coffe_powder'] -= self.ingredients['coffe_powder']
                machine_resources['milk'] -= self.ingredients['milk']
                if cash > self.cost:
                    print(f"Take your change: {cash - self.cost} rs")

        if available == False:
            print(f"Ingredients are'nt Enough in Machine to Make: {self.item}")
            self.print_report(machine_resources)
            print(f"You can't order For now ")




def program():

    while True:
        global is_cash_minimum

        a = Menu("Expresso", 50, {"water": 50, "coffe_powder": 18, "milk": 0, })
        b = Menu("Latte", 100, {"water": 200, "coffe_powder": 24, "milk": 150})
        c = Menu("Cappaciuno", 150, {"water": 250, "coffe_powder": 24, "milk": 150})

        choice=int(input("what would you like ent number: (1:expresso, 2:latte, 3:cappuccino, 4:report, 5:quit ) :  "  ))

        if choice == 1:
            a.order_a_coffe()
            if is_cash_minimum==True:
                continue

        if choice==2:
            b.order_a_coffe()
            if is_cash_minimum==True:
                continue

        if choice==3:
            c.order_a_coffe()
            if is_cash_minimum==True:
                continue


        if choice==4:
            # we can take any class for printing report other than b it will no harm program
            b.print_report(machine_resources)
            continue

        if choice==5:
            print("Thanks for using Our Software")
            break

program()
