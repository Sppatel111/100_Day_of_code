data = {
    "coffee_ingredients": {
        "Espresso": {"milk": "0 ml", "water": "50 ml", "coffee": "18 gm", "price": "$1.50","cost":"$0.75"},
        "Latte": {"milk": "150 ml", "water": "200 ml", "coffee": "24 gm", "price": "$2.50","cost":"$1.5"},
        "Cappuccino": {"milk": "100 ml", "water": "250 ml", "coffee": "24 gm", "price": "$3.00","cost":"$1.75"}
    },
    "available_ingredients": {"milk": "2 liter", "water": "2.5 liter", "coffee": "0.5 kg"},
    "money": 0
}
profit=0
# resource conversion: resource1
resource = data["available_ingredients"]
r1 = []
for i in resource:
    r1.append(resource[i].split()[0])
r3 = [float(i) for i in r1 if i.replace('.', '').isdigit()]

r4 = []
for i in r3:
    r4.append(i * 1000)

res = ["milk", "water", "coffee"]

# available ingredients in ml,ml,gm
resource1 = {}
for i in range(3):
    resource1[res[i]] = r4[i]
# print(f'resources:{resource1}')

#for price conversion
def money_conversion(drink_money):
    mon=''
    for i in range(1,len(drink_money)):
        mon += drink_money[i]
    mon1=float(mon)

    return mon1

def cost_conversion(drink_cost):
    cos = ''
    for i in range(1, len(drink_cost)):
        cos += drink_cost[i]
    mon1 = float(cos)
    print(mon1)
    return mon1

# order conversion
def conversion(order_drink):
    str1 = []
    for i in order_drink:
        str1.append(order_drink[i].split()[0])
    int1 = [int(i) for i in str1 if i.isdigit()]
    res1 = ["milk", "water", "coffee"]
    drink1 = {}
    for i in range(3):
        drink1[res1[i]] = int1[i]
    return drink1



def is_sufficient(order_resource):
    for i in order_resource:
        if order_resource[i] > resource1[i]:
            print("not enough resources.")
            return False
    return True

def amount():
    x = int(input("insert money:"))
    return x


def transaction_resource(drink_money, given_money,drink_cost):
    global is_on,profit
    if given_money < drink_money:
        print(" sorry not enough amount of money is given. ")
        is_on=False
        return False
    else:
        change = given_money - drink_money
        if change != 0:
            print(f" here your change {change}$ !!!")

        data["money"] += drink_money
        p = drink_money - drink_cost
        profit += p
        return True


def make_coffee(drink_ingre,total_resource):
    for i in total_resource:
        total_resource[i] = total_resource[i] - drink_ingre[i]
    return True


nope=data["coffee_ingredients"]
print(f"here the coffee option: ")
for coffee,detail in nope.items():
    print(f"{coffee} : {detail['price']}")

is_on=True
while is_on:
    print(" Do you want to buy coffee ? ")
    order = input("order (Espresso/Latte/Cappuccino) / for ingredients report type 'Report' / for off the machine type 'Off':").title()

    if order == 'Report':
        print(f"milk:{resource1['milk']}ml \n water:{resource1['water']}ml \n coffee:{resource1['coffee']}gm, \nmoney:{data['money']}$ \nprofit:{profit}$")
    elif order == 'Off':
        is_on=False
    else:
        how_many = int(input("enter how many ordered coffee do you want:"))
        List1 = data["coffee_ingredients"]

        drink = List1[order]
        #for money
        price1=drink["price"]
        order1_money=money_conversion(price1)
        order1_money *= how_many

        #for cost-profit
        cost11=drink["cost"]
        order1_cost=cost_conversion(cost11)
        order1_cost *= how_many

        #order conversion
        order_res = conversion(drink)
        for i in order_res:
            x = order_res[i]
            order_res[i] = 0
            order_res[i] += x * how_many

        if is_sufficient(order_res):
            given_price=amount()
            if transaction_resource(order1_money,given_price,order1_cost):
                if make_coffee(order_res,resource1):
                    print(f" here your order {order}...")

