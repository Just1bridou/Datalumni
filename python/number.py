def isPrime(nb):
    if nb > 1:
        for i in range(2,nb):
            if(nb%i==0):
                return False
        return True
    return False


def twoNumbers(nb):
    if(len(str(nb))>=2):
        return True
    else:
        return False
  
  
def filterNumber(nb):
    if '1' in str(nb) or '7' in str(nb):
        return False
    else:
        return True
    
    
def sumNumber(nb):
    sum = 0;
    
    while nb>1:
        sum += nb%10
        nb=(nb/10) - (nb%10)/10
    
    if sum <= 10:
        return True
    else:
        return False
    
    
def twoFirstOdd(nb):
    firsts = int(str(nb)[:2])
    if (firsts%10 + ((firsts/10) - (firsts%10)/10))%2 == 0:
        return False
    else:
        return True
        
        
def beforeLastIsFour(nb):
    if((str(nb)[-2:])[:1])=='4':
        return True
    else:
        return False
    
    
def lastNumber(nb):
    if(str(nb)[-1:] == len(str(nb))):
        return True
    else:
        return False


def isMysteryNumber(nb):
    if isPrime(nb) and twoNumbers(nb) and filterNumber(nb) and sumNumber(nb) and twoFirstOdd(nb) and beforeLastIsFour(nb) and lastNumber(nb):
        return True
    else:
        return False


for nb in range(1,1001):
    if isMysteryNumber(nb):
        print(f'Le nombre mystère est le : {nb}')
    



    

