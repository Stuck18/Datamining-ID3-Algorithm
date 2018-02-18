'''
Seth Tucker
2/9/2018
'''

from collections import Counter
import math
import copy

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

def Gain(A, class_list, D):
	'''
	info = I(S, s1, s2)
	entropy = E(A, S, s1, s2)
	info = info - entropy
	return info
	'''
	attribute_gain = I(training_data, class_list) - E(A, class_list, D)
	return attribute_gain

def E(A, class_list, D):
	'''
	attr_list = []
	total = 0

	for attr in range(0, len(training_data)):
		val = training_data[attr][0].get(A)
	'''
	#print("Class list from E: ", class_list)
	attr_value_list = {}
	for value in range(0, len(D)):
		attr = D[value][0].get(A)
		if attr not in attr_value_list:
			attr_value_list[attr] = 1
		else:
			attr_value_list[attr] += 1
	#print(attr_value_list)

	output = {}
	for val in attr_value_list:
		output[val] = (subSet(A, val, D))
		#print("\n----------------")
	# for i in output:
	# 	print(i)
	# 	print("\n----------------")
	# 	print(output[i])
	# 	print("\n-----------------------------------")

# Sum Loop starts
	total = 0
	for key in attr_value_list:
		#print("Output key: ", output[key], "\nClass list: ", class_list)
		total += (attr_value_list[key] / len(D)) * (I(output[key], class_list))
	#print("Total from E: ", total, "\n")
	#I(S, attr_value_list)
	return total

def subSet(A, val, D):
	td_copy = []

	for i in range(0, len(D)):
		value = D[i][0].get(A)
		#print(value)
		if value == val:
			td_copy.append(D[i])
	return td_copy


# Compute the info needed to classify an object
def I(S, class_list):
	'''
	info = -(((s1/S) * math.log((s1/S), 2)) + ((s2/S) * math.log((s2/S), 2)))
	return info
	'''
	for i in class_list:
		class_list[i] = 0
	total = 0
	for i in range(0, len(S)):

		attr = S[i][1]
		class_list[attr] += 1
		total += 1

	#print("From I: " ,class_list, "\n")

	output = 0
	for s in class_list.values():
		#print("This is S: ", s, "\nThis is total: ", total)
		if s == 0:
			output = 0
		else:
			output += -((s/total) * (math.log((s/total), 2)))
	#print("Ouput from I: " ,output, "\n")

	for i in class_list:
		class_list[i] = 0

	return output




def ID3(D, attribute_list, class_list, class_list2):
	# Create node N
	#N = ""

	# If samples are all of the same class, return N as leaf node labeled with class C
	one_class = True
	temp_class = D[0][1]
	for i in range(0, len(D)):
		if D[i][1] != temp_class:
			one_class = False

	if one_class:
		N = temp_class
		print("1 : ", N)
		return N

	# If attribute_list is empty, return N as leaf node labeled with most common
	# class in the training samples (majority voting)
	# if not attribute_list:
	# 	label_list = []
	# 	for elem in range(0, len(training_data)):
	# 		print(training_data[elem][1])
	# 		label_list.append(training_data[elem][1])
	# 	most_common_label = Counter(label_list).most_common()
	# 	N = most_common_label
	# 	return N

	highest = 0
	test_class = ""
	for i in class_list2:
		if class_list2[i] > highest:
			highest = class_list2[i]
			#print(i)
			test_class = i
	#print("Class List: ", class_list2)
	#print("Test Class: ", test_class)
	print("Attribute list: ", attribute_list)
	if not attribute_list:
		N = test_class
		print("2 : ", N)
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
	info_gains = {}
	for A in attribute_list:
		info_gains[A] = Gain(A, class_list, D)
	print("Info gains: ", info_gains)
	highest = 0
	test_attribute = ''
	for val in info_gains:
		if info_gains[val] > highest:
			highest = info_gains[val]
			test_attribute = val


	N = (test_attribute, {})

	attr_value_list = {}
	for value in range(0, len(training_data)):
		attr = training_data[value][0].get(test_attribute)
		if attr not in attr_value_list:
			attr_value_list[attr] = 1
		else:
			attr_value_list[attr] += 1

	#print('---------------------------\n Test Attribute: ', test_attribute)
	for val in attr_value_list:
		subset = subSet(test_attribute, val, D)
		#print("Subset: ", subset, "\n Value: " , val)
		if not subset:

			N[1][val] = test_class
			print("3 : ", N)
		else:
			#print("Test attr: ", test_attribute, "\n Attr list: ", attribute_list)
			if test_attribute in attribute_list:
				attribute_list.remove(test_attribute)
			#else:
				#return N
				#N[1][val] = test_class
			#temp_attr_list = attribute_list
			temp = ID3(subset, attribute_list, class_list, class_list2)
			#print("TEMP :", temp)

			N[1][val] = temp #ID3(subset, temp_attr_list, class_list)
			print("4 : ", N)

	#print("Info from gain: ", info_gains)

	#ID3(D, attribute_list, class_list)
	return N

def classify(DT, sample):
	if type(DT) != tuple:
		return DT
	output = classify(DT[1][sample[DT[0]]], sample)
	return output

def main():
	# List of training data attributes
	attribute_list = []
	temp = training_data[0][0]
	for elem in temp:
		attribute_list.append(elem)
	#print(attribute_list)

	class_list = {}
	class_list2 = {}
	for label in range(0, len(training_data)):
		if training_data[label][1] not in class_list:
			class_list[(training_data[label][1])] = 0
			class_list2[(training_data[label][1])] = 0
		else:
			class_list[(training_data[label][1])] += 1
			class_list2[(training_data[label][1])] += 1
	#print(class_list)

	# Call to ID3 function
	DT = ID3(training_data, attribute_list, class_list, class_list2)
	sample = {'level':'Junior', 'lang':'Java', 'tweets':'yes', 'phd':'yes'}
	print(classify(DT, sample))

main()
