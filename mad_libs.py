import numpy as np

def madlib1():
    print("Mad Lib 1:")
    name = input("Enter a noun:")
    adj = input("Enter an adjective:")
    noun = input("Enter a noun:")
    print("Please excuse " + name + " who is far too " + adj + " to attend " + noun + " class.")

def madlib2():
    print("Mad Lib 2:")
    name = input("Enter a name:")
    body_part = input("Enter a part of the body:")
    fluid = input("Enter a type of fluid:")
    substance = input("Enter a type of substance:")
    print (name + " is sick with the " + body_part + " flu. Drink more "  + fluid + " and take " + substance
                + " as needed.")
def madlib3():
    print("Mad Lib 3:")
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    noun = input("Enter a noun: ")
    print(name + " is authorized to be at " + place + " instead of " + noun + " class.")

def madlib4():
    print("Mad Lib 4:")
    name = input("Enter a name: ")
    noun = input("Enter a noun: ")
    event = input("Enter an event: ")
    print(name + " is too cool for " + noun + " class. Instead, he will  be attending " + event)

def madlib5():
    print("Mad Lib 5:")
    adj = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    adj2 = input("Eneter an adjective: ")   
    print("Every " + adj + " spy  needs a pair of X-ray " + noun + ", an invisible " + noun + ", and a spy phone equipped with"
                                                                                   "the most " + adj2 + " features")
def madlib6():
    print("Mad Lib 6:")
    adj = input("Enter an adjective: ")
    nationality = input("Enter a nationality: ")
    person = input("Enter the name of a person: ")
    print("Pizza was invented by a " + adj + " " + nationality + " named " + person)
   
def madlib7():
    print("Mad Lib 7:")
    company = input("Enter a company name: ")
    product = input("Enter a product: ")
    group = input("Enter the name of a group: ")
    problem = input("Enter a problem: ")
    print("My company, " + company + ", is developing " + product + " to help " + group + " with " + problem)

def madlib8():  
    print("Mad Lib 8:")  
    name = input("Enter a name: ")
    verb_pt = input("Enter a past-tense verb: ")
    family_member = input("Enter a family member: ")
    verb = input("Enter a verb:")
    print("You! My name is " + name + ", you " + verb_pt + " my " + family_member + " prepare to " + verb)
 
def madlib9():  
    print("Mad Lib 9:") 
    family_member = input("Enter a family member: ")
    noun = input("Enter a noun: ")
    adj = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    print("Yesterday, my " + family_member + " and I went to the " + noun + " park. There we saw a " + adj + " " + noun2
        + " on a bike")
    
def madlib10():
    print("Mad Lib 10:")
    noun = input("Enter a noun: ")
    girls_name = input("Enter a girl's name: ")
    adj = input("Enter an adjective: ")
    adj2 = input("Enter an adjective: ")
    print("There was once a young " + noun + " named Cinderella, well actually her name was " + girls_name + " but her "
            + adj + " stepsisters called her that because she was " + adj2)
            
def random():#defines a random number from 1 to 10, runs the corresponding mad lib
    i = 0
    while(i < 10):
        rNum = int(np.random.randint(1,10))
        
        if(rNum == 1):
            madlib1()       
        if(rNum == 2):
            madlib2()
        if(rNum == 3):
            madlib3()
        if(rNum == 4):
            madlib4()
        if(rNum == 5):
            madlib5()
        if(rNum == 6):
            madlib6()
        if(rNum == 7):
            madlib7()
        if(rNum == 8):
            madlib8()
        if(rNum == 9):
            madlib9()
        if(rNum == 10):
            madlib10()
        i = i + 1
    
ran = int(input("Would you like a random order of mad libs(Enter 1 or 2)?\n1.Yes\n2.No\n"))

if(ran == 1):
    random()
else:
    madlib1()
    madlib2()
    madlib3()
    madlib4()
    madlib5()
    madlib6()
    madlib7()
    madlib8()
    madlib9()
    madlib10()