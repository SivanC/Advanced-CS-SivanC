import cProfile, pstats
from sortfunctions import insertSort

profile = cProfile.Profile() #Creating the profile class
sortMethod = 'cumtime' #Defining filter for data
outputPath = '/Users/Sivan/Advanced-CS-SivanC/Advanced CS/profileTestingOutput.txt'
output = open(outputPath, 'w') #Opening the output file for writing

profile.enable() #Starting tracking of data
for i in range(50):
	insertSort([9,8,7,6,5,4,3,2,1])
profile.disable #Ending tracking of data

stats = pstats.Stats(profile, stream=output).strip_dirs().sort_stats(sortMethod).print_stats() #Creating a stats printout from the data of our profile and writing it to the output file without directories, and sorted by cumulative time.