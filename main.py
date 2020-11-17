!pip install pandas
import pandas as pd #Database Framework

#Database initialization. Currently tailored to perform feature 1 from spec sheet.
Food = pd.DataFrame({ #Food table initialized with pasta data
    'Food_ID':[0,1,2],
    'Name':['Pasta','Pizza', 'Cheeseburger'],
    'Description':["It's pasta.",'Actually just pizza.', "Almost as cheesy as my jokes."],
    'Price':[19.99, 19.99, 14.99], # I have no idea how food is priced normally. Someone can fix this but it doesn't really matter.
    'Chef_ID':[0,0,1], #Foreign key that tells which chef this food is from.
    'Picture':['images/pasta.jpg','images/pizza.jpg','images/cheeseburger.jpg'], #These are file names of pictures saved on the git.
    'Times_Ordered':[10,10,10],
    'Rating':[7,7,7], # This is a sum of customer feedback. +1 per compliment, -1 per complaint.
    'Tag':['Italian', 'Italian', 'Burger']}) #Tag to implement different listings shown for customers. Display based on similar tags of past ordered food.

Customer = pd.DataFrame({
    'Username':['A','B'],
    'Password':['password','alsoPassword']})

Order = pd.DataFrame({
    'Customer_ID':[0],
    'Food_ID':[0]})

Chef = pd.DataFrame({
    'Chef_ID':[0,1]})

Food #Prints the customer table. You can delete or comment this out if you want, it's just so you can see how the examples work.

# Front-end outline for feature 1:
# Feature 1 is to provide a GUI that shows pictures, descriptions, and the price of food. There needs to be a log-in functionality using the customer username and password.
# If a customer is logged in, they should see three food items based on their order history. New customers and people that aren't logged in see the top three most ordered and top three highest rated dishes.
#
# To select a row and column, use the function .loc[<Condition>][<Column name>]
# So for example:
#
# Food.loc[Food['Tag'] == 'Italian']
#
# Will return all rows with the Italian tag. You can check by uncommenting that line of code and running it. Furthermore:
#
# Food.loc[Food['Tag'] == 'Italian']['Name']
#
# Will return only the name column. That's a string you can just display. Or you can use the Picture column to link to the appropriate file to display.
#
# To show the top three most ordered or highest rated do .nlargest(3, <column name>). So:
#
# Food.nlargest(3,'Times_Ordered')
#
# Will give the top 3 ordered food.
#
# Logging in would be defining a Python function that takes a username and password as parameters (inputs from the user) and doing:
#
# Customer.loc[Customer['Username' == usernameParam] & Customer['Password' == passwordParam]]
#
# If that returns a value, change some status variable to show that the user is logged in. Else do nothing.
#
# To find the most common tags from a customers history, join the orders and food table with something like:
#
# FoodHistory = Order.join(Food.set_index('Food_ID'))
#
# Then narrow it down to a specific customer (customer with ID 0 in this example, but use a parameter otherwise) with:
#
# CustomerFoodHistory = FoodHistory.loc[FoodHistory['Customer_ID'] == 0]
#
# Finally, isolate the tag.
#
# MostPopularTag = CustomerFoodHistory['Tag'].value_counts().idxmax()
#
# Now you can use this MostPopularTag variable to .loc the proper food to display.
#
# If you need more help with accessing the database you can ask me, but all I'm doing is basically Googling "pandas how to x"
# -Nicholas