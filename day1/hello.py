first = [True, False]
second = [True, False]
third = [True, False]
forth = [True, False]

for f in first:
    for s in second:
        for t in third:
            for fo in forth:
                print f, s, t, fo, f or s and t and not fo, ": ", f or ((s and t) and (not fo))

