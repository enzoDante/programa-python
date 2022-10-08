n = int(input())
if n >= 1 and n <= 2000:
    l = list()
    for i in range(0, n):
        leds = 0
        num = str(input())
        if num >= 1 and num <= 100000:
            for x in range(0, len(num)):
                if num[x] == '0': leds += 6
                if num[x] == '1': leds += 2
                if num[x] == '2': leds += 5
                if num[x] == '3': leds += 5
                if num[x] == '4': leds += 4
                if num[x] == '5': leds += 5
                if num[x] == '6': leds += 6
                if num[x] == '7': leds += 3
                if num[x] == '8': leds += 7
                if num[x] == '9': leds += 6
                
            l.append(leds)
        for x in l:
            print(f'{x} leds')