import sys

class Person:
    id = 0,
    lastName = '',
    firstName = '',
    address = '',
    phone = '',
    email = ''

# Define a main() function 
def main():
    # initialize
    people = {}
    newPerson = Person()
    
    # populate dictionary with 3 people
    newPerson.id = 1
    newPerson.lastName = 'Smith'
    newPerson.firstName = 'John'
    newPerson.address = '1 Main Street, NY, NY'
    newPerson.phone = '(212) 555-1111'
    newPerson.email = 'jsmith@yahoo.com'
    print(newPerson.lastName)    #  works
    people[1] = newPerson
    print(people[1].lastName)    #  error

    newPerson.lastName = 'Jones'
    newPerson.firstName = 'Robert'
    newPerson.address = '2 Main Street, NY, NY'
    newPerson.phone = '(212) 555-2222'
    newPerson.email = 'rjones@yahoo.com'    
    people[2] = [2, newPerson]
    
    newPerson.lastName = 'Williams'
    newPerson.firstName = 'Emma'
    newPerson.address = '3 Main Street, NY, NY'
    newPerson.phone = '(212) 555-3333'
    newPerson.email = 'ewilliams@yahoo.com'    
    people[3] = [3, newPerson]
   
    newPerson.lastName = 'Brown'
    newPerson.firstName = 'Mia'
    newPerson.address = '4 Main Street, NY, NY'
    newPerson.phone = '(212) 555-4444'
    newPerson.email = 'mbrown@yahoo.com'    
    people[4] = [4, newPerson]
    
    for key, value in people.items():
        print('key=', key, 'Value=', value)
        
    for my_var in people:
        print(my_var, 'corresponds to', people[my_var])
        
# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
