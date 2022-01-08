class FourDigitYearConverter:
    # 127.0.0.1:8000/2020/
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # 2020
        return '%04d' % value
