import random
words=["office","panda","cabin","ginger"]
random_word=random.choice(words)
display=[]
for latter in random_word:
    display.append("_")
print(display)
guess_latter=input("please guess a latter:").lower()
for position in range(len(random_word)):

    if random_word[position] == guess_latter:
        display[position]=guess_latter
print(display)
print(random_word)
    
