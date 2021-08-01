menu_list=[
    'wings', 'cookies', 'spring rolls', 
    'salmon', 'steak', 'meat tornado', 
    'a literal garden', 'ice Cream', 
    'cake', 'pie', 'coffee', 'tea', 
    'unicorn tears'
]

order_list=[]



list_checker=[]
print(
    """
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
    """
)

def snakes_cafe():
    user_order=input('  -->    ')
   
    user_order = user_order.capitalize()
    if user_order.lower() in menu_list:
        order_list.append(user_order)
       
        if user_order not in list_checker:
            list_checker.append(user_order)
        print(f'** {order_list.count(user_order)} order of {user_order} have been added to your meal **')
        snakes_cafe()
    elif user_order.lower()=='quit' or user_order.lower()=='q' or user_order.lower()=='exit':
        
        for i in list_checker:
            print(f'{order_list.count(i)} order of {i} ')
    elif user_order.lower() not in menu_list:
        print('** Your order is not in the menu **')



snakes_cafe()