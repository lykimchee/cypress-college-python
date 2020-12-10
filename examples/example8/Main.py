from Movie import Movie


def main():
    m = Movie("My Movie")
    m.add_review(5)
    m.add_review(5)
    m.add_review(4)
    m.add_review(1)
    m.add_review(2)
    m.add_review(3)
    m.add_review(5)
    print(m)
    print("Average score 'My Movie' is:", round(m.get_average(), 2))
    print()

    m2 = Movie("Other Movie")
    m2.add_review(5)
    m2.add_review(5)
    m2.add_review(5)
    m2.add_review(4)
    print(m2)
    print("Average score for 'Other Movie' is:", round(m2.get_average(), 2))


main()
