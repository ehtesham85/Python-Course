# list, tuple, set, dict
# List Datatype and its operation
my_list=[5,10,13,20,15,25,30,25]
print(type(my_list))
my_list.append(35)                         #add element at the end of list
my_list.insert(4,12)        #add element at which index you want
my_list.pop(5)                             #delete index value
print(my_list.count(25))                   #count number of time element come
my_list.sort()                             #sort list ascending order wise
# my_list.sort(reverse=True)               #sort list descending order wise
# my_list.sort(reverse=False)              #sort list ascending order wise
print(my_list)                             #simply print list



# Set Datatype and its operation
setA={1,3,5,7,9}
setB={2,4,6,8,10}
setC={1,2,3,4,5,6,7,8,9,10}

# print(type(setA))                        #print type set

union=setA.union(setB)                     #add elements of both sets
inter=setA.intersection(setC)              #select common elements of sets
diff=setB.difference(setA)
subset=setA.issubset(setC)
superset=setC.issuperset(setA)
disjoint=setC.isdisjoint(setB)
print("Union Operation: ",union)
print("Intersection Operation: ",inter)
print("Difference Operation: ",diff)
print("Subset Operation: ",subset)
print("Superset Operation: ",superset)
print("Disjoint Operation: ",disjoint)


