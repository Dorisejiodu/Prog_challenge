

def letter_counter():
    word = input("Enter a word  ")
    letter = input("Enter a letter  ")

    def inner_func():
        counting = word.count(letter)
        return counting
    return inner_func()

print(letter_counter())

