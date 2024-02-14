class LeapYear:
    def __init__(self, start_year=2000, end_year=2100):
        self.start_year = start_year
        self.end_year = end_year

    def __iter__(self):
        return LeapYearIterator(self.start_year, self.end_year)

class LeapYearIterator:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
        if start_year % 4 == 0 and (start_year % 400 == 0 and start_year % 400 == 0):
            self.current_leap = start_year
        else:
            if start_year % 4 != 0:
                if start_year + (4 - start_year % 4) % 400 == 0:
                    self.current_leap = start_year + (4 - start_year % 4) + 4
                else:
                    self.current_leap = start_year + (4 - start_year % 4)
            else:
                self.current_leap = start_year + 4
                
    def __next__(self):
        if self.current_leap < self.end_year:
            current = self.current_leap
            if (self.current_leap + 4) % 400 == 0 and (self.current_leap + 4) % 100 != 0:
                self.current_leap += 8
            elif (self.current_leap + 4) % 400 == 0:
                self.current_leap += 8
            else:
                self.current_leap += 4
            return current
        else:
            raise StopIteration()

# leap_year_sequence = LeapYear(1978, 2023)
# for leap_year in leap_year_sequence:
    # print(leap_year, "is a leap year")
# 1980 is a leap year
# 1984 is a leap year
# 1988 is a leap year
# 1992 is a leap year
# 1996 is a leap year
# 2000 is a leap year
# 2004 is a leap year
# 2008 is a leap year
# 2012 is a leap year
# 2016 is a leap year
# 2020 is a leap year
# leap_year_sequence = LeapYear(1892, 1906)
# for leap_year in leap_year_sequence:
    # print(leap_year, "is a leap year")
# 1892 is a leap year
# 1896 is a leap year
# 1904 is a leap year
leap_year_sequence = LeapYear()
for leap_year in leap_year_sequence:
    print(leap_year, "is a leap year")
    
# 2000 is a leap year
# 2004 is a leap year
# 2008 is a leap year
# 2012 is a leap year
# 2016 is a leap year
# 2020 is a leap year
# 2024 is a leap year
# 2028 is a leap year
# 2032 is a leap year
# 2036 is a leap year
# 2040 is a leap year
# 2044 is a leap year
# 2048 is a leap year
# 2052 is a leap year
# 2056 is a leap year
# 2060 is a leap year
# 2064 is a leap year
# 2068 is a leap year
# 2072 is a leap year
# 2076 is a leap year
# 2080 is a leap year
# 2084 is a leap year
# 2088 is a leap year
# 2092 is a leap year
# 2096 is a leap year
class LeapYear:
    def __init__(self, start_year=2000, end_year=2100):
        self.start_year = start_year
        self.end_year = end_year

    def __iter__(self):
        return LeapYearIterator(self.start_year, self.end_year)

class LeapYearIterator:
    def __init__(self, start_year, end_year):
        self.start_year = start_year
        self.end_year = end_year
        while self.start_year % 4 != 0:
            self.start_year += 1
        self.current_year = self.start_year-4

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_year <= self.end_year-4:
            self.current_year += 4
            
            if self.current_year % 400 == 0:
                return self.current_year
            
            elif self.current_year % 100 == 0:
                
                self.current_year += 4
                if self.current_year >= self.end_year:
                    raise StopIteration
                return self.current_year
            
            return self.current_year
        
        else:
            raise StopIteration
