#CoreN-1
└── [Tree Traversals]
    │   / Systematic ways to visit all nodes in a tree /
    │
    ├── ─ [[Depth-First Search (DFS) Variants]]
    │   │   / Explore as far as possible along a branch before backtracking /
    │   │   ├── [Recursive DFS]
    │   │   │   / Implementation using function call stack /
    │   │   │   ├── [Preorder Traversal (Root → Left → Right)]
    │   │   │   │   ├── Problem: "144. Binary Tree Preorder Traversal"
    │   │   │   │   ├── Problem: "589. N-ary Tree Preorder Traversal"
    │   │   │   │   └── Application: "257. Binary Tree Paths"
    │   │   │   │
    │   │   │   ├── [Inorder Traversal (Left → Root → Right)]
    │   │   │   │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │   │   │   │   ├── Problem: "98. Validate Binary Search Tree"
    │   │   │   │   └── Problem: "230. Kth Smallest Element in a BST"
    │   │   │   │
    │   │   │   ├── [Postorder Traversal (Left → Right → Root)]
    │   │   │   │   ├── Problem: "145. Binary Tree Postorder Traversal"
    │   │   │   │   ├── Problem: "590. N-ary Tree Postorder Traversal"
    │   │   │   │   └── Problem: "124. Binary Tree Maximum Path Sum"
    │   │   │   │
    │   │   │   └── [Path-Based DFS]
    │   │   │       / Finding specific paths in trees /
    │   │   │       ├── [Root-to-Leaf Paths]
    │   │   │       │   ├── Problem: "112. Path Sum"
    │   │   │       │   └── Problem: "113. Path Sum II"
    │   │   │       │
    │   │   │       ├── [Any Path (Node-to-Node)]
    │   │   │       │   ├── Problem: "437. Path Sum III"
    │   │   │       │   └── Problem: "687. Longest Univalue Path"
    │   │   │       │
    │   │   │       └── [Ancestor-Descendant Relationships]
    │   │   │           ├── Problem: "236. Lowest Common Ancestor of a Binary Tree"
    │   │   │           └── Problem: "1644. Lowest Common Ancestor of a Binary Tree II"
    │   │   │
    │   │   ├── [Iterative DFS (Stack-based)]
    │   │   │   / Implementation using explicit stack /
    │   │   │   ├── [Explicit Stack Traversals]
    │   │   │   │   ├── Problem: "144. Binary Tree Preorder Traversal"
    │   │   │   │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │   │   │   │   └── Problem: "145. Binary Tree Postorder Traversal"
    │   │   │   │
    │   │   │   └── [State-Tracking DFS]
    │   │   │       / Using additional state information /
    │   │   │       ├── Problem: "331. Verify Preorder Serialization of a Binary Tree"
    │   │   │       └── Problem: "1008. Construct Binary Search Tree from Preorder Traversal"
    │   │   │
    │   │   └── [Morris Traversal (O(1) Space)]
    │   │       / DFS without using stack or recursion /
    │   │       ├── [Morris Inorder]
    │   │       │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │   │       │   └── Problem: "99. Recover Binary Search Tree"
    │   │       │
    │   │       └── [Morris Preorder]
    │   │           └── Problem: "144. Binary Tree Preorder Traversal"
    │
    ├── [[Breadth-First Search (BFS) Variants]]
    │   │   / Level by level traversal using a queue /
    │   │   ├── [Level-Order Traversals]
    │   │   │   / Processing nodes level by level /
    │   │   │   ├── [Standard Level Order]
    │   │   │   │   ├── Problem: "102. Binary Tree Level Order Traversal"
    │   │   │   │   ├── Problem: "107. Binary Tree Level Order Traversal II"
    │   │   │   │   └── Problem: "429. N-ary Tree Level Order Traversal"
    │   │   │   │
    │   │   │   ├── [Level-wise Processing]
    │   │   │   │   / Working with entire levels /
    │   │   │   │   ├── Problem: "199. Binary Tree Right Side View"
    │   │   │   │   ├── Problem: "515. Find Largest Value in Each Tree Row"
    │   │   │   │   └── Problem: "116. Populating Next Right Pointers in Each Node"
    │   │   │   │
    │   │   │   └── [Depth-Based Analysis]
    │   │   │       / Analyzing tree by depth /
    │   │   │       ├── Problem: "104. Maximum Depth of Binary Tree"
    │   │   │       ├── Problem: "111. Minimum Depth of Binary Tree"
    │   │   │       └── Problem: "662. Maximum Width of Binary Tree"
    │   │   │
    │   │   ├── [Multi-Source BFS]
    │   │   │   / Starting BFS from multiple nodes /
    │   │   │   └── [Simultaneous Expansion]
    │   │   │       ├── Problem: "1161. Maximum Level Sum of a Binary Tree"
    │   │   │       └── Problem: "1302. Deepest Leaves Sum"
    │   │   │
    │   │   └── [Bidirectional BFS]
    │   │       / BFS from both source and target /
    │   │       └── [Meeting-Point Search]
    │   │           └── Problem: "863. All Nodes Distance K in Binary Tree"
    │
    ├── [[Specialized Tree Traversals]]
    │   │   / Advanced or problem-specific traversals /
    │   │   ├── [Boundary Traversals]
    │   │   │   / Following the outline of the tree /
    │   │   │   └── Problem: "545. Boundary of Binary Tree"
    │   │   │
    │   │   ├── [Vertical Traversals]
    │   │   │   / Based on horizontal distance from root /
    │   │   │   └── Problem: "987. Vertical Order Traversal of a Binary Tree"
    │   │   │
    │   │   ├── [Spiral/Zigzag Patterns]
    │   │   │   / Alternating direction by level /
    │   │   │   └── Problem: "103. Binary Tree Zigzag Level Order Traversal"
    │   │   │
    │   │   └── [View-Based Traversals]
    │   │       / What's visible from different perspectives /
    │   │       ├── [Side Views]
    │   │       │   └── Problem: "199. Binary Tree Right Side View"
    │   │       │
    │   │       └── [Top/Bottom Views]
    │   │           └── Problem: "314. Binary Tree Vertical Order Traversal"
    │
    └── [[Tree Construction via Traversals]]
        / Building trees from traversal sequences /
        ├── [From Multiple Traversals]
        │   ├── Problem: "105. Construct Binary Tree from Preorder and Inorder Traversal"
        │   └── Problem: "106. Construct Binary Tree from Inorder and Postorder Traversal"
        │
        └── [Serialization/Deserialization]
            / Converting trees to/from string representations /
            ├── Problem: "297. Serialize and Deserialize Binary Tree"
            └── Problem: "449. Serialize and Deserialize BST"