%matplotlib inline
from matplotlib.pyplot import imshow
from PIL import Image
import requests
from io import BytesIO
import json

#set up API CONFIGURATION
apiUrl="https://westeurope.api.cognitive.microsoft.com/luis/v2.0/apps/"
appId="225dd1a4-bba9-494f-8808-79f1d2f56568"
appKey="9c12031c6d924d4ca45bde62722f5407"
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
    
