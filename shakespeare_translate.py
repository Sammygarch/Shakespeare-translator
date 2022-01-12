__author__ = "Sammy Garcia s@mmygarcia.com"
__version__ = "0.0.0"









def shakespeare_translate(words):
    words = words.lower().split(" ")


    for word in words:
        word_index = words.index(word)

        if word == "you":
            words[word_index] = "thou"

        elif word == "your":
            words[word_index] = "thy"

        elif word == "yours":
            words[word_index] = "thine"

        elif word == "reject":
            words[word_index] = "abhor"

        elif word == "perfect":
            words[word_index] = "absoloute"

        elif word == "tendency" or word == "proneness":
            words[word_index] = "addiction"

        elif word == "hesitated" or word == "disputed":
            words[word_index] = "balked"

        elif word == "handsome":
            words[word_index] = "brave"

        elif word == "letter" or word == "word":
            words[word_index] = "character"

        elif word == "distress" or word == "trouble":
            words[word_index] = "coil"

        elif word == "clever":
            words[word_index] = "cunning"

        elif word == "accusation":
            words[word_index] = "delation"

        elif word == "merit" or word == "reward":
            words[word_index] = "deserving"

        elif word == "equal":
            words[word_index] = "egal"

        elif word == "quickness":
            words[word_index] = "expedience"

        elif word == "desired":
            words[word_index] = "fancied"

        elif word == "oppose" or word == "affront" or word == "object":
            words[word_index] = "front"

        elif word == "scared" or word == "aghast":
            words[word_index] = "gast"

        elif word == "bury":
            words[word_index] = "grave"

        elif word == "sad" or word == "painful" or word == "mournful":
            words[word_index] = "heavy"

        elif word == "honest":
            words[word_index] = "pure"

        elif word == "given":
            words[word_index] = "inherit"

        elif word == "fair" or word == "equitable":
            words[word_index] = "judicious"

        elif word == "hit" or word == "strike":
            words[word_index] = "knap"

        elif word == "servant" or word == "boy":
            words[word_index] = "knave"

        elif word == "yard":
            words[word_index] = "land"

        elif word == "shocked" or word == "overcome":
            words[word_index] = "lapsed"

        elif word == "crazy" or word == "wild":
            words[word_index] = "mad"

        elif word == "confuse" or word == "match":
            words[word_index] = "mate"

        elif word == "bill" or word == "list":
            words[word_index] = "note"

        elif word == "promised":
            words[word_index] = "ought"

        elif word == "difficult":
            words[word_index] = "painful"

        elif word == "consider":
            words[word_index] = "perpend"

        elif word == "beautiful" or word == "ornate":
            words[word_index] = "quaint"

        elif word == "shake" or word == "tremble":
            words[word_index] = "quake"

        elif word == "ecstasy":
            words[word_index] = "rapture"

        elif word == "hunger":
            words[word_index] = "ravin"

        elif word == "forethought" or word == "consideration":
            words[word_index] = "respect"

        elif word == "retreat":
            words[word_index] = "retire"

        elif word == "admit":
            words[word_index] = "shrift"

        elif word == "counterfeit":
            words[word_index] = "simular"

        elif word == "always" or word == "forever":
            words[word_index] = "still"

        elif word == "acquiescence" or word == "obediance":
            words[word_index] = "subscription"

        elif word == "overtake" or word == "enthrall":
            words[word_index] = "take"

        elif word == "blame" or word == "censure":
            words[word_index] = "tax"

        elif word == "worrisome":
            words[word_index] = "testy"

        elif word == "triangle":
            words[word_index] = "trigon"

        elif word == "idiotic" or word == "inane":
            words[word_index] = "unpregnant"

        elif word == "disgusting" or word == "hateful":
            words[word_index] = "vile"

        elif word == "vengeful":
            words[word_index] = "vindictive"

        elif word == "wide-eyed" or word == "angry" or word == "surprised":
            words[word_index] = "wall-eyed"

        elif word == "lack":
            words[word_index] = "want"

        elif word == "why":
            words[word_index] = "wherefore"

        elif word == "prepared" or word == "ready":
            words[word_index] = "yare"

        elif word == "recent":
            words[word_index] = "young"

        elif word == "clownish":
            words[word_index] = "zany"

    return " ".join(words)
