from src.env_objects.expert_sys.Rule import Rule


class Rules_base:

    def rulesOfGame(self):
        listOfRules = []

        #Liste des règles

        #Si il y a de la chaleur, le robot va sur la case dans 60% des cas
        rule1 = Rule(["W"], ["go sur case"])
        listOfRules.append(rule1)

        #Si il y a des poussières, les cases autour pourraient avoir des décombres
        rule2 = Rule(["D"], ["ignore"])
        listOfRules.append(rule2)

        #Si il y a des cris, le robot a trouvé la victime
        rule3 = Rule(["scream"], ["human"])
        listOfRules.append(rule3)

        #Si il y a un feu, le robot l'éteint
        rule4 = Rule(["F"], ["extinguish"])
        listOfRules.append(rule4)

        #Si il y a des ruines, le robot contourne les ruines
        rule5 = Rule(["Ru"], ["avoid"])
        listOfRules.append(rule5)

        #Si il une case vide dans le voisinage non visitée, on y va
        rule6 = Rule(["??"], ["continue"])
        listOfRules.append(rule6)

        #Si le robot éteint le feu, le feu est supprimer et les zones de chaleurs également
        rule7 = Rule(["extinguish"], ["delete fire and warm area"])
        listOfRules.append(rule7)

        # Si il y a de la chaleur et des ruines, le robot évite
        rule8 = Rule(["W", "Ru"], ["avoid"])
        listOfRules.append(rule8)

        # Si il y a de la chaleur et de la poussière, le robot évite
        rule9 = Rule(["W", "D"], ["avoid"])
        listOfRules.append(rule9)

        # Si il y a un feu et des ruines, le robot évite
        rule10 = Rule(["F", "Ru"], ["avoid"])
        listOfRules.append(rule10)

        # Si il y a un humain, aller le sauver
        rule11 = Rule(["H"], ["rescue"])
        listOfRules.append(rule11)

        rule12 = Rule(["V"], ["less priority"])
        listOfRules.append(rule12)

        return listOfRules