# README

Project by: Sahrina Bhuiyan, Fnu Palak, Hope Dunner, Nicholas Comer
Contact us at: sahrina.bhuiyan12@gmail.com

Downloads required: 
We used Visual Studio Code for our project

Install python first, from official site
_________________________

Run these on CMD after installing python:

pip install Django==3.1.4

pip install Pillow

pip install pytz

pip install sqlparse

___________________________
Once everything is set, open the project and write the commands:

cd restorabd

python3 manage.py migrate

python3 manage.py createsuperuser

Here you have to create a username, enter an email address, and a password

If you want to bypass creating an account you are given [y/n] option so choose y

python3 manage.py runserver

Here you are given the website so open the website and you can login and place your orders as the customer

The given website + \admin will take you to the admin page where you can login as the admin and control the restaurant. You are able to add/delete menu, staff, reviews and everything else there. 

# Specs
An online restaurant order and delivery system was developed so that the restaurant provided menus of food, customers browsed and ordered food from the menu, and delivery people of the restaurant delivered the food.

There are three groups of users:
1. Restaurant:
  a) At least two chefs who independently decide the menus.
  b) At least two delivery people who compete for food delivery.
  c) The manager/superuser who processes customer registrations, handles customer compliments and complaints, hire/fire/raise or cut pay for the chef(s) and delivery people.
2. Customers:
  a) Registered customers who can browse/search, order and vote (lowest 1 star to highest 5 stars) food delivered (on food and delivery quality/manners individually); can start/participate a discussion topic on cooks/dishes/delivery people.
  b) VIP customers who spent more than $500 or placed 50 orders as registered customers, whichever comes first, in addition to the actions of registered customers, will receive 10% discount off their ordinary orders, have access to specially developed dishes, and their complaints/compliments are weighted twice as heavily as ordinary ones.
3. Surfers: Who can browse the menus and ratings only, can apply to be the registered customers with fixed amount of deposit money and are checked by the manager.

# How to use
This program runs on the Python Django framework. Therefore, to run it you must have django installed and execute the command "python restorabd/manage.py runserver", among any other steps necessary to run a Django program such as creating a superuser.

# System Features
1. Provide a GUI, not necessarily web-based, with pictures to show the components and descriptions of each dish and price; each registered customer/VIP has a password to login. When they log in, based on the history of their prior choices, different registered customer/VIP will have different top 3 listing dishes. For new customers or surfers, the top 3 most popular (ordered most) dishes and top 3 highest rated dishes are listed on the page.
2. The chef whose dishes received consistently low ratings or 3 complaints, or no order at all for 3 days, will be demoted (less salary), a chef demoted twice is fired. Conversely, a dish whose dishes received high ratings or 3 compliments, will be promoted (higher salary). One compliment can be used to cancel one complaint. The delivery people are handled the same way.
3. A customer can choose to 1) eat the food in the restaurant, 2) pick up the dishes by self or 3) by delivery. For 1) s/he needs to fix the available time and seating in the restaurant; for case 1) and 2) s/he can only give feedback about the chef.
4. Customers can file complaints/compliments to the chef of the food s/he purchased and delivery people who delivered the dish or other customers who didn't behave in the discussion formums. Delivery person can complain/compliment customers s/he delivered to, all are handled by the manager. The complained person has the right to dispute the complaint, the manager makes the final call to dismiss the complaint or convert it to one formal warning and inform the impacted parties. Customers/delivery people whose complaints are decided without merit will receive one warning.
5. Registered customers having 3 warnings are de-registered. VIPs having 2 warnings are put back to registered customers (with warnings cleared). The warnings should be displayed in the personalized page when the customers log in.
6. If the price of the order is more expensive than the deposited money in the account, the order is frozen until the customer puts more money into the account.
7. Customers who are kicked out of the system or choose to quit the system will be handled by the manager: clear the deposit and close the account.
8. The chef is the one who puts in the description and keywords for people to search and browse. The average ratings for each food/dish by customers are available for all.
9. The manager keeps a taboo list of words, any customer who uses those taboo words will receive one warning automatically and the words are replaced by ***, a message with more than 3 taboo words are blocked automatically.
10. A notification system that informs users of the status of their orders.

# Screenshots
![Alt text](/ss/home1.png?raw=true)
![Alt text](/ss/home2.png?raw=true)
![Alt text](/ss/my-cart.png?raw=true)
![Alt text](/ss/order-confirm.png?raw=true)
![Alt text](/ss/restaurant-foods.png?raw=true)
![Alt text](/ss/restaurant-reviews.png?raw=true)
![Alt text](/ss/restaurant-list.png?raw=true)
