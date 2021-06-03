"""
Created on 6/3/21

@author: fayfayning
"""
import math

# checks if L1 and L2 are equal
def checkL1L2(tree):
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    L1 = [tree[i] - 1 for i in range(1, m)]
    L2 = [tree[i] for i in range(m, len(tree))]
    L2.insert(0, tree[0])
    if L1 == L2:
        return True
    return False

# Gets the label of the rth node of the tree
def get_label(r, tree):
    lr = tree[r]
    last_step = True
    for i in range(r + 1, len(tree)):
        if tree[i] <= lr:
            r1 = i - 1
            last_step = False
            break
    if last_step:
        r1 = len(tree)
    for j in range(r - 1, -1, -1):
        if tree[j] == lr - 1:
            r2 = j + 1
            break
    label = [r2]
    label.extend(tree[r:r1 + 1])
    return label

# Iterates through the tree to get all the labels
def all_labels(tree):
    labels = []
    #print(get_label(10, tree))
    for r in range(1, len(tree)):
        label = get_label(r, tree)
        labels.append(label)
    return labels

# Calculates the number of automorphisms using the labels
def calc_aut(labels):
    labels.sort()
    label = labels[0]
    indexes = []
    count = 0
    for i in range(1, len(labels)):
        if label != labels[i]:
            indexes.append(i - count)
            count = i
            label = labels[i]
    indexes.append(len(labels) - count)
    num = 1
    for i in indexes:
        if i != 1:
            num *= math.factorial(i)
    return num

# Runs program on a given tree
def aut(tree):
    if not checkL1L2(tree):
        labels = all_labels(tree)
        num = calc_aut(labels)
    else:
        ind_1 = tree.index(1)
        m = tree.index(1, ind_1 + 1)
        L1 = [tree[i] - 1 for i in range(1, m)]
        aut_L1 = calc_aut(L1)
        num = aut_L1 * aut_L1 * 2
    return num

if __name__ == '__main__':
    tree = [0, 1, 2, 3, 3, 3, 2, 1, 2, 2, 1, 2, 2]
    fin = aut(tree)
    print("fin", fin)

    """
    for i in range(r + 1, len(tree)):
        if (tree.index())
        if tree[i] == lr:
            r1 = i - 1
            break

    try:
        r1 = tree.index(lr, r + 1) - 1
        try:
            r1_1 = tree.index(lr - 1, r + 1) - 1
            r1 = min(r1, r1_1)
        except ValueError:
            print(2)
            pass
    except ValueError:
        r1 = r

    try:
        r1_1 = tree.index(lr, r + 1) - 1
    except ValueError:
        r1_1 = len(tree) + 1
    try:
        r1_2 = tree.index(lr - 1, r + 1) - 1
    except ValueError:
        r1_2 = len(tree) + 1
    r1 = min(r1_1, r1_2)
    """