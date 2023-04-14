PaísA = 80000
PaísB = 200000
Anos = 0

while (PaísB > PaísA):
    PaísA *= 1.03
    PaísB *= 1.015
    Anos += 1
print('Irá demorar',Anos,'anos para o país A alcançar o país B')

    