import string


def count_words(text):
    words = text.split()
    return len(words)

def longest_words(text):
    words = text.split()
    if not words:
        return []

    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]


def word_frequency(text):
    words = text.lower().split()
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def average_word_length(text):
    words = text.split()
    if len(words) == 0:
        return 0 
    total_length = 0
    for word in words:
        total_length += len(word)

    average_length = total_length / len(words)
    return average_length

# TEST  FUNCTIONS 
if __name__ == "__main__":
    sample_text = """
    The quick brown fox jumps over the lazy dog the fox
    """

    print("Total words:", count_words(sample_text))
    print("Average word length:", round(average_word_length(sample_text), 2))
    print("Longest words:", longest_words(sample_text))
    print("Word Frequencies:", word_frequency(sample_text))