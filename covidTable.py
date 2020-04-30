#covid - tables
from math import log

from PIL import Image, ImageDraw, ImageFont
fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 26)
bold = ImageFont.truetype('/System/Library/Fonts/Supplemental/HelveticaNeue.ttc', 26, index = 1)



pic = Image.new("RGBA",[1950,1220],None)
draw = ImageDraw.Draw(pic, 'RGBA')

d = []
for x in range(0,87):
    d.append(x+1)

dataStr = open("covid/County Data.txt","r").read().replace(",","").split("\n")
data = []
for el in dataStr:
    data.append(el.split("\t"))

def hsv_to_rgb(h, s, v):
    h/=360
    v*=255
    if s == 0.0: return (v, v, v, 230)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = round(v*(1.-s)), round(v*(1.-s*f)), round(v*(1.-s*(1.-f))); i%=6
    v = round(v)
    if i == 0: return (v, t, p, 230)
    if i == 1: return (q, v, p, 230)
    if i == 2: return (p, v, t, 230)
    if i == 3: return (p, q, v, 230)
    if i == 4: return (t, p, v, 230)
    if i == 5: return (v, p, q, 230)

denData = []
for el in data:
    if el[3] != "0":
        denData.append(float(el[3]))

dataMax = log(max(denData))
dataMin = log(min(denData))  
def col(val): #gets the color value for each of the cells.
    if val == "0":
        return None
    else:
        val = log(float(val))
        hue = 95 - (val-dataMin) * 85  / (dataMax - dataMin)
        sat = 0.4+ (val-dataMin) * 0.09 / (dataMax - dataMin)
        return hsv_to_rgb(hue, sat, 1)
                      
# Green 0.3991,0.8941
# Red   0.4941,1.0000






i = 0
def rightT(pos,n):
    s = data[i][n]
    if s != "0":
        draw.text((pos[0]-draw.textsize(s,fnt)[0],pos[1]),s, font=fnt,fill="#000000")
    else:
        if n == 1:#CHANGE THIS
            dis = 50
        elif n == 2:
            dis = 55
        elif n == 3:
            dis = 50
        else:
            dis = 35
        draw.text((pos[0]-dis,pos[1]),"-", font=fnt,fill="#aaaaaa")
    return

for k in range(0,3):
    draw.rectangle([10+650*k,10,220+650*k,50],"#bebebe","#000000") #change alpha value?
    draw.rectangle([220+650*k,10,330+650*k,50],"#bebebe","#000000")
    draw.rectangle([330+650*k,10,450+650*k,50],"#bebebe","#000000")
    draw.rectangle([450+650*k,10,530+650*k,50],"#bebebe","#000000")
    draw.rectangle([530+650*k,10,640+650*k,50],"#bebebe","#000000")
    
    draw.text((73+650*k,15), "County", font=bold, fill="#000000")
    draw.text((237+650*k,15), "Cases", font=bold, fill="#000000")
    draw.text((344+650*k,15), "Change", font=bold, fill="#000000")
    draw.text((458+650*k,15), "Dead", font=bold, fill="#000000")
    draw.text((538+650*k,15), "Density", font=bold, fill="#000000")
    for n in range(0,29):
        draw.rectangle([10+650*k,50+40*n,220+650*k,90+40*n],None,"#000000")
        draw.rectangle([220+650*k,50+40*n,330+650*k,90+40*n],None,"#000000")
        draw.rectangle([330+650*k,50+40*n,450+650*k,90+40*n],None,"#000000")
        draw.rectangle([450+650*k,50+40*n,530+650*k,90+40*n],None,"#000000")
        draw.rectangle([530+650*k,50+40*n,640+650*k,90+40*n],col(data[i][3]),"#000000")

        draw.text((20+650*k,55+40*n), data[i][0], font=fnt, fill="#000000")
        rightT((320+650*k,55+40*n),1)
        rightT((440+650*k,55+40*n),2)
        rightT((520+650*k,55+40*n),4)
        rightT((630+650*k,55+40*n),3)
        i+=1

    #draw.rectangle([10+650*k,10,640+650*k, 1210], fill=None,outline = "#000000")#Bold Borders
    draw.line([10+650*k,50,640+650*k,50],"#000000",width = 4)
    
    draw.line([10+650*k,10,10+650*k,1210],"#000000",width = 4)
    draw.line([10+650*k,10,640+650*k,10],"#000000",width = 4)
    draw.line([10+650*k,1210,640+650*k,1210],"#000000",width = 4)
    draw.line([640+650*k,10,640+650*k,1210],"#000000",width = 4)

pic.save('covid/Table.png')







