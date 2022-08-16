import random

hiragana = {
    "a":"あ",
    "i":"い",
    "u":"う",
    "e":"え",
    "o":"お",
    "n":"ん",
    "ka":"か",
    "ki":"き",
    "ku":"く",
    "ke":"け",
    "ko":"こ",
    "sa":"さ",
    "shi":"し",
    "su":"す",
    "se":"せ",
    "so":"そ",
    "ta":"た",
    "chi":"ち",
    "tsu":"つ",
    "te":"て ",
    "to":"と",
    "na":"な",
    "ni":"に",
    "nu":"ぬ",
    "ne":"ね",
    "no":"の",
    "ha":"は",
    "hi":"ひ",
    "fu":"ふ",
    "he":"へ",
    "ho":"ほ",
    "ma":"ま",
    "mi":"み",
    "mu":"む",
    "me":"め",
    "mo":"も",
    "ya":"や",
    "yu":"ゆ",
    "yo":"よ",
    "ra":"ら",
    "ri":"り",
    "ru":"る",
    "re":"れ",
    "ro":"ろ",
    "wa":"わ",
    "wo":"を"
}

def practice_hiragana():

    while True:
        for choice in random.choice(list(hiragana.values())):
            hira_char = choice


        romaji_choice = input(f"What is the romaji equivalent of {hira_char}? ")
        if romaji_choice == "done":
            break
        else:
            try:
                if hira_char == hiragana[romaji_choice]:
                    print("Correct!")
                else:

                    print(f"Incorrect...\n {hira_char} is ", list(hiragana.keys())[list(hiragana.values()).index(hira_char)])
            except KeyError:
                print(f"Incorrect...\n {hira_char} is ", list(hiragana.keys())[list(hiragana.values()).index(hira_char)])


practice_hiragana()