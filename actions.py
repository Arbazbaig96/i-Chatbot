# Importing libraries
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import pandas as pd
import json
import smtplib, ssl
import email.message
from rasa_sdk.events import FollowupAction
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mailaddress = 'arbazanandgithub@gmail.com'
mailpassword = '8123587702'

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['Delhi', 'Gurugram', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

def RestaurantSearch(City,Cuisine):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating','Currency']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budgetMax = int(tracker.get_slot('budgetMax'))
		budgetMin = int(tracker.get_slot('budgetMin'))
		results = RestaurantSearch(City=loc,Cuisine=cuisine)
		response="Showing you top rated restaurants: \n\n"
		restaurantList = []
		mailList = []
		if results.shape[0] == 0:
			response= "No restaurant found with your search criteria"
		else:
			for restaurant in results.iterrows():
				restaurant = restaurant[1]
				if len(restaurantList)>=1:
					break
				if int(restaurant['Average Cost for two'])>budgetMin and int(restaurant['Average Cost for two'])<budgetMax:
					restaurantList.append(F"{restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} \n\n")
					mailList.append(F"{restaurant['Restaurant Name']} in {restaurant['Address']} has been rated {restaurant['Aggregate rating']} with average budget for two people {restaurant['Average Cost for two']}₹\n\n")
		if len(restaurantList)>0:
			for index,value in enumerate(restaurantList):
				response = response + str(index+1) + ". " + value
			dispatcher.utter_message(response)
			return [SlotSet('restaurantList',mailList)]
		else:
			dispatcher.utter_message('Could not find restaurants with your search criteria. Please try again')
			return[FollowupAction("utter_goodbye"), SlotSet('cuisine', None), SlotSet('location', None), SlotSet('budgetMin', None), SlotSet('budgetMax', None)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		mail_address = tracker.get_slot('mail_id')
		msg = tracker.get_slot('restaurantList')
		self.sendmail(mail_address, msg)
		return [FollowupAction("utter_mail_sent")]
	
	def sendmail(self, mail_address, msg):
		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			response="Showing you top rated restaurants: <br/><br/>"
			if len(msg)>0:
				for index,value in enumerate(msg):
					response = response + str(index+1) + ". " + value + "<br/>"
			email_text = MIMEMultipart()
			email_text['From']=mailaddress
			email_text['To']=mail_address
			email_text['subject']='Restaurant List'
			email_text.attach(MIMEText(response, 'html'))
			server.login(mailaddress, mailpassword)
			server.sendmail(mailaddress, mail_address, email_text.as_string())
			server.quit()
		except:
			print("Something went wrong")
		return

class checkOperatingCities(Action):
	def name(self):
		return 'check_operating_cities'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		if location:
			if location.upper() not in map(str.upper, WeOperate):
				return[FollowupAction("utter_ask_location_again")]
			else:
				return

class checkBudget(Action):
	def name(self):
		return 'check_budget'

	def run(self, dispatcher, tracker, domain):
		budgetMin = None
		budgetMax = None
		try:
			print(tracker.get_slot('budgetMin'))
			print(tracker.get_slot('budgetMax'))
			budgetMin = int(tracker.get_slot('budgetMin'))
			budgetMax = int(tracker.get_slot('budgetMax'))
		except ValueError:
			dispatcher.utter_message('Invalid budget selected. Please enter again')
			return[FollowupAction("utter_ask_budget"), SlotSet('budgetMin', None), SlotSet('budgetMax', None)] 

		if budgetMin in [0,300,700] and (budgetMax in [300,700] or budgetMax>700):
			return
		else:
			dispatcher.utter_message('Invalid budget selected. Please enter again')
			return[FollowupAction("utter_ask_budget"), SlotSet('budgetMin', None), SlotSet('budgetMax', None)]
		
