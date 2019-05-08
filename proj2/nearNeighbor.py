import sys
import math
import timeit
import signal

#Nuclear option
class TimeoutException(Exception):
	pass

def timeout_handler(signum, frame):
	raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

def nearest_neighbor(roster, op):
	internal_timer = timeit.default_timer()
	size = len(roster)
	optimal_distance = sys.maxsize
	optimal_route = []
	tick = 0
	tock = 0	
	
	#Initiate a matrix populated with 0 for an n by n grid 
	adjacency_matrix = [[0 for x in range(size)] for y in range(size)]

	#Test case 3 is too large to reasonably resolve, attempting to reduce time spent on it
	if size > 5000:
		tock = 3
		print("Given the size of the current file there will be an attempt to save the most recent minimum path to file given example 3's first path is already sufficiently small.")
	#First for-loop will determine the starting node that the pathing will be based off of
	for i in range(size):
		#Copy of roster for each pass
		#Append the active var to travel_order
		#Remove current var from roster_copy listing for next loop
		travel_order = []
		roster_copy = [ _ for _ in roster]
		travel_order.append(roster_copy[i]['var'])
		roster_copy.remove(roster_copy[i])
		cheapest_path = 0

		#For each city starting with the last
		while len(roster_copy) > 0:
			#While roster_copy isn't empty
			single_city = roster[travel_order[len(travel_order) - 1]]
			minimum_distance = sys.maxsize
			#for each city in relation to the current one selected
			for j in range(len(roster_copy)):
				temp_distance = adjacency_matrix[single_city['var']][roster_copy[j]['var']]
				#Check if it is still set to default valueOB
				if temp_distance == 0:
					loc1 = single_city
					loc2 = roster_copy[j]
					#Get distance between cities
					temp_distance = round(math.hypot(loc2['x'] - loc1['x'], loc2['y'] - loc1['y']))
					
					#Add to matrix to save
					adjacency_matrix[single_city['var']][roster_copy[j]['var']] = temp_distance
					adjacency_matrix[roster_copy[j]['var']][single_city['var']] = temp_distance
				#If first entry
				if minimum_distance > temp_distance:
					minimum_distance = temp_distance
					minimum_city = roster_copy[j]
			#Add minimum route to travel order
			travel_order.append(minimum_city['var'])
			roster_copy.remove(minimum_city)
			#Add to tally
			cheapest_path = cheapest_path + minimum_distance
			
		
		#Take first and last element and bind them together
		first = roster[travel_order[0]]['var']
		last = roster[travel_order[len(travel_order) - 1]]['var']
		temp_distance = adjacency_matrix[first][last]
		#if there isn't a link between them yet manually link them
		if temp_distance == 0:
			fi = roster[travel_order[0]]
			la = roster[travel_order[len(travel_order) - 1]]
			round(temp_distance = math.hypot(la['x'] - fi['x'], la['y'] - fi['y']))
			
			adjacency_matrix[first][last] = temp_distance
			adjacency_matrix[last][first] = temp_distance

		cheapest_path = temp_distance + cheapest_path
	
		#If current path is cheaper than all others found so far make it the minimum	
		if cheapest_path < optimal_distance:
			optimal_distance = int(cheapest_path)
			optimal_route = [ _ for _ in travel_order]					
			print("Current cheapest path: ")
			print(int(cheapest_path))

			#To handle exceptionally long computation times there will be an attempt to save progress after each new minimum is established
			if tock > -1:
				internal_stop = timeit.default_timer()
				internal_time = internal_stop - internal_timer
				output_file = open(op, 'w')
				output_file.write(str(optimal_distance) + '\n')
				size = len(roster)
				for k in range(size):
					output_file.write(str(optimal_route[k]) + '\n')
				output_file.close()
				print("Checkpoint reached at: " + str(internal_time))
	return optimal_distance, optimal_route

#START --->
input_file = sys.argv[1]
roster = []
#signal.signal(signal.SIGALRM, timout_handler)

iFile = open(input_file, 'r')
op = str(input_file + '.tour')
for i in iFile:
	#Split by line and store within a dictionary
	single_city = i.split()
	#Originally called dict() but it turns out that is between 3-6 times slower
	curr_city = {'var': int(single_city[0]), 'x': int(single_city[1]), 'y': int(single_city[2])}
	roster.append(curr_city)
iFile.close()

#Declare variables for receiving from function
tour_distance = 0
tour_route = []

#Start timer and call function
start_timer = timeit.default_timer()
signal.alarm(179)

tour_distance, tour_route = nearest_neighbor(roster, op)


stop_timer = timeit.default_timer()

final_time = stop_timer - start_timer

print("Completed in: " + str(final_time) + "seconds")

op = str(input_file + '.tour')
output_file = open(op, 'w')
output_file.write(str(tour_distance) + '\n')

size = len(roster)
for k in range(size):
	output_file.write(str(tour_route[k]) + '\n')

output_file.close()
