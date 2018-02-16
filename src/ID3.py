'''
Seth Tucker
2/9/2018
'''

from collections import Counter
import math

training_data = [
	({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'no'}, False),
	({'level':'Senior', 'lang':'Java', 'tweets':'no', 'phd':'yes'}, False),
	({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
	({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, True),
	({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
	({'level':'Junior', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, False),
	({'level':'Mid', 'lang':'R', 'tweets':'yes', 'phd':'yes'}, True),
	({'level':'Senior', 'lang':'Python', 'tweets':'no', 'phd':'no'}, False),
	({'level':'Senior', 'lang':'R', 'tweets':'yes', 'phd':'no'}, True),
	({'level':'Junior', 'lang':'Python', 'tweets':'yes', 'phd':'no'}, True),
	({'level':'Senior', 'lang':'Python', 'tweets':'yes', 'phd':'yes'}, True),
	({'level':'Mid', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, True),
	({'level':'Mid', 'lang':'Java', 'tweets':'yes', 'phd':'no'}, True),
	({'level':'Junior', 'lang':'Python', 'tweets':'no', 'phd':'yes'}, False)
] 

def Gain(S, A, class_list):
	'''
	info = I(S, s1, s2)
	entropy = E(A, S, s1, s2)
	info = info - entropy
	return info
	'''
	attribute_gain = I(S, class_list) - E(S, A)
	return attribute_gain

def E(S, A):
	'''
	attr_list = []
	total = 0
	
	for attr in range(0, len(training_data)):
		val = training_data[attr][0].get(A)
	'''
	attr_value_list = {}
	for value in range(0, len(training_data)):
		attr = training_data[value][0].get(A)
		if attr not in attr_value_list:
			attr_value_list[attr] = 1
		else:
			attr_value_list[attr] += 1
	print(attr_value_list)
	I(S, attr_value_list)
		
# Compute the info needed to classify an object
def I(S, class_list):
	'''
	info = -(((s1/S) * math.log((s1/S), 2)) + ((s2/S) * math.log((s2/S), 2)))
	return info
	'''
	total = 0;
	for s in class_list.values():
		#print(s)
		total += -(((s/S) * math.log((s/S), 2)))
	print(total)
	return total
	
		

def ID3(attribute_list, class_list):
	# Create node N
	N = ''
	
	# If samples are all of the same class, return N as leaf node labeled with class C
	if len(class_list) == 1:
		N = class_list[0]
		return N
	
	# If attribute_list is empty, return N as leaf node labeled with most common
	# class in the training samples (majority voting)
	if not attribute_list:
		label_list = []
		for elem in range(0, len(training_data)):
			print(training_data[elem][1])
			label_list.append(training_data[elem][1])
		most_common_label = Counter(label_list).most_common()					
		N = most_common_label
		return N
	
	# Select test_attribute, the attribute among attribute_list with the highest info gain
	# c1 = True, c2 = False, |c1| = s1 = 9, |c2| = s2 = 5, |S| = s1 + s2 = 14
	'''
	for elem in range(0, len(training_data)):
		if training_data[elem][1] == c1: # True "Hired"
			s1 += 1
		elif training_data[elem][1] == c2: # False "Don't hire"
			s2 += 1
	S = s1 + s2
	
	gain(S, A, s1, s2)
	'''
	S = len(training_data)
	info_gains = []
	for A in attribute_list:
		info_gains.append(Gain(S, A, class_list))


def main():	
	# List of training data attributes
	attribute_list = []
	temp = training_data[0][0]
	for elem in temp:
		attribute_list.append(elem)
	#print(attribute_list)
		
	class_list = {}
	for label in range(0, len(training_data)):
		if training_data[label][1] not in class_list:
			class_list[(training_data[label][1])] = 1
		else:
			class_list[(training_data[label][1])] += 1
	#print(class_list)
	
	# Call to ID3 function
	ID3(attribute_list, class_list)
	
main()