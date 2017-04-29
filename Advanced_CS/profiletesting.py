import cProfile, pstats
import nGramsParser
reload(nGramsParser)

profile = cProfile.Profile() #Creating the profile class
sortMethod = 'cumtime' #Defining filter for data
outputPath = '/Users/Sivan/Documents/Github/Advanced-CS-SivanC/Advanced_CS/profileTestingOutput.txt'
output = open(outputPath, 'w') #Opening the output file for writing

profile.enable() #Starting tracking of data
nGramsParser.nGramsParse()
profile.disable #Ending tracking of data

stats = pstats.Stats(profile, stream=output).strip_dirs().sort_stats(sortMethod).print_stats() #Creating a stats printout from the data of our profile and writing it to the output file without directories, and sorted by cumulative time.