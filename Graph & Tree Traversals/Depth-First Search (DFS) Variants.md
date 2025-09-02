#CoreN-2
└── [Depth-First Search (DFS) Variants]
    │   / Explore as far as possible along a branch before backtracking /
    │
    ├── ─ [[Recursive DFS]]
    │   │   / Implementation using function call stack /
    │   │   ├── [Preorder Traversal (Root → Left → Right)]
    │   │   │   ├── Problem: "144. Binary Tree Preorder Traversal"
    │   │   │   ├── Problem: "589. N-ary Tree Preorder Traversal"
    │   │   │   └── Application: "257. Binary Tree Paths"
    │   │   │
    │   │   ├── [Inorder Traversal (Left → Root → Right)]
    │   │   │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │   │   │   ├── Problem: "98. Validate Binary Search Tree"
    │   │   │   └── Problem: "230. Kth Smallest Element in a BST"
    │   │   │
    │   │   ├── [Postorder Traversal (Left → Right → Root)]
    │   │   │   ├── Problem: "145. Binary Tree Postorder Traversal"
    │   │   │   ├── Problem: "590. N-ary Tree Postorder Traversal"
    │   │   │   └── Problem: "124. Binary Tree Maximum Path Sum"
    │   │   │
    │   │   └── [Path-Based DFS]
    │   │       / Finding specific paths in trees /
    │   │       ├── [Root-to-Leaf Paths]
    │   │       │   ├── Problem: "112. Path Sum"
    │   │       │   └── Problem: "113. Path Sum II"
    │   │       │
    │   │       ├── [Any Path (Node-to-Node)]
    │   │       │   ├── Problem: "437. Path Sum III"
    │   │       │   └── Problem: "687. Longest Univalue Path"
    │   │       │
    │   │       └── [Ancestor-Descendant Relationships]
    │   │           ├── Problem: "236. Lowest Common Ancestor of a Binary Tree"
    │   │           └── Problem: "1644. Lowest Common Ancestor of a Binary Tree II"
    │
    ├── [[Iterative DFS (Stack-based)]]
    │   │   / Implementation using explicit stack /
    │   │   ├── [Explicit Stack Traversals]
    │   │   │   ├── Problem: "144. Binary Tree Preorder Traversal"
    │   │   │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │   │   │   └── Problem: "145. Binary Tree Postorder Traversal"
    │   │   │
    │   │   └── [State-Tracking DFS]
    │   │       / Using additional state information /
    │   │       ├── Problem: "331. Verify Preorder Serialization of a Binary Tree"
    │   │       └── Problem: "1008. Construct Binary Search Tree from Preorder Traversal"
    │
    └── [[Morris Traversal (O(1) Space)]]
        / DFS without using stack or recursion /
        ├── [Morris Inorder]
        │   ├── Problem: "94. Binary Tree Inorder Traversal"
        │   └── Problem: "99. Recover Binary Search Tree"
        │
        └── [Morris Preorder]
            └── Problem: "144. Binary Tree Preorder Traversal"