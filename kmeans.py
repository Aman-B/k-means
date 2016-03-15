from __future__ import division
#import sys for exceptions
import sys
import math

#class for initializing values provided by user input:

class Create_list:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def get_coord(self):
		return self.x,self.y
		
	def set_x(self,x):
		self.x=x
	
	def set_y(self,y):
		self.y=y	
		
		
	def get_x(self):
		return self.x
	
	def get_y(self):
		return self.y
		
	def set_cluster(self, clusterNumber):
		self.clusterNumber = clusterNumber
    
	def get_cluster(self):
		return self.clusterNumber	
		

def calc_distance(valueX,valueY,centroidX,centroidY):
	# Calculate Euclidean distance.
    return math.sqrt(math.pow((centroidX - valueX), 2) + math.pow((centroidY - valueY), 2))

print "------ This is k means ------"


value_set=[]
centroids=[]
#value_set.append(Create_list(1,1))
#value_set.append(Create_list(1.5,2))
#value_set.append(Create_list(3,4))
#value_set.append(Create_list(5,7))
#value_set.append(Create_list(3.5,5))
#value_set.append(Create_list(4.5,5))
#value_set.append(Create_list(3.5,4.5))

#no_of_pairs=7
no_of_pairs= input(" Enter no of coordinates/pairs : ")

i=0;
while i!=no_of_pairs:
	try:
		values=raw_input("Enter pair  %s : "%(i+1))
		x,y=map(float,values.strip('()').split(','))
		print "x",x
		print "y",y
		value_set.append(Create_list(x,y))
		i=i+1
	except:
		print "Enter values in format like = (x,y)"
			
#print "matrix : ",value_set[0].get_coord()

#print "x :",value_set[0].get_x()

no_of_cluster = input(" Enter no. of clusters to create : ")
 
print " Choosing arbitary intial centroid values.."

for j in range(no_of_cluster):
	centroids.append(Create_list(value_set[j].get_x(),value_set[j].get_y()))
	
	

for k in range(no_of_cluster):
	print " Centroid  ",(k+1)," : ",centroids[k].get_coord()


isShuffling=True;
passes=0
no_of_pass=1

while isShuffling:
#calculating distance of each pair from centroids and putting in clusters
	isShuffling=False
	for num in range(no_of_pairs):
		'''
		Providing arbitarily min_distance as distance from first centroid for comparing.
		And putting it in first cluster, by default.
		'''
		if(no_of_pass==1):
			min_dist= calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[0].get_x(),centroids[0].get_y())
			value_set[num].set_cluster((1))
			print"first pass"
		else:
			print"second pass"
			current_cluster=(value_set[num].get_cluster()-1)
			min_dist= calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[current_cluster].get_x(),centroids[current_cluster].get_y())
			#print "min_dist of : ",value_set[num].get_coord(),"with: ",centroids[current_cluster].get_coord()," is : ",min_dist

		
		for cluster in range(no_of_cluster):
			dist=calc_distance(value_set[num].get_x(),value_set[num].get_y(),centroids[cluster].get_x(),centroids[cluster].get_y())
			#print "dist of : ",value_set[num].get_coord(),"with: ",centroids[cluster].get_coord()," is : ",dist
			if(dist<min_dist):
				#setting cluster number even if it's comparing dist with itself
				#print "value of cluster set : ",cluster
				value_set[num].set_cluster((cluster+1))
				if(centroids[cluster].get_coord()!= value_set[num].get_coord()):
					#print "min dist :",min_dist
					#print "dist of : ",value_set[num].get_coord(),"with: ",centroids[cluster].get_coord()," is : ",dist
					#print "I'm in"
					isShuffling=True
	no_of_pass=no_of_pass+1
				
			
		
	
#print "",value_set[num].get_cluster()		

#printing clusters:

	
	for cluster in range(no_of_cluster):
		centroids[cluster].set_y(0)
		centroids[cluster].set_x(0)
		print " Printing cluster ",(cluster+1)," : "
		num_of_elements=0;
		for num in range(no_of_pairs):
			if((cluster+1)==value_set[num].get_cluster()):
				
				print "  ",value_set[num].get_coord()
				#if(centroids[cluster].get_coord() != value_set[num].get_coord()):
				num_of_elements=num_of_elements+1
				print "num_of_elements :",num_of_elements
				centroids[cluster].set_x(float(centroids[cluster].get_x()+value_set[num].get_x()))
				centroids[cluster].set_y(float(centroids[cluster].get_y()+value_set[num].get_y()))
				#print "mean x: ",((centroids[cluster].get_x()+value_set[num].get_x())/num_of_elements)
				#print "cluster x now :", centroids[cluster].get_x()
				#print "cluster y now: ", centroids[cluster].get_y()
		print " centeroidX: ",centroids[cluster].get_x()
		print "centroidY:",centroids[cluster].get_y()
		
		centroids[cluster].set_x((centroids[cluster].get_x()/num_of_elements))
		centroids[cluster].set_y((centroids[cluster].get_y()/num_of_elements))
		print "Mean of cluster ",(cluster+1)," : ",centroids[cluster].get_coord()
	passes=passes+1
	#if(passes>3):
		#isShuffling=False
		
print "Done."	
