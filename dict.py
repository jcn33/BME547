def create_dict():

    x = {"day" : "sun is out", "night" : "moon is out"}
    
    return x
    
    
def add_dict(my_dict, key, def1):
    
    #Mutable variable, don't need to return dict, modifies

    my_dict[key] = def1
    
    
def output_def(dictionary, key):
    if(dictionary.get(key) == none:
        print("key does not exist")
    else:
        def1 = dictionary[key]
        print("definition of {}: {}".format(key, def1))
        
def output_dict(dictionary):

    l1 = dictionary.keys()      #List of keys
    l2 = dictionary.values()    #List of definitions
    ct = dictionary.length()    #Number of items
    
    #Can also clear, pop values off/on, etcetera
    
    
if __name__ == "__main__":
    my_dict = create_dict()
    add_dict(my_dict, "sun", "flaming ball in space")
    output_def(my_dict, "night")