
num_iter = int(input())
money = 0

for i in range(num_iter):
    info = input()
    time, duration = info.split()
    hh, mm = map(int, time.split(':'))
    dd = int(duration)

    tm = (60*hh + mm) % 1440
    if tm <= 420 < (tm + dd):
        money = money + (420-tm)*5 + (tm+dd-420)*10
    elif 420 < tm <= 1140 < tm+dd:
        money = money + (1140-tm)*10 + (tm+dd-1140)*5
    elif tm+dd <= 420 or tm > 1140:
        money = money + 5*dd
    else:
        money = money + 10*dd

print(money)
