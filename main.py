!pip install pandas
import pandas as pd #Database Framework
import numpy as np

#Database initialization. Currently tailored to perform feature 1 from spec sheet.
Food = pd.DataFrame({ #Food table initialized with pasta data
    'Food_ID':[0,1,2],
    'Name':['Pasta','Pizza', 'Cheeseburger'],
    'Description':["It's pasta.",'Actually just pizza.', "Almost as cheesy as my jokes."],
    'Price':[19.99, 19.99, 14.99], # I have no idea how food is priced normally. Someone can fix this but it doesn't really matter.
    'Chef_ID':[0,0,1], #Foreign key that tells which chef this food is from.
    'Picture':['images/pasta.png','images/pizza.png','images/cheeseburger.png'], #These are file names of pictures saved on the git.
    'Times_Ordered':[10,10,10],
    'Rating':[7,7,7], # This is a sum of customer feedback. +1 per compliment, -1 per complaint.
    'Tag':['Italian', 'Italian', 'Burger']}) #Tag to implement different listings shown for customers. Display based on similar tags of past ordered food.

Customer = pd.DataFrame({
    'Username':['A','B'],
    'Password':['password','alsoPassword'],
    'Warnings':[0,2],
    'Deposit':[100,10], #Amount of money a customer has
    'VIP_Status':[0,1] # 0 = NOT a VIP. 1 = Is a VIP
    })

Order = pd.DataFrame({
    'Customer_ID':[0],
    'Delivery_Person_ID': [0],
    'Method': [2], # 0 = In restaurant, 1 = By self, 2 = by delivery
    'Food_ID':[0]})

Restaurant_Times = pd.DataFrame({
    'Times':['9:30 AM', '10:30 AM', '12:30 PM']
    'Status':[0,0,1] # 0 = Unavailable, 1 = available.
})

Chef = pd.DataFrame({
    'Salary':[200,300],
    'Demotion_Count':[0,1], #Times demoted.
    'Chef_ID':[0,1]})

Delivery_Person = pd.DataFrame({
    'Salary':[200,300],
    'Demotion_Count':[0,1], #Times demoted.
    'Delivery_person_ID':[0,1]})

Manager = pd.DataFrame({
    'Username':['admin'],
    'Password':['admin']
})

Feedback = pd.dataframe({
    'Chef_ID':[np.nan],
    'Delivery_Person_ID':[0],
    'Food_ID': [1],
    'Description': ["Good enough."], # This is scanned for taboo words before being entered.
    'Content':[1] # Defines whether the feedback was positive or negative. 0 = Negative/complaint. 1 = Positive/compliment
})



#Food #Prints the customer table. You can delete or comment this out if you want, it's just so you can see how the examples work.

# Front-end tips for feature 1 and how to query the database:
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


# Front-end tips for feature 2 (demotion and promotion feature):
# First create way to add feedback to feedback table. Feedback for food increases or decreases the rating by 1, depending on the content. Add feedback 
# when an order is made. Use the food, chef, and delivery_person (if there is one) as parameters for the feedback function.
#
# Create function to check for demotion with parameters for chef_id or delivery_person_id:
# (Amount of feedback for employee with content == 1) - (Amount of feedback for employee with content == 0) = VAR
# If VAR < -3 OR (there are at least three food belonging to that chef with rating < 4) then lower salary and increase demotion count by 1. If demotion count becomes 2 then remove from database.
# If VAR > 3 OR (there are at least three food belonging to that chef with rating > 6) then increase salary.
# if the feedback is for a chef, include the feedback for food belonging to that chef. This means linking to the food table.
# 
# Run the demotion/promotion check function every time new feedback is made.

# Front-end tips for feature 3:
# If option 1, use the Restaurant_Time table.

# Front-end tips for feature 4 & 5:
# Check the feedback table for content = 0 (negative feedback), and let the manager click a button that runs a function that
# deletes the feedback, increases the warning count for the feedback creator, and checks if the warning amount is large enough to de-register/demote a user from VIP.

#Front-end tips for feature 6:
# Check customer table for deposit. Compare against the order price.

#Front-end tips for feature 7:
# Just a button to delete a row from the customer database.

# Front-end tips for feature 8:
# Allow chefs to add food to the database. Search based on tags from the food table.

# Front-end tips for feature 9:
# Only need the back-end to update the warning count in the customer table. The rest is searching the string for the taboo words, keeping a counter for each one found.
# If the number is >= 1, then increase the warning count. If it's >= 3, block the message entirely.