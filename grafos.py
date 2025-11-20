# ------------------------------------------------------------
# Trabalho - Busca em Profundidade e Detecção de Ciclos em Grafos
# Integrantes do Grupo:
# Mateus Amaro – RA: 2015116
# Vitor Henrique – RA: 2002807
# Jeann Garconi – RA: 2019032
# ------------------------------------------------------------

class Grafo:
    def __init__(self):
        self.adj = {}

    def adicionar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u, v):
        self.adj.setdefault(u, [])
        self.adj.setdefault(v, [])
        self.adj[u].append(v)

    def dfs(self, inicio):
        visitado = set()
        ordem_visita = []

        def dfs_rec(v):
            visitado.add(v)
            ordem_visita.append(v)

            for viz in self.adj[v]:
                if viz not in visitado:
                    dfs_rec(viz)

        dfs_rec(inicio)
        return ordem_visita
      
    def tem_ciclo(self):
        visitado = set()
        pilha_rec = set()  

        def dfs_ciclo(v):
            visitado.add(v)
            pilha_rec.add(v)

            for viz in self.adj[v]:
                if viz not in visitado:
                    if dfs_ciclo(viz):
                        return True

                elif viz in pilha_rec:
                    return True

            pilha_rec.remove(v)
            return False

        for v in self.adj:
            if v not in visitado:
                if dfs_ciclo(v):
                    return True

        return False

if __name__ == "__main__":
    g = Grafo()

    # Exemplo de grafo
    g.adicionar_aresta("A", "B")
    g.adicionar_aresta("A", "C")
    g.adicionar_aresta("B", "D")
    g.adicionar_aresta("C", "E")
    g.adicionar_aresta("E", "A")  

    print("\n--- DFS (Busca em Profundidade) ---")
    ordem = g.dfs("A")
    print("Ordem de visita:", ordem)

    print("\n--- Detecção de Ciclos ---")
    if g.tem_ciclo():
        print("O grafo POSSUI ciclo.")
    else:
        print("O grafo NÃO possui ciclo.")
