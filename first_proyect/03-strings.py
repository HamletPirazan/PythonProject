course3 = '''  
    Hi Hamlet,
    you are invited to the party

'''
course = "Python's course for beginners"
course2 = 'Python course for "beginners"'



print(course[0:-1])


print(course2)
print(course3)
print(course[-1])
print(course[-1:-5]) # No se puede, it will not return from s to the -5

another = course[:]

course = "I am a new course"

print(another + " im am another")