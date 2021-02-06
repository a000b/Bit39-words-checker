FILE_NAME = "bip39_en_words.txt"


def load_words() -> list:
    """Loading words from file
    """

    with open(FILE_NAME, "r") as f:
        wordlist = [w.strip() for w in f.readlines()]
    return wordlist


def get_position(searched_word: str, words: list) -> int:
    """Finding position of the given word on the list
    """

    try:
        return words.index(searched_word)
    except:
        return -1


def get_word(position_number: int, words: list) -> str:
    """Finding word on the list

    """

    try:
        return words[position_number]
    except:
        return 'err'


if __name__ == '__main__':

    choice = int(input("1 -  get positions, 2 - get words: "))
    bip39_list = load_words()

    if choice == 1:
        given_seed = input('Enter your seed: ').strip().split(' ')

        for word in given_seed:
            pos = get_position(word, bip39_list)
            if pos != -1:
                print(pos, end=' ')
            else:
                print(f'\nErr no position found for {word}')

    elif choice == 2:
        given_positions = input('Enter your numbers: ').strip().split(' ')

        for number in given_positions:
            word = get_word(int(number), bip39_list)
            if word != 'err':
                print(word, end=' ')
            else:
                print(f'\nErr no word for position {number} found.')

