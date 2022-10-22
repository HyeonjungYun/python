while 1:
    N = input()
    if N == "EOI": break
    N = N.lower()
    if N.count("nemo") > 0: print("Found")
    else: print("Missing")