
n = int(input())
Rodoslov = dict()

for i in range(n-1):
    child, parent = input().split()
    Rodoslov[child] = parent

def get_height(name):
    height = 0
    while name in Rodoslov:
        height += 1
        name = Rodoslov[name]
    return height

all_people = set(Rodoslov.keys()) | set(Rodoslov.values())

heights = {}
for person in all_people:
    heights[person] = get_height(person)

for person in sorted(heights):
    print(f"{person} {heights[person]}")
