class KnowledgeBase:

    def __init__(self, size):
        self.fact = []
        self.size = size
        self.listKnowledge = [[[] for i in range(size)] for j in range(size)]


    def addFact(self, pos, fact):
        self.listKnowledge[pos[0]][pos[1]].append(fact)

    def removeFact(self, pos, fact):
        self.listKnowledge[pos[0]][pos[1]].remove(fact)

