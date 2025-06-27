from fastapi import FastAPI     
#Annotated allows you to add extra metadata to type hints.
from Models.predictionn import prediction_data
from logic.encodings_logic import encoding_thingsss
from DataValidation.PydanticFile import (User_input , temass_short_name,
                                          Team_Vs_team_Data , Teamsss)
from logic.ipl import (starting_date, Ending_date, 
                       team_Vs_team,  Ipl_team_allrecored , team_api)

app  = FastAPI()

# Root Url
@app.get("/")  
def main():
    
    return {
        
        "Message" : "This is Cricket Score prediction api",
        "Prediction_API" : "/predict_",
        "All_Teams_list_api" : "/team_list",
        "/teamss" : "Show the Specific tems Vs All the teams",
        "Data" : f"Data Start from {starting_date} to {Ending_date}"
    }

##Predictionn URL   
@app.post("/predict_")
def predictionss(UserInput : User_input) -> dict:
    # print("Predictionnnn Functionnn Callll-------------->>>>>>")
    if UserInput.Batting_teams == UserInput.Bowlling_teams:
        return {
                "Warning" : "Kabhi same teams ko khelte dekhaa hai???"
            }
            
    input_validation = [
    
        UserInput.Batting_teams,
        UserInput.Bowlling_teams,
        UserInput.Wickets,
        UserInput.Runns,
        UserInput.Over,
        UserInput.Last_five_overs_wickets,
        UserInput.Ground
    ]

    # print(input_validation)
    # ['Sunrisers_Hyderabad', 'Kolkata_Knight_Riders', 2, 80, 10.0, 1, 'Eden Gardens']

    ###Enncodingggggggg 
    all_array = encoding_thingsss(input_validation)
    
    result = prediction_data(all_array)
    # print(result)

    return {
            "Message" : "Successs - 200",
            "Teams" : input_validation[0] + " " + "Vs"+ " " + input_validation[1],
            "First Innings Projected Score" : round(result[0])
    }

##FIndd the all teamss namesss 
@app.get("/team_list")
def temass_listt():
    
    return{
        "Teams" : list(temass_short_name.values())     
    }

#IPL Teamsss Recordssss 
@app.post("/temsss_information")
def temass_data(UserTeams : Teamsss):
    data =  Ipl_team_allrecored(UserTeams)
    return data


###FIndd the information of particular temass 
@app.post("/team_vs_team")
def team_vs_team_comarision(UserTeamInput : Team_Vs_team_Data ):
    data = team_Vs_team(UserTeamInput.Batting_teams , UserTeamInput.Bowlling_teams)
    return data


##Find the teams information with others
@app.post("/teamss")
def TeamInformation(UserTeam : Teamsss):
    data = team_api(team = UserTeam.teamss)

    return data 
