class Movie:
    def __init__(self, name):
        self._name = name
        self._num_reviews = 0
        self._reviews = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def add_review(self, num_stars):
        if num_stars < 1 or num_stars > 5:
            print("Invalid number of stars!")
            return
        self._num_reviews += 1
        self._reviews[num_stars] += 1

    def __str__(self):
        return_string = self.name + "\n"
        return_string += "1 Star: " + str(self._reviews[1]) + "\n"
        return_string += "2 Star: " + str(self._reviews[2]) + "\n"
        return_string += "3 Star: " + str(self._reviews[3]) + "\n"
        return_string += "4 Star: " + str(self._reviews[4]) + "\n"
        return_string += "5 Star: " + str(self._reviews[5]) + "\n"
        return return_string

    def get_average(self):
        total_stars = 0
        for num_stars, num_reviews in self._reviews.items():
            total_stars += num_stars * num_reviews
        return total_stars / self._num_reviews
