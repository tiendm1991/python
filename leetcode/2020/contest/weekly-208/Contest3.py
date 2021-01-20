class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.childs = {kingName: []}
        self.isDeath = {}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.childs:
            self.childs[parentName].append(childName)
        else:
            self.childs[parentName] = [childName]

    def death(self, name: str) -> None:
        self.isDeath[name] = True

    def getInheritanceOrder(self):
        def help(name):
            if name not in self.isDeath:
                ans.append(name)
            if name not in self.childs:
                return
            for c in self.childs[name]:
                help(c)
            return

        ans = []
        help(self.king)
        return ans


ThroneInheritance
t = ThroneInheritance("king")  # order: king
t.birth("king", "andy")  # order: king > andy
t.birth("king", "bob")  # order: king > andy > bob
t.birth("king", "catherine")  # order: king > andy > bob > catherine
t.birth("andy", "matthew")  # order: king > andy > matthew > bob > catherine
t.birth("bob", "alex")  # order: king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha")  # order: king > andy > matthew > bob > alex > asha > catherine
print(t.getInheritanceOrder())  # return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob")  # order: king > andy > matthew > bob > alex > asha > catherine
print(t.getInheritanceOrder())  # return ["king", "andy", "matthew", "alex", "asha", "catherine"]
