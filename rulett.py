import random
rennk = 0
bakiye = 0
def rulet(renk: str,sayi: int ,tc: int,rd: int,to: int,bet: int ):
    global rennk, bakiye
    a = random.randint(0,36)
    if renk == "kırmızı" or renk == "siyah":
        if a%2 == 1:
            rennk = "siyah"
            if rennk == renk or tc == "tek":
                bakiye += bet*2
            else:
                bakiye -= bet    
        elif a%2 == 0:
            rennk = "kırmızı"
            if rennk == renk or tc =="çift":
                bakiye += bet*2
            else:
                bakiye -= bet     
    elif to > -1:
        if 1 <= a <=34:
            if to == 1:
                bakiye += bet*3
            else:
                bakiye -= bet     
        if 2 <= a <=35:
            if to == 2:
                bakiye += bet*3
            else:
                bakiye -= bet         
        if 3 <= a <=36:
            if to == 3:
                bakiye += bet*3
            else:
                bakiye -= bet      
    elif sayi > -1:
        if sayi == a:
            bakiye += bet*36
        if sayi != a:
            bakiye -= bet    
    elif rd > -1:
        if 1 <= a <=12:
            if rd == 1:
                bakiye += bet*3
            else:
                bakiye -= bet     
        if 13 <= a <=24:
            if rd == 2:
                bakiye += bet*3
            else:
                bakiye -= bet         
        if 25 <= a <=36:
            if rd == 3:
                bakiye += bet*3
            else:
                bakiye -= bet
    
    return a, bakiye
     

    