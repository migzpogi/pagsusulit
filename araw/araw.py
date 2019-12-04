class Araw(object):

    def foo(self):
        return 1

    def get_number_of_days(self, year):
        """
        Gets the number of days in a year
        :param int year: Year to get the number of days of
        :return int: Number of days
        """

        if year % 4 == 0:
            return 366
        else:
            return 365

        #TODO add more case handling
