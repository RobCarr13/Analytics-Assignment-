# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:42:52 2015

@author: RobertCarr
"""
#Analytics Research & Implementation
#MIS40750
#Due: 11/10/2015
import sqlite3

conn = sqlite3.connect('renewable.db') # create a "connection"
c = conn.cursor() # create a "cursor" 
c.execute("SELECT * FROM ports;") # execute an SQL command
for item in c:
    print item
    
print "\n" #to seperate the tables on console 
   
c.execute("SELECT * FROM location;")
for item in c:
    print item

#created a list of all the longtitudes of each port
list_port_long=[]
c.execute("SELECT long FROM ports;") # execute an SQL command
for item in c:
    list_port_long.append(item[0])

#created a list of all the latitudes of each port
list_port_lat=[]
c.execute("SELECT lat FROM ports;") # execute an SQL command
for item in c:
    list_port_lat.append(item[0])

#created a list of all the latitudes of each plant
list_lat=[]
c.execute("SELECT lat FROM location;")
for item in c:
    list_lat.append(item[0])

#created a list of all the longtitudes of each plant
list_long=[]
c.execute("SELECT long FROM location;")
for item in c:
    list_long.append(item[0])
    
#created a list of all the production tonnes at each plant
list_resource=[]
c.execute("SELECT production FROM location;")
for item in c:
    list_resource.append(item[0])


#the function below calculates the distance between two co-ordinates
    
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 #difference in longitudes
    dlat = lat2 - lat1 #difference in latitude
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return "%0.2lf" % km

print "\n"

#Created loops to find distances of each port to 
#each plant using haversine function
x=[]
for i in range(0,len(list_long)):
        x.append(haversine(list_port_long[0],list_port_lat[0],list_long[i],list_lat[i]))
print x
print "\n"

y=[]
for i in range(0,len(list_long)):
        y.append(haversine(list_port_long[1],list_port_lat[1],list_long[i],list_lat[i]))
print y
print "\n"

z=[]
for i in range(0,len(list_long)):
        z.append(haversine(list_port_long[2],list_port_lat[2],list_long[i],list_lat[i]))
print z

print "\n"

#finding amount of trips trucks must make to move all production from a plant,
#considering that accoring to 
#www.parliament.uk/briefing-papers/sn00654.pdf trucks can only hold 44 tonnes
#so for example if a plant had 440 tonnes of production at it, you will be 
#required to make 10 trips to move all the production to another plant
#so you would have to multiply distances between the two plants by 10
#i assumed the company would hire someone to do this so they wouldnt be doing 
#round trips. this means that even if a plant is close, if it has a lot of 
#production at it, it will still require a lot of travelling to move all goods.
#for example i have assumed a plant that is 10kms away with 44 tonnes of goods
#would be better than a plant 2km away with 440 tonnes as the total 
#travelling distance for the first one would be 10km where as the second one
#would be 20km

trips = []
for i in list_resource:
    print i/44.0
    trips.append(i/44.0)
print trips


#This function sums up the values in a list           
def sumcount(a):
    count = 0.0
    for i in a:
        count += i
    return count

#how far each plant is away from each port, x111 is the list of distances from
#port 1 to all the plants
x111 =[]
y111 = []
z111 = []
for i in x:
    x111.append(float(i)/1.0)
print x111

for i in y:
    y111.append(float(i)/1.0)
print y111

for i in z:
    z111.append(float(i)/1.0)
print z111

nearestports = []
#this adds the distance from each plant to their nearest port to a list
for i in range(0, len(list_long)):
    if x111[i] < z111[i] and x111[i] < y111[i]:
        nearestports.append(x111[i])
    elif z111[i] < y111[i] and z111[i] < x111[i]:
        nearestports.append(z111[i])
    else:
        nearestports.append(y111[i])
print nearestports
print list_resource

#this adds up all the production tonnes and divides it by 44 to see how many 
#trips must be made from the production plant to the port to move all the 
#production tonnes
totaltripstoport = sumcount(list_resource)/44.0
print totaltripstoport
#this multiplies the amount of trips needed by the distance of from the plant 
#to its nearest port
nearestporttoprod = []
for i in nearestports:
    a = i * totaltripstoport
    nearestporttoprod.append(a)
print nearestporttoprod

#X1 will contain the distance from the first plant to all the other plants 
#in 9 values in a list. For example the first value in x1 will be the distance
#between the first plant and the second plant.
x1= []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
    
for i in range(0,len(list_long)):
    if i != 0:
        x1.append(haversine(list_long[0],list_lat[0],list_long[i],list_lat[i]))
for i in range(0,len(list_long)):
    if i != 1:
        x2.append(haversine(list_long[1],list_lat[1],list_long[i],list_lat[i]))
print x1
print "\n"
print x2
print "\n"
for i in range(0,len(list_long)):
    if i != 2:
        x3.append(haversine(list_long[2],list_lat[2],list_long[i],list_lat[i]))
print x3
print "\n"
for i in range(0,len(list_long)):
    if i != 3:
        x4.append(haversine(list_long[3],list_lat[3],list_long[i],list_lat[i]))
print x4
print "\n"
for i in range(0,len(list_long)):
    if i != 4:
        x5.append(haversine(list_long[4],list_lat[4],list_long[i],list_lat[i]))
print x5
print "\n"
for i in range(0,len(list_long)):
    if i != 5:
        x6.append(haversine(list_long[5],list_lat[5],list_long[i],list_lat[i]))
print x6
print "\n"
for i in range(0,len(list_long)):
    if i != 6:
        x7.append(haversine(list_long[6],list_lat[6],list_long[i],list_lat[i]))
print x7
print "\n"
for i in range(0,len(list_long)):
    if i != 7:
        x8.append(haversine(list_long[7],list_lat[7],list_long[i],list_lat[i]))
print x8
print "\n"
for i in range(0,len(list_long)):
    if i != 8:
        x9.append(haversine(list_long[8],list_lat[8],list_long[i],list_lat[i]))
print x9
print "\n"
for i in range(0,len(list_long)):
    if i != 9:
        x10.append(haversine(list_long[9],list_lat[9],list_long[i],list_lat[i]))
print x10

totaldistprodtoprod = [] 
#this list will contain 10 values. each value will represent the total distance
#required to get all the production goods to that plant 

import numpy as np

#I will now create a new list, that will change the values in the list x1
#into floats. I will then create a numpy array of the list and multiply it 
#by the numpy array that contains the amount of trips needed to move the 
#all the production from each plant. In the example immediately below this, I 
#am multiplying the distance from production plant one to each other production
#plant by the respective amount of trips needed to move the production quantity
#from that plant. I am presuming they hire someone to move the goods and hence
#would only have to pay for it one way.

x1x = []
for i in x1:
    print float(i)/1.0
    x1x.append(float(i)/1.0)
a = np.array(x1x)
b = np.array(trips[1:10])
s = np.multiply(a, b)

#i am putting the values from s into a list so that i can add them later
cc = []
for i in s:
    print i
    cc.append(i)

#here i am added the first addition to the list i created above
a1 = sumcount(cc)
totaldistprodtoprod.append(a1)

#I am now doing the same for the second plant
d = np.array(trips[0:1])
e = np.array(trips[2:10])
xy = []
for i in d:
    xy.append(float(i))
for i in e:
    xy.append(float(i))
print xy

x2x = []
for i in x2:
    x2x.append(float(i)/1.0)
print x2x
g = np.array(x2x)
f = np.array(xy)
dd = np.multiply(g, f)
newlist = []
for i in dd:
    newlist.append(float(i))
a2 = sumcount(newlist)
totaldistprodtoprod.append(a2)

#3rd plant
a1 = np.array(trips[0:2])
a2 = np.array(trips[3:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x3:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a3 =  sumcount(newlist1)
totaldistprodtoprod.append(a3)

#4th plant
a1 = np.array(trips[0:3])
a2 = np.array(trips[4:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x4:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a4 = sumcount(newlist1)
totaldistprodtoprod.append(a4)

#5th Plant
a1 = np.array(trips[0:4])
a2 = np.array(trips[5:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x5:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a5 = sumcount(newlist1)
totaldistprodtoprod.append(a5)

#6th Plant
a1 = np.array(trips[0:5])
a2 = np.array(trips[6:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x6:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a6 = sumcount(newlist1)
totaldistprodtoprod.append(a6)

#7th Plant
a1 = np.array(trips[0:6])
a2 = np.array(trips[7:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x7:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a7 = sumcount(newlist1)
totaldistprodtoprod.append(a7)

#8th Plant
a1 = np.array(trips[0:7])
a2 = np.array(trips[8:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x8:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a8 = sumcount(newlist1)
totaldistprodtoprod.append(a8)

#9th Plant
a1 = np.array(trips[0:8])
a2 = np.array(trips[9:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x9:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a9 = sumcount(newlist1)
totaldistprodtoprod.append(a9)

#10th Plant
a1 = np.array(trips[0:9])
a2 = np.array(trips[10:10])
a33 = []
for i in a1:
    a33.append(float(i))
for i in a2:
    a33.append(float(i))
print a33

x3x = []
for i in x10:
    print float(i)/1.0
    x3x.append(float(i)/1.0)
print x3x
a11 = np.array(x3x)
a22 = np.array(a33)
ddd = np.multiply(a11, a22)
newlist1 = []
for i in ddd:
    newlist1.append(float(i))
a10 = sumcount(newlist1)
totaldistprodtoprod.append(a10)

print totaldistprodtoprod

#Naming which port is used for each production plant
for i in range(0,10):
    if x111[i] == nearestports[i]:
        print "For Plant " + str(i+1) + ", Port 1 should be used"
    elif y111[i] == nearestports[i]:
        print "For Plant " + str(i+1) + ", Port 2 should be used"
    else:
        print "For Plant " + str(i+1) + ", Port 3 should be used"

#Below, I am adding the total distance needed to travel from each production 
#plant to the nearest port with the total distance needed to travel from each 
#port to all the other ports
#for example, the first value in sssss would be (the distance from the first 
#plant to the second plant  times the amount of trips needed to get all the 
#production goods from plant 2) + (the amount of trips needed from plant 1 to
#plant 1's nearest port to ship all the total production)

ss = np.array(nearestporttoprod)
sss = np.array(totaldistprodtoprod)
print ss
sssss = ss + sss
print sssss

print "This is the total distance if plant 1 is selected is " + str(sssss[0])
print "This is the total distance if plant 2 is selected is " + str(sssss[1])
print "This is the total distance if plant 3 is selected is " + str(sssss[2])
print "This is the total distance if plant 4 is selected is " + str(sssss[3])
print "This is the total distance if plant 5 is selected is " + str(sssss[4])
print "This is the total distance if plant 6 is selected is " + str(sssss[5])
print "This is the total distance if plant 7 is selected is " + str(sssss[6])
print "This is the total distance if plant 8 is selected is " + str(sssss[7])
print "This is the total distance if plant 9 is selected is " + str(sssss[8])
print "This is the total distance if plant 10 is selected is " + str(sssss[9])

for i in range(0, 1):
    if sssss[0] < sssss[1] and sssss[0] < sssss[2] and sssss[0] < sssss[3] and sssss[0] < sssss[4] and sssss[0] < sssss[5] and sssss[0] < sssss[6] and sssss[0] < sssss[7] and sssss[0] < sssss[8] and sssss[0] < sssss[9]:
        print "Plant 1 must therefore be the optimal solution"
    elif sssss[1] < sssss[2] and sssss[1] < sssss[0] and sssss[1] < sssss[3] and sssss[1] < sssss[4] and sssss[1] < sssss[5] and sssss[1] < sssss[6] and sssss[1] < sssss[7] and sssss[1] < sssss[8] and sssss[1] < sssss[9]:
        print "Plant 2 must therefore be the optimal solution"
    elif sssss[2] < sssss[1] and sssss[2] < sssss[0] and sssss[2] < sssss[3] and sssss[2] < sssss[4] and sssss[2] < sssss[5] and sssss[2] < sssss[6] and sssss[2] < sssss[7] and sssss[2] < sssss[8] and sssss[2] < sssss[9]:
        print "Plant 3 must therefore be the optimal solution"
    elif sssss[3] < sssss[1] and sssss[3] < sssss[2] and sssss[3] < sssss[0] and sssss[3] < sssss[4] and sssss[3] < sssss[5] and sssss[3] < sssss[6] and sssss[3] < sssss[7] and sssss[3] < sssss[8] and sssss[3] < sssss[9]:
        print "Plant 4 must therefore be the optimal solution"
    elif sssss[4] < sssss[1] and sssss[4] < sssss[2] and sssss[4] < sssss[3] and sssss[4] < sssss[0] and sssss[4] < sssss[5] and sssss[4] < sssss[6] and sssss[4] < sssss[7] and sssss[4] < sssss[8] and sssss[4] < sssss[9]:
        print "Plant 5 must therefore be the optimal solution"
    elif sssss[5] < sssss[1] and sssss[5] < sssss[2] and sssss[5] < sssss[3] and sssss[5] < sssss[4] and sssss[5] < sssss[0] and sssss[5] < sssss[6] and sssss[5] < sssss[7] and sssss[5] < sssss[8] and sssss[5] < sssss[9]:
        print "Plant 6 must therefore be the optimal solution"
    elif sssss[6] < sssss[2] and sssss[6] < sssss[1] and sssss[6] < sssss[3] and sssss[6] < sssss[4] and sssss[6] < sssss[5] and sssss[6] < sssss[0] and sssss[6] < sssss[7] and sssss[6] < sssss[8] and sssss[6] < sssss[9]:
        print "Plant 7 must therefore be the optimal solution"
    elif sssss[7] < sssss[1] and sssss[7] < sssss[2] and sssss[7] < sssss[3] and sssss[7] < sssss[4] and sssss[7] < sssss[5] and sssss[7] < sssss[6] and sssss[7] < sssss[0] and sssss[7] < sssss[8] and sssss[7] < sssss[9]:
        print "Plant 8 must therefore be the optimal solution"
    elif sssss[8] < sssss[1] and sssss[8] < sssss[2] and sssss[8] < sssss[3] and sssss[8] < sssss[4] and sssss[8] < sssss[5] and sssss[8] < sssss[6] and sssss[8] < sssss[7] and sssss[8] < sssss[0] and sssss[8] < sssss[9]:
        print "Plant 9 must therefore be the optimal solution"
    elif sssss[9] < sssss[1] and sssss[9] < sssss[2] and sssss[9] < sssss[3] and sssss[9] < sssss[4] and sssss[9] < sssss[5] and sssss[9] < sssss[6] and sssss[9] < sssss[7] and sssss[9] < sssss[8] and sssss[9] < sssss[0]:
        print "Plant 10 must therefore be the optimal solution"


#Hence I would pick plant 5 and use Port 3 with it!
#Robert Carr - 12303056