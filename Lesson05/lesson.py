
things = ['dog', 'Da Vinci\'s David', 'tree', 'house', 'rock', 'x-wing fighter', 'unicorn', ]
# TODO: figure out how to make lists like this way more legible.
animals = list()

for item in things:
    if item in ['dog', 'bird', 'cat', 'unicorn', 'donkey', 'goat']:
        animals.append(item)

for critter in animals:
    print(critter)
