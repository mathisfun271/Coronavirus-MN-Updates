#background

from PIL import Image, ImageDraw, ImageFont
from time import time
from math import ceil

st = time()

fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 26)
small = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 20)
title = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 40,index = 1)
bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 30,index = 1)

pic = Image.new("RGBA",[1950,2440],"#ffffff")
draw = ImageDraw.Draw(pic, 'RGBA')

backImage = Image.open('/Users/nathanmihm/Math Graphics/covid/CovidBackgroundClear.png')

datas = backImage.getdata()
newData = []
for item in datas:

    newData.append((item[0], item[1], item[2], ceil(item[3]/3) ))
    
backImage.putdata(newData)


backImage = backImage.resize((1950,1950))
pic.paste(backImage, (0,240), backImage)

draw.text((505,70), 'Daily Minnesota SARS-Coronavirus-2 Infographic', font=title, fill="#000000")

draw.text((10,40), 'Posted on:', font=fnt, fill="#000000")
draw.text((210,15), 'r/CoronavirusMN', font=fnt, fill="#000000")
draw.text((210,65), 'r/minnesota', font=fnt, fill="#000000")
MinnesotaLogo = Image.open('/Users/nathanmihm/Math Graphics/covid/MinnesotaLogo.png').resize((50,50))
CovidMN = Image.open('/Users/nathanmihm/Math Graphics/covid/CoronavirusMN.png').resize((50,50))
pic.paste(CovidMN, (150,5), CovidMN)
pic.paste(MinnesotaLogo, (150,55), MinnesotaLogo)

draw.text((1760,20), 'u/mathisfun271', font=fnt, fill="#000000")
myLogo = Image.open('/Users/nathanmihm/Math Graphics/covid/myLogo.png').resize((50,50))
pic.paste(myLogo, (1700,10), myLogo)
draw.text((1435,20), 'Created in Python by:', font=fnt, fill="#000000")

draw.text((240,1165), 'Density on the charts refers to the number of cases per 10,000 people. Colored with red being the highest and green the lowest', font=fnt, fill="#000000")


draw.text((1310,670), 'Sources and previous posts links can be found', font=fnt, fill="#000000")
draw.text((1310,700), 'in the comments section', font=fnt, fill="#000000")

draw.text((1310,770), 'Primary Source: Minnesota Department of Health', font=fnt, fill="#000000")

draw.text((1310,900), 'Due to the fact that I am now using Python,', font=fnt, fill="#000000")
draw.text((1310,930), 'I will seamlessly be able to add complex', font=fnt, fill="#000000")
draw.text((1310,960), 'maps of Minnesota. They will be added in the', font=fnt, fill="#000000")
draw.text((1310,990), 'coming days.', font=fnt, fill="#000000")

bottomNote = 'Thanks for everybody’s support! I love tracking data, and I’m happy to share this information with all of you.'
draw.text((510,2410), bottomNote, font=small, fill="#000000")


draw.text((190,200),'General Infomation',font=bold,fill="#000000")
draw.text((177,500),'Recovery Infomation',font=bold,fill="#000000")
draw.text((185,800),'Hospital Infomation',font=bold,fill="#000000")

pic.save('/Users/nathanmihm/Math Graphics/covid/Background.png')

print(time()-st)
