#function to 

import random
import requests
value = random.randint(1, 10)

all_cards =[[]]
card_map = []
temp = []
##make map
for num in range(1,53):
    temp = [num,0]
    card_map.append(temp)

#print(card_map)


'''
import requests

url = 'https://api.pokerapi.dev/v1/winner/texas_holdem?cc=AC,KD,QH,JS,7C&pc[]=10S,8C&pc[]=3S,2C&pc[]=QS,JH'

response = requests.get(url = url)
data = response.json()
print(data)
'''
#def check_if_exists:



def who_won(cc,player_cards):
    
    url = 'https://api.pokerapi.dev/v1/winner/texas_holdem?'
    url = url + cc
    
    #cc=AC,KD,QH,JS,7C&pc[]=10S,8C&pc[]=3S,2C&pc[]=QS,JH
    





def pass_cards(numppl):

	for passcard_int in num
    





