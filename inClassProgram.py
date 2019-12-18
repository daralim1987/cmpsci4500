#Course: cs4500-002
#Data: 10/03/19
#Assignment: In class group programming challenge
#Group member name: Jacob Potter, Alton Maiocco, Dara Lim, Ashley Simmons, Brandon Sharp, Brian Hamil, Ingram Tolish

#Assignment Description: The program is to count the words in a text file. Program prompt the user
#for the name of the textfile. If the textfile not exist, program display the error message and reprompt.
#After the file is opened successfully, the program creates a list of word (converted to lowercase) that read from the file and the
#list is in alphabetical order and each word followed by a blank and the number of times the word occurs in
#the file and output to an external file named WordCounts.txt. If the output file already exists, the
#program overwrite the old file; if the file does not already exist, a new file is created. The program
#display the bar graph to the screen showing the frequency of the 20 most appearing words as addition.

#External Libraries, modules that import to this program are: numpy and matplotlib.

#To install matplotlib, type this command:  python -m pip install -U matplotlib
#To install numpy, type this command: python -m pip install numpy

import os.path
import operator
import matplotlib.pyplot as plt
import numpy as np
#Ask interactive user to enter file name untill the entered file is exist in the system
while True:
    file_name = input("Enter file name\n")
    if os.path.exists(file_name):
        break
    else:
        print("The file is not exist")
        continue

#Open and read the file
file_objct = open(file_name, "r")
text_string = file_objct.read().lower()

#break the string into a list
list_of_string = text_string.split()

#create empty list
unique_str = []

#loop the list of string
for i in list_of_string:
    #check for the duplicate word
    if i not in unique_str:
        unique_str.append(i)

#sort the string alphabetically
sorted_word = sorted(unique_str)

#open file to write to
dict = {}
lst_t = []
f_out = open("WordCounts.txt", "w")
for i in range(0, len(sorted_word)):
    words = sorted_word[i]
    freq = list_of_string.count(sorted_word[i])
    f_out.write('{0} {1}\n'.format(words, freq))
#    dict.update({words : freq})
    lst_t.append((words, freq))

#sort the list of turple by the second element
sorted_by_second = sorted(lst_t, key = lambda tup: tup[1])

#take the most 20 frequency
lst_m_f = []
l = len(sorted_by_second) - 1
while l > 20:
    lst_m_f.append(sorted_by_second[l])
    l -= 1
#separate the word and its frequency into two different lists
lst_freq = []
word_str = []

for i in lst_m_f:
    word_str.append(i[0])
    lst_freq.append(i[1])

#create a bar graph using matplotlib and numpy modules
index = np.arange(len(word_str))
plt.bar(index, lst_freq)
plt.title("Bar Graph")
plt.xlabel("word", fontsize = 5)
plt.ylabel("Frequency", fontsize = 5)
plt.xticks(index, word_str, fontsize = 5, rotation = 30)
plt.show()
