# Write your code 
def remove_duplicates(xs):
    sett= set()
    oplossing = []
    for x in xs:
        if x not in sett:
            oplossing.append(x)
            sett.add(x)
    return oplossing
