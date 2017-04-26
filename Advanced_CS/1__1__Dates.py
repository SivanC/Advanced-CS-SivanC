class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False
        
    def copy(self):
        """ Returns a new object with the same month, day, year
        as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew
    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
            
    def tomorrow(self):
        """finds the date that occured after the input date
        """
        febDays = 28
        daysInMonth = [0, 31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.day += 1
        
        if daysInMonth[self.month] == 31:
            if self.day == 32:
                self.day = 1
                self.month += 1
        elif daysInMonth[self.month] == 30:
            if self.day == 31:
                self.day = 1
                self.month += 1
        else:
            if self.isLeapYear() == True:
                if self.day == 30:
                    self.day = 1
                    self.month += 1
            elif self.isLeapYear() == False:
                if self.day == 29:
                    self.day = 1
                    self.month += 1
        
        if self.month == 13:
            self.month = 1
            self.year += 1
            
    def yesterday(self):
        """finds the date that occurred before the input date
        """
        febDays = 28
        self.day -= 1
        daysInMonth = [31, 31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.day == 0:
            if daysInMonth[self.month - 1] == 31:
                self.day = 31
                self.month -= 1
            elif daysInMonth[self.month - 1] == 30:
                self.day = 30
                self.month -= 1
            else:
                if self.isLeapYear() == True:
                    self.day = 29
                    self.month -= 1
                else:
                    self.day = 28
                    self.month -= 1
                    
        if self.month == 0:
            self.month = 12
            self.year -= 1

    def addDays(self, numDays):
        """advances the date numDays forward
        """
        i = numDays
        while i > 0:
            self.tomorrow()
            i -= 1
        newDate = Date(self.day, self.month, self.year)
        
    def subDays(self, numDays):
        """subtracts numDays days from a given date
        """
        i = numDays
        while i > 0:
           self.yesterday()
           i -= 1
        newDate = Date(self.day, self.month, self.year)
       
    def isEarlier(self, dateTwo):
        """determines if date is earlier than
        dat2 and returns true or false
        """
        if self.year < dateTwo.year:
            return True
        elif self.year == dateTwo.year:
            if self.month < dateTwo.month:
                return True
            elif self.month == dateTwo.month:
                if self.day < dateTwo.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
            
    def isLater(self, dateTwo):
        """determines if date is later than
        date2 and returns true or false
        """
        if self.year > dateTwo.year:
            return True
        elif self.year == dateTwo.year:
            if self.month > dateTwo.month:
                return True
            elif self.month == dateTwo.month:
                if self.day > dateTwo.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False