def create_an_empty_list():
    return []

def create_a_list():
    created_list = [1,2,3,4]
    # created_list.insert(4)
    return created_list

def add_element_to_end_of_list(l, element):
    l.append(element)    
    return(l) 
add_element_to_end_of_list([1,2], 3)

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    del (l[-1])
    return l

def remove_element_from_start_of_list(l):
    del (l[-0])
    return l

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
