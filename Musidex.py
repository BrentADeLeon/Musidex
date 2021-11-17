import webbrowser as wb

#1) Make dictionary Of genres with {num : genre}
genres = {1 : 'lofi',
2 : 'jazz',
3 : 'study',}

#2) Make dictionary of choices for each genre
def lofichoice():

    #Make list of lofi links
    lofilist = ['https://www.youtube.com/watch?v=5qap5aO4i9A', 
    'https://www.youtube.com/watch?v=5yx6BWlEVcY',
    'https://www.youtube.com/watch?v=NVLROzKcgsA']

    #lofi link selection dictionary
    lofi = {
    'lofi1' : lofilist[0],
    'lofi2' : lofilist[1],
    'lofi3' : lofilist[2]}

    #Empty list to append key value names to display to user
    lofikeys = []

    for k in lofi:
        lofikeys.append(k)

    lofimessage = 'Please choose from choices 1 - 3'
    print(lofikeys)
    lofichoose = input(lofimessage + '\n')

    if lofichoose == lofichoose:
        wb.open(lofi['lofi' + lofichoose])

def jazzchoice():

    #Make list of lofi links
    jazzlist = ['https://www.youtube.com/watch?v=3jWRrafhO7M', 
    'https://www.youtube.com/watch?v=bMt81mNhuZA',
    'https://www.youtube.com/watch?v=QN1uygzp56s']

    #lofi link selection dictionary
    jazz = {
    'jazz1' : jazzlist[0],
    'jazz2' : jazzlist[1],
    'jazz3' : jazzlist[2]}

    #Empty list to append key value names to display to user
    jazzkeys = []

    for k in jazz:
        jazzkeys.append(k)

    jazzmessage = 'Please choose from choices 1 - 3'
    print(jazzkeys)
    jazzchoose = input(jazzmessage + '\n')

    if jazzchoose == jazzchoose:
        wb.open(jazz['jazz' + jazzchoose])

def studychoice():

    #Make list of study links
    studylist = ['https://www.youtube.com/watch?v=CfqhWCY7-t4', 
    'https://www.youtube.com/watch?v=Wt_SR4zmmBg',
    'https://www.youtube.com/watch?v=qPbOdQ4UAlU']

    #study link selection dictionary
    study = {
    'study1' : studylist[0],
    'study2' : studylist[1],
    'study3' : studylist[2]}

    #Empty list to append key value names to display to user
    studykeys = []

    for k in study:
        studykeys.append(k)

    studymessage = 'Please choose from choices 1 - 3'
    print(studykeys)
    studychoose = input(studymessage + '\n')

    if studychoose == studychoose:
        wb.open(study['study' + studychoose])   

#3) Make the message/interaction sequence
print('Hello, which genre would you like to hear?')
print(genres)
genre_input = input("Please choose from 1 - 3\n")

#4) If/Elif Statements based on genre choice
if genre_input == str(1):
    lofichoice()
elif genre_input == str(2):
    jazzchoice()
elif genre_input == str(3):
    studychoice()

    

