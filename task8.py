def change_to_hm(num):
    hour = num // 60
    hour1 = num % 60
    minute = hour1 % 60
    print(hour, "hours", minute, "minutes")


change_to_hm(71)

