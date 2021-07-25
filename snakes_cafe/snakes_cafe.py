flag=True
orderList=[]
counter=1
while flag:
    
    
    userOrder=input("""$ python snakes_cafe.py
    
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    """)
    if userOrder=="quit":
        flag=False
    elif userOrder in orderList:
        counter=counter+1    
        orderList.append(userOrder)
        print("**" +  str(counter) + " order of "+userOrder+" have been added to your meal **")
    else:
        orderList.append(userOrder)
        print("**" +  str(counter) + " order of "+userOrder+" have been added to your meal **")

