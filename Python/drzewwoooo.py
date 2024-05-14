class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 # wysokosc wezla inicjalnie ustawiona na 1

def update_height(node):
    # Aktualizacja wysokosci wezla na podstawie wysokosci jego dzieci
    node.height = max(height(node.left), height(node.right)) + 1

def height(node):
    # Pobieranie wysokosci wezla, jesli wezel nie istnieje zwroc 0
    if not node:
        return 0
    return node.height

def right_rotate(y):

# wykonanie rotacji w prawo na wezle y
    x = y.left
    T2 = x.right
# Przeprowadzenie rotacji
    x.right = y
    y.left = T2
# Aktualizacja wysokosci po rotacji
    update_height(x)
    update_height(y)
# Nowy korzen po rotacji
    return x

def left_rotate(x):
# wykonanie rotacji w lewo na wezle x
    y = x.right

    T2 = y.left
# Przeprowadzenie rotacji
    y.left = x
    x.right = T2
# Aktualizacja wysokosci po rotacji
    update_height(x)
    update_height(y)
# Nowy korzen po rotacji
    return y



def right_left_rotate(node):
    node.right = right_rotate(node.right)

    return left_rotate(node)
# Użycie:
# Załóżmy, ze mamy drzewo AVL i potrzebujemy wykonać rotację w prawo na węźle 'y'
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print(root.key)
# wykonanie rotacji w prawo
root = right_left_rotate(root)
print(root.key)