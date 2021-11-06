

def monotonic_decreasing(list):
    return all(x>=y for x, y in zip(list, list[1:]))

def monotonic_increasing(list):
    return all(x<=y for x, y in zip(list, list[1:]))

def monotone_min(list):
    
    min_list = min(list)
    index_min = list.index(min_list)

    first_el = list[ : index_min+1]
    second_el = list[index_min+1 : ]

    if monotonic_decreasing(first_el):
        if monotonic_increasing(second_el):
            return min_list
        else: raise ValueError("Second Half of provided list is not monotonic")
    else: raise ValueError("Fist Half of provided list is not monotonic")
        
    