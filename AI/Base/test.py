from AI.Base.State import State



board = [
    ['O','O','O','O','O','O','O','O'],
    ['O','O','O','O','O','O','O','O'],
    ['O','O','O','O','O','O','O','O'],
    ['O','O','O','X','O','O','O','O'],
    ['O','O','O','O','O','O','O','O'],
    ['O','O','O','O','O','.','O','O'],
    ['O','O','O','O','O','O','O','O'],
    ['O','O','O','O','O','O','O','O']
]
print(State('X', board).actionSet())