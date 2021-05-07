x = [4, True, 'hello']
x.append('hello')  # adds to the list
x.extend([4, 5, 5, 5, 5])  # adds multiple to list
x.pop()  # removes last element in the list or (specify the index number of the element)
(x[1])  # access the index of an element
x[0] = 'hello'  # lists are mutable
print(len(x))
# A list can store different elements. Order matters.

# tuples are imutable and in ()
# x = (0,0,2,2) cannot be .append or changed.
