import random
words = [
    "apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape",
    "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
    "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "apricot", "blackberry", "cantaloupe",
    "date", "eggplant", "feijoa", "guava", "huckleberry", "imbe", "jackfruit",
    "kumquat", "lime", "mulberry", "nectar", "olive", "persimmon", "quararibea",
    "rambutan", "soursop", "tomato", "ugni", "voavanga", "wolfberry", "ximenia",
    "yellowfruit", "ziziphus"
]
def help():
 for i in range(0, len(words), 10):
    print(words[i:i+10])
    input("Press Enter for more...")
help()
random = random.choice(words)
attempt = 0

while True:
 answer = input(f"Choose a word between these words:\n >")
 if answer == "help":
     help()
     continue
 if answer == random:
   print(f"Correct the answer was {random}")
   break
 else:
  attempt +=1