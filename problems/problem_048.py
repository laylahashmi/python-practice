# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
sentence = "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

def count_word_frequencies(sentence):
    split_sentence = sentence.split(" ")
    result = {}
    for word in split_sentence:
        if word not in result:
            result[word] = 0
        result[word]+=1
    return result


print(count_word_frequencies(sentence))
