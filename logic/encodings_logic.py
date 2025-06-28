import pandas as pd
import requests

def encoding_thingsss(data):
    temp_array = list()
    temp_array1 = []
    temp_array2 = []
    temp_array3 = []

    # if requests == 'POST':    

    # batti ng_team = request.form['batting_teams']
    if data[0] == 'Chennai_Super_Kings':
        temp_array1 = temp_array1 + [1,0,0,0,0,0,0,0]
    elif data[0] == 'Delhi_Daredevils':
        temp_array1 = temp_array1 + [0,1,0,0,0,0,0,0]
    elif data[0] == 'Kings_XI_Punjab':
        temp_array1 = temp_array1 + [0,0,1,0,0,0,0,0]
    elif data[0] == 'Kolkata_Knight_Riders':   
        temp_array1 = temp_array1 + [0,0,0,1,0,0,0,0]
    elif data[0] == 'Mumbai_Indians':
        temp_array1 = temp_array1 + [0,0,0,0,1,0,0,0]
    elif data[0] == 'Rajasthan_Royals':
        temp_array1 = temp_array1 + [0,0,0,0,0,1,0,0]
    elif data[0] == 'Royal_Challengers_Bangalore':
        temp_array1 = temp_array1 + [0,0,0,0,0,0,1,0]
    elif data[0] == 'Sunrisers_Hyderabad':   
        temp_array1 = temp_array1 + [0,0,0,0,0,0,0,1]
        
        
    # data[1] = request.form['bowlling_teams']
    if data[1] == 'Chennai_Super_Kings':
        temp_array2  = temp_array2  + [1,0,0,0,0,0,0,0]
    elif data[1] == 'Delhi_Daredevils':
        temp_array2  = temp_array2  + [0,1,0,0,0,0,0,0]
    elif data[1] == 'Kings_XI_Punjab':
        temp_array2  = temp_array2  + [0,0,1,0,0,0,0,0]
    elif data[1] == 'Kolkata_Knight_Riders':
        temp_array2  = temp_array2  + [0,0,0,1,0,0,0,0]
    elif data[1] == 'Mumbai_Indians':
        temp_array2  = temp_array2  + [0,0,0,0,1,0,0,0]
    elif data[1] == 'Rajasthan_Royals':
        temp_array2  = temp_array2  + [0,0,0,0,0,1,0,0]
    elif data[1] == 'Royal_Challengers_Bangalore':
        temp_array2  = temp_array2  + [0,0,0,0,0,0,1,0]
    elif data[1] == 'Sunrisers_Hyderabad':
        temp_array2  = temp_array2  + [0,0,0,0,0,0,0,1]

    # ground = request.form['data[-1]']
    if   data[-1] == "Eden_Gardens":
        temp_array3 = temp_array3 + [1,0,0,0,0,0,0]
    elif data[-1] == "Chinnaswamy_Stadium":
        temp_array3 = temp_array3 + [0,1,0,0,0,0,0]
    elif data[-1] == "MA_Chidambaram_Stadium_Chepauk":
        temp_array3 = temp_array3 + [0,0,1,0,0,0,0]
    elif data[-1] == "Mohali": 
            temp_array3 = temp_array3 + [0,0,0,1,0,0,0]
    elif data[-1] == "Rajiv_Gandhi_International_Stadium_Uppal":
        temp_array3 = temp_array3 + [0,0,0,0,1,0,0]
    elif data[-1] == "Sawai_Mansingh_Stadium":
        temp_array3 = temp_array3 + [0,0,0,0,0,1,0]
    elif data[-1] == "Wankhede_Stadium":
        temp_array3 = temp_array3 + [0,0,0,0,0,0,1]

    if data[0] != data[1]:

        #[0,0,0,0,0,0,1,0] +  [0,0,0,0,0,0,1,0] + [0,0,0,1,0,0,0] + [5] + [50] + [2] + [0]
        temp_array = temp_array1 + temp_array2 
        # print("-->>>>",temp_array)
        overs =  int(data[4])#int(request.form['overs'])
        # print("OVerrrrrsssssssssssssssssssssssssssssssssssss" , overs)
        runs = data[3]#int(request.form['runs_last_5'])
        wickets = data[2]#int(request.form['wickets'])
        Last_5_over_wickets = data[-2]#int(request.form['wickets_last_5'])




        all_array =  temp_array +  [ overs ,runs , wickets , Last_5_over_wickets] + temp_array3     
        
        return all_array       


    