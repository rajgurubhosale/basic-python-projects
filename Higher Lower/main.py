#imports

from higher_lower_logo import gamelogo,vs
from higher_lower_data import data
import random

########constants
current_score=0

#first  two random data
person_1=random.choice(data)
person_2=random.choice(data)

flag=False

while True:
    print(gamelogo)
    print(f"compare a : {person_1['name']} ,a {person_1['description']} ,from {person_1['country']}")
    print(vs)
    print(f"compare b : {person_2['name']} ,a {person_2['description']} ,from {person_2['country']}")

    choose=input("Who has more followers ? Type 'a' or 'b':  ")
    if choose=="a" or choose=="A":
        if person_1['follower_count'] > person_2['follower_count']:
            print("You'r Right ! ")
            current_score+=1
            flag=True
        else:
            print(f"Wrong Answer ! , Current score : {current_score}")
            break

    if choose=="b" or choose=="B":
        if person_2['follower_count'] > person_1['follower_count']:
            current_score+=1
            print("you'r Right ! ")
            flag=True
        else:
            print(f"Wrong Answer ! , Current Score: {current_score}")
            break

    if flag==True:
        person_1=person_2
        person_2=random.choice(data)
        continue

    else:
        print("FFFFFFFFFFFFFFFFFF")
