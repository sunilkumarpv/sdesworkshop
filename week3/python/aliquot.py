#The aliquot of a number is defined as: the sum of the proper of the number.
#For example, the aliquot(12) = 1 + 2 + 3 + 4 + 6 = 16.
#Write a function that returns the aliquot number of a given number.

def aliquot(n):
        alq = 0
        for i in range(1,n/2 + 1):
                if n % i == 0:
                       alq = alq + i
        return(alq)
                



