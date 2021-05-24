###############  if the server fails to handle the request ############### 
{
    "ok": False,
    "msg" : "error message"
}




############### if the server handle correctly :  ############### 




###############  api: /incomesentiment
{
    "ok": True
    
    "data": [
        "area": "String",
        "positive": "float 0-100" ,# ratio of positive tweet
        "negative": "float 0-100",
        "income_average": "int"  #annual income average
    ]
}


############### api: /topfiveemoji

# top five emoji of victoria , return a list of top 5 emoji codes in vic 
{
    "ok": True,
    "data": [
        "emojicode "
    ] 


}
###############  api: /time

{
    "ok": True,
    "data":[
        {
            "time": "0-24" ,
            "positive": "float 0-100" ,# ratio of positive tweet
            "negative": "float 0-100"
        }
    ]



}

###############  api: /allstatistics
{
    "ok": True,
    
    "data": [
        "area": "String",
        "positive": "float 0-100" ,# ratio of positive tweet
        "negative": "float 0-100",
        "income_average": "int",  #annual income average

        "age_distribution": {
            "five_to_nineteen": "float",
            "twenty_to_thirtynine": "float",
            "forty_to_sixty": "float",
            "medium_age": "float"
        }，
        "population_density": "float",
        
        # 5 emojis
        "top_five_emojis": []
            {
                "code": "emojicode",
                "ratio": "float 0-100"
            }
    ]
    ]
}

###############  api: /totalCollected

{
    "ok": True,
    "data": {
        "total": "int", # total number of tweets collected 
        "areas": [
            {
                "name": "string" , #area name,
                "number": "int " # number of tweet collected in this area 
            }
        ]
    }
}