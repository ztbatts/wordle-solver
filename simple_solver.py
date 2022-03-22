from typing import List, Tuple
from enum import Enum, auto


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
        self.prev_guesses = []

    def find_best_guesses(self):
        for candidate_guess in self.word_list:
            for hypothetical_answer in self.word_list:  # scan thru every other possible answer
                if candidate_guess == hypothetical_answer:
                    continue
                # ...


    def is_word_possible(self, word: str) -> bool:
        """ For example,
        word =       A     | P    | P    | L    | E
        prev_guess = A     | L    | I    | K    | E
        clue =       GREEN | GRAY | GRAY | GRAY | GREEN

        """

        for prev_guess, clue in zip(self.prev_guesses, self.clues):  # probs only need to check latest clue...
            for letter, clue_letter, color in zip(word, prev_guess, clue):
        #

    def add_guess(self, guess: str, clue: List[Color]):
        assert len(guess) == self.word_length
        assert len(clue) == self.word_length
        self.prev_guesses.append(guess)
        self.clues.append(clue)
        self.current_guess_number = self.current_guess_number + 1
        if self.current_guess_number > self.max_number_of_guesses:
            print("YOU LOSE")

        for letter, color, possible_letters in zip(guess, clue):
            if color == Color.GREEN:

        # self.word_list = \
        #     [word for word in self.word_list if self.is_word_possible(word)]
        self.word_list = filter(self.is_word_possible, self.word_list)  # trim word list based on current guesses


if __name__ == "__main__":
    solver = BruteForceSolution()
    print(solver.word_list)
