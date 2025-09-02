#CoreN-1
└── [Basic Union Find Operations]
    │   / Core functionality of the data structure /
    │
    ├── ─ [[Initialization]]
    │   │   / Setting up the data structure /
    │   │   ├── [Array Representation]
    │   │   │   └── Problem: "547. Number of Provinces" (implementation)
    │   │   │
    │   │   ├── [Tree Representation]
    │   │   │   └── Problem: "684. Redundant Connection" (implementation)
    │   │   │
    │   │   └── [Custom Element Mapping]
    │   │       └── Problem: "721. Accounts Merge"
    │
    ├── [[Find Operation]]
    │   │   / Determining which set an element belongs to /
    │   │   ├── [Basic Find]
    │   │   │   └── Problem: "547. Number of Provinces" (basic implementation)
    │   │   │
    │   │   ├── [Path Compression]
    │   │   │   ├── Problem: "684. Redundant Connection" (with path compression)
    │   │   │   └── Problem: "128. Longest Consecutive Sequence" (optimized)
    │   │   │
    │   │   └── [Path Splitting/Halving]
    │   │       └── Concept: "Alternative path compression techniques"
    │
    ├── [[Union Operation]]
    │   │   / Merging two sets /
    │   │   ├── [Basic Union]
    │   │   │   └── Problem: "547. Number of Provinces" (basic implementation)
    │   │   │
    │   │   ├── [Union by Rank/Size]
    │   │   │   ├── Problem: "684. Redundant Connection" (with union by rank)
    │   │   │   └── Problem: "1202. Smallest String With Swaps" (optimized)
    │   │   │
    │   │   └── [Union by Custom Criteria]
    │   │       └── Problem: "1632. Rank Transform of a Matrix"
    │
    └── [[Data Structure Optimizations]]
        / Improving union-find performance /
        ├── [Path Compression + Union by Rank]
        │   ├── Problem: "684. Redundant Connection" (fully optimized)
        │   └── Problem: "1202. Smallest String With Swaps" (fully optimized)
        │
        ├── [Size Tracking]
        │   ├── Problem: "323. Number of Connected Components in an Undirected Graph" (with size)
        │   └── Problem: "952. Largest Component Size by Common Factor"
        │
        └── [Dynamic Element Addition]
            ├── Problem: "721. Accounts Merge"
            └── Problem: "1697. Checking Existence of Edge Length Limited Paths"