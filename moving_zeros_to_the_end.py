#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#move_zeros([1, 0, 1, 2, 0, 1, 3])
# returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    for i in range(1, len(array)+1):
        if array[-i] == 0 and array[-i] is not False:
            array.append(array.pop(-i))
    return array

#OR:
def move_zeros(array):
    z = []
    n = []
    for i in range(len(array)):
        if array[i] != 0 :
            n.append(array[i])
    for i in range(len(array)):
        if array[i] == 0 :
            z.append(array[i])
    array = []
    for i in range(len(n)):
        array.append(n[i])
    for i in range(len(z)):
        array.append(z[i])
    return array
