import pandas as pd

df = pd.read_csv("Data/ipl_matches.csv")

#Datastart from to DataEnd
starting_date = df['Date'].min()
Ending_date = df['Date'].max()


## 
def comparing_team1_team2(team_1 , team_2):
    return df[(df['Team1'] == team_1) & (df['Team2'] == team_2) | (df['Team1'] == team_2) & (df['Team2'] == team_1)].shape

###Ipl teamss All Recordsssss 
def Ipl_team_allrecored(team):
    df_team = df[(df["Team1"] == team) | (df['Team2'] == team)]
    total_matches = df_team.shape[0]
    won_matches = df_team[df_team['WinningTeam'] == team].shape[0]
    no_result = df_team[df_team['WinningTeam'].isnull()].shape[0]
    loss = (total_matches - won_matches - no_result)
    Final_matches = df_team[(df_team['WinningTeam'] == team) & (df_team['MatchNumber'] == 'Final')].shape[0]

    total_matches =  {
        "Team" : team,
        "total_matches" : total_matches ,
        "won_matches" : won_matches ,
        "no_result" : no_result ,
        "loss" : loss ,
        "Final_matches_won" : Final_matches
    } 

    return total_matches


###Api temaVsTeam Comparisionssssss
def team_Vs_team(teams1 , teams2):
    # print(teams1)
    # print(teams2)
    try:
        teams_df = df[((df['Team1'] == teams1) | (df['Team2'] == teams1)) & ((df['Team1'] == teams2) | (df['Team2'] == teams2))]
        total_matches = teams_df.shape[0]
        try:
            matches_won_team1 = int(teams_df['WinningTeam'].value_counts()[teams1])
        except:
            matches_won_team1 = 0
        try:
            matches_won_team2 = int(teams_df['WinningTeam'].value_counts()[teams2])
        except:
            matches_won_team2 = 0
        
        draws = total_matches - (matches_won_team1 + matches_won_team2)

        teams_dict = {
                "total_matches" : str(total_matches),
                teams1 : matches_won_team1,     
                teams2 : matches_won_team2,
                "total draws" : draws
            }

        return teams_dict
    except :
        raise Exception("No Matches")
    

##here this function describe the overall and against the temas performance 
def team_api(team):
    try:
        df_team = df[(df["Team1"] == team) | (df['Team2'] == team)]
        #print(df_team)
        self_record = Ipl_team_allrecored(team)
        #print("doen")
        u_team = [i for i in (df_team['Team1'].unique())  if (i != team )and (i != "Pune Warriors")and  (i != 'Kochi Tuskers Kerala')]
        #print(u_team)
        #print("Doneeee")
        #[print(t) for t in u_team]
        # for i in u_team:
        #     print(i)
        again = {t : team_Vs_team( teams1 = team , teams2 = t)  for t in u_team }
        #print("doeeeenenene")
        data = {
            team : {
            "OverAll" : self_record,
            "against" : again
            }
        }

        return data
    
    except: 
        raise Exception("Not Good Somthing")
    
