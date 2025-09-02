#CoreN-1
└── [Basic Bit Operations]
    │   / Fundamental bit manipulation techniques /
    │
    ├── ─ [[Single Bit Operations]]
    │   │   / Manipulating individual bits /
    │   │   ├── [Set a Bit]
    │   │   │   / num | (1 << i) /
    │   │   │   └── Problem: "1486. XOR Operation in an Array"
    │   │   │
    │   │   ├── [Clear a Bit]
    │   │   │   / num & ~(1 << i) /
    │   │   │   └── Problem: "1342. Number of Steps to Reduce a Number to Zero"
    │   │   │
    │   │   ├── [Toggle a Bit]
    │   │   │   / num ^ (1 << i) /
    │   │   │   └── Problem: "1506. Find Root of N-Ary Tree"
    │   │   │
    │   │   └── [Check a Bit]
    │   │       / (num >> i) & 1 /
    │   │       ├── Problem: "191. Number of 1 Bits"
    │   │       └── Problem: "461. Hamming Distance"
    │
    ├── [[Multiple Bit Operations]]
    │   │   / Working with sets of bits /
    │   │   ├── [Clear Rightmost Set Bit]
    │   │   │   / n & (n-1) /
    │   │   │   └── Problem: "231. Power of Two"
    │   │   │
    │   │   ├── [Extract Rightmost Set Bit]
    │   │   │   / n & -n /
    │   │   │   ├── Problem: "260. Single Number III"
    │   │   │   └── Problem: "201. Bitwise AND of Numbers Range"
    │   │   │
    │   │   └── [Clear All Bits From LSB to ith Bit]
    │   │       / n & ~((1 << (i+1)) - 1) /
    │   │       └── Problem: "371. Sum of Two Integers"
    │
    ├── [[Bit Counting & Manipulation]]
    │   │   / Counting and calculating with bits /
    │   │   ├── [Count Set Bits]
    │   │   │   ├── Problem: "191. Number of 1 Bits"
    │   │   │   └── Problem: "338. Counting Bits"
    │   │   │
    │   │   ├── [Parity Checking]
    │   │   │   └── Problem: "1386. Cinema Seat Allocation"
    │   │   │
    │   │   └── [Bit Reversal]
    │   │       ├── Problem: "190. Reverse Bits"
    │   │       └── Problem: "1009. Complement of Base 10 Integer"
    │
    └── [[Bit Shifting Techniques]]
        / Moving bits left or right /
        ├── [Logical Shifts]
        │   ├── Problem: "29. Divide Two Integers"
        │   └── Problem: "7. Reverse Integer"
        │
        ├── [Multiplication/Division by Powers of 2]
        │   ├── Problem: "50. Pow(x, n)"
        │   └── Problem: "372. Super Pow"
        │
        └── [Bit Rotation]
            └── Problem: "1238. Circular Permutation in Binary Representation"