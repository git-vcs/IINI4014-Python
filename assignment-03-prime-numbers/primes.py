import time

# sending inn the amount of primes you like to generate
def lessNaive(maxAmout):
    primeArray = []
    foundPrimes=0 # the amout of primes that is found
    numberToCheck=1 # the number that is beeing chekd
    while foundPrimes < maxAmout:
        isPrime = True
        #There is no need to run the check past 1/2 of the number to check,
        # because no number in this range can be multiplied with 2 an get a number lower that the number we are checking
        for i in range (2, int(numberToCheck/2 +1)): # +1 i case the int casing round down
           if numberToCheck % i == 0: #modulo to check the reminder of division between the two numbers. If it’s 0 that means its possible to divide to 2 numbers and not get an reminder, this means this is NOT a prime
               isPrime=False
               break #there is no need to test more numbers because we have already proven that this number is not a prime
        if isPrime:
            # appending the Prime to the array
            primeArray.append(numberToCheck)
            foundPrimes += 1
        numberToCheck += 1 # setting the next number to find
    return primeArray




#this code is based on this https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes algorithm
# sending inn the value you want to test up to.
# for example a maxValiue=10 means that you will find all the primes between 0 and 10
def sieveOfEratosthenes(maxValiue):
    primeArray = [True]*maxValiue  # an array with all true booleans
    currentPrime = 2 # the current prime number
    while currentPrime < maxValiue:
        position = 2
        try: # this code fails without a try catch but a cant see why
            while position < maxValiue:
            #Changing all positions that can’t be a prime
                if[position*currentPrime < maxValiue]:
                    # false = NOT A PRIME
                    primeArray[position*currentPrime]=False # this line fails without the try catch
                    position += 1
            currentPrime += 1
        except: #
            currentPrime += 1 # catching error and continuing the generation of primes
    primeNumbers=[] #this array is for generating numbers from the Boolean array(primeArray)

    #Generating a table with all the prime-numbers
    for x  in range(1,len(primeArray)):
        if primeArray[x] == True:
            #this means that the number i IS A PRIME and is appended ti the end of the array
            primeNumbers.append(x)
    return primeNumbers



def main():
    print()

if __name__=="__main__":
   lessNaiveStart=time.time()  #staring a timer to mesure the timed user
   lessNaivePrimes = lessNaive(1000)
   lessNaiveStop=time.time()    # geting the time after the code is run to find the amout og time used
   print("Time for lessnaive:", lessNaiveStop-lessNaiveStart)
   print(lessNaivePrimes)
   fasterStart=time.time()
   fastPrimes=sieveOfEratosthenes(7908) #faster apriatch but you need to know the plast prime +1
   fasterStop=time.time()
   print(fastPrimes)
   print("Faster Metode: ",fasterStop-fasterStart)
   print("Difference:",(lessNaiveStop-lessNaiveStart)-(fasterStop-fasterStart))


