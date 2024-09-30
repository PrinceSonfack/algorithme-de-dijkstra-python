graph_data = {
    'A': [('B', 3), ('D', 10)],
    'B': [('A', 3), ('C', 8), ('D', 2), ('I',1)],
    'C': [('B', 8), ('F', 3), ('G', 12)],
    'D': [('A', 10), ('B', 2), ('E', 5)],
    'E': [('D', 5), ('F', 4)],
    'F': [('C', 3), ('E', 4), ('G', 1), ('H', 7), ('I',5)],
    'G': [('C', 12), ('F', 1), ('H', 5)],
    'H': [('G', 5), ('F', 7)],
    'I': [('F', 5), ('B', 1)]
}

# Fonction pour obtenir un nœud valide de l'utilisateur
def get_valid_node(prompt, graph):
    while True:
        node = input(prompt).strip()  # Enlever les espaces inutiles
        if not node.isalpha():
            print("Erreur : Veuillez entrer un nom de nœud valide avec des lettres uniquement.")
        elif node not in graph:
            print(f"Erreur : Le nœud '{node}' n'existe pas dans le graphe.")
        else:
            return node  # Retourner le nœud valide


def court_chemin(graph, start, end):
    # Étape 1: Initialisation des distances
    distances = {node: float('inf') for node in graph}  # On met tous les nœuds à une distance infinie
    distances[start] = 0  # La distance du départ est 0

    # On garde une trace des nœuds précédents pour reconstruire le chemin plus tard
    predecessors = {}

    # Liste des nœuds non visités
    non_visited = list(graph.keys())

    # Étape 2: Tant qu'il reste des nœuds à visiter
    while non_visited:
        # Trouver le nœud avec la plus petite distance parmi les nœuds non visités
        current_node = min(non_visited, key=lambda node: distances[node])

        # Si la distance du nœud actuel est infinie, on arrête (aucun chemin possible)
        if distances[current_node] == float('inf'):
            break

        # Étape 3: Explorer les voisins du nœud actuel
        for neighbor, weight in graph[current_node]:
            # Calculer la nouvelle distance vers le voisin
            new_distance = distances[current_node] + weight
            # Si cette nouvelle distance est plus courte, on la met à jour
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

        # Marquer le nœud actuel comme visité
        non_visited.remove(current_node)

        # Si on a atteint le nœud de fin, on arrête
        if current_node == end:
            break

    # Étape 4: Reconstruire le chemin à partir du prédécesseur
    path = []
    current_node = end
    # La boucle continue tant qu'un prédécesseur existe
    while current_node in predecessors:
        path.insert(0, current_node)  # Insérer au début du chemin
        current_node = predecessors[current_node]
    path.insert(0, start)  # Ajouter le nœud de départ au début

    # Si le nœud de fin n'a pas été atteint, afficher un message d'erreur
    if distances[end] == float('inf'):
        print(f"Aucun chemin trouvé entre {start} et {end}")
    else:
        print(f"Chemin trouvé: {path}")
        print(f"Coût total: {distances[end]}")

def main():
    while True:
        # Obtenir le nœud de départ et de fin valides
        start = get_valid_node('Entrer le nœud de départ (lettre seulement) : ', graph_data)
        end = get_valid_node('Entrer le nœud de fin (lettre seulement) : ', graph_data)

        # Si le nœud de départ et de fin sont les mêmes
        if start == end:
            print(f"Le nœud de départ et de fin sont identiques : {start}. Le coût est 0.")
        else:
            # Appel de la fonction
            court_chemin(graph_data, start, end)
        
        # Demander si l'utilisateur souhaite recommencer ou quitter
        again = input("Voulez-vous calculer un autre chemin ? (O/N) : ").strip().lower()
        if again != 'o':  # Si l'utilisateur n'entre pas 'o', on quitte la boucle
            print("Au revoir!")
            break

main()