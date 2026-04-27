h = int(input('Hours - '))
min = int(input('Minutes - '))
sec = int(input('Seconds - '))

dr_h = int(input('Dr_Hours - '))
dr_min = int(input('Dr_Minutes - '))
dr_sec = int(input('Dr_Seconds - '))

time_h = (h + dr_h) % 24  + ((min + dr_min) // 60)
time_min =(min + dr_min) % 60 + ((sec + dr_sec) // 60)
time_sec =(sec + dr_sec) % 60
print(f"Hours - {time_h} Minutes - {time_min} Seconds - {time_sec}")
