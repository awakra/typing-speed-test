def get_word_list():
    """
    Reads a file named 'words_alpha.txt' and returns a list of words.

    The function opens the file in read mode with UTF-8 encoding, processes each line
    to strip any leading or trailing whitespace, and filters out empty lines. The resulting
    list contains all non-empty words from the file.

    Returns:
        list: A list of words (strings) from the 'words_alpha.txt' file.
    """
    with open("words_alpha.txt", "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
            return words
        