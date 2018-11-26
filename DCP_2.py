##################################################
###______     DAILY CODING PROBLEM #2     _____###
###                                            ###
### DESCRIPTION: write a method to             ###
###     measure the time efficiency            ###
###     of a given method/function of          ###
###     2 parameters
###
### PARAMETERS: function - a method/function   ###
###                        to test             ###
###             arg1 - function parameter 1    ###
###             arg2 - function parameter 2    ###
###             cycles - range of function
###                      executions. default   ###
###                      to 10 executions      ###
###
### OUTPUT: starting time, stopping time,      ###
###         and duration                       ###
###                                            ###
##################################################

import time

def time_test(function, arg1, arg2, cycles=10):
    start_time = time.time()

    # loop to run test script
    for i in range(cycles):
        function(arg1,arg2)
        
    end_time = time.time()
    
    print "\n"
    print "Time In: " + str(start_time) + "\n"
    print "Time Out: " + str(end_time) + "\n"
    
    time_lapsed = end_time - start_time
    print "duration: " + str(time_lapsed)
