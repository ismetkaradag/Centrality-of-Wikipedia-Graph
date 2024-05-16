import networkx as nx
graph = nx.read_graphml("cna.graphml")

degree_centrality = nx.degree_centrality(graph)
betweenness_centrality = nx.betweenness_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)
eigenvector_centrality = nx.eigenvector_centrality(graph)

# print(degree_centrality)
# print(betweenness_centrality)
# print(closeness_centrality)
# print(eigenvector_centrality)

max_degree_centrality_key = max(degree_centrality.keys(), key=lambda k: degree_centrality[k])
max_betweenness_centrality_key = max(betweenness_centrality.keys(), key=lambda k: betweenness_centrality[k])
max_closeness_centrality_key = max(closeness_centrality.keys(), key=lambda k: closeness_centrality[k])
max_eigenvector_centrality_key = max(eigenvector_centrality.keys(), key=lambda k: eigenvector_centrality[k])

print("betweenness:",max_betweenness_centrality_key)
print("closeness:",max_closeness_centrality_key)
print("degree:",max_degree_centrality_key)
print("eigenvector:",max_eigenvector_centrality_key)

##Output
# betweenness: Computer Science
# closeness: Doi (Identifier)
# degree: Social Network
# eigenvector: Doi (Identifier)