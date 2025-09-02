#CoreN-1
└── [Graph Traversals]
    │   / Algorithms for visiting all vertices/edges in a graph /
    │
    ├── ─ [[Depth-First Search (DFS) on Graphs]]
    │   │   / Exploring deep paths before backtracking /
    │   │   ├── [Connected Components]
    │   │   │   / Finding isolated subgraphs /
    │   │   │   ├── [Basic Connectivity]
    │   │   │   │   ├── Problem: "200. Number of Islands"
    │   │   │   │   └── Problem: "547. Number of Provinces"
    │   │   │   │
    │   │   │   └── [Component Size Analysis]
    │   │   │       ├── Problem: "695. Max Area of Island"
    │   │   │       └── Problem: "1254. Number of Closed Islands"
    │   │   │
    │   │   ├── [Cycle Detection]
    │   │   │   / Finding loops in graphs /
    │   │   │   ├── [Undirected Graph Cycles]
    │   │   │   │   └── Problem: "684. Redundant Connection"
    │   │   │   │
    │   │   │   └── [Directed Graph Cycles]
    │   │   │       ├── Problem: "207. Course Schedule"
    │   │   │       └── Problem: "802. Find Eventual Safe States"
    │   │   │
    │   │   ├── [Path Finding & Exploration]
    │   │   │   / Finding routes between vertices /
    │   │   │   ├── [All Paths]
    │   │   │   │   └── Problem: "797. All Paths From Source to Target"
    │   │   │   │
    │   │   │   └── [Path Existence]
    │   │   │       └── Problem: "1971. Find if Path Exists in Graph"
    │   │   │
    │   │   └── [Topological Sort]
    │   │       / Ordering vertices based on dependencies /
    │   │       ├── [DFS-Based Topological Sort]
    │   │       │   ├── Problem: "210. Course Schedule II"
    │   │       │   └── Problem: "269. Alien Dictionary"
    │   │       │
    │   │       └── [Lexicographic Ordering]
    │   │           └── Problem: "953. Verifying an Alien Dictionary"
    │
    ├── [[Breadth-First Search (BFS) on Graphs]]
    │   │   / Level by level exploration /
    │   │   ├── [Shortest Path (Unweighted)]
    │   │   │   / Finding paths with minimum number of edges /
    │   │   │   ├── [Single Source Shortest Path]
    │   │   │   │   ├── Problem: "1091. Shortest Path in Binary Matrix"
    │   │   │   │   ├── Problem: "994. Rotting Oranges"
    │   │   │   │   └── Problem: "127. Word Ladder"
    │   │   │   │
    │   │   │   └── [Level-by-Level Expansion]
    │   │   │       ├── Problem: "542. 01 Matrix"
    │   │   │       └── Problem: "1162. As Far from Land as Possible"
    │   │   │
    │   │   ├── [Multi-Source BFS]
    │   │   │   / Starting from multiple points /
    │   │   │   ├── [Simultaneous Propagation]
    │   │   │   │   ├── Problem: "994. Rotting Oranges"
    │   │   │   │   └── Problem: "542. 01 Matrix"
    │   │   │   │
    │   │   │   └── [Boundary Expansion]
    │   │   │       ├── Problem: "1020. Number of Enclaves"
    │   │   │       └── Problem: "130. Surrounded Regions"
    │   │   │
    │   │   ├── [Bidirectional BFS]
    │   │   │   / BFS from both source and target /
    │   │   │   └── [Meet-in-the-Middle]
    │   │   │       ├── Problem: "127. Word Ladder"
    │   │   │       └── Problem: "752. Open the Lock"
    │   │   │
    │   │   └── [Topological Sort (Kahn's Algorithm)]
    │   │       / BFS-based approach to topological sorting /
    │   │       ├── [Indegree-Based Processing]
    │   │       │   ├── Problem: "210. Course Schedule II"
    │   │       │   └── Problem: "310. Minimum Height Trees"
    │   │       │
    │   │       └── [Lexicographic Topological Sort]
    │   │           └── Problem: "1203. Sort Items by Groups Respecting Dependencies"
    │
    └── [[Advanced Graph Traversal Patterns]]
        │   / Specialized algorithms for complex graph problems /
        │   ├── [Union-Find (Disjoint Set Union)]
        │   │   / Efficiently track connected components /
        │   │   ├── [Path Compression + Union by Rank]
        │   │   │   ├── Problem: "547. Number of Provinces"
        │   │   │   └── Problem: "684. Redundant Connection"
        │   │   │
        │   │   └── [Dynamic Connectivity]
        │   │       └── Problem: "721. Accounts Merge"
        │   │
        │   ├── [Shortest Path Algorithms (Weighted)]
        │   │   / Finding optimal paths with weighted edges /
        │   │   ├── [Dijkstra's Algorithm]
        │   │   │   ├── Problem: "743. Network Delay Time"
        │   │   │   └── Problem: "1631. Path With Minimum Effort"
        │   │   │
        │   │   ├── [Floyd-Warshall (All Pairs)]
        │   │   │   └── Problem: "1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance"
        │   │   │
        │   │   └── [Bellman-Ford (Negative Weights)]
        │   │       └── Problem: "787. Cheapest Flights Within K Stops"
        │   │
        │   └── [Minimum Spanning Tree]
        │       / Finding a tree that connects all vertices with minimum weight /
        │       └── Problem: "1584. Min Cost to Connect All Points"