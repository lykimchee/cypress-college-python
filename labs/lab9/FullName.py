class FullName:
    def __init__(self, last, first):
        self.last = last.lower()
        self.first = first.lower()

    def __str__(self):
        return self.first[:1].upper() + self.first[1:].lower() + " " + self.last[:1].upper() + self.last[1:].lower()

    def __eq__(self, other):
        return self.last == other.last and self.first == other.first

    def __gt__(self, other):
        if self.last == other.last:
            return self.first > other.first
        return self.last > other.last
