#data fetch

from datetime import date, timedelta
import clipboard
from math import log

print("Review County Info First, Update MDH .txt file!")
tests = int(input("Test total: "))
cases = int(input("Case total: "))
recov = int(input("Recovered total: "))
deaths = int(input("Death total: "))
hosps = int(input("Hospitalization total: "))
chosps = int(input("Current Hospitalizations: "))
ICU = int(input("ICU: "))
county = int(input("County Count: "))
popCount = 0

cdata = [cases,deaths,tests,recov,hosps,chosps,county,ICU]

def percent(num,den):
    if den == 0:
        return ""
    else:
        return round(num/den * 100,3)

#County Data (Hard)

#clipboard?
MDHtxt = open("covid/MDHcounty.txt","r").read().replace(",","").replace("Lake of the Woods","Lk of the Woods")

popTxt = open("covid/countyPop.txt","r").read().replace(",","")

pcDataTxt = open("covid/county Data.txt","r").read()

pcData = []
for el in pcDataTxt.split("\n"):
    pcData.append(el.split("\t")[:2])
pcData.sort(key=lambda x: x[0])

pop = []
for el in popTxt.split("\n"):
    pop.append(el.split("\t"))

MDHar = []
for el in MDHtxt.split("\n"):
    MDHar.append(el.split("\t"))

def signed(n):
    if n>0:
        return "+%s" % n
    elif n<0:
        return str(n)
    else:
        return "0"


chartAr = []
Mpos = 0
den = 0
countyChange = ""
for n,el in enumerate(pop):
    if el[0] == MDHar[Mpos][0]:
        den = round(int(MDHar[Mpos][1])/int(el[1])*10000,3)
        if MDHar[Mpos][1] != "0" and pcData[n][1] == "0":
            countyChange = signed(int(MDHar[Mpos][1]))+ " (first)"
        else:
            countyChange = signed(int(MDHar[Mpos][1])-int(pcData[n][1]))
        chartAr.append([el[0],int(MDHar[Mpos][1]),countyChange,den,MDHar[Mpos][2]])
        Mpos += 1
        popCount += int(el[1])
    else:
        chartAr.append([el[0],0,0,0,0])

chartAr.sort(reverse = True, key=lambda x: x[1])

chartStr = ""
csvStr = "Name,density"
for n,arEl in enumerate(chartAr):
    csvStr += '\n%s,%s' % (arEl[0],arEl[3])
    chartStr += "%s\t%s\t%s\t%s\t%s" % (arEl[0],arEl[1],arEl[2],arEl[3],arEl[4])
    if n != 86:
        chartStr += "\n"

csvStr = csvStr.replace("Lk of","Lake of")

print(csvStr)

popCountStr = str(popCount)
popCountStr = popCountStr[0] + ',' + popCountStr[1:4] + ',' + popCountStr[4:]


with open("covid/County Data.txt","w") as myfile:
    myfile.write(chartStr)

with open("covid/mapData.csv","w") as myfile:
    myfile.write(csvStr)




#Graph Data
graphTxt = open("covid/graphData.txt","r")
graphTxt = graphTxt.read()
yest = graphTxt.split("\n")[-1].split("\t")[0]
if yest != (date.today() - timedelta(days=1)).strftime('%m/%d'):
    print("Warning. Missing main data, please check")

num = int(graphTxt.split("\n")[-1].split("\t")[1])+1
now = date.today().strftime('%m/%d')
newGraph = "\n%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (now,num,cases,hosps,deaths,tests,percent(cases,tests),percent(deaths,cases))

with open("covid/graphData.txt","a") as myfile:
    myfile.write(newGraph)

#Main Data
mainTxt = open("covid/maindata.txt","r").read()
txtAr = mainTxt.split("\n\n\n")[2].split("\n")

yest = mainTxt[:5]
if yest != (date.today() - timedelta(days=1)).strftime('%m/%d'):
    print("Warning. Missing chart data, please check")


pData = []
for el in txtAr:
    pData.append(int(el.split("\t")[2]))

def change(n):
    if n == 5 or n==7:
        if cdata[n]-pData[n]>=0:
            s = "up "
        else:
            s = "down "
        return s + str(abs(cdata[n]-pData[n]))
    else:
        return cdata[n]-pData[n]

    
chartStr = ""
d = []
labels = ['pos','deaths','tests','recov','hosp','presH','countyC','ICU']
for n,el in enumerate(cdata):
    d.append([labels[n],pData[n],el,change(n)])
    chartStr += "%s\t%s\t%s\t%s\n" % (labels[n],pData[n],el,change(n))

#County Summary: 78/87 Counties with infections (0 new). 5,430,455 (98.247%) Minnesotans total in these counties

print("Title copied to clipboard")
clipboard.copy('%s Update: %s Positives (+%s), %s Deaths (+%s), %s new tests' % (now.lstrip("0"),d[0][2],d[0][3],d[1][2],d[1][3],d[2][3]))

genStr = "Total: %s positives (%s%% of tests), %s deaths (%s%% of cases) out of %s tests. " % (d[0][2],percent(d[0][2],d[2][2]),d[1][2],percent(d[1][2],d[0][2]),d[2][2])
genStr += "From today: %s new positives (%s%% of new tests) and %s deaths out of %s new tests." % (d[0][3],percent(d[0][3],d[2][3]),d[1][3],d[2][3])

recovStr = 'Cases with outcome: %s, %s recoveries (up %s), %s deaths (%s%%). Active Cases: %s' % (d[3][2]+d[1][2],d[3][2],d[3][3],d[1][2],percent(d[1][2],d[3][2]+d[1][2]),d[0][2]-d[3][2]-d[1][2])

hospStr = 'Hospitalizations: %s total (up %s, %s%% of total cases), %s currently (%s). ' % (d[4][2],d[4][3],percent(d[4][2],d[0][2]),d[5][2],d[5][3])
hospStr += 'Patients in ICU: %s (%s), %s%% of current hospitalizations.' % (d[7][2],d[7][3],percent(d[7][2],d[5][2]))

countyStr = 'County Summary: %s/87 Counties with infections (%s new). ' % (d[6][2],d[6][3])
countyStr += '%s (%s%%) Minnesotans total in these counties.' % (popCountStr,percent(popCount,5527358))

fullStr = "%s\n\n%s\n\n%s\n\n%s" % (genStr,recovStr,hospStr,countyStr)

output = '%s\n\n\n------------\n\n\n%s\n\n------------\n\n\n%s' % (now,chartStr,fullStr)

with open("covid/maindata.txt","w") as myfile:
    myfile.write(output)







