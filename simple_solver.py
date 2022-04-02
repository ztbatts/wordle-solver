from typing import List, Tuple
from enum import Enum, auto
import re


def retrieve_word_bank(path_to_txt_file: str) -> List[str]:
    with open(path_to_txt_file) as f:
        lines = f.readlines()
        return [line.strip() for line in lines]  # .strip() removes \n characters


class Color(Enum):
    GREEN = auto()
    YELLOW = auto()
    GRAY = auto()


class BruteForceSolution:
    def __init__(self):
        self.word_length = 5  # 5-letter words only
        self.word_list = retrieve_word_bank('valid-wordle-words.txt')  # these two will shrink after each guess
        self.possible_letters_for_each_position = []
        for _ in range(self.word_length):
            self.possible_letters_for_each_position.append('abcdefghzijklmnopqrstuvwxyz')

        self.current_guess_number = 0
        self.max_number_of_guesses = 6
        self.clues = []
        self.guesses = []

    # def find_best_guesses(self):
    #     for candidate_guess in self.word_list:
    #         for hypothetical_answer in self.word_list:  # scan thru every other possible answer
    #             if candidate_guess == hypothetical_answer:
    #                 continue
    #             # ...

    def is_word_possible(self, word: str) -> bool:
        """ For example,
        word =       A     | P    | P    | L    | E
        prev_guess = A     | L    | I    | K    | E
        clue =       GREEN | GRAY | GRAY | GRAY | GREEN

        """
        for letter, possible_letters in zip(word, self.possible_letters_for_each_position):
            if not possible_letters.__contains__(letter):
                return False
        return True

    def add_guess(self, guess: str, clue: List[Color]):
        assert len(guess) == self.word_length
        assert len(clue) == self.word_length

        self.guesses.append(guess)
        self.clues.append(clue)
        self.current_guess_number = self.current_guess_number + 1
        if self.current_guess_number > self.max_number_of_guesses:
            print("YOU LOSE")

        # for letter, color, possible_letters in zip(guess, clue, self.possible_letters_for_each_position):
        for i in range(self.word_length):
            letter = guess[i]
            color = clue[i]

            if color == Color.GREEN:
                self.possible_letters_for_each_position[i] = letter
            elif color == Color.YELLOW:  # remove the letter from that position
                possible_letters = self.possible_letters_for_each_position[i]
                self.possible_letters_for_each_position[i] = re.sub(letter, '', possible_letters)
            elif color == Color.GRAY:  # remove the letter from all positions
                for j in range(self.word_length):
                    possible_letters = self.possible_letters_for_each_position[j]
                    self.possible_letters_for_each_position[j] = re.sub(letter, '', possible_letters)
            else:
                raise Exception('Wrong COLOR given.')

        # trim word list based on current guesses
        self.word_list = \
            [word for word in self.word_list if self.is_word_possible(word)]


if __name__ == "__main__":
    solver = BruteForceSolution()

    test_str = 'asdfjk'
    new_test_str = re.sub('s', '', test_str)
    print(test_str)
    print(new_test_str)

    guesses_and_clues = [
        ('weird', [Color.GRAY, Color.GRAY, Color.GRAY, Color.GRAY, Color.GRAY]),
        ('shout', [Color.GREEN, Color.GRAY, Color.GREEN, Color.GREEN, Color.GREEN]),
        ('scout', [Color.GREEN, Color.GRAY, Color.GREEN, Color.GREEN, Color.GREEN]),
        ('snout', [Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN]),
    ]

    for guess, clue in guesses_and_clues:
        solver.add_guess(guess, clue)
        print('number of words remaining:', len(solver.word_list))
        print(solver.word_list[0:10])
