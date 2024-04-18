def indices_of(xs,condition):
    ls =[]
    for x in range(len(xs)):
        if condition(xs[x]):
            ls.append(x)
    return ls

def count(xs, should_be_counted):
    return len([x for x in xs if should_be_counted(x)])

def count_older_than(people,min_age):
    def olderthan(person):
        return person.age >= min_age
    return count(people, olderthan)

def indices_of_cards_with_suit(cards, suit):
    def suitchecker(card):
        return card.suit == suit
    return indices_of(cards,suitchecker)
    