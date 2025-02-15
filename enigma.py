'''
references :-
Computerphile gave a really simple version of the Enigma machine which helped me to start with an easy code :
https://youtu.be/RzWB5jL5RX0?si=ve3n3qK2HILG1jkk

This website clearly explained that there are ring positions in rotors :
https://www.dcode.fr/enigma-machine-cipher

To get the reflectors and rotors :
https://en.wikipedia.org/wiki/Enigma_rotor_details

The caeser cipher between rotors was the hardest to understand, this simulation showed the exact connections between rotors :
https://piotte13.github.io/enigma-cipher/

'''
from flask import render_template
import unicodedata


def remove_accents(text):
    # I completely forgot about accents in letters, a friend of mine tested and told me that
    # accents were causing problems. So, I added the following to remove all accents  (thanks jojo)
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')


def encryption(plaintext, rotors_choice, rotors_pos, reflector_type, rotors, reflectors):

    encrypted_text = list(remove_accents(plaintext.upper()))
    for i in range(len(encrypted_text)):

        if encrypted_text[i].isalpha():
            # moving rotors
            for j in range(len(rotors_pos)):
                rotors_pos[j] += 1
                if rotors_pos[j] >= 26:
                    rotors_pos[j] = 1
                else:
                    break

            letter = encrypted_text[i]

            # going through rotors and finally through reflector
            for j in range(0, len(rotors_choice)):
                # caeser cipher
                if j == 0:
                    letter = chr(((ord(letter) - ord("A")) + rotors_pos[j] - 1) % 26 + ord("A"))
                else:
                    letter = chr(((ord(letter) - ord("A")) +
                                 rotors_pos[j] - rotors_pos[j - 1]) % 26 + ord("A"))

                # rotor lookup
                letter = rotors[rotors_choice[j]][ord(letter) - ord("A")]

            letter = chr(((ord(letter) - ord("A")) + 26 -
                         rotors_pos[len(rotors_choice) - 1] + 1) % 26 + ord("A"))
            # reflector
            letter = reflectors[reflector_type][ord(letter) - ord("A")]

            # leaving reflector and through rotors
            for j in range(len(rotors_choice) - 1, -1, -1):
                # ceaser cipher
                if j == len(rotors_choice) - 1:
                    letter = chr(((ord(letter) - ord("A")) + rotors_pos[j] - 1) % 26 + ord("A"))
                else:
                    letter = chr(((ord(letter) - ord("A")) +
                                 rotors_pos[j] - rotors_pos[j + 1]) % 26 + ord("A"))

                # rotor lookup
                letter = chr(rotors[rotors_choice[j]].index(letter) + ord("A"))

            letter = chr(((ord(letter) - ord("A")) + 26 - rotors_pos[0] + 1) % 26 + ord("A"))

            encrypted_text[i] = letter
    return ''.join(encrypted_text)


def apology(message, code=400):
    # Code from Finance Problem Set
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code
