
playlist = ['A', 'B', 'C', 'D', 'E']
on = True

while on:
    number = int(input())
    amount = int(input())
    for i in range(amount):
        if number == 1:
            playlist.append(playlist[0])
            playlist.pop(0)
        elif number == 2:
            playlist.insert(0, playlist[4])
            playlist.pop()
        elif number == 3:
            playlist[0], playlist[1] = playlist[1], playlist[0]
        elif number == 4:
            for i in playlist:
                    print(i, end=' ')
            on = False
            break
