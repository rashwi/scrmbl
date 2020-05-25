import time
from constants import ScrmblConstants

def keyprint(sentence):
    print(sentence, end="\r")
    time.sleep(ScrmblConstants.KEY_DISPLAY_TIME)

    print(" " * ScrmblConstants.SENTENCE_LENGTH)


if __name__ == "__main__":
    keyprint('blue')

