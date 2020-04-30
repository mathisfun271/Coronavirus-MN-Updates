# main program
mainDataAr = open("/Users/nathanmihm/Math Graphics/covid/mainData.txt","r").read().split("------------\n\n\n")[-1].split("\n\n")


from PIL import Image, ImageDraw, ImageFont

import datetime

fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 30)
bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 30,index = 1)
small = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 20)

def wrapText(pos,text,font,fill):
    x1 = pos[0]
    width = pos[2]-pos[0]
    ypos = pos[1]
    #draw.rectangle(pos,fill=None,outline = "#000000")
    s1,s2 = "",""
    textAr = text.split(" ")
    for el in textAr:
        s1 += el
        if draw.textsize(s1,font=font)[0]>width:
            draw.text((pos[0],ypos),s2,font=font,fill="#000000")
            ypos += 40
            s1 = el + " "
        else:
            s2 = s1
            s1 += " "
    draw.text((pos[0],ypos),s1,font=font,fill="#000000")
    if ypos > pos[3]:
        print("Warning: Text printed outside box.")




pic = Image.open('/Users/nathanmihm/Math Graphics/covid/Background.png')
draw = ImageDraw.Draw(pic, 'RGBA')

wrapText((10,250,640,500),mainDataAr[0],fnt,"#000000")
wrapText((10,550,640,800),mainDataAr[1],fnt,"#000000")
wrapText((10,850,640,1100),mainDataAr[2],fnt,"#000000")


chart = Image.open('/Users/nathanmihm/Math Graphics/covid/Table.png')
pic.paste(chart, (0, 1190), chart)

date = datetime.datetime.now()#Timestamp Generation
timestamp = "Updated: %s at %s" % (date.strftime("%x"),date.strftime("%X"))
timeW = draw.textsize(timestamp, font=bold)[0]
draw.text((round((1950-timeW)/2),120), timestamp, font=bold, fill="#000000")

countyS = mainDataAr[3]
countyW = draw.textsize(countyS, font=fnt)[0]
draw.text((round((1950-countyW)/2),1120), countyS, font=fnt, fill="#000000")




# GRAPHS
# HERE
def trans(img):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)

linGraph = Image.open('/Users/nathanmihm/Math Graphics/covid/linGraph.png').convert("RGBA")
trans(linGraph)
pic.paste(linGraph, (660, 170), linGraph)

logGraph = Image.open('/Users/nathanmihm/Math Graphics/covid/logGraph.png').convert("RGBA")
trans(logGraph)
pic.paste(logGraph, (1310, 170), logGraph)

pGraph = Image.open('/Users/nathanmihm/Math Graphics/covid/percentGraph.png').convert("RGBA")
trans(pGraph)
pic.paste(pGraph, (660, 630), pGraph)





fileName = "%d|%d Update.png" % (date.month,date.day)
pic.save('/Users/nathanmihm/Math Graphics/covid Updates/'+fileName)

