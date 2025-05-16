menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'coffee':80,
}
print("welcome to python Restaurant")
print("1.Pizza: Rs 40")
print("2.Pasta: Rs 50")
print("3.Salad: Rs 70")
print("4.Coffee:Rs 80")
order_total=0
item_1=input("Enter the name of item you want to order(1-4):")

if item_1 in menu:
    order_total=order_total+menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item {item_1}is not avaliable yet")

another_order=input("Do you want to add another item?(Yes/No):")
if another_order=='yes':
    item_2=input("Enter the name of second item=")
    if item_2 in menu:
        order_total=order_total+menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not avaliable!")
print(f"the total amount of items is : {order_total}")









menu={
    "pizza":40,
    "pasta":50
}

print("welcome")
print("1.pizza:Rs 40")
print("2.pasta:Rs 50")
t=0
item1=input(" enter the name of the item:")
if item1 in menu:
    t+=menu[item1]
    print(f"your item is {item1} added to ur order")
else:
    print(f"your item is {item1}not avaliable")

another_item=input("do u  want  order (yes/no):")
if another_item=='yes':
    item2=input(f"enter the second item")
    t+=menu[item2]
    print(f"your ordered item added")
