#  CMPT-142 - A2Q1 - Pokemon Attacks.
#  Function: Output the effectiveness of an attack 
#            between two pokemon based on a set table.
#  ---------------------------------------------
#  Created by: Jeffrey Hamilton, nfj513, 11393559.
#  Created on: November 18th, 2024, 9:50am.
#  Last modified: November 18th, 2024, 10:50am.
#  ---------------------------------------------

def Pokemon_Attack_Effectiveness(atk: str, dfd: str) -> str:
    """
    :params: (str, str) -> (atk, dfd)\n
    atk: Attacker pokemon type\n
    dfd: Defender pokemon type\n
    :output: (str) -> effectiveness of an attack based on defender and attacker pokemon types.
    """
    # Attack effectiveness strings.
    ok = "Okay"
    se = "super effective!!!"
    nve = "not very effective"

    if atk == "normal" or dfd == "normal": # Normal on attacker or defender always leads to OK attack.
        return(ok)
    
    elif atk == "fire" and not (dfd == "electric"): # Attacker is fire type.
        if dfd == "fire" or dfd == "water": # Not Very Effective (Strong Defenders).
            return(nve)
        elif dfd == "grass" or dfd == "ice": # Super Effective (Weak Defenders).
            return(se)
        
    elif atk == "water" and not (dfd == "electric" or dfd == "ice"): # Attacker is water type.
        if dfd == "water" or dfd == "grass": # Not Very Effective (Strong Defenders).
            return(nve)
        elif dfd == "fire": # Super Effective (Weak Defenders).
            return(se)
        
    elif atk == "grass" and not (dfd == "electric" or dfd == "ice"): #Attacker is grass type.
        if dfd == "fire" or dfd == "grass": # Not Very Effective (Strong Defenders).
            return(nve)
        elif dfd == "water": # Super Effective (Weak Defenders).
            return(se)
        
    elif atk == "electric" and not (dfd == "fire" or dfd == "ice"): # Attacker is electric type.
        if dfd == "grass" or dfd == "electric": # Not Very Effective (Strong Defenders).
            return(nve)
        elif dfd == "water": # Super Effective (Weak Defenders).
            return(se)
        
    elif atk == "ice" and not (dfd == "electric"): # Attacker is ice type.
        if dfd == "fire" or dfd == "water" or dfd == "ice": # Not Very Effective (Strong Defenders).
            return(nve)
        elif dfd == "grass": # Super Effective (Weak Defenders).
            return(se)
    else:
        return(ok)
        
    
attacker = input("Attacker: ").lower()
defender = input("Defender: ").lower()

print("Attack is " + Pokemon_Attack_Effectiveness(attacker, defender))