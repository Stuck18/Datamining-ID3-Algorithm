# Datamining-ID3-Algorithm
## ID3 implementation as part of CSC 535 Datamining

## Instructions
Implement the ID3 decision tree induction algorithm discussed in class using Python.

## Input
A list of tuples, where each tuple represents a training sample. Each training sample is an (input, class_label) pair, where **input** is a dictionary of the form attribute: value pairs, and each class_label is either True(representing class C1), or False(representing class C2). The following example data is about candidates who interviewed for a job and whether or not the candidate was hired. The attributes represent the candidate's level, preferred programming language, whether the candidate is active on Twitter, and whether the candidate has a PhD:

```python
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
```

## Output
The program will construct and output a decision tree (DT) that is built using the training data. To help decide how to represent a DT for output purposes, we will define a tree to be one of the following:
*True
*False
*A tuple(attribute, subtree_dict)

Where True represents a leaf node that returns True(i.e., class C1 or 'Hire') for any input, False represents a leaf node that returns False(i.e., class C2 or 'Do not Hire') for any input, and a tuple represents a decision node that, for any input, finds its attribute value, and classifies the input using the corresponding subtree(i.e., this is an internal node with test_attribute attribute).

With this representation, the DT(and the output from the program for the above data) would look like:

```python
('level',
    {'Junior': ('phd', {'no': True, 'yes': False})
     'Mid': True,
     'Senior': ('tweets', {'no': False, 'yes': True})
     }
)
```
Note: the corresponding DT is as follows:
![DT Example](/DTExample.PNG)

After building a decision tree, the program should allow us to classify new samples. Add a function, **classify**, that makes as an argument a sample, represented as a dictionary with the attribute:value pairs of the new sample. The function should return the class classification of the new sample. For example the function returns True for the test sample:
```pyhon
{"level" : "Junior","lang" : "Java","tweets" : "yes","phd" : "no"}
```
and False on the sample:
```python
{"level" : "Junior","lang" : "Java","tweets" : "yes","phd" : "no"} 
```

The code should handle unexpected and and missing attribute values. For example, if we encounter a test sample with "level":"Intern", classify to the most common class. The code should be tested on samples with missing or unexpected values, such as:
```python
{"level" : "Intern"} # True
{"level" : "Senior"} # False 
```