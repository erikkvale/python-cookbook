_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:

    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def __format__(self, code):
        if code = '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


if __name__=='__main__':
    import doctest
    doctest.testmod()
