class KnowledgeBase:

    def __init__(self, size):
        self.fact = []
        self.size = size
        self.listKnowledge = []
        self.init()

    def init(self):
        for i in range(self.size):
            for j in range(self.size):
                self.listKnowledge.append([])

    def addFact(self, pos, fact):
        self.listKnowledge[pos[0]][pos[1]].append(fact)

    def removeFact(self, pos, fact):
        self.listKnowledge[pos[0]][pos[1]].remove(fact)

