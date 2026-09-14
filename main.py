from random import shuffle , choice
try:
    word_save=[]
    word=["axe","awkward","arm","apple","ambulance","angry","average","act","action","actor","acid","armor","alright","amazing","art","artist","banana","bar","barber","bank","big","best","bull","ball","black","bad","bald","bread","bat","bed","brother","brown","box","bath","bean","bee","badminton","bunny","blanket","boss","bus","bye","buy","bucket","cat","car","cut","coconut","candy","candle","case","cost","crown","crow","common","confuse","cancel","call","cow","cookie","cooler","cool","code","cry","city","daddy","dad","donut","dumb","dumbbell","disk","dictionary","dollar","doll","door","earth","electric","enjoy","espresso","egg","foot","feet","feel","football","farm","follow","fool","full","free","gold","good","great","gangster","game","galaxy","hammer","hamburger","honey","hungry","ice","icecream","joke","jellyfish","jelly","kangaroo","lick","luck","look","like","live","love","lose","lost","long","loop","list","lesson","lemon","lie","monkey","money","mom","mother","mommy","monster","mango","mister","miss","mid","mad","milk","math","mask","night","nut","nice","nasty","name","open","okay","orange","order","old","print","pizza","pocket","play","park","queen","quiz","quick","run","rush","ring","risk","rope","rule","roll","star","sun","sister","sing","song","soul","sell","seal","television","tomato","time","tickle","tool","teeth","user","van","virus","video","wolf","wall","well","wish","weak","xray","yogurt","you","young","yes","zoo","zip"]
    
    print("we don't have space so some words like \"ice cream\" changed into \"icecream\" and \"x-ray\" is xray in the game")#starter warning
    
    #choose 5 words
    while not len(word_save)==5:
        save=choice(word)
        if not save in word_save: word_save.append(save)
     
    #clean up deleting vars that we don't need enymore
    del save ; del word ; word=word_save ; del word_save ; l=[]
    
    # "#" instead of words
    for i in range(len(word)):
        print("#" * len(word[i]),end=" ")
    
    # latters
    for i in range(len(word)):
        for a in range(len(word[i])):
            if not str(word[i])[0+a:1+a] in l:
                l.append(str(word[i])[0+a:1+a])
    shuffle(l)
    
    #clean printing with for
    print() #for "\n"
    for i in range(len(l)):
        print(l[i] , end=" ")
    print()#\n
    
    player_list=[]
    
    #main game
    while True:
        player_inp=input("word:")
        
        #cheat code
        if player_inp=="cheat_code":
            for i in range(len(word)):
                print(word[i],end=" ")
            print()
            
        else: #no cheating!!
            player_inp=player_inp.lower()
            for i in range(len(word)):
                if player_inp==word[i] and not player_inp in player_list:player_list.append(player_inp)
             
             #showing tries
        print("tries:",end="")
        if len(player_list)==0: print("(nothing)")
        else:
            for i in range(len(player_list)):
                 print(player_list[i],end=",")
            print()#\n
            
    #the end
        if len(player_list)==len(word):break
    print("Good job!")
except KeyboardInterrupt: print("bye")
