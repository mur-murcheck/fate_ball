# import random module
import random

# wright down several ball's remarks
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

# print out greetings and salutations for the user
print("Welcome, traveller!")
# ask him to type in the question
print("Ask me any question, what is bothering you lately?")

# function for random choice of the remark
# the query must be a string and the remark must be a string as well
def fate(question: str) -> str:
    answer = random.choice(remarks)
    return answer

# the question input
question = input()
print(fate(question))