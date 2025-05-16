menu={
    "Latte":{
        "ingredients":{
    "water":200,
    "milk":150,
    "coffee":24,
        },
    "cost":150
    },
"espresso":{
        "ingredients":{
    "water":500,
        "coffee":100,
        },
    "cost":100
},
"espressos":{
        "ingredients":{
    "water":500,
        "coffee":100,
        },
    "cost":100

}
}
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100
}

is_on=True
while is_on:
    choice=input("what would you like to have?(latte/espresso/cappuccino:)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}ml")
        print(f"Money=Rs{profit}")
    else:










