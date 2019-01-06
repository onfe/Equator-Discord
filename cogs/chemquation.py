import re

def equate(inp):

    # Check if the input contains mixed text and equations.
    m = re.search(r"(#{.+})", inp)
    if m is not None:
        # contains both, split text and equations.
        print("Mixed input.")
        pass
    else:
        # contains only equation, go straight to the parser.
        result = parse(inp)

    return result

def parse(eqn):
    equation = eqn.split()
    out = []
    for word in equation:
        comp = str(Compound(word))

        for word, replace in Lookup.keywords.items():
            comp = comp.replace(word, replace)

        out.append(comp)

    return ' '.join(out)

class Lookup:
    superscriptDict = {
        '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵',
        '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰',
        '+': '⁺', '-': '⁻'
    }

    subscriptDict = {
        '1': '₁', '2': '₂', '3': '₃', '4': '₄', '5': '₅',
        '6': '₆', '7': '₇', '8': '₈', '9': '₉', '0': '₀',
        '+': '₊', '-': '₋'
    }

    keywords = {
        '<=>': '⇌',
        '=>': '→',
        '[e]': '*e⁻*',
        '[h]': 'H⁺',
        '[oh]': 'OH⁻',
        '[D]': 'Δ',
        '[d]': 'δ',
        '[pi]': 'π',
        '[S]': 'Σ',
        '*': '·'
    }

    state = {
        's': '₍𝓼₎',
        'l': '₍𝓁₎',
        'g': '₍𝓰₎',
        'aq': '₍𝒶𝓆₎'
    }


class Token:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Element(Token):
    def __init__(self, value):
        self.value = value
        self.quantity = 1

        m = re.search(r"\d+", self.value)
        if m and len(m.group(0)) > 0:
            self.quantity = int(m.group(0))
            self.value = self.value[:m.start()]

    def __str__(self):
        sub = ''
        if self.quantity > 1:
            for char in str(self.quantity):
                sub = sub + Lookup.subscriptDict[char]

        return self.value + sub



class Compound(Token):
    def __init__(self, value):
        self.value = value
        self.quantity = 1
        self.state = None
        self.charge = 0

        # extract the quantity, if it exists, using regex.
        quantRegex = re.match(r"\d+", self.value)
        if quantRegex:
            self.quantity = int(quantRegex.group(0))
            startpoint = len(quantRegex.group(0))
            self.value = self.value[startpoint:]

        # extract the state, if it exists, using regex.
        stateRegex = re.search(r"@(s|l|g|aq)", self.value)
        if stateRegex:
            self.state = stateRegex.group(1)
            before = self.value[:stateRegex.start()]
            after = self.value[stateRegex.end():]
            self.value = before + after

        self.items = self.elementify(self.value)

    def elementify(self, inp):
        remainingString = inp
        elements = []

        while True:

            m = re.search(r"[A-Z][a-z]?\d*", remainingString)
            if not m:
                # no more elements, break out.
                break

            if m.start() > 0:
                elements.append(remainingString[:m.start()])

            remainingString = remainingString[m.end():]
            elements.append(Element(m.group(0)))

        elements.append(remainingString)

        return elements



    def __str__(self):
        quantity = str(self.quantity) if self.quantity > 1 else ''
        compound = ''.join([str(x) for x in self.items])
        state = Lookup.state[self.state] if self.state else ''
        return quantity + compound + state



if __name__ == '__main__':
    # If called directly from shell, take in the equation from the args.
    import sys

    inp = ' '.join(sys.argv[1:])
    res = equate(inp)
    print(res)
