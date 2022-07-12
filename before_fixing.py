# -*- coding: utf-8 -*-
"""
Author: Alexandr Terestschuk
Datum: 30.09.2021
Zweck der Datei: Programmierprojekt 2021
"""
# to exit the program any time
import sys



#####################

while True:

    
   


    print("— POTSDAM HBF —")
    print("You are at Potsdam Hbf heading to Golm’s library to borrow that book you need for your exam. Hurry up, the next train will depart soon!")
    
    answer = input("Do you want to take the train? (yes/no)").lower().strip()
    
    if answer == "yes":
        
        answer = input("Hey, you should not board the train without a valid ticket! Go buy the ticket first. (inspect bag)").lower().strip()
        
        if answer == 'exit':
            sys.exit() 
    
        
        
        if answer != "inspect bag" :
            print("you should inspect your bag!")
        
        else:
            print("You have 20 euros.") 
            
            
            answer = input("Do you want to get to Golm? (yes/no)").lower().strip()
            
            if answer == 'exit':
                sys.exit() 
            
            if answer != "yes":
                
                print("Unfortunately you can't reach your goal like this.")
                
            
            else:
                print("You cannot do it here!")
                
                answer = input("Do you want to buy a ticket to Golm? (yes/no)").lower().strip()
                
                if answer == 'exit':
                    sys.exit() 
                
                if answer != "yes":
                    
                        print("You have to buy a ticket.")
                        
                
    
                else:          
                        print("")
                        print("— TICKET MACHINE —")
                        print("")
                        
                        import nltk
                        #nltk.download('averaged_perceptron_tagger')
                        from nltk.corpus import gutenberg
                        
                        text = gutenberg.raw('carroll-alice.txt')
                        
                        a_list = nltk.sent_tokenize(text)
                        
                        #random sentences
                           
                        import random
                        words1 = random.choice(a_list )   
                        print('{',words1,'}')
                        #words1 have to be shown
                        print("")
                        ####################
                        
                        #indexing words in POS token
                        from nltk.tokenize import word_tokenize
                        text = word_tokenize(words1)
                        nltk.pos_tag(text)
                        #print(text)
                        
                        #POS doesn't have to be shown
                        
                        ###########################                                                      		
                        item = random.choice(text)						
                        my_text = words1.replace(item, "xxxx")			
                        print(my_text)
                        
                        ####################
                        #guess the correct word
                        
                        attempt = 0
                        attempt_2 = 0
                        
                        #record time
                        
                        import time
                        start = time.time()
    
                        question = input("Welcome! A two-way ticket to Golm costs 5 euros. To buy it, you need to guess the secret word from 'xxxx':").lower().strip()
                        question == item
    
    
                        while question != item and question != "####" and attempt <= 2:
                            question = input('Guess the secret word again: ')
                            attempt = attempt + 1
        
                            if attempt == 2 and question != item:
                                print("")
                                print("You have already used three attempts. A new word must be guessed. The secret word was: ", item)
                                
                                ####################################
                                
                                text = gutenberg.raw('carroll-alice.txt')
                                
                                a_list = nltk.sent_tokenize(text)
                                
                                #random sentences
                                   
                                
                                words1 = random.choice(a_list )   
                                print('{',words1,'}')
                                #words1 have to be shown
                                print("")
                                ####################
                                
                                #indexing words in POS token
                                
                                text = word_tokenize(words1)
                                nltk.pos_tag(text)
                                #print(text)
                                
                                #POS doesn't have to be shown
                                
                                ###########################                                                      		
                                item = random.choice(text)						
                                my_text = words1.replace(item, "xxxx")			
                                print(my_text)
                                
                                ####################
                                #guess the correct word
                                
                                attempt = 0
                                attempt_2 = 0
                                
                                #record time
                                
                                
                                start = time.time()
                                
                                
                                #####################
                                
                                question = input("yes secret word:").lower().strip()
                                question == item
                                
                                while question != item and question != "####" and attempt_2 <= 2:
                                    question = input('Guess the secret word again: ')
                                    attempt_2 = attempt_2 + 1
                                    
                                    if attempt == 2 and question != item:
                                        print("")
                                        print("You have already used three attempts. A new word must be guessed. The secret word was: ", item)
                                        
                                        break
                                                                                               
                                #######################
                                                          
                                end = time.time()
                                print(end - start, "don't show it to a user")
                                whole_time = end - start
                                
                                #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                              
                                break    
        
                        if question == item:
                            print("")
                            print("Correct answer! Get your ticket and hurry up, the train is about to leave! ")
                            
                        elif question == "####":
                            print("")
                            print("You choosed not to guess the secret word.")  
                            
                        end = time.time()
                        print(end - start, "don't show it to a user")
                        whole_time = end - start
                        
                       
                            
                        answer = input("Do you want to inspect you bag after the game? (yes/no)").lower().strip()
                        
                        if answer == 'exit':
                            sys.exit() 
    
                        if answer == "yes":
        
                            answer = input("Enter: (inspect bag)").lower().strip()
                            
                            if answer == 'exit':
                                sys.exit() 
                            
                       
                            if answer != "inspect bag":
                                print("You should inspect your bag!")
                                
                            
                            else:
                                print("You have 15 euros and one train ticket.") 
                                
                                
                                
                                
                                answer = input("Do you want to get the train? (yes/no)").lower().strip()
                                
                                if answer == 'exit':
                                    sys.exit() 
    
                                if answer == "yes":
        
                                    answer = input("Enter 'get to golm:' ").lower().strip()
                                    
                               
        
                                    if answer != "get to golm":
                                        print("You have to go to Golm to borrow that book you need for your exam.")
                                        
                                  
                                        
                                    elif answer == "get to golm":
                                 
                                        if whole_time < 120:
                                            print("")
                                            print("— FIRST TRAIN — ")
                                            print("")
                                            print("Great, you made it to the first train. You find a window seat and start listening to your favourite band. What do you want to do? ")
                                            
                                            answer = input("Enter 'get to golm:' ").lower().strip()
                                            
                                            if answer == 'exit':
                                                sys.exit() 
                                            
                                        
        
                                            if answer != "get to golm":
                                                print("You have to go to Golm to borrow that book you need for your exam.")
                                                
                                           
            
                                            elif answer == "get to golm":
                                            
                                                #Percentage chance to make action
                                                import random
            
                                                if random.randint(0,100) < 40:
                                                    print("")
                                                    print("You come directly to Golm.")
            
                                                else:
                                                    print("")
                                                    print("This is not a direct route to Golm.")
                
                                                    if random.randint(0,100) < 60:
                                                        print("")
                                                        print("Your ticket was checked.")
                                                        print("")
                    
                                                        if random.randint(0,100) < 50:
                                                            invalid = "Your ticket is invalid, therefore a fee of 15 euros will be charged."
                                                            print(invalid)
                                                            print("")
                                                                                                  
                                                        else:
                                                            print("Your ticket is valid.")
                                                            print("")
                                                                         
                                                    else:
                                                        print("")
                                                        print("Your ticket wasn't checked.")
    
                                        elif whole_time >= 120:
                                            print("")
                                            print("— SECOND TRAIN — ")
                                            print("")
                                            print("Great, you made it to the second train. You find a window seat and start listening to your favourite band. What do you want to do? ")
                                            
                                            
                                            ###################################
                                            
                                            
                                        from nltk.corpus import wordnet as wn
    
    
    
                                        noun = random.choice(open('C:/Users/User/OneDrive/Рабочий стол/animals.csv').read().split()).strip()
                                            
                                        print("")
                                        print("don't show it to a user':", noun)
                                        print("")
                                                                                
                                        definition = wn.synset(noun + '.n.01').definition()
                                        print(definition)
                                            
                                            
                                        # 3 attempts
                                                                                
                                        attempt = 0
                                        attempt_2 = 0
    
    
    
                                        question = input("To borrow the book, you need to guess the secret animal from the sentence above:").lower().strip()
                                        question == noun
                                                                                
                                            
                                        while question != noun and question != "####" and attempt <= 2:
                                            question = input('Guess the secret word again: ')
                                            attempt = attempt + 1
                                                
                                            if attempt == 2 and question != noun:
                                                print("")
                                                print("You have already used three attempts. A new word must be guessed. The secret anymal was: ", noun)
                                                                                            
                                                    
                                                noun = random.choice(open('C:/Users/User/OneDrive/Рабочий стол/animals.csv').read().split()).strip()
                                                                                        
                                                print("")
                                                print("don't show it to a user':", noun)
                                                print("")
                                                                                        
                                                definition = wn.synset(noun + '.n.01').definition()
                                                print(definition)
                                                        
                                                    
                                                while question != noun and question != "####" and attempt_2 <= 2:
                                                    question = input('Guess the secret word again: ')          
                                                    attempt_2 = attempt_2 + 1
                                                                                                    
                                                                                                
                                                if attempt_2 == 2 and question != noun:
                                                    print("")
                                                    print("You have already used three attempts. A new word must be guessed. The secret anymal was: ", noun)
                                                                                                    
                                                    break
                                                                                        
                                                
                                        if question == noun:
                                            print("")
                                            print("Correct answer! You finally got the book! ")
                                                                                        
                                        elif question == "####":
                                            print("")
                                            print("You choosed not to guess the secret word.")
                                            
                                            
                                            
                                        answer = input("Enter 'inspect bag' for the next step: ").lower().strip()
                                        
                                        if answer == 'exit':
                                            sys.exit() 
        
                                        if answer != "inspect bag":
                                            print("you should inspect your bag!")
                                                
                                        elif answer == "inspect bag":
                                          
                     
                                                           
                                            try:
                                                invalid
                                                print("")
                                                print("Your ticket was invalid, therefore you have no money.")
                                                print("")
                                                print("You can only read your book.(Enter:'read book')")
                                                
                                            except:
                                                print("You can get a coffee if you want to.(Enter: 'get coffee/read book')")
                                                
                                            answer = input("> ").lower().strip()
                                            if answer == 'exit':
                                                sys.exit() 
                                            
                                           
                                            if whole_time < 120:
                                                
        
                                                if answer == "read book": #back tab
                                                    print("Have fun with your new book.")
                                                    print('The end of the game.')
                                                    print("")
                                                    
                                                elif answer == "get coffee":
                                                    print("Enjoy your coffee.")
                                                    print('The end of the game.')
                                                    print("")
                                                    
                                             
                                                    
                                                else:
                                                    print("Not correct action.")
                                                    print("")
                                                    
                                                    
                                            elif whole_time >= 120:
                                                    print("Your train arrived after the library closed.")
                                                                                                                                                
                                                    if answer == "get coffee":
                                                            print("Enjoy your coffee.")
                                                            print('The end of the game.')
                                                            print("")
                                                            
                                                    elif answer != "get coffee":
                                                            print("To end the game you need to get a coffee.")
                                                            print("")
                                                            
                                                   
                                                            
                                            answer = input("Do you want to play again or quit the program? (Enter: 'again/quit')").lower().strip()
                                            if answer == 'exit':
                                                sys.exit() 
                                                            
                                            if answer == "again":
                                                continue
                                                
                                            else:
                                                sys.exit()
                                                
                                            
    elif answer == 'exit':
        sys.exit()                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                              
    else:
        print("Unfortunately you can't reach your goal like this.")


