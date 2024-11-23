#---------------------------------------------------#
#                 EKSAMEN 2023 KONT                 #
#---------------------------------------------------#

#Oppgave 1
'''
s[x] ---> string (feil , ERROR)
i == x ---> BOOL (riktig)
s-t ---> ERROR (riktig)
i/i ---> float (riktig)
i*x ---> float (riktig)
7//i ---> int (riktig)
s+t ---> string (riktig)
i % 0 ---> ERROR (riktig)
'''

#Oppgave 2
'''
1.67 ---> ikke eksakt (riktig)
8342... ---> eksakt (riktig)
1.5e-7 ---> ikke eksakt (riktig)
-3.75 ---> ikke eksakt (feil , eksakt)
0.8 ---> eksakt (feil , ikke eksakt)
-55 --->eksakt (riktig)
'''

#Oppgave 3
'''
1 : (r) (riktig)
2 : (rr) (riktig)
3 : (agir) (riktig)
4 : (riga) (riktig)
5 : (a) (riktig)
'''

#Oppgave 4
'''
respons(d,3,0) --> 9        (feil , -2)      
respons(d,0,0) --> -2       (feil , 'a')
respons(d,3,1) --> 7.0      (riktig)
respons(t,0,0) --> -1       (riktig)
respons(d,1,2) --> 1.0      (riktig)
'''

#Oppgave 5
''' Svar:   (Fasit)
1 : FEIL    (Feil)
2 : FEIL    (Feil)
3 : Riktig  (Riktig)
4 : Riktig  (Feil)
5 : FEIL    (Feil)
6 : Riktig  (Riktig)
'''

#Oppgave 6

def count_start_end_words(word_list , letter):
    svar = [word for word in word_list if word[0] == word[-1] == letter]
    return len(svar)

#test av oppg 6
word_list = ['ada' , 'ida' , 'alta' , 'ana' , 'y']
letter = 'a'

print(count_start_end_words(word_list , letter))

#Oppgave 7 
def legal_alcohol(age , booze , wine , beer):
    
    if booze == 0.0:
        maksimalt = 5
        sprit = 0.0
        if wine == 0.0:
            vin = 0
            øl = 5
        else:
            vin = 3
            øl = 2
        
    else:
        maksimalt = 4.5
        vin = 1.5
        øl = 2.0
        sprit = 1.0

    kunde = booze + wine + beer

    if age < 18:
        return False
    elif age < 20 and booze == 0.0:
        if kunde <= maksimalt and wine <= vin and beer <= øl:
            return True
        else:
            return False
    elif age >= 20:
        if kunde <= maksimalt and booze <= sprit and wine <= vin and beer <= øl:
            return True
        else:
            return False
    else:
        return False
#test for oppgave 7
age = 20
sprit = 0.5
vin = 1.5
øl = 4.0

print(legal_alcohol(age , sprit , vin , øl))

#Oppgave 8
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.25*x**3-0.25*x**2-2*x+1
def g(x):
    return 3*x**2/(np.sin(x)+5)-5
def h(x):
    return -3*np.cos(x**2)-x

fig, ax= plt.subplots()

x = np.arange(-4,4)
ax.plot(x,g(x))

x = np.linspace(-4,4,5) 
ax.plot(x,f(x))

x = np.linspace(-3,3,100)
ax.plot(x , h(x))

#plt.show()

#Oppgave 18
def check(vector1 , vector2 , n):
    if list(vector1) == list(vector2) and len(vector1) >= n:
        return True
    elif n > 0:
        for j in range(len(vector1)-n+1):
            for i in range(len(vector2)-n+1):
                if list(vector1[j:j+n]) == list(vector2[i:i+n]):
                    return True
    return False
 
def same_row_col(a,b,n = 0):

    resultat = []
    for row in range(a.shape[0]):
        for col in range(b.shape[1]):
            if check(a[row] , b[:,col] , n):
                resultat.append((row , col))
    
    return resultat
    

a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [1,1,1,1]
])

b = np.array([
    [5,0,6,6],
    [6,0,6,7],
    [7,0,8,8],
    [8,1,1,1]
])
print(same_row_col(a,b , 0))