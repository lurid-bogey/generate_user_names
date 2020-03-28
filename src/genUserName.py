import secrets

from wordlists import NOUNS, ADJECTIVES


if __name__ == '__main__':
    theNoun = secrets.choice(NOUNS)
    theAdj = secrets.choice(ADJECTIVES)

    print(f'Username: {theAdj.capitalize()}_{theNoun.capitalize()}')
