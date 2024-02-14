import math;

year = int(input("Enter the year: "));
a = year % 19;
b = math.floor(year / 100);
c = year % 100;
d = math.floor(b / 4);
e = b % 4;
f = math.floor((b+8)/25);
g = math.floor((b-f+1)/3);
h = ((19 * a) + b - d - g + 15) % 30;
i = math.floor(c/4);
k = c % 4;
m = (32 + (2 * e) + (2 * i) - h - k) % 7;
n = math.floor((a + (11 * h) + (22 * m)) / 451);
month = math.floor((h + m  - (7*n) + 114) / 31);
day = 1 + (h + m  - (7 * n) + 114) % 31

print(f"In {year}, Easter will occur on day {day} of month {month}")