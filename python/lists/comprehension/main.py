"""Ins and Outs of Python Lists/Matrices"""


# L = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
# flattened = [item for sublist in L for item in sublist]

# # remove items at indices [1,3,4]
# indices = [1,3,4]
# flattened = [f for i,f in enumerate(flattened)]
# flattened

# # implement extend
# # implement append
# # implement insert
# # implement remove
# # implement map
# # implement reduce
# # implement filter
# # implement len
# # build a nested list
# # any
# # all







import numpy 
num = 5

# Create a 2D Numpy array of shape (5, 0) and convert it to a nested list
MyList = numpy.zeros((num)).tolist()
MyOtherList = MyList[:]

# for item in MyList:
#     MyOtherList.remove(item)
#     print(item in MyOtherList)
#     MyOtherList.append(item)

first_item = MyList[0]
MyOtherList.remove(first_item)
print(first_item in MyOtherList)
print('first_item',  id(first_item))

for item in MyOtherList:
    print('item', id(item))
