def interfacesMadlib():
    import time

    print "Hi! Welcome to the Interfaces Madlib!"
    time.sleep(2)
    print "Before we can read the story, I need some help from you."
    time.sleep(3)
    print "Please give me a "
    time.sleep(2)
    
    bodyPart = raw_input("body part: ")
    linguisticTopic = raw_input("a topic in linguistics: ")
    number1 = raw_input("a number: ")
    number2 = raw_input("another number: ")
    adjective1 = raw_input("an adjective: ")
    negativeAdjective = raw_input("a negative adjective: ")
    language = raw_input("the name of a language: ")
    syntaxthing = raw_input("some syntactic function, like c-command, but not c-command: ")
    ccommand = "c-command"
    if syntaxthing == ccommand:
        print "You're an asshole. Anyway, let's continue."
    inappropriateWord = raw_input("an inappropriate word that you wouldn't  say in a classroom: ")
    consonants = raw_input("4 uppercase consonants: ")
    plantType = raw_input("a type of plant: ")
    number3 = raw_input("a number: ")
    smallerNumber = raw_input("a smaller number: ")
    print "Almost finished! I just need three more things: "
    time.sleep(2)
    
    day = raw_input("a day of the week: ")
    timeDay = raw_input("a time of day: ")
    importantJob = raw_input("an important job: ")

    print "Whew! Thanks for all that input. Now I'm gonna use it to make a story!"
    time.sleep(2)
    print "Just hit any key to move to the next line of the story. Now, let's begin..."
    time.sleep(2)

    
    print '"Shall we get started?" Riny asks, standing at the front of the classroom, scratching his ' + bodyPart + '.'
    raw_input()
    print '"Yes, yes, yes, yes, today we are going to be talking about ' + linguisticTopic + ', and I\'ve given  you ' + number1 + ' pages to read,'
    raw_input()
 
    print ' but I realized last night that you shouldn\'t read them, because this handout I\'ve made is ' + number2 + ' times better than the original.'
    raw_input()
    print ' The next hour should be very ' + adjective1 + '. So, the theory, I should say this beforehand, it\'s not a very good theory because... '
    raw_input()
    print ' well it\'s a ' + negativeAdjective + ' theory. It uses fuzzy facts, yes very fuzzy, with data from ' + language + ', and while the facts may be true, '
    print ' it\'s just not very beautiful...'
    raw_input()
    print ' actually, the data from this language reminds me of a joke. How did it go... '
    raw_input()
    print ' yes, there\'s a '+ language + ' person and, well, you have ' + syntaxthing +' and in this language, you see '


    print 'the ' +syntaxthing + ' is a lot like ' + inappropriateWord + '."'
    raw_input()
    
    print ' Suddenly Martin raises his hand, "But Riny, we should tell them that this isn\'t the only theory.'
    raw_input()
    print ' I mean there are theories of syntax like ' + consonants + ' grammar that don\'t even use trees! They use ' + plantType + ' diagrams."'
    raw_input()
    print ' Riny nods and steps back and forth a few times. "No, no, no, no, no, no. You\'re absolutely right,'
    raw_input()
    print ' but you\'re wrong. But I\'m afraid we don\'t have any time left to discuss this, but if you all try it out in the assignment,'
    raw_input()
    print ' I\'ve made ' + number3 + ' questions, but you only have to do ' + smallerNumber + ', but I haven\'t emailed it to you yet,'
    raw_input()
    print ' I will send it to you on ' + day + ' at ' + timeDay + '. So, if there aren\'t any questions, we can talk about how being a linguist is much more important than, say,'
    raw_input()
    print ' being a ' + importantJob + '."'
    time.sleep(2)

    print "The End!"
    time.sleep(2)
    
    finish = raw_input ("Did you like the story? (y/n): ")
    
    y = "y"
    n = "n"
    if finish == y:
        print "Hooray! I'm so happy you enjoyed it! You are obviously a very smart and sexy person."
    if finish == n:
        print "Well you can't please everyone. I'm going to turn myself off now."
        quit()
                                
interfacesMadlib()
