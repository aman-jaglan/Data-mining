#%%
print("Hello world!")


#%%
# Question 1: Create a Markdown cell with the following:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.

#%%
#About Myself
#
#I'm Aman, and while my name means "peace," I'm more of an enthusiast than a calm person. 
#I studied Information Technology at Maharaja Agrasen Institute of Technology. During my studies 
#I wrote two research papers—one on Intrusion Detection Systems and another on searching for relevant text using Python and machine learning.
#
#I started my career at Protiviti as a Software Engineer, where I worked on tasks like cleaning and processing data. 
#Now, I'm working towards becoming a data scientist, excited about the opportunities in this field. 
#I look forward to the journey ahead and appreciate your consideration of my background and goals.
#
#I love sports, whenever I get bore or have free time I always prefer this website https://www.espn.com. It's really have all the details regarding every sports.
# They run the matches all day long and keeps you updated for the upcoming games.


#%%
# Question 2: Create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

classes = ['Intro to data science','Intro to data mining', 'Intro to data warehousing', 'Machine learning 1', 'Machine learning 2', 'Deep learning']
print(classes[5])


#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in Python here.

classes[1] = 'Intro to coal mining'
print(classes)


#%%
# Question 4: Before you go see your academic advisor, you are 
# asked to create a Python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

subjectDict = {
    6101 : "Intro to data science",
    6102 : "Data warehousing",
    6103 : "Intro to data mining"  
}

print(subjectDict[6101])

#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.

for key in subjectDict:
    print(key)

#%%
# Question 6: Using loops 
# Goal: print out the list of days (31) in Jan 2023 like this
# Sun - 2023/1/1
# Mon - 2023/1/2
# Tue - 2023/1/3
# Wed - 2023/1/4
# Thu - 2023/1/5
# Fri - 2023/1/6
# Sat - 2023/1/7
# Sun - 2023/1/8
# Mon - 2023/1/9
# ...
# You might find something like this useful, especially if you use the remainder property x % 7
dayofweektuple = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
date = 1
day = 0
for i in range(31):
    if(day > 6):
        day = 0
    print(dayofweektuple[day],"-","2023/1/"+str(date))
    day+=1
    date+=1


# %%[markdown]
# # Additional Exercise: 
# Choose three of the five exercises below to complete.
#%%
# =================================================================
# Class_Ex1: 
# Write Python codes that converts seconds, say 257364 seconds,  to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------

x = 257364
hour = x//(60*60)
min = (x%(60*60))//60
sec = (x%(60*60))%60

print(hour,"Hour,",min,"min,",sec,"seconds")





#%%
# =================================================================
# Class_Ex2: 
# Write a Python code to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# Hint: one way is to create three nested loops.
# ----------------------------------------------------------------

letters = 'ABC'

for x in letters:
    for y in letters:
        for z in letters:
            if (x != y) and (y!= z) and (x != z):
                permutation = x + y + z
                print(permutation)

   





#%%
# =================================================================
# Class_Ex3: 
# Write a Python code to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------

from itertools import permutations
str = 'ABCD'
for x in permutations(str):
    print(''.join(x))






#%%
# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user, like this, for a height of 5:
#      *
#     ***
#    *****
#   *******
#  *********
# ----------------------------------------------------------------





#%%
# =================================================================
# Class_Ex5: 
# Write Python codes to print prime numbers up to a specified 
# values, say up to 200.
# ----------------------------------------------------------------






# =================================================================