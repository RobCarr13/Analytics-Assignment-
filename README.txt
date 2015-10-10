# Analytics-Assignment-

This file details how I completed my assignment.
Robert Carr - 12303056
We had to find the optimum plant and port for a production location in order to minimize road transportation costs.

1) Firstly I found the nearest port to each production location and distance needed to get all production material from a production plant to port.. 
How did I do this?

Step 1) 
I found the distances from each location to each port using the haversine function.
Step 2)
I then added the nearest port to each location to a list.
Step 3)
Assuming that trucks can carry 44 tonnes (www.parliament.uk/briefing-papers/sn00654.pdf), I divided the total amount of production material by 44. This gave me the amount of trips I would need to make from whatever production plant I chose to the port. I assumed here that the company would hire someone to do this and therefore they would only be charged for the distance from the plant to the port and not on a round trip basis.
Step 4)
I then multiplied the distance from each plant to their nearest port by the amount of trips needed from plant to port.

2) Secondly, I found the total distance of going from each plant to a certain plant times the amount of times each respective trip needed to be made to get all production material to the one plant. I did this for all 10 plants.
How did I do this?

Step 1)
I again used the haversine function to find the distance between all the plants individually.
Step 2) 
I then created a list that included all the distance from one plant to all the other plants individually.
Step 3)
I then found out how many trips would be needed to move all material from each plant. I did this by dividing the amount of material at each respective plant by 44.0 and adding them individually to a list.
Step 4)
For each plant, I multiplied the amount of trips needed to collect the material from each plant by the distance these plants were away and then added all the values together. 

3) Finally, I needed to get the total distance.
How did I do this?

Step 1) 
I had created two lists, one with the total distance from the production plant to the nearest port in order to move all the material and secondly, a list that contained the total distance required to get all the  material from all the plants to each individual plant.
Step 2)
I used numpy arrays to add these two figures together and give the result.
I found that plant 5 and port 3 would give us the optimal solution for this scenario.

You will see commented throughout my code more in depth detail of how I completed this assignment and what I exactly did at each step.

