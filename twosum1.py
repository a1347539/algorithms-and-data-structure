def twoSum(table, Array, pos, Target, result):
    if result + Array[pos] == Target:
        table[pos] = 1
        return True

    if result + Array[pos] < Target:
        table[pos] = 1
        
        if twoSum(table, Array, pos + 1, Target, result+Array[pos]) == True:
            return True

        table[pos] = 0
            
    return False


def getValue(Array, Target):

    table = [0,0,0,0,0]
    
    if twoSum(table, Array, 0, Target, 0) == False:
        print("Not exist")
    else:
        return table

    




Array = [1,2,3,4,5]
Target = 4
print(getValue(Array, Target))
