from src.env_objects.expert_sys.Rule import Rule


class Rules_base:

    def rulesOfGame(self):
        listOfRules = []

        #Liste des règles

        #Si il y a de la chaleur, les cases autour de celle-ci pourraient avoir un feu
        rule1 = Rule(["warm"], ["fire in neighboor"])
        listOfRules.append(rule1)

        #Si il y a des poussières, les cases autour pourraient avoir des décombres
        rule2 = Rule(["dust"], ["ruins in neighboor"])
        listOfRules.append(rule2)

        #Si il y a des cris, le robot a trouvé la victime
        rule3 = Rule(["scream"], ["human"])
        listOfRules.append(rule3)

        #Si il y a un feu, le robot l'éteint
        rule4 = Rule(["fire"], ["extinguish"])
        listOfRules.append(rule4)

        #Si il y a un feu et ??, le robot contourne le feu
        rule5 = Rule(["fire"], ["avoid"])
        listOfRules.append(rule5)

        #Si il y a des ruines, le robot contourne les ruines
        rule6 = Rule(["ruins"], ["avoid"])
        listOfRules.append(rule6)

        #Si il n'y a rien dans le voisinage ou sur la case du robot, suivre parcourt
        rule7 = Rule(["nothing"], ["continue"])
        listOfRules.append(rule7)

        #Si le robot éteint le feu, le feu est supprimer et les zones de chaleurs également
        rule8 = Rule(["extinguish"], ["delete fire and warm area"])
        listOfRules.append(rule6)

        return listOfRules