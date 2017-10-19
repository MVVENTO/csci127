#Sci 127 Teaching Staff
#October 2017
#Count which cars got the most parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = "tickets.csv"			#Name of the CSV file
tickets = pd.read_csv(csvFile)		#Read in the file to a dataframe
print(tickets) 				#Print out the dataframe
print(tickets["Plate ID"])	#Print out licence plates 
print(tickets["Plate ID"].value_counts())	#Print out plates & number of tickets each got

print(tickets["Plate ID"].value_counts()[:10])	#Print 10 worst & number of tickets 


