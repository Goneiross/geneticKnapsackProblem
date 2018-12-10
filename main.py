import random
import matplotlib as plt

def gTriIns(liste):
    """Effectue le tri d'une liste par insertion"""
    for i in range (1,len(liste)):
        elem = liste[i]
        k=i
        while (k > 0) and (liste[k-1] > elem) :
            liste[k]=liste[k-1]
            k-=1
        liste[k]=elem
    return(liste)

def gTriS(liste,year) :
    for i in range (1,len(liste)):
        elem = liste[i]
        k=i
        while (k > 0) and (liste[k-1][2][year] > elem[2][year]):
            liste[k]=liste[k-1]
            k-=1
        liste[k]=elem
    return(list(reversed(liste))) 

def gRange(a,b):
    """ Si a est une liste : for element a sans les elements de b
        Si a est un int, for i in range (0,a) sans les elements de b"""
    c=[]
    if type(a) == 'list' and type (b) == 'list' :
        for k in a :
            tmp=0
            for l in b :
                if l == k :
                    tmp += 1
            if tmp == 0 :
                c.append(k)
        return(c)
    elif type(a) == 'int' and type (b) == 'list' :
        c=[]
        for k in range(0,nb) :
            tmp=0
            for l in b :
                if l == k :
                    tmp += 1
            if tmp == 0 :
                c.append(k)
        return(c)
    else :
        print("Type error")
        return(1)

def gTabIni(a,n):
    """Genere un tableau de a avec n elements"""
    tab=[]
    for i in range (0,n) :
        tab.append(a)
    return(tab)
    
def gMerge(a,b):
    c=list(a)+list(b)
    return(c)
    
def ecartT(matrice):
    if False : #type(matrice) != 'list' :
        print("error")
        return(0)
    else :
        ecart=[]
        nbY=len(matrice[0])
        nbT=len(matrice)
        for i in range (nbY):
            moy = 0
            for j in range (nbT) :
                moy+=matrice[j][i]
            moy/=nbT
            s=0
            for j in range (nbT) :
                s+=(matrice[j][i]-moy)**2
            ecart.append(math.sqrt((1/nbT)*s))
        return(ecart)
                    

def ini(nbProducts,nbUnits,poidsMax,products):
    # print("############################## Initialisation ##############################")
    
    # products=[]
    # for i in range (0,nbProducts):
        # products.append([random.randint(1,20),random.randint(1,20)])
    
    units=[]
    for i in range (0,nbUnits) : #Pour chaque individu
        tmp2=[]
        tmp=gTabIni(0,nbProducts) #La valeur binaire de l'unite i pour le produit j --> units[i][0][j]
        tmp2.append(tmp)
        tmp2.append(0) #L'age de l'unite i --> units[i][1]
        tmp2.append([]) #Le score de l'unite i --> units[i][2][year]
        units.append(tmp2)  
        
    unitsTmp=[]
    for i in range (0,nbUnits) : 
        tmp2=[]
        tmp=gTabIni(0,nbProducts) 
        tmp2.append(tmp)
        tmp2.append(0) 
        tmp2.append([]) 
        unitsTmp.append(tmp2)

    for i in range (0,nbUnits): #On aleatoirise les unites
        actual=gTabIni(0,nbProducts) #Tableau permettant de savoir quels produits deja traites
        end=gTabIni(1,nbProducts)
        poids = 0
        while (poids < poidsMax) and actual != end :
            r = random.randint(0,nbProducts-1)
            actual[r]=1
            if products[r][0] + poids <= poidsMax :
                poids += products[r][0]
                units[i][0][r]=1
    # print("generation de la population initiale effectuee")
    return(units,unitsTmp,products)

def evaluation(units,products,nbProducts,nbUnits,year): #Note chaque unite
        for i in range (0,nbUnits):
            tmp=0
            for j in range (0,nbProducts):
                tmp += products[j][1] * units[i][0][j]
            units[i][2].append(tmp)
        return(units)
        
def selection(units,products,nbProducts,nbUnits,year):
        somme = 0
        for i in range (0,nbUnits) :
            somme += units[i][2][year]
        selected=-1
        gTriS(units,year) 
        r = random.randint(0,somme)
        while r > 0 :
            selected+=1
            r-=units[selected][2][year]
        return(selected)
        
def reproduction(c,pere,mere,units,unitsTmp,products,nbProducts,nbUnits,year,poidsMax):
        poids=0
        unitsTmp[c][1]=0 # On remet a 0 l'age
        r = random.randint(0,1)
        if r == 0 :
            for k in range (0,int(nbProducts / 2)):
                unitsTmp[c][0][k]=units[pere][0][k]
                poids+=unitsTmp[c][0][k]*products[k][1]
            for k in range (int(nbProducts / 2), nbProducts):
                if poids + units[mere][0][k]*products[k][1] <= poidsMax :
                    unitsTmp[c][0][k]= units[mere][0][k]
                    poids+=unitsTmp[c][0][k]*products[k][1]
                else :
                    unitsTmp[c][0][k] = 0
        else :
            for k in range (int(nbProducts / 2), nbProducts):
                unitsTmp[c][0][k]=units[pere][0][k]
                poids+=unitsTmp[c][0][k]*products[k][1]
            for k in range (0,int(nbProducts / 2)):
                if poids + units[mere][0][k]*products[k][1] <= poidsMax :
                    unitsTmp[c][0][k]= units[mere][0][k]
                    poids+=unitsTmp[c][0][k]*products[k][1]
                else :
                    unitsTmp[c][0][k] = 0
        return(unitsTmp)
        
def eugenisme(units,unitsTmp2,nbProducts,nbUnits,year):
    unitsTmp2=gTriS(unitsTmp2,year)
    for i in range (0,nbUnits) :
        units[i]=list(unitsTmp2[i])
    #print(units)
    return(units)
    
def deces(units,products,nbUnits,nbProducts,poidsMax):
    for i in range (0,nbUnits):
        if units[i][1] > 3:
            actual=gTabIni(0,nbProducts) 
            end=gTabIni(1,nbProducts)
            poids = 0
            while (poids < poidsMax) and actual != end :
                r = random.randint(0,nbProducts-1)
                actual[r]=1
                if products[r][0] + poids <= poidsMax :
                    poids += products[r][0]
                    units[i][0][r]=1
    return(units)

def main(nbProducts,nbUnits,poidsMax,products):
    units,unitsTmp,products = ini(nbProducts,nbUnits,poidsMax,products) #On genere les matrices units et products
    # print(units)
    # print("prod",products)
    maximum=[]
    # print("############################## Algorithme genetique ##############################")
    for year in range (0,50): #Pour chaque annee
        #print("#################### Age actuel :",year," ####################")
        units = evaluation(units,products,nbProducts,nbUnits,year) #On evalue
        for c in range (0,nbUnits) : #On reproduits pour avoir 2n units
            units[c][1]+=1
            pere = selection(units,products,nbProducts,nbUnits,year)
            mere = selection(units,products,nbProducts,nbUnits,year)
            unitsTmp = reproduction(c,pere,mere,units,unitsTmp,products,nbProducts,nbUnits,year,poidsMax)
            # print("pere",units[pere], pere,"mere", mere, units[mere], "unit",unitsTmp[c])
        unitsTmp = evaluation(unitsTmp,products,nbProducts,nbUnits,year) #On evalue
        unitsTmp2 = gMerge(units,unitsTmp) #On merge les deux units
        units = eugenisme(units,unitsTmp2,nbProducts,nbUnits,year) #On ne garde que les meilleurs
        units=deces(units,products,nbUnits,nbProducts,poidsMax)
        tmp=0
        for c in range (0,nbUnits):
            if tmp <= units[c][2][year] :
                tmp = units[c][2][year]
        maximum.append(tmp)
    # print(maximum)
    # print(units[0])
   
    plt.plot(maximum)
    # plt.show()
    
    return(maximum)
    
def analysis(nb, products,a) :
    ''' Si a == 0 : Calcul et affiche la moyenne de difference entre l'objectif et le max de chaque annee
        Si a == 1 : Calcul et affiche l'ecart type des max par an
    '''
    maxs=[]
    for i in range (nb) :
        print("analyse", i)
        maxs.append(main(len(products),50,10,products))
    yearEnd=len(maxs[0])
    conv=maxs[0][yearEnd-1]
    if a == 0 :
        diff=[]
        for i in range (yearEnd) :
            tmp=0
            for j in range (nb) :
                tmp+=maxs[j][i]
            diff.append(conv-(tmp/nb))
        plt.plot(diff)
        plt.show()
    if a == 1 :
        ecartype=ecartT(maxs)
        plt.plot(ecartype)
        plt.show()
analysis(10,[[17, 14], [13, 17], [17, 3], [20, 20], [9, 20], [13, 20], [1, 10], [5, 9], [3, 7], [7, 15], [9, 11], [4, 3], [16, 7], [6, 15], [3, 1], [15, 11], [5, 4], [8, 6], [4, 1], [18, 15], [19, 15], [5, 6], [17, 15], [18, 8], [19, 3], [8, 3], [4, 7], [8, 5], [1, 19], [20, 8], [10, 10], [18, 19], [3, 5], [19, 16], [6, 7], [17, 19], [17, 12], [6, 1], [4, 8], [14, 1], [11, 6], [7, 10], [17, 3], [7, 17], [12, 16], [19, 15], [15, 3], [15, 1], [16, 6], [17, 15]],0)
    
#main(50,200,200,[[17, 14], [13, 17], [17, 3], [20, 20], [9, 20], [13, 20], [1, 10], [5, 9], [3, 7], [7, 15], [9, 11], [4, 3], [16, 7], [6, 15], [3, 1], [15, 11], [5, 4], [8, 6], [4, 1], [18, 15], [19, 15], [5, 6], [17, 15], [18, 8], [19, 3], [8, 3], [4, 7], [8, 5], [1, 19], [20, 8], [10, 10], [18, 19], [3, 5], [19, 16], [6, 7], [17, 19], [17, 12], [6, 1], [4, 8], [14, 1], [11, 6], [7, 10], [17, 3], [7, 17], [12, 16], [19, 15], [15, 3], [15, 1], [16, 6], [17, 15]])


#weird pop :
#main(50,10,200) [[12, 13], [14, 18], [16, 15], [18, 13], [11, 17], [6, 2], [6, 2], [11, 17], [8, 13], [7, 13], [16, 3], [10, 6], [9, 3], [17, 18], [8, 10], [13, 6], [3, 9], [4, 9], [3, 12], [4, 2], [11, 2], [11, 13], [13, 8], [9, 14], [15, 6], [7, 7], [19, 4], [6, 19], [10, 5], [18, 1], [14, 16], [2, 12], [5, 3], [9, 3], [16, 4], [11, 10], [20, 4], [7, 7], [11, 10], [8, 18], [13, 7], [7, 15], [12, 3], [5, 8], [16, 2], [19, 2], [3, 6], [18, 6], [4, 20], [6, 16]]



#an other weird one [[4, 8], [15, 1], [16, 12], [2, 13], [2, 14], [7, 7], [18, 2], [6, 15], [16, 16], [11, 2], [15, 6], [4, 12], [16, 19], [20, 12], [13, 1], [19, 5], [15, 15], [4, 8], [19, 2], [7, 4], [14, 5], [4, 10], [15, 12], [1, 9], [7, 16], [15, 14], [9, 7], [8, 10], [19, 5], [16, 18], [20, 3], [20, 10], [12, 1], [14, 5], [18, 6], [5, 9], [16, 11], [18, 13], [1, 9], [20, 9], [16, 6], [5, 20], [19, 15], [1, 15], [1, 16], [17, 15], [13, 13], [11, 8], [19, 19], [16, 3]]