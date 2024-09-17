dict = {
    "Dollar": [12600, 12540, 12900, 12450, 11900],
    "Rubl" : [135, 120, 144, 150, 130],
    "Yevro": [13650, 13520, 13240, 13700, 13000],
    "Funt": [16150, 15380, 16640, 14980, 15540],
    "Tenge": [15, 20, 40, 30, 25]

}

for i in dict:
    print(
        f"{i}: eng baland narx: {max(dict[i])}, eng past narx: {min(dict[i])}"
    )
