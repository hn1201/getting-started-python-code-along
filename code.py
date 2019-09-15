# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data=yaml.load(f)

# Find data type of the file
type_of_data=type(data)
print(type_of_data)

# In which city, and at which venue the match was played and where was it played ?
city=data['info']['city']
print(city)
venue=data['info']['venue']
print(venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams=(data['info']['teams'])
print(teams)
no_of_teams=len(teams)
print(no_of_teams)
# Which team won the toss and what was the decision of toss winner ?
Toss_Winner=data['info']['toss']['winner']
print(Toss_Winner)
Toss_decision=data['info']['toss']['decision']
print(Toss_decision)
# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler=data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
print(first_bowler)
first_batsman=data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
print(first_batsman)
# How many deliveries were delivered in first inning ?
deliveries_1stinning=len(data['innings'][0]['1st innings']['deliveries'])
print(deliveries_1stinning)
# How many deliveries were delivered in second inning ?
deliveries_2stinning=len(data['innings'][1]['2nd innings']['deliveries'])
print(deliveries_2stinning)
# Which team won and how ?
winner=data['info']['outcome']['winner']
print(winner)
runs=data['info']['outcome']['by']['runs']
print(runs)


