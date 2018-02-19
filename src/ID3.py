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

	attribute_gain = I(training_data, class_list) - E(A, class_list, D)
	return attribute_gain

def E(A, class_list, D):

	attr_value_list = {}
	for value in range(0, len(D)):
		attr = D[value][0].get(A)
		if attr not in attr_value_list:
			attr_value_list[attr] = 1
		else:
			attr_value_list[attr] += 1


	output = {}
	for val in attr_value_list:
		output[val] = (subSet(A, val, D))


# Sum Loop starts
	total = 0
	for key in attr_value_list:
		total += (attr_value_list[key] / len(D)) * (I(output[key], class_list))
	return total

def subSet(A, val, D):
	td_copy = []

	for i in range(0, len(D)):
		value = D[i][0].get(A)
		if value == val:
			td_copy.append(D[i])
	return td_copy


# Compute the info needed to classify an object
def I(S, class_list):

	for i in class_list:
		class_list[i] = 0
	total = 0
	for i in range(0, len(S)):

		attr = S[i][1]
		class_list[attr] += 1
		total += 1

	output = 0
	for s in class_list.values():
		if s == 0:
			output = 0
		else:
			output += -((s/total) * (math.log((s/total), 2)))

	for i in class_list:
		class_list[i] = 0

	return output




def ID3(D, attribute_list, class_list, class_list2):
	# Create node N

	# If samples are all of the same class, return N as leaf node labeled with class C
	one_class = True
	temp_class = D[0][1]
	for i in range(0, len(D)):
		if D[i][1] != temp_class:
			one_class = False

	if one_class:
		N = temp_class
		return N

	# If attribute_list is empty, return N as leaf node labeled with most common
	# class in the training samples (majority voting)

	highest = 0
	test_class = ""
	for i in class_list2:
		if class_list2[i] > highest:
			highest = class_list2[i]

			test_class = i
	if not attribute_list:
		N = test_class
		print("2 : ", N)
		return N

	# Select test_attribute, the attribute among attribute_list with the highest info gain
	# c1 = True, c2 = False, |c1| = s1 = 9, |c2| = s2 = 5, |S| = s1 + s2 = 14


	info_gains = {}
	for A in attribute_list:
		info_gains[A] = Gain(A, class_list, D)
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


	for val in attr_value_list:
		subset = subSet(test_attribute, val, D)
		if not subset:
			N[1][val] = test_class
		else:
			if test_attribute in attribute_list:
				attribute_list.remove(test_attribute)
			temp = ID3(subset, attribute_list, class_list, class_list2)

			N[1][val] = temp
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

	class_list = {}
	class_list2 = {}
	for label in range(0, len(training_data)):
		if training_data[label][1] not in class_list:
			class_list[(training_data[label][1])] = 0
			class_list2[(training_data[label][1])] = 0
		else:
			class_list[(training_data[label][1])] += 1
			class_list2[(training_data[label][1])] += 1

	# Call to ID3 function
	DT = ID3(training_data, attribute_list, class_list, class_list2)
	print(DT)
	sample = {'level':'Junior', 'lang':'Java', 'tweets':'yes', 'phd':'yes'}
	print(classify(DT, sample))

main()
