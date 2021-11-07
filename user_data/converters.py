class YearConverter:
    regex = '2[0-1][0-9]{2}'

    def to_python(self, value):
        # co robimy z dopasowanym stringiem
        return int(value)

    def to_url(self, value):
        # co robimy ze zmienną kiedy znajdzie
        # się w tagu url jako parametr

        return f"{value}"