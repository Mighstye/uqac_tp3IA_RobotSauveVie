class Rule:

    def __init__(self, condition, consequence):
        self.condition = condition
        self.consequence = consequence

    def __str__(self):
        return str(self.condition)+str(self.consequence)
