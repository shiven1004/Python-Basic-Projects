'''
#Current time
from datetime import datetime 
  
# now() method is used to 
# get object containing  
# current date & time. 
now_method = datetime.now() 
  
# strftime() method used to 
# create a string representing 
# the current time. 
currentTime = now_method.strftime("%H:%M:%S") 
print("Current Time =", currentTime) 
'''

'''
# python program Find number of times every day occurs in a Year  
   
  
import datetime  
import calendar 
   
def day_occur_time(year): 
      
    # stores days in a week  
    days = [ "Monday", "Tuesday", "Wednesday",   
           "Thursday",  "Friday", "Saturday",  
           "Sunday" ] 
      
    # Initialize all counts as 52 
    L = [52 for i in range(7)] 
      
    # Find the index of the first day 
    # of the year 
    pos = -1
    day = datetime.datetime(year, month = 1, day = 1).strftime("%A") 
    for i in range(7): 
        if day == days[i]: 
            pos = i 
              
    # mark the occurrence to be 53 of 1st day 
    # and 2nd day if the year is leap year 
    if calendar.isleap(year): 
        L[pos] += 1
        L[(pos+1)%7] += 1
          
    else: 
        L[pos] += 1
          
      
    # Print the days 
    for i in range(7): 
        print(days[i], L[i]) 
       
   
# Driver Code  
year = int(input("Enter any year: "))
day_occur_time(year) 
'''

'''
# Python3 code to demonstrate Getting current date and time using now().  
    
# importing datetime module for now()  
import datetime  
    
# using now() to get current time  
current_time = datetime.datetime.now()  
    
# Printing value of now.  
print ("Time now at greenwich meridian is : ", end = "")  
print (current_time) 
'''

'''
# Python program to find yesterday, today and tomorrow 
  
  
# Import datetime and timedelta 
# class from datetime module 
from datetime import datetime, timedelta 
  
  
# Get today's date 
presentday = datetime.now() # or presentday = datetime.today() 
  
# Get Yesterday 
yesterday = presentday - timedelta(1) 
  
# Get Tomorrow 
tomorrow = presentday + timedelta(1) 
  
  
# strftime() is to format date according to 
# the need by converting them to string 
print("Yesterday = ", yesterday.strftime('%d-%m-%Y')) 
print("Today = ", presentday.strftime('%d-%m-%Y')) 
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y')) 
'''

'''
# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM")) 
'''

'''
# importing libraries 
import time 
  
  
# Timer starts 
starttime=time.time() 
lasttime=starttime 
lapnum=1
  
print("Press ENTER to count laps.\nPress CTRL+C to stop") 
  
try: 
     while True: 
              
          # Input for the ENTER key press 
          input() 
  
          # The current lap-time 
          laptime=round((time.time() - lasttime), 2) 
  
          # Total time elapsed  
          # since the timer started 
          totaltime=round((time.time() - starttime), 2) 
  
          # Printing the lap number, 
          # lap-time and total time 
          print("Lap No. "+str(lapnum))  
          print("Total Time: "+str(totaltime)) 
          print("Lap Time: "+str(laptime)) 
            
          print("*"*20) 
  
          # Updating the previous total time 
          # and lap number 
          lasttime=time.time() 
          lapnum+=1
  
# Stopping when CTRL+C is pressed 
except KeyboardInterrupt: 
     print("Done")
'''

'''
#Stopwatch
import os
import time

second,minute,hours=0,0,0

while(True):
    print(hours,":",minute,":",second)
    time.sleep(1)
    second+=1
    if (second==60):
        second=0
        minute+=1
    if (minute==60):
        minute=0
        hour+=1
os.system('cls')
'''
