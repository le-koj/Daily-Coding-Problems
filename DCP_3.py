############################################
###______ DAILY CODING PROBLEM #3  _____####
###                                      ###
### DESCRIPTION: Given an array of       ###
###     integers, return a new array     ###
###     such that each element at index  ###
###     i of the new array is the        ###
###     product of all the numbers in    ###
###     the original array except the    ###
###     one at i                         ###
###                                      ###
### PARAMETERS: array- array of integers ###
###                                      ###
###
### OUTPUT: array - array of integers    ###
###
############################################

def mutate(arr):
    _new_container = []     #--- an empty list to hold new array

    for i in arr:
        value = 1

        # for loop multiplier
        for j in arr:
            if j != i:      #-- condition to exclude current index i
                value *=j

        _new_container.append(value)    #-- add calculated value to new array

    return _new_container
    
def mutate_v2(arr):
	_new_container = []     #--- an empty list to hold new array
	_sub_multiple = 1
	
	# find total multiple of set
	for i in arr:
		_sub_multiple *= i
		
	# create new array
	# divide total multiple by current index value
	# add quotient to new array
	for i in arr:
		quotient = _sub_multiple/i
		_new_container.append(quotient)
		
	return _new_container
                

