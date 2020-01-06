import random

hero = ''
friend = ''

beginning       = ['Жили-были', 'Давным-давно']
action          = ['пошли', 'побежали']
place           = ['замок', 'пещеру']
item            = ['меч', 'ковер', 'палку', '...ничего не нашли']
end             = ['конец', 'fin', 'и пошли обратно домой']

def makeStory():
    h       = hero.lower().capitalize()
    f       = friend.lower().capitalize()
    beg     = random.choice(beginning)
    act     = random.choice(action)
    pl      = random.choice(place)
    ite     = random.choice(item)
    en      = random.choice(end)
    return  beg + " " + h + " и " + f + ", " + act + " в " + pl + " нашли там " + ite + ', ' + en