############################################
###______ DAILY CODING PROBLEM #1_____######
###                                      ###
### DESCRIPTION: Given a list of numbers ###
###     and a number k, return whether   ###
###     any two numbers from the list    ###
###     add up to k.
###
### PARAMETERS: list - list of integers  ###
###             number - integer         ###
###
### OUTPUT: Boolean - True/False         ###
###
############################################

def sum_k(list_of_integers, integer):
    # subract item in list less than given integer from integer 
    # locate difference in list of integers
    for item in list_of_integers:
        if item <= integer:
            difference = integer - item
            if difference in list_of_integers:
                print difference
                print item
                return True
    return False
    
