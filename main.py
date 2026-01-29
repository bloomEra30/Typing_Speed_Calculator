#it helps in measure time
import time

#text for typing test
text = "Python is a versatile and beginner-friendly programming language known for its simple syntax and wide range of applications. I am currently learning Python and using it to build small projects that help me understand core programming concepts like logic building, problem-solving, and basic application development."

#\n -> adds a new line
#input() -> pauses program until user presses Enter

print("TYPING SPEED CALCULATOR")
print('\nType the Following Sentence:\n')
print(text)
print('\nPress Enter when you are ready to type...')
input()


#time.time() returns the present time in seconds
start = time.time()


#takes input from the user
typing = input('\n Start typing from here:\n')


#end time calculation
end = time.time()


#total time taken
time_used = end - start
time_used_per_min = time_used / 60


#split() breaks senetence into words
#len() counts how many words

w_count = len(text.split())


#words per minute
words_per_min = w_count / time_used_per_min



#this variable counts correct character
correct = 0


#loop runs through each character.
#min() helps in removing index error
for i in range(min(len(text), len(typing))):

    #comparing each characters one by one
    if text[i] ==typing[i]:

        #if characters match -> increase count
        correct +=1


#formula of accuracy

accuracy = (correct / len(text)) * 100


#round(value, 2) -> show the number up to 2 digits after the decimal point
#f-string used to insert values inside text
print('\n-----OUTPUT------')
print(f'Time Taken by you: {round(time_used, 2)} seconds')
print(f'Your Typing Speed: {round(words_per_min, 2)} WPM')
print(f'Accuracy : {round(accuracy, 2)} %')


