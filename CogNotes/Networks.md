## What is a network
A *graph/network* is a mathematical set composed of two other sets.
* a set of nodes (or vertices)
* a set of edges (or arcs)
* 

The effectiveness of information flow across sources depends on the *information flows in the network*.
e.g. a network where every node is connected **vs** a network where a node is only connected to the n closest nodes.

Networks differ in the degree of connections between nodes.
Science is a huge *network* of scientific  articles/groups.

#### Glossary from "[Networks in Cognitive Science](https://www.sciencedirect.com/science/article/pii/S136466131300096X?casa_token=koUojR_St84AAAAA:WKTOd8-5LoFvMq0mV12B09MpIkbPwQfJIYPFUjEkxui0ZUx6uNaSmAmmouJH4Zo_5TnuEUtHfzs5)"

**Assortativity:** the preference for nodes to attach to other vertices that are similar in some way. Assortative mixing by degree, for example, describes the case in which nodes of similar degree tend to form connections preferentially among themselves. For instance, in most social networks, high-degree nodes are connected to high-degree nodes and poorly connected vertices tend to link each other. By contrast, disassortativity describes the opposite tendency (e.g., high-degree nodes tend to be connected to low-degree nodes in technological networks).

**Betweenness of a node:** the number of shortest paths between pairs of vertices passing through a given vertex.

**Centrality:** the centrality of a node measures its relative importance inside the network; for example. in terms of degree, betweenness, or distance. In the latter case, the so-called closeness centrality is defined as the inverse of the sum of the shortest path lengths from the considered vertex to all other vertices in the network.

**Clique:** a subset of a network where every pair of nodes is connected.

**Clustering coefficient:** $c_i$ of vertex $i$ is defined as the ratio between $e_i$ , the actual number of edges between its nearest neighbors, and the maximum possible number _k__i_(_k__i_ − 1)/2; that is,[I]The clustering coefficient quantifies the transitivity of a network, measuring the probability that two vertices with a common neighbor are also neighbors of each other. The average clustering coefficient 〈_c_〉 is the average value of _c__i_ over all vertices in a network; that is,[II]In real networks, 〈_c_〉 usually takes values of order unity, in stark contrast with the clustering inversely proportional to network size that is expected for a random network ([Box 2](https://www.sciencedirect.com/science/article/pii/S136466131300096X?casa_token=koUojR_St84AAAAA:WKTOd8-5LoFvMq0mV12B09MpIkbPwQfJIYPFUjEkxui0ZUx6uNaSmAmmouJH4Zo_5TnuEUtHfzs5#tb0015)).

**Community:** although the precise definition of community remains an open question, a minimal and generally accepted description is that the subset of the nodes in a community is more tightly connected to one another than to the rest of the network.

**Connected component:** the maximal subset of vertices in a network such that there is a path joining any pair of vertices in it.

**Connectome:** the detailed ‘wiring diagram’ of the neurons and synapses in the brain.

**Co-occurrence network:** a network with nodes representing the elements present in a given context (e.g., words in a text) and edges representing the ‘co-occurrence’ in the same context according to some criterion; for example, in the case of words in a text, a simple criterion is that they appear in the text one next to the other.

**Core of a network:** a powerful subset of the network because of the high frequency of occurrence of its nodes , their importance for the existence of the remainder of nodes, or the fact that it is both densely connected and central (in terms of graph distance).

**Degree:** the degree of a vertex, _k__i_, is defined as the number of other vertices to which vertex _i_ is connected (or the ‘number of neighbors’.

**Degree distribution:** the probability _P_(_k_) that a randomly chosen vertex has degree _k_ for every possible _k_. For large networks, the degree distribution represents a convenient statistical characterization of a network's topology.

**Diameter:** the longest of the shortest paths between any pair of vertices in a network.

**Directed network:** a network in which each link has an associated direction of flow.

**Hubs:** the vertices in a network with the largest degree (number of connections).

**Network or graph:** a collection of points, called vertices (or nodes), joined by lines, referred as edges (or links). Vertices represent the elementary components of a system, whereas edges stand for the interactions or connections between pairs of components.

**PageRank:** a network analysis algorithm that assigns a numerical weight to each edge of a directed network, aimed at measuring its relative importance. The algorithm is used by the Google search engine to rank Word Wide Web search results.

**Percolation threshold:** percolation theory describes the behavior of connected clusters in a graph. A network is said to percolate when its largest connected component contains a finite fraction of the nodes that form the whole network. Percolation depends in general on some topological quantity (e.g., the average degree in the Erdös–Rényi random graph). The percolation threshold is the value of this quantity above which the network percolates.

**Rich-club phenomenon:** property observed in many real networks in which the hubs have a strong tendency to be connected to each other rather than with vertices of small degree.

**Scale-free networks:** networks with a broad, heavy-tailed degree distribution that can often be approximated by a power-law, _P_(_k_) ∼ _k_−_γ_, where γ is a characteristic exponent usually between 2 and 3. This heavy-tailed power-law form underlies many of the surprising features shown by real complex networks.

**Shortest path length:** the shortest path length, or distance, ℓ_ij_, between vertices _i_ and _j_ is the length (in number of edges) of the shortest path joining _i_ and _j_. The shortest path length thus represents a measure of the distance between pairs of vertices. The average shortest path length 〈ℓ 〉 is the average of the shortest path length over all pairs of vertices in the network; that is, where _N_ is the total number of vertices in the network.

**Small-world property:** a property shown by many real complex networks that exhibit a small value of the average shortest path length 〈ℓ 〉, increasing with network size logarithmically or slower. This property is in stark contrast to the larger diameter of regular lattices, which grows algebraically with lattice size.

**Strength of a node:** the sum of the weights of the edges incident on a vertex.

**Transitivity of a network**: the propensity of two nodes in a network to be connected by an edge if they share a common neighbor.

**Tree:** a network that has as many edges as vertices minus one and is connected; that is, a walk from one node can reach any other node in the network.

**Weighted network:** a network whose links are characterized by different capacities, or weights, defining the strength of the interaction between the nodes they connect.

**Word-association network:** a network where vertices are words and a link connects a cue word with the word that is produced as response.