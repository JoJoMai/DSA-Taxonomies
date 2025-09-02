#CoreN
└──  [Hash Table Pattern]
    │
    ├── [[Direct Lookup]]
    │   │   / Finding values with immediate access /
    │   │
    │   ├── ─ [Existence Checking]
    │   │   │   / Determining if elements exist /
    │   │   │   ├── [Element Presence]
    │   │   │   │   ├── Problem: "217. Contains Duplicate"
    │   │   │   │   ├── Problem: "219. Contains Duplicate II"
    │   │   │   │   └── Problem: "1. Two Sum"
    │   │   │   │
    │   │   │   └── [Character Frequency]
    │   │   │       ├── Problem: "242. Valid Anagram"
    │   │   │       ├── Problem: "383. Ransom Note"
    │   │   │       └── Problem: "49. Group Anagrams"
    │   │   │
    │   │   ├── [Counting & Frequency]
    │   │   │   / Tracking element occurrences /
    │   │   │   ├── [Frequency Counting]
    │   │   │   │   ├── Problem: "347. Top K Frequent Elements"
    │   │   │   │   ├── Problem: "451. Sort Characters By Frequency"
    │   │   │   │   └── Problem: "1394. Find Lucky Integer in an Array"
    │   │   │   │
    │   │   │   └── [Majority Elements]
    │   │   │       ├── Problem: "169. Majority Element"
    │   │   │       └── Problem: "229. Majority Element II"
    │   │   │
    │   │   └── [Pair Matching]
    │   │       / Finding pairs with specific properties /
    │   │       ├── [Sum-Based Matching]
    │   │       │   ├── Problem: "1. Two Sum"
    │   │       │   ├── Problem: "560. Subarray Sum Equals K"
    │   │       │   └── Problem: "523. Continuous Subarray Sum"
    │   │       │
    │   │       └── [Property-Based Matching]
    │   │           ├── Problem: "532. K-diff Pairs in an Array"
    │   │           └── Problem: "2006. Count Number of Pairs With Absolute Difference K"
    │   │
    │   └── [Bijection Problems]
    │       / One-to-one mapping verification /
    │       ├── Problem: "205. Isomorphic Strings"
    │       ├── Problem: "290. Word Pattern"
    │       └── Problem: "246. Strobogrammatic Number"
    │
    ├── [[Hash Map for Structure]]
    │   │   / Organizing data with hash maps /
    │   │
    │   ├── ─ [Grouping & Classification]
    │   │   │   / Categorizing elements /
    │   │   │   ├── Problem: "49. Group Anagrams"
    │   │   │   ├── Problem: "249. Group Shifted Strings"
    │   │   │   └── Problem: "1282. Group the People Given the Group Size They Belong To"
    │   │   │
    │   │   ├── [Prefix Sums with Hash Map]
    │   │   │   / Running sums for range queries /
    │   │   │   ├── Problem: "560. Subarray Sum Equals K"
    │   │   │   ├── Problem: "525. Contiguous Array"
    │   │   │   └── Problem: "1248. Count Number of Nice Subarrays"
    │   │   │
    │   │   └── [Multi-Map Applications]
    │   │       / Maps with multiple values per key /
    │   │       ├── Problem: "249. Group Shifted Strings"
    │   │       ├── Problem: "811. Subdomain Visit Count"
    │   │       └── Problem: "981. Time Based Key-Value Store"
    │   │
    │   └── [Index as Hash Key]
    │       / Using position information /
    │       ├── Problem: "128. Longest Consecutive Sequence"
    │       ├── Problem: "41. First Missing Positive"
    │       └── Problem: "442. Find All Duplicates in an Array"
    │
    ├── [[Specialized Hash Structures]]
    │   │   / Custom hash-based data structures /
    │   │
    │   ├── ─ [LRU & LFU Caches]
    │   │   │   / Caching with access recency/frequency /
    │   │   │   ├── Problem: "146. LRU Cache"
    │   │   │   └── Problem: "460. LFU Cache"
    │   │   │
    │   │   ├── [Design HashMap or HashSet]
    │   │   │   / Implementing hash structures /
    │   │   │   ├── Problem: "705. Design HashSet"
    │   │   │   └── Problem: "706. Design HashMap"
    │   │   │
    │   │   └── [Specialized Dictionaries]
    │   │       / Custom dictionaries /
    │   │       ├── Problem: "588. Design In-Memory File System"
    │   │       └── Problem: "211. Design Add and Search Words Data Structure"
    │   │
    │   └── [Hash with Multi-Pass]
    │       / Multiple processing phases /
    │       ├── Problem: "187. Repeated DNA Sequences"
    │       ├── Problem: "138. Copy List with Random Pointer"
    │       └── Problem: "133. Clone Graph"
    │
    └── [[String Hashing]]
        │   / Hash functions for strings /
        │
        ├── ─ [Rolling Hash]
        │   │   / Hash values that update efficiently /
        │   │   ├── Problem: "28. Find the Index of the First Occurrence in a String" (Rabin-Karp)
        │   │   ├── Problem: "1044. Longest Duplicate Substring"
        │   │   └── Problem: "718. Maximum Length of Repeated Subarray"
        │
        ├── [Character Counting]
        │   │   / Frequency-based hashing /
        │   │   ├── Problem: "242. Valid Anagram"
        │   │   ├── Problem: "49. Group Anagrams"
        │   │   └── Problem: "438. Find All Anagrams in a String"
        │
        └── [String Matching with Hashing]
            │   / Finding string patterns /
            │   ├── Problem: "187. Repeated DNA Sequences"
            │   ├── Problem: "726. Number of Atoms"
            │   └── Problem: "966. Vowel Spellchecker"