class Araw(object):

    def get_number_of_days(self, year):
        """
        Gets the number of days in a year
        :param int year: Year to get the number of days of
        :return int: Number of days
        """

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 366
                else:
                    return 365
            else:
                return 366
        else:
            return 365

    def days_to_year_ratio(self, number_of_days, year):
        """
        Ratio between the given number of days compared to the total number of days in a year
        :param int number_of_days: Number of days given
        :param int year: Year
        :return float: Percentage
        """

        total_days = self.get_number_of_days(year)
        return round((number_of_days/total_days) * 100, 2)

    def accuracy(self, frequency, year):
        """
        Shows the percentage of correctness for events happening on a a year
        :param int frequency: The number of times an event happens in a year
        :param int year: Year
        :return float: Accuracy rounded up to two decimal places
        """

        ratio = self.days_to_year_ratio(frequency, year)
        return round(100 - ratio, 2)

    def once_a_year_event(self, year):
        """
        Shows the accuracy of the app for events happening once a year
        :param int year: Year
        :return:
        """

        return self.accuracy(1, year)
