#Please create a deletePerson function that deletes any given person from the list and returns a new list without that person.
people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

# with my solution, the function returns the list without the person, but a second call to function returns the original list without both persons  
def deletePerson(person_name):
    new_list = []
    for i in people:
        if i == person_name:
            people.remove(person_name)
            new_list.append(people)

    return new_list

print(deletePerson('ana'))
print(deletePerson('juan'))

# def deletePerson(person_name): # This is the solution from the course
def deletePerson(person, people_list):
    new_list = [p for p in people_list if p != person]
    return new_list

print(deletePerson('ana', people))
print(deletePerson('juan', people))