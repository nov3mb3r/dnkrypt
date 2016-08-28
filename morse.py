morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

decoding = {}
for key, val in morse.items(): decoding[val] = key

def encode(text):
    # should really pre-process {'.': 'stop', ',': 'comma', '-': 'dash', ...}
    return ' '.join(map(lambda x, g=morse.get: g(x, ' '), text.upper()))

def decode(message):
    ans = ''.join(map(lambda x, g=decoding.get: g(x, ' '), message.split(' ')))
    return ' '.join(ans.split()) # tidy up spacing

def decipher(message):
    # like decode, but when there are no spaces.
    row = [ ( '', message ) ]
    while filter(lambda x: x[1], row):
        old = row
        row = []
        for it in old:
            txt, code = it
            if code:
                for (t, c) in morse.items():
                    if code[:len(c)] == c:
                        row.append((txt + t, code[len(c):]))
                # NB we discard it if no initial segment of code matches an encoding.
            else: row.append(it)

    return map(lambda it: it[0], row)

if __name__ == '__main__':
    import sys
