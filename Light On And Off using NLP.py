%matplotlib inline
from matplotlib.pyplot import imshow
from PIL import Image
import requests
from io import BytesIO
import json

#set up API CONFIGURATION
apiUrl="https://westeurope.api.cognitive.microsoft.com/luis/v2.0/apps/"
appId="APPID"
appKey="APIKEY"
#prompt for command

command=input('please enter a command:')
#call the LUIS service and get the json response
endpoint=apiUrl+appId+"?subscription-key="+appKey+"&q="+command.replace(" ","+")
response=requests.get(endpoint)
data=json.loads(response.content)
#print(data)
#identifying the top scoring intent
intent=data["topScoringIntent"]["intent"]
if(intent=="Light On"):
        img_url='https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/LightOn.jpg'
elif(intent=="Light Off"):
        img_url='https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/LightOff.jpg'
else:
        img_url='https://raw.githubusercontent.com/MicrosoftLearning/AI-Introduction/master/files/Dunno.jpg'
response=requests.get(img_url)
img=Image.open(BytesIO(response.content))
imshow(img)
    
