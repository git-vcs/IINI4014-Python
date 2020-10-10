

def spliceArray(array, endpossition, valiue):
    temp=[]
    temp.append(valiue)
    return array[:endpossition]+temp+array[endpossition:]



def insertAndSort(array,input):
    plassert = False
    for i in range(len(array)):
        if array[i] == input:
           #print("iput er likt",input)
           plassert = True
           array=spliceArray(array, i, input)
           break
        elif array[i] > input:
            plassert = True
            #print("inpute",input, "er mindre enn",array[i])
            array=spliceArray(array, i, input)
            break

    if len(array) == 0:
        array.append(input)
        return array
    if not plassert:
        array.append(input)

    return array



def main():
    test={}
    temp=test.get(0,[])
    #print(temp)
    test[0]=insertAndSort(temp,"Dette er en test 2")
    temp=test.get(0,[])
    #print(temp)
    test[0]=insertAndSort(temp,"Dette er en test 1")
    temp=test.get(0,[])
    test[0]=insertAndSort(temp,"Dette er en test 1Dette er en test 1Dette er en test 1Dette er en test 1Dette er en test 1Dette er en test 1")
    temp=test.get(0,[])
    #print(temp)
    for i in range(0,max(test.keys())):
        print(test[i])


   # print(test)



if __name__ == '__main__':
    main()