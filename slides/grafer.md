# Grafer i Python

Grafer er en vigtig datastruktur i mange sammenhænge. De består af knuder, der er forbundet med kanter, og de kan bruges til at repræsentere mange forskellige typer af data, f.eks. sociale netværk, vejnetværk, internetforbindelser, osv.

I følgende afsnit vil vi se på hvordan vi kan repræsentere grafer i Python og hvordan vi kan arbejde med grafer. Vi vil se på hvordan vi kan repræsentere grafer som en matrice (også kaldet adjacency matrix) og hvordan vi kan repræsentere grafer som en adjacency list. Vi vil også se på hvordan vi kan traversere grafer og finde korteste veje i grafer.

## Definition af grafer

En graf $G$ består af en mængde af knuder $V$ og en mængde af kanter $E$. En kant $e$ er en urettet forbindelse mellem to knuder $u$ og $v$. 
Hvis grafen er rettet, er kanterne rettet fra en knude til en anden. En vægtet graf har en vægt associeret med hver kant.

En graf kan repræsenteres på flere forskellige måder. En af de mest almindelige måder er at bruge en adjacency matrix. En adjacency matrix er en $n \times n$ matrix, hvor $n$ er antallet af knuder i grafen. Elementet $A_{ij}$ i matricen er 1 hvis der er en kant mellem knude $i$ og knude $j$, og 0 ellers. Hvis grafen er vægtet, kan elementet $A_{ij}$ indeholde vægten af kanten. Herunder en formulering af en adjacency matrix for en graf, der består af 4 knuder og 3 kanter:

$$ A = \begin{bmatrix}
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 0 & 0
\end{bmatrix} $$

Kolonne $i$ repræsenterer knude $i$, og række $j$ repræsenterer knude $j$. Elementet $A_{ij}$ er 1 hvis der er en kant mellem knude $i$ og knude $j$, og 0 ellers.

Hvis grafen er rettet, vil matricen være asymmetrisk og i såfald vil elementet $A_{ij}$ være 1 hvis der er en kant fra knude $i$ til knude $j$.

Hvis grafen er vægtet, vil elementet $A_{ij}$ indeholde vægten af kanten.

## Repræsentation af grafer i Python

I Python kan vi repræsentere grafer på flere forskellige måder. En af de mest almindelige måder er at bruge en adjacency list. En adjacency list er en dictionary, hvor nøglen er en knude og værdien er en liste af naboknuder. Herunder en formulering af en adjacency list for grafen, der består af 4 knuder og 3 kanter:

```python
graph_al = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1]
}
```

Vi kan også repræsentere en adjacency matrix i Python, som reelt bare er en liste af lister. Herunder en formulering af en adjacency matrix for grafen, der består af 4 knuder og 3 kanter:

```python
graph_am = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
```

## Opgave
Betragt følgende adjacency matrix for en graf:

```python
graph_am = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]
```
Tegn grafen. 

## Opgave
Givet følgende graf repræsenteret som en adjacency list:

```python
graph_al = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1]
}
```
Tegn grafen.

## Opgave 
En ny supermetro er ved at blive bygget mellem europæiske hovedstæder. Hovedstæderne er repræsenteret som knuder i en graf, og metrolinjerne er repræsenteret som kanter. Hovedstæderne er nummereret fra 0 til 6, hvor 0 er København, 1 er Berlin, 2 er Paris, 3 er Madrid, 4 er Rom, 5 er London og 6 er Stockholm. Der er følgende metrolinjer:
- Linje 1: København - Berlin - Paris - Madrid
- Linje 2: København - Berlin - Paris - Rom
- Linje 3: København - Berlin - London - Stockholm
- Linje 4: Rom - Paris - Madrid - London - Stockholm

Skriv en adjacency matrix og adjacency list for denne graf.

## Opgave 
Skriv en funktion `adjacency_matrix_to_list` der tager en adjacency matrix som input og returnerer en adjacency list.

Prøv at teste funktionen på foregående opgave.

## Visualisering af grafer

I Python kan vi visualisere grafer ved hjælp af `networkx` biblioteket. `networkx` er et bibliotek til at arbejde med grafer i Python og kan installeres ved at køre `pip install networkx`.

Herunder et eksempel på Python-kode, der viser en graf:

```python
import networkx as nx

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

nx.draw(G, with_labels=True)
```
Koden opretter en graf med 4 knuder og 4 kanter og visualiserer grafen.

Man kan også tilføje vægte til kanterne ved at bruge `G.add_edge(1, 2, weight=3)`: 

```python
import networkx as nx

G = nx.Graph()
G.add_edge(1, 2, weight=3)
G.add_edge(2, 3, weight=4)
G.add_edge(3, 4, weight=5)
G.add_edge(4, 1, weight=6)

nx.draw(G, with_labels=True)
```

Har man en adjacency matrix kan den  visualiseres således:

```python
import networkx as nx
import matplotlib.pyplot as plt

graph_am = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
]

G = nx.Graph(graph_am)
nx.draw(G, with_labels=True)
plt.show()
```

Her bruges `nx.Graph(graph_am)` til at konvertere en adjacency matrix til en graf.

Endelige kan vi også visualisere en adjacency list:

```python
import networkx as nx
import matplotlib.pyplot as plt

graph_al = {
    0: [1],
    1: [0, 2, 3],
    2: [1],
    3: [1]
}

G = nx.Graph(graph_al)
nx.draw(G, with_labels=True)
plt.show()
```

## Opgave
Visualiser grafen fra opgaven med supermetroen. Tilføj passende vægte til kanterne.

## Korteste veje i grafer

Forestil dig, at du har en graf, der repræsenterer et vejnetværk, og du gerne vil finde den korteste vej fra et sted (en startknude) til et andet sted (en slutknude). Vejen kan repræsenteres som en sekvens af knuder, der er forbundet med kanter og hver kant har en længde. Formålet er at finde den korteste vej fra startknuden til slutknuden. 

En af de mest almen kendte algoritmer til at finde den korteste vej i en graf er Dijkstra's algoritme opkaldt efter den hollandske datalog, Edsger W. Dijkstra. Algoritmen fungerer ved at opbygge en korteste vej træ, hvor vi starter med startknuden og tilføjer den næste knude med den korteste vej til startknuden. Dette gentages indtil alle knuder er besøgt. Herunder en prosakode beskrivelse af Dijkstra's algoritme:

1. Initialiser en liste `dist` med afstande fra startknuden til alle andre knuder. Startknuden har afstand 0, og alle andre knuder har afstand uendelig.
2. Initialiser en prioritetskø `pq` med startknuden og dens afstand 0.
3. Gentag indtil `pq` er tom:
    1. Fjern den knude `u` med den korteste afstand fra `pq`.
    2. For hver nabo `v` til `u`:
        1. Hvis afstanden fra startknuden til `u` plus vægten af kanten fra `u` til `v` er mindre end afstanden fra startknuden til `v`, så opdater afstanden fra startknuden til `v` og tilføj `v` til `pq`.

Ved afslutningen af algoritmen vil `dist` indeholde den korteste vej fra startknuden til alle andre knuder. En prioritetkø bruges til at vælge den knude med den korteste afstand fra startknuden. En prioritetskø er en datastruktur, der understøtter to operationer: `heappush` og `heappop`. `heappush` tilføjer et element til køen, og `heappop` fjerner og returnerer det mindste element fra køen. En prioritetskø er kendetegnet ved, at det mindste element altid er det første element i køen.

Herunder en Python-implementering af Dijkstra's algoritme, hvor vi bruger heapq biblioteket til at implementere prioritetskøen:

```python
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

Resultatet printes som en liste af afstande fra startknuden til alle andre knuder. 

Lad os prøve at finde den korteste vej fra København til Stockholm i supermetroen:

```python
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 1), (3, 1)],
    2: [(1, 1)],
    3: [(1, 1)]
}

# visualisering af grafen
G = nx.Graph(graph)
nx.draw(G, with_labels=True)
plt.show()

dist = dijkstra(graph, 0)
print(dist)
```




