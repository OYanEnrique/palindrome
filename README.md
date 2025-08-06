# palindrome
A Python script that checks if a user-provided word or phrase is a palindrome (reads the same backward as forward).

# 🔄 Palindrome Checker

This is a command-line Python program that determines if a word or phrase entered by the user is a palindrome.

A palindrome is a word or phrase that, after removing spaces and ignoring case, reads the same forwards and backward. The script prompts the user for an input, processes it to remove spaces, and compares it to its reversed version to give the verdict.

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `Palindrome.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python Palindrome.py
    ```
5.  Type the word or phrase you want to check and press Enter to see the result.

## Program Logic

* **Input and Processing:**
    * The program prompts for a word or phrase using `input()`.
    * The string is immediately processed: all spaces are removed with `user_word.replace(' ', '')` and all characters are converted to lowercase with `.lower()`. This ensures the comparison is not affected by case or spacing (e.g., "Taco cat" becomes "tacocat").
* **String Reversal:**
    * The "magic" of reversing the string happens with Python's string slicing technique: `check_word[ : :-1]`. This command creates a copy of the string, but read from the end to the beginning.
* **Final Check:**
    * A simple `if/else` structure compares the processed string with its reversed version. If they are identical, the original input is a palindrome.
