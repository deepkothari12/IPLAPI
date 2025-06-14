import pickle
# from fastapi import FastAPI
from fastapi import FastAPI  # type: ignore
from pydantic import BaseModel,Field , computed_field , field_validator
from typing import Annotated,Literal  #Annotated allows you to add extra metadata to type hints.
from Models.predictionn import prediction_data
from logic.encodings_logic import encoding_thingsss

app  = FastAPI()


class User_input(BaseModel):
    Batting_teams  : Annotated[Literal["Sunrisers Hyderabad","Royal Challengers Bangalore","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(... , description = "Batting Team") ]
    
    Bowlling_teams : Annotated[Literal["Sunrisers Hyderabad","Royal Challengers Bangalore","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(..., description = "Bowling Team")]


    Wickets : Annotated[int , Field(... , description="GIve me the total witckets")]
    Runns   : Annotated[int , Field(... , gt=0 ,description="Total runs till lastt balls")]
    Over    : Annotated[float , Field(... , gt=0 , description="Total Overs")]
    Last_five_overs_wickets : Annotated[int , Field(...  ,  description="Last_Five_Over_wickets")]
    Ground  : Annotated[Literal["Eden Gardens","Chinnaswamy Stadium","MA Chidambaram Stadium Chepauk","Mohali",
                               "Rajiv Gandhi International Stadium, Uppal","Sawai Mansingh Stadium","Wankhede Stadium"] 
                               , Field(... , description="Select the Ground")]
    

    @field_validator("Ground")
    @classmethod
    def ground_perfection(cls , Ground_name) -> str:
        return Ground_name.replace(" " , "_")
    

    @field_validator("Bowlling_teams")
    @classmethod
    def bowling_team_perfection(cls , bowlingg_team_name) -> str:
        return bowlingg_team_name.replace(" ", "_")
    
    
    @field_validator("Batting_teams")
    @classmethod
    def batting_team_perfection(cls , Batting_team_name) -> str:
        return Batting_team_name.replace(" ", "_")

@app.get("/")
def main(): 
    return {
        "Message" : "This is Cricket Score prediction api"
    }

@app.post("/predict_")
def predictionss(UserInput : User_input) -> dict:
    # print("Predictionnnn Functionnn Callll-------------->>>>>>")
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
    # print("ALLLLLLLLLLLLLLLLLLLLLLLLLLLLLM ARAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY--->>>>>>>>",all_array)

    result = prediction_data(all_array)
    # print(result)

    return {

            "Message" : "Successs - 200",
            "Teams" : input_validation[0] + " " + "Vs"+ " " + input_validation[1],
            "Accepted Score" : round(result[0])
    }
