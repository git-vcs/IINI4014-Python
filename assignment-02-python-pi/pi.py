# the video referenced in the comments: https://www.youtube.com/watch?v=_rJdkhlWZVQ

import math
def ArchimedesPI(accuracy=0.001):
    # initial values
    pi_estimation=[] #  Array to store all iterations
    pi_estimation.append(0)

    hypotenuse = 1  # initial length called s in the video
    iteration = 1
    running = True
    while running:
        number_of_sides=3*math.pow(2,iteration)  #  number of sides in the poligon called p in the video, this is to get the 6 12 24 as displayed in the video
        lager_catheti = hypotenuse/2  # called s/2 in the video
        calculated_catheti = math.sqrt((1-math.pow(lager_catheti,2)))  # called a in the video
        small_catheti = 1-calculated_catheti  # this is the small catheti in the new right-angled triangle, the length is called b in the video
        number_of_sides = number_of_sides * hypotenuse
        pi_estimation.append(number_of_sides/2)   # pi estimated
        hypotenuse = math.sqrt(math.pow(small_catheti,2)+math.pow(lager_catheti,2)) # new hypotenuse
        if pi_estimation[iteration]-pi_estimation[iteration-1] < accuracy: # Checking if we have achieved the desired accuracy
            running=False
        print("diff:", pi_estimation[iteration]-pi_estimation[iteration-1])  # debug
        iteration += 1

    return pi_estimation[iteration-1]


def main():
    print(ArchimedesPI(0.00001))  # input is the accuracy


 # main
if __name__ == '__main__':
    main()
