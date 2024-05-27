class Arisu:
    def __init__(self, kei):
        self.kei = kei
        self.left = None
        self.right = None
class Genshin_could_never:
    def __init__(self):
        self.root = None

    def insert(self, kei):
        if self.root is None:
            self.root = Arisu(kei)
        else:
            self.le_insert(self.root, kei)

    def le_insert(self, node, kei):
        if kei < node.kei:
            if node.left is None:
                node.left = Arisu(kei)
            else:
                self.le_insert(node.left, kei)
        else:
            if node.right is None:
                node.right = Arisu(kei)
            else:
                self.le_insert(node.right, kei)
#Rawr XD (I ran out of names)
    def rawr_in_order(self):
        result = []
        self._rawr_in_order(self.root, result)
        return result

    def _rawr_in_order(self, node, result):
        if node is not None:
            self._rawr_in_order(node.left, result)
            result.append(node.kei)
            self._rawr_in_order(node.right, result)

bst = Genshin_could_never()
elements = []
nuh_uh = int(input("How many things you wanna put: "))
for _ in range(nuh_uh):
    elemento = input("Enter your stuff: ")
    elements.append(elemento)
    print("Your arrays ༼⁠ ⁠つ⁠ ⁠◕⁠‿⁠◕⁠ ⁠༽⁠つ:", elements)
# It works I guess¯⁠\⁠_⁠(⁠ツ⁠)⁠_⁠/⁠¯
for element in elements:
    bst.insert(element)

WuWa_could_never = int(input("How many additional elements you want to add: "))
for sekai in range(WuWa_could_never):
    yum = input("Add something: ")
    bst.insert(yum)

sheeeshh = bst.rawr_in_order()
print("In-order traversal of the BST:", sheeeshh )
#By Clark Daryll B Omasdang
#IT1R13