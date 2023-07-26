from requests import get,post 
Webhook="" # Add discord webhook link here
API_Key="" # Insert your NASA API key here
Space_Role_ID='' # Add discord space role ID here
try:
    RequestData=get(f'https://api.nasa.gov/planetary/apod?api_key={API_Key}').json() # Requests json data from NASA API
    try:
        artist=RequestData['copyright'] # Attempts to get artist name
    except KeyError:
        artist='**Not Found**' # If artist name fails returns with a bold not found
        pass
    JSON_Data={
        "content":f'<@&{Space_Role_ID}>', # Comment out this line if you do not have a space role
        "username":"Photo Of The Day", # Webhook post username
        "avatar_url":RequestData['url'], # PFP of webhook will be space photo
        "embeds": [{
            'title':RequestData['title'], # Title of the post
            'color':5964804, # Webhook border color
            "description":f"Photo By: {artist}", # Artist for photo
            "image":{"url":RequestData['url']}, # Space Photo
            "footer":{"text":f"Made by DrGecko","icon_url":"https://drgecko.xyz/drgecko_pfp.png"}}]} # Please leave this in
    post(Webhook,json=JSON_Data) # Posts to discord
except Exception as error: 
    JSON_Data={"content":f"**Space Failed**\nERROR: {error}","username": "Photo Of The Day","avatar_url":"https://drgecko.xyz/drgecko_pfp.png"} # In case of some fatal error it posts a fail
    post(Webhook,json=JSON_Data) # Posts fail

# DrGecko 2023
