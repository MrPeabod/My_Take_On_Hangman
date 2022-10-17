import random

words = ["Pool", "Mama", "Egg", "Fire", "Arm", "Sun", "Dinner", "Free", "Horse", "Book", "Ice", "Sea", "Home", "Cross",
         "Funny", "House", "Bed", "Door", "Hair", "Hair", "Good", "Rain", "Drink", "Eye", "Blood", "Dog", "abruptly",
         "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon",
         "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful",
         "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness",
         "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves",
         "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack",
         "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy",
         "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess",
         "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice",
         "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging",
         "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte",
         "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph",
         "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays",
         "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz",
         "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz",
         "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy",
         "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway",
         "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant",
         "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka",
         "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey",
         "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone",
         "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper",
         "zodiac", "zombie"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
hangman_fig = [
    """
        +---+
        |   |
            |
            |
            |
            |
      =========""", """
        +---+
        |   |
        0   |
            |
            |
            |
      =========""", """
        +---+
        |   |
        0   |
        |   |
            |
            |
      =========""", """
        +---+
        |   |
        0   |
       /|   |
            |
            |
      =========""", """
        +---+
        |   |
        0   |
       /|\  |
            |
            |
      =========""", """
        +---+
        |   |
        0   |
       /|\  |
       /    |
            |
      =========""", """
        +---+
        |   |
        0   |
       /|\  |
       / \  |
            |
      ========="""
]
list_of_lives = [6, 4, 1]
difficulty = 0
word_to_guess = words[random.randrange(0, len(words)-1, 1)].lower()
guesses = []
guess_bar = "_ "*len(word_to_guess)

print("\nIt seems you want to play some hangman.\nTo get out of the game press control + c.\n")


def choose_game_mode() -> str:
    print("Choose your difficulty:")
    print("(1) Easy (Not up for the challenge?)")
    print("(2) Medium (Hard but fair.)")
    print("(3) Hard (Good luck. You'll need it.)")
    return input("->")


def update_guess_bar(char: str) -> None:
    global guess_bar
    positions = []
    for pos, letter in enumerate(word_to_guess):
        if letter == char:
            positions.append(pos)
    guess_list = list(guess_bar)
    for index in positions:
        guess_list[2*index] = char
    guess_bar = "".join(guess_list)


def check_guess(char: str) -> bool:
    global num_of_lives
    if char in alphabet:
        char = char.lower()
        if char in word_to_guess:
            print(f"\nThe word you are looking for does contain {char}!")
            update_guess_bar(char)
        else:
            print(f"\nThe word you are looking for does not contain {char}!\nYou loose 1 live.\n")
            num_of_lives -= 1
        return True
    else:
        print("Only enter characters a-z\nTry again.\n")
        return False


while difficulty not in [1, 2, 3]:
    try:
        difficulty = int(choose_game_mode())
    except ValueError:
        print("\nI didn't get that. Try using the numbers assigned to each difficulty level.\n")
    else:
        if difficulty not in [1, 2, 3]:
            print("\nMaybe choose a difficulty level that exists!\n")

num_of_lives = list_of_lives[difficulty-1]

while num_of_lives >= 0:
    print(f"\nYou have {num_of_lives} lives remaining.\nChoose wisely.")
    print("Your guesses:", *guesses)
    print(hangman_fig[6-num_of_lives])
    print(guess_bar)
    curr_guess = input("\nYour guess:")

    if curr_guess not in guesses:
        if check_guess(curr_guess):
            guesses.append(curr_guess.lower())
    else:
        print(f"\nYou already guessed {curr_guess}.\nTry again.")

    if num_of_lives == 0:
        print("You are out of lives! You might need to lower the difficulty.\nOr just try again.")
        print(hangman_fig[6-num_of_lives])
        print(f"The word was \"{word_to_guess}\".")
        break

    if guess_bar.replace(" ", "") == word_to_guess:
        print(f"The word was \"{word_to_guess}\".")
        print("Congratulations, you win!")
        break
