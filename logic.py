import random

class Logic:    
    userInGame = False

    def newGame():
        Logic.userInGame = True

    def inGame():
        return Logic.userInGame
    
    def endGame():
        Logic.userInGame = False
        return Logic.userInGame

    def setPositions(word_bank):
        pos = dict.fromkeys(range(16)) #Positions of the words
        used = set() #Used to see if a random number has already been used

        found = True
        finish = True
        #Creates the gameboard 
        for key, value in pos.items():
            found = True
            while found and finish: #loops until the key is assigned a word
                if value is None:
                    r = random.randint(0, 15)
                if r not in used:
                    pos[key] = word_bank[r]
                    used.add(r)
                    found = False
                    if (key == 16): #once all words are given a key, end
                        finish = False

        #gameBoard = ('``` ' + pos[0] + ' ' + pos[1] + ' ' + pos[2] + '' + pos[3] + '\n ' + pos[4] + ' ' + pos[5] + ' ' + pos[6] + ' ' + pos[7] + '\n '  + pos[8] + ' ' + pos[9] + ' ' + pos[10] + ' ' + pos[11] + '\n ' + pos[12] + ' ' + pos[13] + ' ' + pos[14] + ' ' + pos[15] + '```')

        top = ('``` ' + pos[0] + ' ' + pos[1] + ' ' + pos[2] + ' ' + pos[3] + '```')
        mid1 = ('``` ' + pos[4] + ' ' + pos[5] + ' ' + pos[6] + ' ' + pos[7] + '```')
        mid2 = ('``` ' + pos[8] + ' ' + pos[9] + ' ' + pos[10] + ' ' + pos[11] + '```')
        bot = ('``` ' + pos[12] + ' ' + pos[13] + ' ' + pos[14] + ' ' + pos[15] + '```')

        return top, mid1, mid2, bot
    
    def checkAnswer(userInput, word_bank): 
        
        #splits the answer into multiple arrays
        userInput = userInput.split()
        print(userInput)

        #categories
        cat1 = word_bank[0:4]
        cat2 = word_bank[4:8]
        cat3 = word_bank[8:12]
        cat4 = word_bank[12:16]
        print(cat4)

        try:

            if (set(userInput) == set(cat1)):
                return True, 0 #returns True and the position for completed words
            elif (set(userInput) == set(cat2)):
                return True, 1
            elif (set(userInput) == set(cat3)):
                return True, 2
            elif (set(userInput) == set(cat4)):
                return True, 3
            else:
                return False, -1

        except:
            return False, -1
        
   # def newBoard(answer):
    #make new gameboard with smaller array


                
                

