## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": "300", "budgetMax": "700"}
    - slot{"budgetMin": "300"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMax": "700"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* deny
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": "300", "budgetMax": "700"}
    - slot{"budgetMin": "300"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* deny
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - check_operating_cities
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": "300", "budgetMax": "700"}
    - slot{"budgetMin": "300"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": "300"}
    - slot{"budgetMin": "300"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMax": "300"}
    - slot{"budgetMax": "300"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": "700"}
    - slot{"budgetMin": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMin": "700"}
    - slot{"budgetMin": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMin": "300", "budgetMax": "700"}
    - slot{"budgetMin": "300"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMin": "300", "budgetMax": "700"}
    - slot{"budgetMin": "300"}
    - slot{"budgetMax": "700"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
* affirm
    - utter_goodbye

## custom_story 1
* restaurant_search{"cuisine": "chinese", "location": "rome"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "rome"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMax": "300"}
    - slot{"budgetMax": "300"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    
## custom_story 2 
* restaurant_search{"people": "4", "cuisine": "chinese", "location": "tokyo"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "tokyo"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMax": "300"}
    - slot{"budgetMax": "300"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* deny
    - utter_goodbye

## custom_story 3
* restaurant_search{"people": "4", "cuisine": "chinese", "location": "tokyo"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "tokyo"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMax": "300"}
    - slot{"budgetMax": "300"}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail

* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_ask_budget"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - followup{"name": "utter_mail_sent"}
    - utter_mail_sent

* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_goodbye"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye

* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_goodbye"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye

* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_goodbye"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye

* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 300, "budgetMax": 700}
    - slot{"budgetMin": 300}
    - slot{"budgetMax": 700}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_goodbye"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye

* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 0, "budgetMax": 300}
    - slot{"budgetMin": 0}
    - slot{"budgetMax": 300}
    - check_budget
    - action_search_restaurants
    - followup{"name": "utter_goodbye"}
    - slot{"cuisine": null}
    - slot{"location": null}
    - slot{"budgetMin": null}
    - slot{"budgetMax": null}
    - utter_goodbye

* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 700, "budgetMax": 10000}
    - slot{"budgetMin": 700}
    - slot{"budgetMax": 10000}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - followup{"name": "utter_mail_sent"}
    - utter_mail_sent

* restaurant_search

* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 700, "budgetMax": 10000}
    - slot{"budgetMin": 700}
    - slot{"budgetMax": 10000}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - followup{"name": "utter_mail_sent"}
    - utter_mail_sent

* restaurant_search{"cuisine": "chinese", "location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - check_operating_cities
    - utter_ask_budget
* restaurant_search{"budgetMin": 700, "budgetMax": 10000}
    - slot{"budgetMin": 700}
    - slot{"budgetMax": 10000}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@abc.com"}
    - slot{"mail_id": "abc@abc.com"}
    - action_send_mail
    - followup{"name": "utter_mail_sent"}
    - utter_mail_sent

* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_operating_cities
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budgetMin": 700, "budgetMax": 10000}
    - slot{"budgetMin": 700}
    - slot{"budgetMax": 10000}
    - check_budget
    - action_search_restaurants
    - utter_confirm_sendmail
* affirm{"affirm": "y"}
    - utter_ask_mail_id
* restaurant_search{"mail_id": "abc@domain.com"}
    - slot{"mail_id": "abc@domain.com"}
    - action_send_mail
    - followup{"name": "utter_mail_sent"}
    - utter_mail_sent
