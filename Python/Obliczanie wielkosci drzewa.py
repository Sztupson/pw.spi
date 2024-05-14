# Zadanie 1. Sprawdzanie wysokości drzewa binarnego

# Zadanie: napisz funkcję ktora oblicza  wysokosc drzewa binarnego. Wysokosc drzewa jest najdłuższą ścieżką od korzenia do liścia 

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def height(node):


    if node is None:
        return -1
    else:

        left_height = height(node.left)
        right_height = height(node.right)
        

        return max(left_height, right_height) + 1


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(15)
root.right.right = Node(30)
root.right.right.right = Node(50)

print("Wysokość drzewa:", height(root) + 1)

# Sprawdzenie czy drzewo jest zbalansowane:
# Zadanie 2: Napisz funkcję ktora sprawdza czy dane drzewo binarne jest zbalansowane.
# Drzewo uwaza sie za zbalansowane jesli dla kazdego wezla roznica wysokosci jego 
# poddrzew lewego i prwaego nie przekracza 1

def is_balanced(node):
    if node is None:
        return True

    balance = abs(height(node.left) - height(node.right))

    return balance <= 1 and is_balanced(node.left) and is_balanced(node.right)

if is_balanced(root):

    print("Drzewo zbalansowane.")
else:
    
    print("Drzewo niezbalansowane.")

# Zadanie 3: Wizualizacja rotacji
# Zadanie: Stwórz program lub skrypt ktory pozwoli wizualizowac efekt rotacji pojedynczej i
# podwojnej na drzewie binarnym. uzytkownik powinien moc podac ciag operacji 
# wstawiania a nastepnie zobaczyc jak drzewo jest transforowane przez rotacje


def rotate_right(y):
    x = y.left
    T2 = x.right

    # Wykonanie rotacji
    x.right = y
    y.left = T2

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    # Wykonanie rotacji
    y.left = x
    x.right = T2

    return y

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

def visualize_rotation(operations):
    root = None

    for op in operations:
        if op == 'L':
            print("Rotacja w lewo:")
            root = rotate_left(root)
            inorder_traversal(root)
            print("\n")
        elif op == 'R':
            print("Rotacja w prawo:")
            root = rotate_right(root)
            inorder_traversal(root)
            print("\n")
        elif op == 'I':
            val = int(input("Podaj wartość węzła do wstawienia: "))
            print("Wstawienie węzła o wartości:", val)
            root = insert(root, val)
            inorder_traversal(root)
            print("\n")
        else:
            print("Nieznana operacja:", op)

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Przykładowe użycie:
operations = ['I', 'I', 'I', 'R']
visualize_rotation(operations)