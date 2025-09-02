#CoreN
└──  [Stack & Queue Pattern]
    │
    ├── [[Stack Applications]]
    │   │   / Using LIFO (Last-In-First-Out) structure /
    │   │
    │   ├── ─ [Parentheses & Bracket Matching]
    │   │   │   / Validating balanced symbols /
    │   │   │   ├── [Basic Validation]
    │   │   │   │   ├── Problem: "20. Valid Parentheses"
    │   │   │   │   ├── Problem: "1003. Check If Word Is Valid After Substitutions"
    │   │   │   │   └── Problem: "591. Tag Validator"
    │   │   │   │
    │   │   │   └── [Advanced Matching]
    │   │   │       ├── Problem: "32. Longest Valid Parentheses"
    │   │   │       ├── Problem: "856. Score of Parentheses"
    │   │   │       └── Problem: "1249. Minimum Remove to Make Valid Parentheses"
    │   │   │
    │   │   ├── [Monotonic Stack]
    │   │   │   / Stack with increasing/decreasing elements /
    │   │   │   ├── [Next Greater/Smaller Element]
    │   │   │   │   ├── Problem: "496. Next Greater Element I"
    │   │   │   │   ├── Problem: "503. Next Greater Element II"
    │   │   │   │   └── Problem: "739. Daily Temperatures"
    │   │   │   │
    │   │   │   ├── [Histogram Problems]
    │   │   │   │   ├── Problem: "84. Largest Rectangle in Histogram"
    │   │   │   │   ├── Problem: "85. Maximal Rectangle"
    │   │   │   │   └── Problem: "42. Trapping Rain Water"
    │   │   │   │
    │   │   │   └── [Optimization Problems]
    │   │   │       ├── Problem: "1856. Maximum Subarray Min-Product"
    │   │   │       └── Problem: "907. Sum of Subarray Minimums"
    │   │   │
    │   │   ├── [Expression Evaluation]
    │   │   │   / Calculating expressions /
    │   │   │   ├── [Basic Calculation]
    │   │   │   │   ├── Problem: "224. Basic Calculator"
    │   │   │   │   ├── Problem: "227. Basic Calculator II"
    │   │   │   │   └── Problem: "772. Basic Calculator III"
    │   │   │   │
    │   │   │   └── [Postfix/Prefix Evaluation]
    │   │   │       ├── Problem: "150. Evaluate Reverse Polish Notation"
    │   │   │       └── Problem: "636. Exclusive Time of Functions"
    │   │   │
    │   └── [Stack for Traversal]
    │       / Alternative to recursion /
    │       ├── [Tree Traversal]
    │       │   ├── Problem: "94. Binary Tree Inorder Traversal"
    │       │   ├── Problem: "144. Binary Tree Preorder Traversal"
    │       │   └── Problem: "145. Binary Tree Postorder Traversal"
    │       │
    │       └── [Graph Traversal]
    │           ├── Problem: "133. Clone Graph"
    │           └── Problem: "341. Flatten Nested List Iterator"
    │
    ├── [[Queue Applications]]
    │   │   / Using FIFO (First-In-First-Out) structure /
    │   │
    │   ├── ─ [BFS Implementation]
    │   │   │   / Level-order processing /
    │   │   │   ├── [Tree Level Order]
    │   │   │   │   ├── Problem: "102. Binary Tree Level Order Traversal"
    │   │   │   │   ├── Problem: "103. Binary Tree Zigzag Level Order Traversal"
    │   │   │   │   └── Problem: "116. Populating Next Right Pointers in Each Node"
    │   │   │   │
    │   │   │   └── [Graph BFS]
    │   │   │       ├── Problem: "200. Number of Islands"
    │   │   │       ├── Problem: "994. Rotting Oranges"
    │   │   │       └── Problem: "127. Word Ladder"
    │   │   │
    │   │   ├── [Sliding Window with Queue]
    │   │   │   / Queue-based window maintenance /
    │   │   │   └── Problem: "239. Sliding Window Maximum" (Deque)
    │   │   │
    │   │   ├── [Multi-Source BFS]
    │   │   │   / Starting from multiple points /
    │   │   │   ├── Problem: "994. Rotting Oranges"
    │   │   │   ├── Problem: "1162. As Far from Land as Possible"
    │   │   │   └── Problem: "542. 01 Matrix"
    │   │   │
    │   └── [Task Processing]
    │       / Managing work items /
    │       ├── Problem: "621. Task Scheduler"
    │       ├── Problem: "933. Number of Recent Calls"
    │       └── Problem: "353. Design Snake Game"
    │
    ├── [[Specialized Queue Variants]]
    │   │   / Modified queue structures /
    │   │
    │   ├── ─ [Deque (Double-Ended Queue)]
    │   │   │   / Insert/remove from both ends /
    │   │   │   ├── [Monotonic Deque]
    │   │   │   │   ├── Problem: "239. Sliding Window Maximum"
    │   │   │   │   └── Problem: "1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit"
    │   │   │   │
    │   │   │   └── [General Deque Applications]
    │   │   │       ├── Problem: "950. Reveal Cards In Increasing Order"
    │   │   │       └── Problem: "641. Design Circular Deque"
    │   │   │
    │   │   ├── [Priority Queue]
    │   │   │   / Queue with priority ordering /
    │   │   │   ├── [Top-K Problems]
    │   │   │   │   ├── Problem: "215. Kth Largest Element in an Array"
    │   │   │   │   └── Problem: "347. Top K Frequent Elements"
    │   │   │   │
    │   │   │   └── [Greedy with Priority Queue]
    │   │   │       ├── Problem: "1046. Last Stone Weight"
    │   │   │       └── Problem: "253. Meeting Rooms II"
    │   │   │
    │   │   └── [Circular Queue]
    │   │       / Queue that wraps around /
    │   │       ├── Problem: "622. Design Circular Queue"
    │   │       └── Problem: "1823. Find the Winner of the Circular Game"
    │   │
    │   └── [Queue Reconstruction]
    │       / Rebuilding ordered sequences /
    │       ├── Problem: "406. Queue Reconstruction by Height"
    │       └── Problem: "649. Dota2 Senate"
    │
    └── [[Stack & Queue Design]]
        │   / Implementing custom structures /
        │
        ├── ─ [Stack Design Patterns]
        │   │   / Custom stack implementations /
        │   │   ├── Problem: "155. Min Stack"
        │   │   ├── Problem: "716. Max Stack"
        │   │   └── Problem: "232. Implement Queue using Stacks"
        │
        ├── [Queue Design Patterns]
        │   │   / Custom queue implementations /
        │   │   ├── Problem: "225. Implement Stack using Queues"
        │   │   ├── Problem: "641. Design Circular Deque"
        │   │   └── Problem: "1429. First Unique Number"
        │
        └── [Combined Structures]
            / Using both stacks and queues /
            ├── Problem: "895. Maximum Frequency Stack"
            └── Problem: "1472. Design Browser History"