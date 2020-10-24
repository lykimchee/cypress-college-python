def main():
    words_dictionary = {}
    with open("quote.txt") as file:
        for i, line in enumerate(file):
            for word in line.split():
                if word in words_dictionary:
                    words_dictionary[word].append(i+1)
                else:
                    line_positions = [i+1]
                    words_dictionary[word] = line_positions
    for each_word in words_dictionary:
        print(each_word, *words_dictionary[each_word])


main()
