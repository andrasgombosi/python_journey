def iterator(e,d) :
    i=0
    numbers = []
    while i < e:
        numbers.append(i)

        i=i+d
    return numbers


num_here = iterator(8,2)

print num_here
