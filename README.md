# Readability

## The Coleman-Liau Index

According to [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), E.B. White's *Charlotte's Web* is between a second- and fourth-grade reading level, and Lois Lowry's *The Giver* is between an eighth- and twelfth-grade reading level. What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of "readability tests" have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

``` text
index = 0.0588 * L - 0.296 * S - 15.8
```

where `L` is the average number of letters per 100 words in the text, and `S` is the average number of sentences per 100 words in the text.

It turns out that counting the number of letters, words, and sentences in a passage of text and plugging them into this formula gives a surprisingly accurate estimate of reading level. Let's write a program that does just that!

---

## Getting Started

**Be sure you are working in the GitHub Classroom. To confirm, on startup, you should see a single `$` in the terminal. If you are unsure, stop by during office hours.** 

Before you begin coding, create a folder for this assignment and navigate into it:
```bash
mkdir readability
cd readability
```

Next, download the test suite that will help you verify your solution:
```bash
wget https://raw.githubusercontent.com/SEU-Academics/readability/main/test_readability.py
```

Finally, create your Python file where you'll write your solution:
```bash
code readability.py
```

Your folder should now contain:
- `readability.py` (your solution file — currently empty)
- `test_readability.py` (the automated test suite)

Read the directions in their entirety before beginning. Good luck and have fun!

---

## Assignment Instructions

Write a program that calculates the Coleman-Liau reading level of a given text. Your program must include the four functions described in the Required Functions section below. Here are examples of the program's behavior:

```python
>>> text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
>>> count_letters(text)
65
>>> count_words(text)
14
>>> count_sentences(text)
4
>>> readability(text)
'Grade 3'
```

The text has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 × 100 = 464.29). And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 × 100 = 28.57). Plugged into the Coleman-Liau formula, and rounded to the nearest integer, we get an answer of 3 (because 0.0588 × 464.29 − 0.296 × 28.57 − 15.8 = 3): so this passage is at a third-grade reading level.

```python
>>> text = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
>>> count_letters(text)
214
>>> count_words(text)
56
>>> count_sentences(text)
4
>>> readability(text)
'Grade 5'
```

This text has 214 letters, 4 sentences, and 56 words. That comes out to about 382.14 letters per 100 words, and 7.14 sentences per 100 words. Plugged into the Coleman-Liau formula, we get a fifth-grade reading level.

```python
>>> text = "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."
>>> readability(text)
'Grade 16+'
```

This text scores high enough on the index that the function returns `Grade 16+` instead of the exact number.

---

## Required Functions

Your `readability.py` file must define the following four functions. All four will be tested individually by the automated test suite.

| Function | Parameters | Returns | Description |
|---|---|---|---|
| `count_letters(text)` | `text` (str) | `int` | Returns the number of letters (a–z, A–Z) in the text. |
| `count_words(text)` | `text` (str) | `int` | Returns the number of words in the text. A word is any sequence of characters separated by spaces. |
| `count_sentences(text)` | `text` (str) | `int` | Returns the number of sentences in the text. A sentence ends with a `.`, `!`, or `?`. |
| `readability(text)` | `text` (str) | `str` | Calls the three helper functions above, computes the Coleman-Liau index, and returns the grade level as a string (see Specification below). |

Your `readability` function **must** call `count_letters`, `count_words`, and `count_sentences` rather than duplicating their logic.

---

## Specification

* In `readability.py`, implement the four functions listed in the Required Functions section.
* You may assume that a letter is any lowercase character from `a` to `z` or any uppercase character from `A` to `Z`, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
* The `readability` function should return `"Grade X"` where `X` is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
* If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), the function should return `"Grade 16+"` instead of giving the exact index number.
* If the index number is less than 1, the function should return `"Before Grade 1"`.

---

## Advice

Learning how to debug is a valuable skill in programming. We encourage you to attempt this problem independently before consulting the hints below. If you find yourself stuck for more than 15 minutes, take a short break—sometimes stepping away helps ideas surface. If you're still stuck after your break, feel free to expand the collapsible sections in the Advice below for guidance.

<details>
<summary><strong>Write some code that you know will run</strong></summary>

Even though these functions won't do anything useful yet, they should at least run without errors. Start by defining all four function stubs:
```python
def count_letters(text):
    # TODO: count and return the number of letters
    pass

def count_words(text):
    # TODO: count and return the number of words
    pass

def count_sentences(text):
    # TODO: count and return the number of sentences
    pass

def readability(text):
    # TODO: use the helpers to compute and return the grade level
    pass
```

</details>

<details>
<summary><strong>Write some pseudocode before writing more code</strong></summary>

If unsure how to solve the problem itself, break it down into smaller problems that you can probably solve first. Each function is its own small problem:

**`count_letters`:**
1. Start a counter at 0.
2. Loop through each character in the text.
3. If the character is a letter, increment the counter.
4. Return the counter.

**`count_words`:**
1. Split the text by spaces.
2. Return the number of parts.

**`count_sentences`:**
1. Start a counter at 0.
2. Loop through each character in the text.
3. If the character is `.`, `!`, or `?`, increment the counter.
4. Return the counter.

**`readability`:**
1. Call the three helper functions to get letter, word, and sentence counts.
2. Calculate `L` (average letters per 100 words).
3. Calculate `S` (average sentences per 100 words).
4. Plug `L` and `S` into the Coleman-Liau formula.
5. Round the result to the nearest integer.
6. Return the appropriate grade string.

</details>

<details>
<summary><strong>Implementing count_letters</strong></summary>

To count letters, you need to loop through each character in the text and check whether it is alphabetic. Python's `.isalpha()` method is useful here:
```python
def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters
```

Alternatively, you could check if a character falls within the ranges `a`–`z` or `A`–`Z`.

</details>

<details>
<summary><strong>Implementing count_words</strong></summary>

Since any sequence of characters separated by spaces counts as a word, Python's `.split()` method is a convenient way to count words:
```python
def count_words(text):
    return len(text.split())
```

The `.split()` method splits a string by whitespace and returns a list of the parts. The length of that list is the word count.

</details>

<details>
<summary><strong>Implementing count_sentences</strong></summary>

A sentence ends with a period (`.`), exclamation point (`!`), or question mark (`?`). You can count how many of these characters appear in the text:
```python
def count_sentences(text):
    sentences = 0
    for char in text:
        if char in '.!?':
            sentences += 1
    return sentences
```

</details>

<details>
<summary><strong>Implementing readability</strong></summary>

Now bring it all together. Call your helper functions, compute the index, and handle the special cases:
```python
def readability(text):
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    grade = round(index)

    # Return the appropriate string based on the grade
```

Use conditional statements to return the correct string based on the value of `grade`.

</details>

---

## Testing

As you develop your solution, you can manually test your functions with the examples provided above. Test the helper functions individually before testing `readability` — this makes it much easier to track down bugs.

**Helper function tests:**

* `count_letters("One fish. Two fish. Red fish. Blue fish.")` should return `29`.
* `count_words("One fish. Two fish. Red fish. Blue fish.")` should return `8`.
* `count_sentences("One fish. Two fish. Red fish. Blue fish.")` should return `4`.
* `count_letters("Congratulations! Today is your day. You're off to Great Places! You're off and away!")` should return `65`.
* `count_words("Congratulations! Today is your day. You're off to Great Places! You're off and away!")` should return `14`.
* `count_sentences("Congratulations! Today is your day. You're off to Great Places! You're off and away!")` should return `4`.

**Readability function tests:**

* `readability("One fish. Two fish. Red fish. Blue fish.")` should return `"Before Grade 1"`.
* `readability("Would you like them here or there? I would not like them here or there. I would not like them anywhere.")` should return `"Grade 2"`.
* `readability("Congratulations! Today is your day. You're off to Great Places! You're off and away!")` should return `"Grade 3"`.
* `readability("Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.")` should return `"Grade 5"`.
* `readability("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.")` should return `"Grade 7"`.
* `readability("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \"and what is the use of a book,\" thought Alice \"without pictures or conversation?\"")` should return `"Grade 8"`.
* `readability("When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.")` should return `"Grade 8"`.
* `readability("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.")` should return `"Grade 9"`.
* `readability("It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.")` should return `"Grade 10"`.
* `readability("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.")` should return `"Grade 16+"`.

### Automated Testing

Once you're confident in your solution, you can run the full automated test suite. The test suite you downloaded in the Getting Started section will check all four functions against the required test cases.

To run the automated tests, use the following command in your terminal:
```bash
pytest test_readability.py
```

The test suite will run all test cases and show you which ones pass and which ones fail. If any tests fail, the output will show you what was expected versus what your program produced, helping you debug your solution.

**Note:** Make sure you're in the `readability` directory when running the test command, and that both `readability.py` and `test_readability.py` are in the same folder.

---

## Submission

Ensure all tests pass before the due date and submit your GitHub username with the homework. Your submission will be reviewed through GitHub Classroom.

