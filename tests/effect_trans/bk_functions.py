# stub rpy translation func
def __(text):
    return text
def is_string(text):
    return isinstance(text, str)
    
# Rounds to the nearest decimal number (remember to force a float when dividing two integers
# python is a dick about that)
def round_int(x): 
    x = float(x)
    return int(round(x))
# Returns a string of an integer
def str_int(x): 
    return str(round_int(x))
def round_best(x, decimals=1):
    for d in range(decimals):
        if not (x * 10 ** (d)) % 1:
            if d == 0:
                return int(x)
            else:
                return round(x, d)
    return round(x, decimals)

def make_list(it, obj_type = None): # Will automatically make a list of a single string, integer or float. Specify object type to list otherwise.
    if not it:
        return []
    if isinstance(it, str) or isinstance(it, int) or isinstance(it, float):
        return list([it])
    if obj_type:
        if isinstance(it, obj_type):
            return list([it])
    return list(it)

extended_sex_acts = ["naked", "service", "sex", "anal", "fetish", "bisexual", "group"]