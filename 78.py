# Function to count word occurrences in a list of sentences without using string module
def count_word_occurrences(sentences):
    word_count = {}

    # Custom punctuation characters to remove
    punctuation = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for sentence in sentences:
        # Remove punctuation and convert to lowercase
        sentence = ''.join([char for char in sentence if char not in punctuation])
        words = sentence.lower().split()
        
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

# Example list of sentences
sentences = [
    "This is a sample sentence.",
    "Count occurrences of words in this sentence.",
    "This is another sentence with repeated words.",
]

word_occurrences = count_word_occurrences(sentences)

# Print word occurrences
for word, count in word_occurrences.items():
    print(f"'{word}': {count}")
