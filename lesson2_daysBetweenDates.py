def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    days_old = 0
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #create function to define if particular year is leap year
    def leapYear(year):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False
    
    def firstYearDays(year1, month1, day1):
        """
            Function that return a number of days in the fist year
        """
        result = 0

        #set a range of monthes in first year strting from  the month next to month1
        first_monthes = xrange(month1 + 1, 13)

        #for every month in first_monthes add respective value from daysOfMOnths to result
        for x in first_monthes:
            result += daysOfMonths[x-1]

        #check if first year is a leap year and if we have February in our range. If yes, add 1 extra day to result
        if leapYear(year1):
            
            if month1 <= 2:
                result += 1
        #add count of days in very first month to result and return result       
        return result + (daysOfMonths[month1-1] - day1)

    def secondYearDays(year2, month2, day2):

        """
            Function that return a number of days in the last year
        """
        result = 0

        #set a range of monthes in the last year from 1 up to but not including last one 
        second_monthes = xrange(1, month2)

        #for every month in second_monthes add respective value from daysOfMonths to result
        for y in second_monthes:
            result += daysOfMonths[y-1]

        #check if last year is the leap year and we have February in our range. If yes, add 1 extra day to result    
        if leapYear(year2):
            if month2 > 2:
                result += 1

        #add number of days in the very last month to result and return it        
        return result + day2        
                
    #check if year1 is the same as year1
    if year1 == year2:
        #check if month1 is the same as month2
        if month1 == month2:
            #if yes, return the difference between day2 and day1
            days_old = day2 - day1
            return days_old
        else:
            #check if month2 is the next to month1
            if month2 - month1 == 1:
                #if yes, add to days_old the number of days in first month
                days_old += daysOfMonths[month1-1] - day1
                #ad to days_old the number of days in the last month
                days_old += day2
                return days_old
            else:
                #set a range of monthes between month next to month1 up to but not including month2
                monthes = xrange(month1+1, month2)
                for month in monthes:
                    #for every particular month add respective value from daysOfMonths to days_old
                    days_old += daysOfMonths[month-1]
                    #add number of days in first month to days_old
                    days_old += daysOfMonths[month1-1] - day1
                    #add number of days in last month to days_old
                    days_old += day2
                #check if our year is a leap year, and check if we have February in our range. If yes, add 1 extra day ro result    
                if leapYear(year1):
                    if month1 <= 2 or month2 > 2:
                        days_old += 1
                return days_old
    #check if year2 is next to year1        
    elif year2 - year1 == 1:
        #if yes, add the sum of days in year1 and year2 to days_old and return it
        days_old += firstYearDays(year1, month1, day1) + secondYearDays(year2, month2, day2)
        return days_old
    else:
        #set the range of years between year next to year1 and up to but not including year2
        years = xrange(year1+1, year2)
        #for every year in range, check if it is the leap year, and add respective number of days in the year to days_old
        for year in years:
            if leapYear(year):
                days_old += 366
            else:
                days_old += 365
        #add the number of days in the first and last years to days_old and return it
        return days_old + firstYearDays(year1, month1, day1) + secondYearDays(year2, month2, day2)   

            
