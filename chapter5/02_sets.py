# Set is collection of non repetitive elements.
# Sets are unordered => Element's order doesn't matter
# Sets are unindexed => Cannot access elements by index
# There is no way to change items in sets.
# Sets cannot contain duplicate values.


# s = set() # Empty set created (Neber use d = {} It will    create empty dictionary)
# s = {1,5,5,5,4,4,6,54,32} # It will print 5 & 4 only one time because repetition is not allowed in sets
# print(s)

# Methods of sets

s = {1,8,2,3,"Patu"} # This is valid
s2 = {1,8,1,78}
s.add(566)
print(s,type(s))

# Properties 
# print(len(s)) # returns length
# print(s.pop()) # Removes an arbitrary element from the set and retuen the element removed.
# print(s.remove(8)) # Updates the set s and removes 5 from s
# print(s.clear()) # It empties the set s
# print(s.union({8,11})) # Returns a new set with all items from both sets {1,8,2,3,11}
print(s.intersection(s2)) # Return a set which contains only item in both sets {8}
print(s.difference(s2))
