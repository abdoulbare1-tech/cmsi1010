
import random
templates = [
    {
        "test": "A :adjective ghost is behind you!", "author": "abdoul"
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert.", "author": "abdoul"
    },
    {"text": "The :adjective :noun of my family is really :adjective.", "author": "abdoul"
     },
    {
        "text": "The :color :animal :action over the :adjective :plant.", "author": "abdoul"
    },
    {
        "text": "A :adjective :animal ate :number :food for breakfast.", "author": "abdoul"
    },
    {
        "text": "My :adjective :animal danced : adverb in th :place.", "author": "abdoul"
    },
    {
        "text": "yesterday, I saw a :animal wearing a :colour clothing.", "author": "abdoul"
    },
    {
        "text": "The :adjective :person ran :adverb to catch the :vehicle.", "autor": "abdoul"
    },
    {
        "text": "My :adjective :object suddenly turned into a :animal.", "author": "abdoul"
    },
    {
        "text": "The :animal likes to :verb in the :place.", "author": "abdoul"
    }
]
template = random.choice(templates)
yes_answers = {"yes", "y", "si", "sí", "oui"}


def fill_template(template):
    text = template["text"]
    words = text.split()

    for word in words:
        if word.startswith(":"):
            answer = input("Enter a" + word[1:] + ":")
            text = text.replace(word, answer, 1)
    return text


while True:
    template = random.choice(templates)
    story = fill_template(template)

    print("\n" + story)
    print("\nTemplate written by " + template["author"])

    answer = input("\nDo you want to play again?").lower().strip()
    if answer not in yes_answers:
        print("Thanks for playing!")
        break
