# The standard-library random module provides random.choice(), which selects
# one item from the collection of available prophecies.
import random

# Keep game content separate from HTTP handling so the same prediction logic
# can be reused by the console program, Flask API, and future tests.
remarks = [
    "The moon approves, but your Wi-Fi has filed an objection.", 
    "Absolutely. A goose in another dimension has already confirmed it.",
    "The answer is yes, although destiny asks you not to make it weird.",
    "Unclear. The spirits are arguing over who forgot to charge the crystal ball",
    "Your future is loading. Please do not refresh the universe.",
    "A bold 'maybe' echoes through the forbidden spreadsheet.",
    "The prophecy says no. It also says you should blame Mercury, as tradition demands.",
    "Ask again after coffee. Fate refuses to work before sunrise.",
    "The stars predict success, followed by one extremely educational mistake."
]

# Return one randomly selected prophecy. The question is accepted now so the
# function has a stable interface for future question-aware prediction logic.
def fate(question: str) -> str:
    prophecy = random.choice(remarks)
    return prophecy


# Run the original console version only when this file is executed directly.
# Importing fate() from app.py must not print messages or wait for input.
if __name__ == "__main__":
    print("Welcome, traveller!")
    print("Ask me any question, what is bothering you lately?")

    question = input()
    print(fate(question))
