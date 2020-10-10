import rsa
import threading
from multiprocessing import Pool
from queue import Queue
import time
import math
start=time.time()
print_lock = threading.Lock()
q = Queue()
message=""
n=0
message = []
def bruteForce(publickKey,mesage):

    n=publickKey[1]
    testEncrypted=[50786, 62544, 29219, 24566, 11357, 29219, 24566, 11357, 14356, 11357, 24566, 21068, 29476, 52833, 21068, 27065, 11357, 45100, 21068, 24566, 24566, 14356, 44077, 21068, 62287]
    ## n=65383
    #  tester alle mulig input for private nøkkel
    for keyTest in range(1,n):
        try:
            print(keyTest)
            message=rsa.decrypt((keyTest,n),mesage)
            if message[0] == 'h':
                print("Key:",keyTest,n)
                print(message)
                print("Time:",time.time()-start)


        except Exception as e:
            print("Tall:",keyTest,e)



def decrypt(privateNøkkel):
    encryptedMesage = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    #print(privateNøkkel)
    message=rsa.decrypt((privateNøkkel,n),encryptedMesage)
    if message[0] == 'h':
        print("Key:",privateNøkkel,n)
        print(message)
        print("Time:",time.time()-start)


def multiThread():
    p = Pool(7)
    testKeys=range(1,14600)
    p.map(decrypt,testKeys)
    p.close()
    p.join()





def main():
    encryptedMesage = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
    global message
    message = encryptedMesage
    publicKey=(29815, 100127)
    global n
    n=publicKey[1]
    multiThread()
    #bruteForce(publicKey,encryptedMesage)
    #test(encryptedMesage)







if __name__ == '__main__':
    main()
    print("Ferdig")
