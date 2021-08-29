def baby_shark_lyrics():
    s = {1: "Baby shark", 2: "Mommy shark", 3: "Daddy shark", 4: "Grandma shark", 5: "Grandpa shark", 6: "Let's go hunt", 7: "doo"}
    o = ''
    for k in range(1, 7):
        o += f"{s[k]}, {(s[7]+' ')*5}{s[7]}\n"*3+f"{s[k]}!\n"
    o += 'Run away,…'
    return o

print(baby_shark_lyrics())