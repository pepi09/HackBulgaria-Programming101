def sort_fractions(fractions):
    mult = 1
    for i in range(0,len(fractions)):
        mult*=fractions[i][1]
   
    comp_fractions = []
    for i in range(0,len(fractions)):
        comp_fractions.append([[fractions[i][0]*(mult//fractions[i][1]),mult],fractions[i]])
    
    comp_fractions =  sorted(comp_fractions)
    result_fractions = []
    
    for i in range(0,len(comp_fractions)):
        result_fractions.append(comp_fractions[i][1])
    return result_fractions