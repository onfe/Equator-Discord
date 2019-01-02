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
        print("Standard input.")
        result = parse(inp)

    return result

def parse(eqn):
    equation = eqn.split()
    out = []
    for word in equation:
        cmp = Compound(word)


class Token:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Element(Token):
    def __init__(self, value):
        self.value = value



class Compound(Token):
    def __init__(self, value):
        self.value = value
        self.quantity = 1

        # use regex to obtain the quantity of the compound
        quantRegex = re.match(r"\d+", self.value)
        if quantRegex:
            self.quantity = int(quantRegex.group(0))
            startpoint = len(quantRegex.group(0))
            self.value = self.value[startpoint:]

        self.elements = self.elementify(self.value)
        print([str(x) for x in self.elements])

    def elementify(self, inp):
        elements = []
        elRegex = re.findall(r"[A-Z][a-z]?\d*", inp)
        for elementString in elRegex:
            elements.append(Element(elementString))

        return elements



if __name__ == '__main__':
    # If called directly from shell, take in the equation from the args.
    import sys

    inp = ' '.join(sys.argv[1:])
    res = equate(inp)
    print(res)
