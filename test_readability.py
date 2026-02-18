"""Automated tests for readability.py"""

import pytest
from readability import count_letters, count_words, count_sentences, readability


# ── Test texts ────────────────────────────────────────────────────────────────

ONE_FISH = "One fish. Two fish. Red fish. Blue fish."

GREEN_EGGS = (
    "Would you like them here or there? I would not like them here or "
    "there. I would not like them anywhere."
)

DR_SEUSS = (
    "Congratulations! Today is your day. You're off to Great Places! "
    "You're off and away!"
)

HARRY_POTTER = (
    "Harry Potter was a highly unusual boy in many ways. For one thing, "
    "he hated the summer holidays more than any other time of year. For "
    "another, he really wanted to do his homework, but was forced to do "
    "it in secret, in the dead of the night. And he also happened to be "
    "a wizard."
)

GATSBY = (
    "In my younger and more vulnerable years my father gave me some "
    "advice that I've been turning over in my mind ever since."
)

ALICE = (
    'Alice was beginning to get very tired of sitting by her sister on '
    'the bank, and of having nothing to do: once or twice she had peeped '
    'into the book her sister was reading, but it had no pictures or '
    'conversations in it, "and what is the use of a book," thought Alice '
    '"without pictures or conversation?"'
)

MOCKINGBIRD = (
    "When he was nearly thirteen, my brother Jem got his arm badly broken "
    "at the elbow. When it healed, and Jem's fears of never being able to "
    "play football were assuaged, he was seldom self-conscious about his "
    "injury. His left arm was somewhat shorter than his right; when he "
    "stood or walked, the back of his hand was at right angles to his "
    "body, his thumb parallel to his thigh."
)

SHAKESPEARE = (
    "There are more things in Heaven and Earth, Horatio, than are dreamt "
    "of in your philosophy."
)

NINETEEN_EIGHTY_FOUR = (
    "It was a bright cold day in April, and the clocks were striking "
    "thirteen. Winston Smith, his chin nuzzled into his breast in an "
    "effort to escape the vile wind, slipped quickly through the glass "
    "doors of Victory Mansions, though not quickly enough to prevent a "
    "swirl of gritty dust from entering along with him."
)

COMPUTATIONAL = (
    "A large class of computational problems involve the determination of "
    "properties of graphs, digraphs, integers, arrays of integers, finite "
    "families of finite sets, boolean formulas and elements of other "
    "countable domains."
)


# ── count_letters tests ──────────────────────────────────────────────────────

class TestCountLetters:
    def test_one_fish(self):
        assert count_letters(ONE_FISH) == 29

    def test_dr_seuss(self):
        assert count_letters(DR_SEUSS) == 65

    def test_harry_potter(self):
        assert count_letters(HARRY_POTTER) == 214

    def test_gatsby(self):
        assert count_letters(GATSBY) == 96

    def test_computational(self):
        assert count_letters(COMPUTATIONAL) == 184


# ── count_words tests ────────────────────────────────────────────────────────

class TestCountWords:
    def test_one_fish(self):
        assert count_words(ONE_FISH) == 8

    def test_dr_seuss(self):
        assert count_words(DR_SEUSS) == 14

    def test_harry_potter(self):
        assert count_words(HARRY_POTTER) == 56

    def test_gatsby(self):
        assert count_words(GATSBY) == 23

    def test_computational(self):
        assert count_words(COMPUTATIONAL) == 31


# ── count_sentences tests ────────────────────────────────────────────────────

class TestCountSentences:
    def test_one_fish(self):
        assert count_sentences(ONE_FISH) == 4

    def test_dr_seuss(self):
        assert count_sentences(DR_SEUSS) == 4

    def test_harry_potter(self):
        assert count_sentences(HARRY_POTTER) == 4

    def test_gatsby(self):
        assert count_sentences(GATSBY) == 1

    def test_green_eggs(self):
        assert count_sentences(GREEN_EGGS) == 3

    def test_alice(self):
        assert count_sentences(ALICE) == 1


# ── readability tests ────────────────────────────────────────────────────────

class TestReadability:
    def test_before_grade_1(self):
        assert readability(ONE_FISH) == "Before Grade 1"

    def test_grade_2(self):
        assert readability(GREEN_EGGS) == "Grade 2"

    def test_grade_3(self):
        assert readability(DR_SEUSS) == "Grade 3"

    def test_grade_5(self):
        assert readability(HARRY_POTTER) == "Grade 5"

    def test_grade_7(self):
        assert readability(GATSBY) == "Grade 7"

    def test_grade_8_alice(self):
        assert readability(ALICE) == "Grade 8"

    def test_grade_8_mockingbird(self):
        assert readability(MOCKINGBIRD) == "Grade 8"

    def test_grade_9(self):
        assert readability(SHAKESPEARE) == "Grade 9"

    def test_grade_10(self):
        assert readability(NINETEEN_EIGHTY_FOUR) == "Grade 10"

    def test_grade_16_plus(self):
        assert readability(COMPUTATIONAL) == "Grade 16+"
