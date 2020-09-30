# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:51:38 2020

@author: hollachr
"""
import pandas as pd
import time

# number of golfers in a team
n_man_scramble = 4

# record of all golfers handicaps comment out non players
golfers ={
        'holland':11,        
        'pazz':28,
        'rich':28,
        'heath':25,
        'angus':16,
        'snowy':13,
        'sean':8,
        #'dametto':9,
        'dylan':6,
        'tic':19,
        #'carrion':2,
        'dorling':5,
        'johan':18,
        #'james':22,
        'jimmy':32,
        #'rough':17,
        'ashley':17,
        #'dan':32,
        'sam':27,
        'fredrik':18,
        'neil':21,
        #'ben':12,
        'barrett':30,
        'pete':26,
        'ian':14,
        'reno':21,
        'jason':9,
        'flash':20,
        'joe':36,
        'tim':32,
        'kasper':18,
        'berry':4,
        'scott':26,
        'mason':8
        }

# handicapping function that returns /6 for 3 ball and /10 for 4 ball
def handicapping(n_man_scramble):
    if n_man_scramble == 3:
        return 6
    elif n_man_scramble == 4:
        return 10

# create dataframe from dictionary
df = pd.DataFrame(list(golfers.items()), columns=['golfer','handicap'])

# sort dataframe from lowest to highest handicap
df.sort_values(by='handicap',inplace=True)

# calculate number of players in each pot (i.e number of teams)
n_teams = int(len(df)/n_man_scramble)


# set up empty list of dataframes for each pot
pots = []

# split the dataframe into pots to draw from and shuffle pots
for i in range(n_man_scramble):
    df_pot = df[n_teams*i:n_teams*(i+1)][:]
    
    # shuffle the golfers with the seeded pot
    df_pot = df_pot.sample(frac=1).reset_index(drop=True)
    
    # appended each seeded pot to the list of pots
    pots.append(df_pot)

# pick a member from each pot to form a team loops through for n teams
for i in range(n_teams):
    
    # list of dataframes to contain team members for team i
    team = []
    
    # for pot assign player in position i to team i
    for pot in pots:
        member = pot.iloc[[i]]
        team.append(member)
    
    # concatenate dataframe for team i
    df_team = pd.concat(team)
    
    # calculate team handicap based on /6 for 3 ball and /10 for 4 ball
    #handicap = round((df_team['handicap'].sum())/handicapping(n_man_scramble))
    handicap = (df_team['handicap'].sum())/handicapping(n_man_scramble)
    
    # print details of each team and associated handicaps
    print(df_team)
    print('Handicap: ',handicap)
    print('')
   #time.sleep(8)
