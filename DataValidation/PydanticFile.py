from pydantic import BaseModel, field_validator , Field
from typing import Annotated, Literal

temass_short_name = {
    "CSK" : "Chennai Super Kings",
    "RCB" : "Royal Challengers Bangalore",
    "RR"  : "Rajasthan Royals",
    "MI"  : "Mumbai Indians",
    "KKR" : "Kolkata Knight Riders",
    "KXIP": "Kings XI Punjab",
    "DD"  : "Delhi Daredevils",
    "SRH" : "Sunrisers Hyderabad"
}

class User_input(BaseModel):
    Batting_teams  : Annotated[Literal["Sunrisers Hyderabad","Royal Challengers Bangalore","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(... , description = "Batting Team") ]
    
    Bowlling_teams : Annotated[Literal["Royal Challengers Bangalore","Sunrisers Hyderabad","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(..., description = "Bowling Team")]
                
  
    Wickets : Annotated[int   , Field(... , lt=11 , description="GIve me the total witckets")]
    Runns   : Annotated[int   , Field(... , gt=0 ,description="Total runs till lastt balls")]
    Over    : Annotated[float , Field(... , gt=5 , lt=21, description="Total Overs in between 6 to 20")]
    Last_five_overs_wickets : Annotated[int , Field(...  ,  description="Last_Five_Over_wickets")]
    Ground  : Annotated[Literal["Eden Gardens","Chinnaswamy Stadium","MA Chidambaram Stadium Chepauk","Mohali",
                                "Rajiv Gandhi International Stadium, Uppal","Sawai Mansingh Stadium","Wankhede Stadium"] 
                              , Field(... , description="Select the Ground")]
     
  
    @field_validator("Batting_teams" , mode="before")
    @classmethod
    def convert_short_into_long_batting(cls , namess):
        if isinstance(namess , str):
            names_upper = namess.upper()
             
            return temass_short_name.get(names_upper , namess)
    
    @field_validator("Bowlling_teams" , mode = "before")
    @classmethod
    def convert_short_into_long_bowling(cls , names_blowling):
        if isinstance(names_blowling , str):
            names_blowling_upper = names_blowling.upper()

            return temass_short_name.get(names_blowling_upper , names_blowling)
        
        
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


##Validation of temaVsteam API
class Team_Vs_team_Data(BaseModel):
    Batting_teams  : Annotated[Literal["Sunrisers Hyderabad","Royal Challengers Bangalore","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(... , description = "Batting Team") ]
    
    Bowlling_teams : Annotated[Literal["Royal Challengers Bangalore","Sunrisers Hyderabad","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(..., description = "Bowling Team")]
    
    @field_validator("Batting_teams" , mode="before")
    @classmethod
    def convert_short_into_long_batting(cls , namess):
        if isinstance(namess , str):
            names_upper = namess.upper()
             
            return temass_short_name.get(names_upper , namess)
        
    
    @field_validator("Bowlling_teams" , mode = "before")
    @classmethod
    def convert_short_into_long_bowling(cls , names_blowling):
        if isinstance(names_blowling , str):
            names_blowling_upper = names_blowling.upper()
            
            return temass_short_name.get(names_blowling_upper , names_blowling)




###The Class for only particulat Teamssss 
class Teamsss(BaseModel):
    teamss :  Annotated[Literal["Sunrisers Hyderabad","Royal Challengers Bangalore","Rajasthan Royals","Mumbai Indians",
                  "Kolkata Knight Riders","Kings XI Punjab","Delhi Daredevils","Chennai Super Kings"], Field(... , description = "Wirte the Teams Name") ]

    @field_validator("teamss" , mode="before")
    @classmethod
    def convert_short_into_long_batting(cls , namess):
        if isinstance(namess , str):
            names_upper = namess.upper()
             
            return temass_short_name.get(names_upper , namess)

