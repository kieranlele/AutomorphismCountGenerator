import math

"""A method that checks whether or not L1 and L2 of a given tree are equal"""
def check_equality(tree):
    m = tree.index(1,2)
    L1 = [tree[i] - 1 for i in range(1,m)]
    L2 = [tree[i] for i in range(m,len(tree))]
    L2.insert(0,0)
    if L1 == L2:
        print("L1 and L2 are the same")
        return True
    return False


"""A method that creates outputs automorphism count based upon L1 if L1 and 
L2 are equal """
def create_l1_aut(tree):
    m = tree.index(1, 2)
    L1 = [tree[i] - 1 for i in range(1, m)]
    ret = get_aut(L1)**2 * 2
    return ret


"""A method that creates K1 and K2 based upon K when creating labels"""
def getks(tree, k):
    K1 = 0
    K2 = 0
    for x in range(k,len(tree)):
        if x == len(tree) - 1:
            K1 = x
            break
        elif tree[x+1] == tree[k]:
            K1 = x
            break
        elif tree[k+1] == tree[k] - 1:
            K1 = x
            break
    for y in reversed(range(0,k)):
        if (tree[k] - 1) == tree[y]:
            K2 = y
            break
    return [K1,K2]


"""A method that creates creates all of the labels for each K"""
def get_mapping(tree):
    output = []
    for x in range(1,len(tree)):
        vals = getks(tree, x)
        label = [tree[i] for i in range(x,vals[0] + 1)]
        label.insert(0,vals[1])
        output.append(''.join(str(label[i]) for i in range(0,len(label))))
    return output


"""A method that calculates the number of automorphisms based upon label 
groupings"""
def get_aut(tree):
    map = get_mapping(tree)
    dict = {}
    ret = 1
    for x in map:
        if x not in dict:
            dict[x] = map.count(x)
        else:
            continue
    for x in dict.values():
        ret *= math.factorial(x)
    return ret


if __name__ == '__main__':
    tree = [0,1,2,2,1,1]
    if check_equality(tree):
        print(str(create_l1_aut(tree)) + " Automorphisms")
    else:
        print(str(get_aut(tree)) + " Automorphisms")

