class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: # change 0 < to 0 <=
            return 50
        elif 13 <= age <= 20: # change < 20 to <= 20
            return 100
        elif 21 <= age <= 60: # change 21 < to 21 <=
            return 150
        # on this line have no error but have one false that is joint between worker(21-60)
        # then i change >= 60 to > 60
        elif age > 60:
            return 100