## intent:affirm
- yes
- yep
- yeah
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- please
- thank you
- yes. Please
- [y](affirm)

## intent:deny
- Nope
- Not required
- Nope
- False
- no
- nah

## intent:goodbye
- bye
- goodbye
- good bye
- stop 
- end
- farewell
- Bye bye
- have a good day

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- [chinese](cuisine) restaurant in [300](budgetMin)-[700]{"entity": "budgetMax", "value": "Rs. 300 to 700"} range in [delhi](location) in [rome](location)
- [300](budgetMin)-[700]{"entity": "budgetMax", "value": "Rs. 300 to 700"} range [chinese](cuisine) restaurant
- [<300]{"entity": "budgetMax", "value": "300"}
- [>700]{"entity": "budgetMin", "value": "700"}
- [300](budgetMin)-[700]{"entity": "budgetMax", "value": "Rs. 300 to 700"} range
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me a [chinese](cuisine) restaurant in [rome](location)
- find me a restaurant in [chinese](cuisine) restaurant in [tokyo](location)
- can you please find me a [italian](cuisine) restaurant in [mumbai](location)
- more than [700] {"entity": "budgetMax", "value": "700"}
- Rs. [300](budgetMin) to [700](budgetMax)
- Lesser than Rs. [300](budgetMax)
- [Gurgaon](location)
- [chinese](cuisine) restaurant in [tokyo](location)
- find me [chinese](cuisine) food priced below [200](budgetMax)
- find me food priced between [200](budgetMin) and [400](budgetMax)
- [Noida](location)
- [chinese](cuisine) restaurant in [noida](location)
- yes. Please send it to [ahbcdj@dkj.com](mail_id)
- [asdasdas@gmail.com](mail_id)
- find me restaurant in [bengaluru]{"entity": "location", "value": "bangalore"}
- find me a [italian](cuisine) restaurant in [noida](location)
- [Bangalore](location)
- I’m hungry. Looking out for some good restaurants
- [Bengaluru]{"entity": "location", "value": "bangalore"}
- [bengaluru]{"entity": "location", "value": "bangalore"}
- find restaurant in [Noida](location)
- find [chinese](cuisine) restaurant in [bangalore](location)
- [sestajespo@biyac.com](mail_id)
- restaurant in [bengaluru]{"entity": "location", "value": "bangalore"}
- /restaurant_search{"budgetMin":300,"budgetMax":700}
- [anything@gmail.com](mail_id)
- [test@upgrad.com](mail_id)
- find restaurant in madhupur
- find restaurant in [mysuru](location)
- [mysore](location)
- [shubhamverma.friends@gmail.com](mail_id)
- find restaurant in [mumbai](location)
- find [italian](cuisine) restaurant in [mumbai](location)
- find restaurant in [bombay]{"entity": "location", "value": "mumbai"}
- find restaurant in [chennai](location)
- find restaurant in [kolkata](location)
- find restaurant in calcuttra
- find restaurant in [calcutta]{"entity": "location", "value": "Kolkata"}
- [yirkahordu@biyac.com](mail_id)
- find [chinese](cuisine) restaurant in [calcutta]{"entity": "location", "value": "Kolkata"}
- find restaurant in [madras]{"entity": "location", "value": "chennai"}
- Find restaurant in [madras]{"entity": "location", "value": "chennai"}
- find restaurant in [Mysuru](location)

## synonym:300
- <300

## synonym:700
- >700

## synonym:Coimbatore
- Koyampuththur

## synonym:Dehradun
- Dehradunam

## synonym:Delhi
- New Delhi

## synonym:Hyderabad
- Darul Jihad

## synonym:Indore
- Indrapura

## synonym:Jaipur
- Pink City

## synonym:Kanpur
- Kanpur Dehat

## synonym:Kochi
- Cochin

## synonym:Kolkata
- calcutta
- Calcutta

## synonym:Lucknow
- Lakhanavati
- Lakhnauti
- Lakhnau
- Laksmanauti
- Laksmnaut
- Lakhsnaut
- Lakhsnau

## synonym:Mangalore
- Mangaluru

## synonym:Nagpur
- Fanindrapura

## synonym:Nashik
- Nasik

## synonym:Puducherry
- Pondicherry

## synonym:Pune
- Poona

## synonym:Rs. 300 to 700
- 700

## synonym:Varanasi
- Banaras
- Kashi

## synonym:Vizag
- Visakhapatnam Vizag
- Visakhapatnam
- Vizagapatam
- Waltair
- Visakha

## synonym:agra
- Agravan

## synonym:ahmedabad
- Karnavati

## synonym:allahabad
- Prayagraj

## synonym:Gurugram
- Gurgaon

## synonym:amritsar
- Ramdaspur

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:bhopal
- Bhojpal

## synonym:chandigarh
- New Chandigarh

## synonym:chennai
- madras

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:mumbai
- bombay

## synonym:mysore
- mysuru
- Mahisūru

## synonym:patna
- patliputra

## synonym:varoda
- Badodra

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:location
- [^\s]*

## regex:mail_id
- ^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$

## regex:pincode
- [0-9]{6}
