def groupby(func,seq):
    f = {}
    for i in range(0,len(seq)):
        result = func(seq[i])
        if result in f.keys():
            f[result].append(seq[i])
        else:
            f[result] = [seq[i]]
    return f