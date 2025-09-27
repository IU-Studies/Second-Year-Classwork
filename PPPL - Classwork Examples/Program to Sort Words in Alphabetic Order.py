#Program to Sort Words in Alphabetic Order

def sort_words(words):
    words.sort()
    return words

word_list = ["Cookie", "Apple", "Soup", "Waffel", "Burger"]

sorted_words = sort_words(word_list)

print(sorted_words)
