# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 17:02:27 2020

@author: Chung
"""

"""

rd km ptype lat lon latx lonx
1 0.0 100m 14.11885846 100.555145 14.119 100.555
1 0.1 100m 14.11987748 100.5561615 14.120 100.556
1 1.0 1km

"""
import re
import math
import pandas as pd

def p100m45(x,y):
    return x+0.0005*math.sqrt(2),y+0.0005*math.sqrt(2)

def findDirection(p11,p12,p21,p22):
    mag = math.sqrt((p21-p11)**2 + (p22-p12)**2)
    return (p21-p11)/mag , (p22-p12)/mag

def findDistance(p11,p12,p21,p22):
    return math.sqrt(((p21-p11)**2)+((p22-p12)**2))

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def mark100m(row):
    
    rid=row.id
    road=row.rd
    
    #convert string 
    strPoly=row.polyline
    strTuple = strPoly.strip('[]')
    strTuple = re.split(',',strTuple)
    polyline = [] 
    tempPoly = [] 
    for token in strTuple: 
        latlon = float(token.replace("(", "").replace(")", "")) 
        tempPoly.append(latlon) 
        
        if ")" in token: 
            polyline.append(tuple(tempPoly)) 
            tempPoly = []  
    
    keep,remain = 0,0
    num = 0.0
    total = []
    for point in polyline:
        
        if point == polyline[0]:
            lats, lons = point[0], point[1]
            latp, lonp = point[0], point[1]
            continue
        
        #dist = findDistance(latp,lonp,point[0], point[1])
        dist = distance(tuple([latp,lonp]),tuple([point[0], point[1]]))
        keep = dist
        
        #print('before',keep)
        if remain > 0:
            keep += remain
            remain = 0
            
        #if keep < 0.001:
        if keep < 0.1:
            remain += keep          
            latp, lonp = point[0], point[1]
        #print('mid',dist, keep)

        #if keep >= 0.001:
        if keep >= 0.1:
            
            #time = keep/0.001
            time = keep/0.1
            for y in range(0,int(time)):
                
                cosa, cosb = findDirection(lats,lons,point[0], point[1])
                
                if round((num*10.0))%10.0 == 0.0 and num!=0:
                    rtype = "1km"
    
                else:
                    rtype = "100m" 
    
                temp = [rid,road,round(num,1),rtype,lats,lons,round(lats,3),round(lons,3)]
                total.append(temp)
                num += 0.1
                if keep >= 0.001:
                    lats, lons = lats + (cosa * 0.001), lons + (cosb * 0.001)
                    keep -= 0.001
        
                if keep < 0.001:
                    remain = keep
                #print('after',keep)
            latp, lonp = lats, lons
        #print('after2',keep)
    print(total)
    return total


path = "D:/_meowppp/KMITL/intern uni/work job2/" 
df7 = pd.read_csv('C:/Users/Krung/Desktop/INTERN/Job/Job2.1/RoadData/KM_Data/road-polyline-id.csv',sep=";")

n = [(17.0047442902248029,99.8321148371804838), 
     (16.9981560632762552,99.8373569985652125)]

m = [(17.0047442902248029,99.8321148371804838),
     (17.0014866337248947,99.8352705366134927),
     (16.9981560632762552,99.8373569985652125)]

l = [(17.0047442902248029,99.8321148371804838), 
     (17.0047876456793361,99.8322813181069506), 
     (17.0048320892817024,99.8325186262986790), 
     (17.0047683036156592,99.8327459622259568), 
     (17.0046079325800008,99.8329211938857668), 
     (17.0044427780323311,99.8330857467589254), 
     (17.0042787727738549,99.8332490502638450), 
     (17.0041086322914161,99.8334050541278089), 
     (17.0039378144665001,99.8335609703773059), 
     (17.0037666669178940,99.8337173447454518), 
     (17.0035840080779330,99.8338579446251089), 
     (17.0033922051473674,99.8339880213132744), 
     (17.0032019838326924,99.8341163031008136), 
     (17.0030109202660711,99.8342428789396195), 
     (17.0028207897659023,99.8343719958984366), 
     (17.0026318899247784,99.8345037957628847), 
     (17.0024416471089310,99.8346329927269096), 
     (17.0022512246939677,99.8347622721382066), 
     (17.0020634979285461,99.8348941611737359), 
     (17.0018723023640703,99.8350207893595893), 
     (17.0016787559999010,99.8351444189498665), 
     (17.0014866337248947,99.8352705366134927), 
     (17.0012953254835324,99.8353994747448610), 
     (17.0011037056422722,99.8355275211553703), 
     (17.0009138237612518,99.8356574771701446), 
     (17.0007251972969726,99.8357815287845369), 
     (17.0005351970759371,99.8359133901116849), 
     (17.0003459146449210,99.8360428097009702), 
     (17.0001590917968919,99.8361754000655139), 
     (16.9999769178996765,99.8363144458382692), 
     (16.9997995316770094,99.8364591818253615), 
     (16.9996284654373362,99.8366119159601055), 
     (16.9994598946652573,99.8367678189678429), 
     (16.9992937408480778,99.8369293740433505), 
     (16.9991246250298644,99.8370872559343070), 
     (16.9989299551264601,99.8372120627748814), 
     (16.9987076941984370,99.8372736135038252), 
     (16.9984794479257886,99.8372974585873720), 
     (16.9982569235506382,99.8373175898416889), 
     (16.9981560632762552,99.8373569985652125)]

header = ['rid','rd','km','ptype','lat','lon','latx','lonx']

result = []

df6 = df7.head(1)
for i in range(0,len(df6)):
    locs = df6.apply(lambda row: mark100m(row), axis=1)
    print(locs)
df = pd.DataFrame(columns=header)
dbiloc = 0
for i in range(len(locs.iloc[0])):
    df.loc[dbiloc,"rid"] = locs.iloc[0][i][0]
    df.loc[dbiloc,"rd"] = locs.iloc[0][i][1]
    df.loc[dbiloc,"km"] = locs.iloc[0][i][2]
    df.loc[dbiloc,"ptype"] = locs.iloc[0][i][3]
    df.loc[dbiloc,"lat"] = locs.iloc[0][i][4]
    df.loc[dbiloc,"lon"] = locs.iloc[0][i][5]
    df.loc[dbiloc,"latx"] = locs.iloc[0][i][6]
    df.loc[dbiloc,"lonx"] = locs.iloc[0][i][7]
    dbiloc = dbiloc+1
    
df.to_csv('test_job_2.2.csv')
#distance(tuple([17.0047442902248029,99.8321148371804838]),tuple([16.9981560632762552,99.8373569985652125]))
           