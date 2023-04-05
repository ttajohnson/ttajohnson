# LAB 08: CALCULATE ARI
# Compute the ARI for a given body of text loaded in from a file.
# 4.71(chars/words)+0.5(words/sents)-21.43

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# >>>
ari_scale = {
    1: {"ages": "5-6", "grade_level": "Kindergarten"},
    2: {"ages": "6-7", "grade_level": "1st Grade"},
    3: {"ages": "7-8", "grade_level": "2nd Grade"},
    4: {"ages": "8-9", "grade_level": "3rd Grade"},
    5: {"ages": "9-10", "grade_level": "4th Grade"},
    6: {"ages": "10-11", "grade_level": "5th Grade"},
    7: {"ages": "11-12", "grade_level": "6th Grade"},
    8: {"ages": "12-13", "grade_level": "7th Grade"},
    9: {"ages": "13-14", "grade_level": "8th Grade"},
    10: {"ages": "14-15", "grade_level": "9th Grade"},
    11: {"ages": "15-16", "grade_level": "10th Grade"},
    12: {"ages": "16-17", "grade_level": "11th Grade"},
    13: {"ages": "17-18", "grade_level": "12th Grade"},
    14: {"ages": "18-22", "grade_level": "College"},
}

with open("text.txt", "r") as f:
    contents = f.read()


def character_counter(text):
    text = text.replace(" ", "")
    return len(text)


def word_counter(text):
    text = text.replace(",", "")
    text = text.split(" ")
    return len(text)


def sentence_counter(text):
    text = text.split(".")
    return len(text)


def ari_calculator(chars, words, sents):
    ari_score = 4.71 * (chars / words) + 0.5 * (words / sents) - 21.43
    return round(ari_score)


characters = character_counter(contents)
words = word_counter(contents)
sentences = sentence_counter(contents)
score = ari_calculator(characters, words, sentences)

print(
    f"This text has an ARI-Score of {score}.\nThis text is intended for people aged {ari_scale[score]['ages']} and is considered {ari_scale[score]['grade_level']} level."
)
