cofee_data={
    "expresso": {
        'water':50 ,                       #in ml
        'coffe_powder':18,                  #in gram
        'milk':0,
        'price':50
    },
    "latte": {
        'water': 200,
        'coffe_powder': 24,
        'milk':150,
        'price':100
    },
    "cappuccino": {
        'water': 250,
        'coffe_powder': 24,
        'milk': 100,
        'price':150
    }
}

machine_resources={
    'water':300,#ml
    'milk':200,#ml
    'coffe_powder':100#gram
}

def remaniningResources():
    print(f"Water: {machine_resources['water']}ml")
    print(f"Milk: {machine_resources['milk']}ml")
    print(f"coffe Powder: {machine_resources['coffe_powder']}g")



#4 for report of all resources
while True:
    choice=int(input("what would you like ent number: (1:expresso, 2:latte, 3:cappuccino, 4:report, 5:quit ) :  "  ))
    if choice == 4:
        remaniningResources()
    if choice == 5:
        print("Thanks for using our Software !.")
        break
    if choice == 1:
        if machine_resources['water'] <= 50:
            print(f"sorry there is not enough Water.")

        if machine_resources['coffe_powder'] <= 18:
            print(f"sorry there is not enough cofee powder.")

        if  machine_resources['water'] >=50 and machine_resources['coffe_powder'] >=18 and machine_resources['milk'] >=0:

            cash = int(input(f"enter cash:{cofee_data['expresso']['price']}rs: "))
            if cash < cofee_data['expresso']['price']:
                print(f"coffe price is : {cofee_data['expresso']['price']}rs enter valid amount.")
                continue
            machine_resources['water']=machine_resources['water']-cofee_data['expresso']['water']
            machine_resources['coffe_powder']=machine_resources['coffe_powder']-cofee_data['expresso']['coffe_powder']
            machine_resources['milk']=machine_resources['milk']-cofee_data['expresso']['milk']
            print(f"Here is Your{'☕'} Expresso sir ")

            if cash > cofee_data['expresso']['price']:
                print(f"Take your change: {cash-cofee_data['expresso']['price']}")



    if choice == 2:
        if machine_resources['water'] < 200:
            print(f"sorry there is not enough Water.")

        if machine_resources['coffe_powder'] < 24:
            print(f"sorry there is not enough coffe powder.")

        if machine_resources['milk'] < 150:
            print(f"sorry there is not enough Milk.")

        if  machine_resources['water'] >=200 and machine_resources['coffe_powder'] >=24  and machine_resources['milk'] >= 150:
            cash = int(input(f"enter cash:{cofee_data['latte']['price']}rs: "))
            if cash < cofee_data['latte']['price']:
                print(f"coffe price is : {cofee_data['latte']['price']}rs enter valid amount.")
                continue
            machine_resources['water'] = machine_resources['water'] - cofee_data['latte']['water']
            machine_resources['coffe_powder'] = machine_resources['coffe_powder'] - cofee_data['latte']['coffe_powder']
            machine_resources['milk'] = machine_resources['milk'] - cofee_data['latte']['milk']
            print(f"Here is Your{'☕'} Latte sir , Enjoy your Day. ")
            if cash > cofee_data['latte']['price']:
                print(f"Take your change: {cash - cofee_data['latte']['price']}")




    if choice == 3:
        if machine_resources['water'] < 250:
            print(f"sorry there is not enough Water.")

        if machine_resources['coffe_powder'] < 24:
            print(f"sorry there is not enough coffe powder.")

        if machine_resources['milk'] < 100:
            print(f"sorry there is not enough Milk.")

        if machine_resources['water'] >= 250 and machine_resources['coffe_powder'] >= 24 and machine_resources['milk'] >= 100:
            cash = int(input(f"enter cash:{cofee_data['cappuccino']['price']}rs: "))
            if cash < cofee_data['cappuccino']['price']:
                print(f"coffe price is : {cofee_data['cappuccino']['price']}rs enter valid amount.")
                continue
            machine_resources['water'] = machine_resources['water'] - cofee_data['cappuccino']['water']
            machine_resources['coffe_powder'] = machine_resources['coffe_powder'] - cofee_data['cappuccino']['coffe_powder']
            machine_resources['milk'] = machine_resources['milk'] - cofee_data['cappuccino']['milk']
            print(f"Here is Your{'☕'} Cappuccino sir , Enjoy your Day. ")
            if cash > cofee_data['cappuccino']['price']:
                print(f"Take your change: {cash - cofee_data['cappuccino']['price']}")





