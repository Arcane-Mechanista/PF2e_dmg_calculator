#   A script to calculate damage
'''Pathfinder 2nd edition is a table top roleplaying game based in a fantasy setting (similar in concept to DnD). This script is intended to allow you to see how effective various weapon and or ability combinations 
are in the three action economy cycle.'''
#! python 3

''' To do damage to an enemy, you first have to hit it. which you determine this by rolling 1d20, adding your to hit modifier and comparing it with the targets AC. If you hit, you will deal damage equivalent to 
the damage dice of the weapon plus a modifier determined by your strength / dexterity and other factors to be added in.
Critical hits double damage and may have special effects depending on the weapon traits.
Basics: physical attacks. In general, attacks suffer 'mulitple attack penalties'''

import os
import matplotlib.pylab as plt
os.system('cls')

#   Take inputs into the program and generate an average damage value for a list of AC's 
#   Input arguments = Target AC, To Hit value, damage dice values (think about adding multiple dice sometime) & damage modifiers from strength and class abilities etc.
#   Output return value = average damage
def dmgCalc(ac, toHit, dLow, dHigh, dmgMod):
    
      

    dmgLow = dLow + dmgMod
    dmgHigh = dHigh + dmgMod


    dmgCount = 0
    for d in range(1,21):
        if d == 1: # nat 1 miss will never cause damage
            #print(d,'-')
            continue            
        elif (d == 20) and (ac-toHit <21):   # Nat 20 could either be a success or crit success find a way to test.
            dmg = (((dHigh-dLow)/2)+dmgMod+1)*2
            dmgCount = dmgCount+dmg
            print(d, 'Nat 20 + tohit =',(toHit+20),'matches or exceeds ac=',ac)
        elif  d==20 :
            #print(ac, d, 'Nat 20:',dmg,'damage.')
            dmg = (((dHigh-dLow)/2)+dmgMod+1)
            dmgCount = dmgCount+dmg
            #print(ac, d, 'Nat 20:',dmg,'damage.')
            continue        
        elif toHit+d < ac:
            #print(d,'-')
            continue
        elif (toHit+d)-ac > 9: # Critical hit 10 above AC
            dmg = (((dHigh-dLow)/2)+dmgMod+1)*2
            #print(d, 'Crit hit:',dmg,'damage.')
            dmgCount = dmgCount+dmg
            continue
        else:               # normal / non-critical hit
            dmg = ((dHigh-dLow)/2)+dmgMod+1
            #print(d, 'Hit:',dmg,'damage.')
            dmgCount = dmgCount+dmg
    dmgCount = dmgCount/20
    return(dmgCount)

#=============
# Main Program
#=============
tHit = 10

dLo = 1
dHi = 12
dmgMo = 8
dmgDict = {}
dmgDiffDic = {}
for targAC in range(1,50):
    dmgDict.setdefault(targAC,dmgCalc(targAC, tHit, dLo, dHi, dmgMo))
    
    if (targAC-1) in dmgDict: 
        dmgDiffDic.setdefault(targAC,(dmgDict[targAC]-dmgDict[targAC-1]))
    else: dmgDiffDic.setdefault(targAC,None)
    #print('AC =',targAC,'Avg DMG =',dmgCalc(targAC, tHit, dLo, dHi, dmgMo),'| difference from prev val =', dmgDiffDic[targAC])
    
lists = sorted(dmgDict.items())
x,y = zip(*lists)
plt.plot(x,y)
plt.show()

    
#print('average damage output = ',dmgCount/20)

# cycle through armor class values and determine average damage.
#for i in range(10,35):
print('End.')