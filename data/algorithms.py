questions = {
    "Easy": [
        {
            "question": "What is an algorithm?",
            "expected_answer": "An algorithm is a step-by-step procedure used to solve a particular problem or perform a specific task. It takes input, processes it through a finite set of well-defined steps, and produces the required output. A good algorithm should be correct, efficient, clear, and should terminate after a finite number of steps."
        },
        {
            "question": "What are the characteristics of a good algorithm?",
            "expected_answer": "A good algorithm should be correct, efficient, clear, and finite. It should produce the correct output for valid inputs, use reasonable time and memory, have well-defined steps, and eventually terminate. It should also be practical to implement."
        },
        {
            "question": "What is the difference between an algorithm and a program?",
            "expected_answer": "An algorithm is a logical step-by-step solution to a problem, independent of a particular programming language. A program is the actual implementation of that algorithm using a programming language such as C, C++, Java, or Python."
        },
        {
            "question": "What is time complexity?",
            "expected_answer": "Time complexity describes how the running time of an algorithm grows as the size of the input increases. It does not usually represent the exact execution time. Instead, it describes the growth rate using notations such as O(n), O(log n), and O(n²)."
        },
        {
            "question": "What is space complexity?",
            "expected_answer": "Space complexity describes how much memory an algorithm requires as the input size increases. It includes the additional memory used by variables, data structures, recursion, and other temporary storage required while the algorithm is running."
        },
        {
            "question": "What is Big O notation?",
            "expected_answer": "Big O notation is used to describe the upper bound or growth rate of an algorithm's time or space complexity as the input size increases. For example, O(1) is constant, O(log n) is logarithmic, O(n) is linear, and O(n²) is quadratic."
        },
        {
            "question": "What is the best case of an algorithm?",
            "expected_answer": "The best case represents the situation in which an algorithm performs the minimum amount of work for a particular input size. For example, in linear search, the best case occurs when the required element is found at the first position, giving O(1) time."
        },
        {
            "question": "What is the worst case of an algorithm?",
            "expected_answer": "The worst case represents the situation in which an algorithm performs the maximum amount of work for a particular input size. For example, in linear search, the worst case occurs when the element is at the last position or is not present, resulting in O(n) time."
        },
        {
            "question": "What is the average case of an algorithm?",
            "expected_answer": "The average case describes the expected performance of an algorithm over a typical or assumed distribution of inputs. It provides an estimate of how the algorithm generally behaves rather than considering only the best or worst possible input."
        },
        {
            "question": "What is constant time complexity?",
            "expected_answer": "Constant time complexity, written as O(1), means that the amount of work performed by an algorithm does not depend on the size of the input. For example, accessing an element at a known index in an array usually takes O(1) time."
        },
        {
            "question": "What is linear time complexity?",
            "expected_answer": "Linear time complexity, written as O(n), means that the running time grows approximately in proportion to the input size. For example, checking every element of an array once requires O(n) time."
        },
        {
            "question": "What is logarithmic time complexity?",
            "expected_answer": "Logarithmic time complexity, written as O(log n), means that the problem size is reduced significantly, often by half, during each step. Binary search is a common example because it eliminates half of the remaining search space after each comparison."
        },
        {
            "question": "What is quadratic time complexity?",
            "expected_answer": "Quadratic time complexity, written as O(n²), means that the amount of work grows approximately with the square of the input size. Algorithms containing two nested loops that each process n elements often have O(n²) complexity."
        },
        {
            "question": "What is linear search?",
            "expected_answer": "Linear search is a simple searching algorithm that checks each element one by one until the required element is found or the end of the collection is reached. It works on both sorted and unsorted data. Its worst-case time complexity is O(n)."
        },
        {
            "question": "What is the time complexity of linear search?",
            "expected_answer": "The best-case time complexity of linear search is O(1), when the target is the first element. The average-case complexity is O(n), and the worst-case complexity is also O(n), when the target is at the end or is not present."
        },
        {
            "question": "What is binary search?",
            "expected_answer": "Binary search is a searching algorithm used on sorted data. It compares the target with the middle element and eliminates either the left or right half depending on the comparison. This process continues until the target is found or no elements remain. Its time complexity is O(log n)."
        },
        {
            "question": "What is the main requirement for binary search?",
            "expected_answer": "The main requirement for standard binary search is that the data must be sorted. Without sorted data, we cannot safely eliminate half of the search space after each comparison."
        },
        {
            "question": "What is the time complexity of binary search?",
            "expected_answer": "Binary search has O(1) best-case time when the middle element is the target. Its average and worst-case time complexity is O(log n), because the search space is divided approximately in half during every step."
        },
        {
            "question": "What is sorting?",
            "expected_answer": "Sorting is the process of arranging data according to a particular order, such as ascending or descending order. Sorting makes data easier to search, analyze, and process. Common sorting algorithms include bubble sort, selection sort, insertion sort, merge sort, and quick sort."
        },
        {
            "question": "What is bubble sort?",
            "expected_answer": "Bubble sort repeatedly compares adjacent elements and swaps them when they are in the wrong order. After each pass, one of the largest elements moves toward its correct position. It is simple to understand but inefficient for large datasets, with O(n²) worst-case time complexity."
        },
        {
            "question": "What is the time complexity of bubble sort?",
            "expected_answer": "The standard bubble sort has O(n²) average and worst-case time complexity. With an optimized implementation that stops when no swaps occur, its best-case complexity can be O(n) when the array is already sorted."
        },
        {
            "question": "What is selection sort?",
            "expected_answer": "Selection sort divides the array into sorted and unsorted portions. It repeatedly finds the smallest element from the unsorted portion and places it at the beginning of that portion. Its time complexity is O(n²) in the best, average, and worst cases."
        },
        {
            "question": "What is insertion sort?",
            "expected_answer": "Insertion sort builds the sorted portion of an array one element at a time. It takes the next element and inserts it into its correct position among the already sorted elements. It works particularly well for small or nearly sorted datasets."
        },
        {
            "question": "What is the time complexity of insertion sort?",
            "expected_answer": "Insertion sort has O(n) best-case time complexity when the data is already sorted. Its average and worst-case time complexity is O(n²), because elements may need to be shifted many positions."
        },
        {
            "question": "What is merge sort?",
            "expected_answer": "Merge sort is a divide-and-conquer sorting algorithm. It divides the array into smaller halves, recursively sorts those halves, and then merges the sorted halves into one sorted array. Its time complexity is O(n log n) in the best, average, and worst cases."
        },
        {
            "question": "What is quick sort?",
            "expected_answer": "Quick sort is a divide-and-conquer sorting algorithm that selects an element as a pivot and partitions the array around that pivot. Elements smaller than the pivot are placed on one side and larger elements on the other side. The partitions are then sorted recursively."
        },
        {
            "question": "What is a pivot in quick sort?",
            "expected_answer": "A pivot is an element selected during quick sort to divide the array into two parts. Elements smaller than the pivot are generally placed on one side and larger elements on the other. The quality of pivot selection strongly affects quick sort's performance."
        },
        {

            "question": "What is the average time complexity of quick sort?",
            "expected_answer": "The average time complexity of quick sort is O(n log n). This occurs when the pivot generally divides the array into reasonably balanced partitions. Its performance can be very efficient in practice."
        },
        {
            "question": "What is the worst-case time complexity of quick sort?",
            "expected_answer": "The worst-case time complexity of quick sort is O(n²). This can happen when the selected pivot repeatedly produces highly unbalanced partitions, such as when the smallest or largest element is repeatedly selected as the pivot."
        },
        {
            "question": "What is recursion?",
            "expected_answer": "Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem. A recursive solution normally contains a base case that stops the recursion and a recursive case that reduces the problem."
        },
        {
            "question": "What is a base case in recursion?",
            "expected_answer": "A base case is the condition that stops a recursive function from making further recursive calls. It is essential because without a proper base case, the function may continue calling itself indefinitely and cause a stack overflow."
        },
        {
            "question": "What happens if recursion has no proper base case?",
            "expected_answer": "If recursion does not have a proper terminating condition, the function may continue calling itself indefinitely. This consumes more stack memory with each call and can eventually result in a stack overflow or program failure."
        },
        {
            "question": "What is an iterative algorithm?",
            "expected_answer": "An iterative algorithm solves a problem by repeatedly executing instructions, usually with loops such as for or while. Unlike recursion, it does not depend on repeated function calls and can often use less stack memory."
        },
        {
            "question": "What is the difference between recursion and iteration?",
            "expected_answer": "Recursion solves a problem through repeated function calls, while iteration uses loops to repeat operations. Recursion can make some problems easier to express, but it may use additional stack memory. Iteration generally avoids recursive call overhead."
        },
        {
            "question": "What is divide and conquer?",
            "expected_answer": "Divide and conquer is an algorithmic technique that divides a large problem into smaller subproblems, solves those subproblems, and then combines their results to obtain the final solution. Merge sort and binary search are common examples."
        },
        {
            "question": "Give examples of divide-and-conquer algorithms.",
            "expected_answer": "Common divide-and-conquer algorithms include merge sort, quick sort, binary search, and certain algorithms for matrix multiplication. These algorithms solve smaller versions of the original problem and combine or use their results."
        },
        {
            "question": "What is a greedy algorithm?",
            "expected_answer": "A greedy algorithm makes the best-looking choice at the current step with the hope that these local choices will lead to a globally optimal solution. Greedy algorithms can be efficient, but they produce an optimal solution only when the problem has the required greedy-choice property."
        },
        {
            "question": "Give an example of a greedy algorithm.",
            "expected_answer": "Examples of greedy algorithms include activity selection, Kruskal's algorithm, Prim's algorithm, and fractional knapsack. In each case, a locally best choice is made according to a specific rule."
        },
        {
            "question": "What is dynamic programming?",
            "expected_answer": "Dynamic programming is a technique used to solve problems that contain overlapping subproblems and optimal substructure. It stores the results of smaller problems so that they do not need to be calculated repeatedly. It can be implemented using memoization or tabulation."
        },
        {
            "question": "What is memoization?",
            "expected_answer": "Memoization is a top-down dynamic programming technique in which the results of previously solved subproblems are stored, usually in a table or dictionary. When the same subproblem occurs again, its stored result is reused instead of recalculating it."
        },
        {
            "question": "What is tabulation?",
            "expected_answer": "Tabulation is a bottom-up dynamic programming technique. Instead of using recursive calls, it starts with the smallest subproblems and fills a table step by step until the solution to the original problem is obtained."
        },
        {
            "question": "What is backtracking?",
            "expected_answer": "Backtracking is an algorithmic technique that builds a solution step by step and abandons a partial solution as soon as it determines that the solution cannot be completed successfully. It is commonly used for problems such as N-Queens, Sudoku, and generating permutations."
        },
        {
            "question": "What is BFS?",
            "expected_answer": "BFS, or Breadth-First Search, is a graph traversal algorithm that explores vertices level by level. It starts from a source vertex, visits its immediate neighbors, then their neighbors, and so on. BFS commonly uses a queue and is useful for finding shortest paths in unweighted graphs."
        },
        {
            "question": "What is DFS?",
            "expected_answer": "DFS, or Depth-First Search, is a graph traversal algorithm that explores one path as deeply as possible before backtracking. It can be implemented using recursion or an explicit stack and is useful for problems such as cycle detection and connected components."
        },
        {
            "question": "What is the difference between BFS and DFS?",
            "expected_answer": "BFS explores a graph level by level and normally uses a queue, while DFS explores as deeply as possible along each path and uses recursion or a stack. BFS is useful for shortest paths in unweighted graphs, while DFS is useful for deep exploration and many graph-analysis problems."
        },
        {
            "question": "What is a graph algorithm?",
            "expected_answer": "A graph algorithm is an algorithm designed to solve problems involving vertices and edges. Graph algorithms can be used for traversal, shortest paths, connectivity, cycle detection, minimum spanning trees, and many other problems."
        },
        {
            "question": "What is a shortest path algorithm?",
            "expected_answer": "A shortest path algorithm finds the path with the minimum total cost or distance between vertices in a graph. The appropriate algorithm depends on the graph, such as BFS for unweighted graphs and Dijkstra's algorithm for graphs with non-negative edge weights."
        },
        {
            "question": "What is Dijkstra's algorithm?",
            "expected_answer": "Dijkstra's algorithm is a shortest-path algorithm used to find the minimum distance from a source vertex to other vertices in a weighted graph with non-negative edge weights. It repeatedly selects the unvisited vertex with the smallest known distance and relaxes its neighboring edges."
        },
        {
            "question": "What is a minimum spanning tree?",
            "expected_answer": "A minimum spanning tree, or MST, is a subset of edges in a connected, weighted, undirected graph that connects all vertices without forming cycles and has the minimum possible total edge weight."
        },
        {
            "question": "Name two algorithms used to find a minimum spanning tree.",
            "expected_answer": "The two commonly used minimum spanning tree algorithms are Prim's algorithm and Kruskal's algorithm. Both find an MST, but they build it using different approaches."
        },
        {
            "question": "Why is algorithm analysis important?",
            "expected_answer": "Algorithm analysis helps us understand how efficiently a solution uses time and memory as the input grows. It allows us to compare different solutions and choose an approach that is suitable for the expected input size and system constraints."
        }
    ],
    #hard
    "Hard": [
    {
        "question": "How would you optimize an algorithm that works correctly but is too slow for large inputs?",
        "expected_answer": "First, I would analyze the algorithm's time and space complexity and identify the main bottleneck. Then I would check whether a better algorithm or data structure can reduce the complexity. I would also remove unnecessary loops, repeated calculations, and redundant memory usage. After optimization, I would test the algorithm with different input sizes to confirm that performance has improved without changing the correctness of the result."
    },
    {
        "question": "How would you find the first occurrence of an element in a sorted array containing duplicates?",
        "expected_answer": "I would use a modified binary search. When I find the target element, I would store its index as a possible answer and continue searching in the left half because an earlier occurrence may exist. If the middle element is smaller than the target, I search the right half; otherwise, I search the left half. This gives O(log n) time complexity."
    },
    {
        "question": "How would you find the last occurrence of an element in a sorted array containing duplicates?",
        "expected_answer": "I would use modified binary search. When the target is found, I would store its index and continue searching in the right half because another occurrence may exist later. If the middle element is smaller than the target, I search right; otherwise, I search left. The time complexity is O(log n)."
    },
    {
        "question": "How would you search for an element in a rotated sorted array?",
        "expected_answer": "I would use a modified binary search. At each step, I determine which half of the array is sorted. Then I check whether the target lies within the range of that sorted half. If it does, I search that half; otherwise, I search the other half. This allows the search to remain logarithmic in the typical distinct-element case."
    },
    {
        "question": "What is Quickselect and where is it used?",
        "expected_answer": "Quickselect is a partition-based algorithm used to find the kth smallest or kth largest element without completely sorting the array. It selects a pivot, partitions the elements, and then continues searching only the partition that contains the desired position. Its average time complexity is O(n), although its worst case is O(n²)."
    },
    {
        "question": "How can you find the kth smallest element efficiently?",
        "expected_answer": "One approach is Quickselect, which has an average time complexity of O(n). Another approach is to use a heap, especially when k is small compared with n. The best method depends on the input size, memory constraints, and whether the data is static or continuously changing."
    },
    {
        "question": "How would you find the median of two sorted arrays efficiently?",
        "expected_answer": "I would use a binary-search partition technique rather than merging the arrays completely. The smaller array is searched to find a partition where the elements on the left side of both arrays are less than or equal to the elements on the right side. This approach can find the median in O(log(min(m,n))) time."
    },
    {
        "question": "How would you detect a cycle in a directed graph?",
        "expected_answer": "I can detect a cycle using DFS with three states: unvisited, currently visiting, and completely processed. If DFS reaches a vertex that is currently being visited, it means there is a back edge and therefore a cycle. Another approach is Kahn's algorithm, where a cycle exists if not all vertices can be included in a topological ordering."
    },
    {
        "question": "How would you detect a cycle in an undirected graph?",
        "expected_answer": "For an undirected graph, I can use DFS while keeping track of the parent vertex. If I encounter an already visited neighbor that is not the current vertex's parent, then a cycle exists. Another efficient method is Union-Find, where a cycle is detected if two vertices of an edge already belong to the same set."
    },
    {
        "question": "What is a topological sort?",
        "expected_answer": "Topological sorting produces a linear ordering of the vertices of a directed acyclic graph such that for every directed edge from A to B, A appears before B. It can be implemented using DFS or Kahn's algorithm. It is commonly used for task scheduling, dependency resolution, and course prerequisite problems."
    },
    {
        "question": "Can a graph containing a cycle have a topological ordering?",
        "expected_answer": "No. A topological ordering is possible only for a Directed Acyclic Graph, or DAG. If a directed graph contains a cycle, there is no valid ordering because each vertex in the cycle would need to appear before another vertex that eventually requires it to come later."
    },
    {
        "question": "What is Dijkstra's algorithm and what limitation does it have?",
        "expected_answer": "Dijkstra's algorithm finds the shortest paths from a source vertex to other vertices in a weighted graph. It repeatedly selects the vertex with the smallest known distance and relaxes its outgoing edges. Its major limitation is that it does not correctly handle negative-weight edges."
    },
    {
        "question": "How does Bellman-Ford differ from Dijkstra's algorithm?",
        "expected_answer": "Both algorithms can find single-source shortest paths, but Bellman-Ford can handle negative-weight edges while Dijkstra's algorithm requires non-negative edge weights. Bellman-Ford can also detect negative-weight cycles. Dijkstra is generally faster for graphs with non-negative weights."
    },
    {
        "question": "How can Bellman-Ford detect a negative-weight cycle?",
        "expected_answer": "Bellman-Ford normally relaxes all edges V-1 times, where V is the number of vertices. After that, it performs one additional relaxation pass. If any distance can still be reduced, then a reachable negative-weight cycle exists."
    },
    {
        "question": "What is the Floyd-Warshall algorithm?",
        "expected_answer": "Floyd-Warshall is a dynamic programming algorithm used to find shortest paths between every pair of vertices in a weighted graph. It gradually considers each vertex as an intermediate vertex and updates the shortest known distances. Its time complexity is O(V³)."
    },
    {
        "question": "When would you use Floyd-Warshall instead of Dijkstra's algorithm?",
        "expected_answer": "I would use Floyd-Warshall when I need shortest paths between all pairs of vertices and the graph is relatively small or dense. Floyd-Warshall also supports negative edge weights as long as there are no negative cycles. Dijkstra is more appropriate for single-source shortest paths with non-negative weights."
    },
    {
        "question": "What is a strongly connected component?",
        "expected_answer": "A strongly connected component is a maximal group of vertices in a directed graph where every vertex is reachable from every other vertex in that group. Algorithms such as Kosaraju's and Tarjan's can find strongly connected components efficiently."
    },
    {
        "question": "What is Kosaraju's algorithm?",
        "expected_answer": "Kosaraju's algorithm finds strongly connected components using two DFS passes. First, it performs DFS on the original graph and records vertices according to their finishing times. Then it reverses all edges and performs DFS in decreasing order of finishing time. Each DFS tree in the second pass represents one strongly connected component."
    },
    {
        "question": "What is Tarjan's algorithm?",
        "expected_answer": "Tarjan's algorithm finds strongly connected components using one DFS traversal. It maintains discovery times and low-link values for vertices and uses a stack to identify components. Its time complexity is O(V + E), where V is the number of vertices and E is the number of edges."
    },
    {
        "question": "How would you find bridges in an undirected graph?",
        "expected_answer": "I would use DFS with discovery times and low-link values. An edge from a vertex u to v is a bridge if the lowest discovery time reachable from v's subtree is greater than the discovery time of u. In other words, removing that edge would disconnect part of the graph."
    },
    {
        "question": "How would you find articulation points in a graph?",
        "expected_answer": "Articulation points can be found using DFS and low-link values. For a non-root vertex u, it is an articulation point if it has a child v for which low[v] is greater than or equal to discovery[u]. The DFS root is an articulation point if it has more than one DFS child."
    },
    {
        "question": "How would you find the shortest path in an unweighted graph?",
        "expected_answer": "I would use Breadth-First Search because every edge has the same cost. BFS explores vertices in increasing order of their distance from the source, so the first time a vertex is reached, the path used is a shortest path in terms of the number of edges. The time complexity is O(V + E)."
    },
    {
        "question": "How would you find the shortest path in a graph with non-negative edge weights?",
        "expected_answer": "I would normally use Dijkstra's algorithm. It repeatedly selects the unvisited vertex with the smallest known distance and relaxes its outgoing edges. With an appropriate priority queue implementation, it is efficient for sparse graphs with non-negative edge weights."
    },
    {
        "question": "How would you find shortest paths in a DAG?",
        "expected_answer": "For a Directed Acyclic Graph, I can first perform a topological sort and then process vertices in topological order. For each vertex, I relax its outgoing edges. Since each edge is processed once, the overall time complexity is O(V + E)."
    },
    {
        "question": "What is a minimum spanning tree?",
        "expected_answer": "A minimum spanning tree is a set of edges in a connected, weighted, undirected graph that connects all vertices without creating cycles and has the minimum possible total edge weight. The two common algorithms for finding an MST are Prim's and Kruskal's algorithms."
    },
    {
        "question": "What is Kruskal's algorithm?",
        "expected_answer": "Kruskal's algorithm constructs a minimum spanning tree by sorting all edges in increasing order of weight and adding an edge if it does not create a cycle. A Union-Find data structure is commonly used to detect cycles efficiently. Its main sorting step gives a time complexity of O(E log E)."
    },
    {
        "question": "What is Prim's algorithm?",
        "expected_answer": "Prim's algorithm constructs a minimum spanning tree by starting from one vertex and repeatedly adding the minimum-weight edge that connects a vertex already in the tree to a vertex outside the tree. A priority queue can be used to make the process efficient."
    },
    {
        "question": "What is the difference between Prim's and Kruskal's algorithms?",
        "expected_answer": "Prim's algorithm grows one connected tree starting from a selected vertex, while Kruskal's algorithm considers edges globally in increasing order and joins different components. Kruskal's is often convenient for sparse graphs, while Prim's can be efficient for dense graphs with a suitable implementation."
    },
    {
        "question": "What is the Union-Find data structure?",
        "expected_answer": "Union-Find, also called Disjoint Set Union, is a data structure used to maintain a collection of disjoint sets. It supports two main operations: find, which identifies the representative of a set, and union, which combines two sets. It is commonly used in Kruskal's algorithm."
    },
    {
        "question": "What are path compression and union by rank?",
        "expected_answer": "Path compression improves the find operation by making nodes point directly toward the representative of their set. Union by rank or size keeps the trees shallow by attaching the smaller tree below the larger one. Using both techniques makes Union-Find operations extremely efficient in practice."
    },
    {
        "question": "What is the 0/1 knapsack problem?",
        "expected_answer": "The 0/1 knapsack problem asks us to select items with given weights and values so that the total weight does not exceed a capacity while maximizing total value. Each item can either be selected completely or not selected at all. Dynamic programming is a common exact solution."
    },
    {
        "question": "Why is greedy not always correct for the 0/1 knapsack problem?",
        "expected_answer": "Greedy strategies such as selecting the item with the highest value-to-weight ratio can make a locally attractive choice that prevents the globally optimal combination. Therefore, unlike fractional knapsack, the general 0/1 knapsack problem requires approaches such as dynamic programming for an exact solution."
    },
    {
        "question": "How would you optimize the space complexity of 0/1 knapsack?",
        "expected_answer": "The standard dynamic programming solution can use a two-dimensional table with O(nW) space. We can reduce it to O(W) space by using a one-dimensional array and processing capacities from high to low so that an item is not used more than once."
    },
    {
        "question": "What is the Longest Common Subsequence problem?",
        "expected_answer": "The Longest Common Subsequence problem asks us to find the longest sequence that appears in two strings while preserving the order of characters, but the characters do not need to be adjacent. Dynamic programming is commonly used to solve it in O(mn) time for strings of lengths m and n."
    },
    {
        "question": "What is the difference between a subsequence and a substring?",
        "expected_answer": "A substring must contain consecutive characters from the original string, while a subsequence only needs to preserve the relative order of characters and does not require them to be consecutive. For example, 'ace' is a subsequence of 'abcde' but is not a substring."
    },
    {
        "question": "What is the Longest Increasing Subsequence problem?",
        "expected_answer": "The Longest Increasing Subsequence problem asks for the longest subsequence of an array whose elements are in strictly increasing order. A dynamic programming solution takes O(n²) time, while an optimized approach using binary search can solve it in O(n log n)."
    },
    {
        "question": "How would you solve the coin change problem?",
        "expected_answer": "For the minimum number of coins version, I would use dynamic programming. I would define a state representing the minimum number of coins needed for each amount and update it using every available denomination. The exact recurrence depends on the problem requirements, such as whether unlimited use of each coin is allowed."
    },
    {
        "question": "Why can a greedy approach fail for coin change?",
        "expected_answer": "Greedy coin selection chooses the largest possible denomination at each step, but for arbitrary coin systems this may not produce the minimum number of coins. For example, with denominations 1, 3, and 4, choosing 4 first for amount 6 leaves 2, requiring three coins total, while 3 + 3 uses only two coins."
    },
    {
        "question": "What is matrix chain multiplication?",
        "expected_answer": "Matrix chain multiplication is a dynamic programming problem where the goal is to determine the best order for multiplying a sequence of matrices so that the total number of scalar multiplications is minimized. The order of multiplication affects the computational cost even though the final mathematical result is the same."
    },
    {
        "question": "How would you solve the N-Queens problem?",
        "expected_answer": "I would use backtracking. I would place one queen in each row and check whether the selected column and both diagonals are safe. If a placement leads to a conflict later, I would remove the queen and try another position. Sets or bit masks can make safety checks faster."
    },
    {
        "question": "What is pruning in backtracking?",
        "expected_answer": "Pruning means stopping the exploration of a partial solution as soon as we know that it cannot lead to a valid or useful final solution. This avoids unnecessary recursive calls and can significantly improve the practical performance of backtracking algorithms."
    },
    {
        "question": "What is branch and bound?",
        "expected_answer": "Branch and bound is an optimization technique that divides a problem into possible choices and calculates bounds on the best result that each branch could produce. If a branch cannot improve the current best solution, it is discarded. It is commonly used for difficult optimization problems."
    },
    {
        "question": "What is the difference between backtracking and branch and bound?",
        "expected_answer": "Backtracking mainly eliminates partial solutions that violate the problem's constraints, while branch and bound eliminates branches that cannot produce a better objective value than the current best solution. Both reduce unnecessary search, but they are commonly used for somewhat different types of problems."
    },
    {
        "question": "What is amortized analysis?",
        "expected_answer": "Amortized analysis calculates the average cost of operations over a sequence of operations rather than considering each operation independently. Some operations may be expensive, but if they occur rarely, the average cost per operation can still be small. A dynamic array expansion is a common example."
    },
    {
        "question": "What is an in-place algorithm?",
        "expected_answer": "An in-place algorithm performs its main operations using the original input structure and requires only a small amount of additional memory. For example, many implementations of quick sort and insertion sort can work in-place, although the exact space usage depends on the implementation."
    },
    {
        "question": "What is the difference between polynomial and exponential complexity?",
        "expected_answer": "Polynomial complexity grows as a polynomial function of the input size, such as O(n), O(n²), or O(n³). Exponential complexity grows much faster, such as O(2^n). Exponential algorithms generally become impractical much sooner as the input size increases."
    },
    {
        "question": "What is an NP-complete problem?",
        "expected_answer": "An NP-complete problem is a problem that belongs to NP and is at least as hard as every other problem in NP through polynomial-time reductions. If a polynomial-time algorithm is found for any NP-complete problem, then every problem in NP can also be solved in polynomial time."
    },
    {
        "question": "What is the difference between P and NP?",
        "expected_answer": "P is the class of problems that can be solved in polynomial time by a deterministic algorithm. NP is the class of problems for which a proposed solution can be verified in polynomial time. Whether P equals NP is one of the most important unsolved questions in computer science."
    },
    {
        "question": "What is an approximation algorithm?",
        "expected_answer": "An approximation algorithm is designed for difficult optimization problems where finding an exact solution may be computationally expensive. Instead of guaranteeing the optimal solution, it produces a solution that is close to optimal, often with a mathematical guarantee on its quality."
    },
    {
        "question": "What is a brute-force algorithm and when would you use it?",
        "expected_answer": "A brute-force algorithm systematically tries all possible solutions without using advanced optimization. Although it can be inefficient for large inputs, it is useful for small inputs, testing, prototyping, and verifying the results of more optimized algorithms."
    },
    {
        "question": "How would you prove that an algorithm is correct?",
        "expected_answer": "I would first show that the algorithm produces a valid result for every valid input. Depending on the algorithm, I could use mathematical induction, loop invariants, contradiction, or proof by cases. The proof should establish that every important step preserves the required correctness properties."
    },
    {
        "question": "What is a loop invariant?",
        "expected_answer": "A loop invariant is a condition that remains true before and after every iteration of a loop. It is useful for proving algorithm correctness. To prove a loop invariant, we normally show initialization, maintenance during each iteration, and termination."
    },
    {
        "question": "How would you compare two algorithms that have the same Big O complexity?",
        "expected_answer": "Big O alone does not determine practical performance. I would compare the constant factors, memory usage, average-case behavior, input characteristics, cache behavior, implementation complexity, and actual benchmark results. For example, two O(n log n) sorting algorithms can perform very differently in practice."
    },
    {
        "question": "How would you design an algorithm for data that is too large to fit into memory?",
        "expected_answer": "I would consider techniques such as streaming, external-memory algorithms, batching, external sorting, indexing, or distributed processing. The choice depends on whether the data must be processed sequentially, searched repeatedly, sorted, or analyzed across multiple machines."
    }
],

#medium
"Medium": [
    {
        "question": "Why is binary search more efficient than linear search for large sorted data?",
        "expected_answer": "Binary search is more efficient because it eliminates approximately half of the remaining search space after every comparison. Therefore, its time complexity is O(log n), while linear search may need to examine every element and has O(n) worst-case complexity. However, binary search requires the data to be sorted."
    },
    {
        "question": "What is the difference between stable and unstable sorting algorithms?",
        "expected_answer": "A stable sorting algorithm preserves the relative order of elements that have equal keys. An unstable sorting algorithm does not guarantee this behavior. Stability is important when sorting records by multiple fields because an earlier ordering may need to be preserved."
    },
    {
        "question": "Why is insertion sort useful for nearly sorted data?",
        "expected_answer": "Insertion sort performs very well on nearly sorted data because most elements are already close to their correct positions. It only needs a small number of shifts to place each element correctly. Its best-case time complexity is O(n), making it useful for small or nearly sorted datasets."
    },
    {
        "question": "Compare merge sort and quick sort.",
        "expected_answer": "Merge sort divides the array into halves and merges the sorted halves. It has O(n log n) time complexity in all cases but generally requires O(n) additional memory for arrays. Quick sort partitions the array around a pivot and has an average complexity of O(n log n), but its worst case is O(n²). Quick sort can also be implemented with very little additional array memory."
    },
    {
        "question": "Why can quick sort have O(n²) worst-case complexity?",
        "expected_answer": "Quick sort becomes O(n²) when the pivot repeatedly creates highly unbalanced partitions, such as when the pivot is always the smallest or largest element. In that case, one partition contains almost all elements and the other contains none, resulting in approximately n recursive levels."
    },
    {
        "question": "How can the worst-case behavior of quick sort be reduced?",
        "expected_answer": "The probability of poor partitions can be reduced using randomized pivot selection, choosing the median or an approximate median as the pivot, or using hybrid sorting techniques. These approaches make consistently unbalanced partitions less likely."
    },
    {
        "question": "What is the recurrence relation for binary search?",
        "expected_answer": "The recurrence relation for binary search is T(n) = T(n/2) + O(1). The problem size is reduced by half at every step, so solving the recurrence gives a time complexity of O(log n)."
    },
    {
        "question": "What is the recurrence relation for merge sort?",
        "expected_answer": "The recurrence relation for merge sort is T(n) = 2T(n/2) + O(n). The array is divided into two halves, each half is sorted recursively, and merging the two sorted halves takes O(n). Therefore, the total time complexity is O(n log n)."
    },
    {
        "question": "What is the Master Theorem?",
        "expected_answer": "The Master Theorem is a mathematical method used to determine the time complexity of certain divide-and-conquer algorithms. It is commonly applied to recurrence relations of the form T(n) = aT(n/b) + f(n), where a represents the number of subproblems, b represents the reduction in problem size, and f(n) represents the additional work."
    },
    {
        "question": "What is tail recursion?",
        "expected_answer": "Tail recursion occurs when the recursive function call is the final operation performed by the function, with no additional calculation after the recursive call returns. Some programming languages can optimize tail recursion to reduce stack usage, although this optimization is language-dependent."
    },
    {
        "question": "What is optimal substructure in dynamic programming?",
        "expected_answer": "A problem has optimal substructure when an optimal solution to the complete problem can be constructed from optimal solutions to its smaller subproblems. This property allows dynamic programming to solve complex problems by solving and combining smaller optimal solutions."
    },
    {
        "question": "What are overlapping subproblems?",
        "expected_answer": "Overlapping subproblems occur when the same smaller problems are solved repeatedly while solving a larger problem. Dynamic programming improves efficiency by storing the results of these subproblems and reusing them instead of calculating them again."
    },
    {
        "question": "What is the difference between memoization and tabulation?",
        "expected_answer": "Memoization is a top-down approach that usually uses recursion and stores the results of subproblems when they are first calculated. Tabulation is a bottom-up approach that starts with the smallest subproblems and iteratively fills a table until the final result is obtained."
    },
    {
        "question": "When should dynamic programming be used?",
        "expected_answer": "Dynamic programming should be considered when a problem has overlapping subproblems and optimal substructure. Instead of solving the same subproblem repeatedly, we store its result and reuse it. Common examples include knapsack, longest common subsequence, coin change, and matrix chain multiplication."
    },
    {
        "question": "What is the difference between greedy algorithms and dynamic programming?",
        "expected_answer": "A greedy algorithm makes the best local choice at each step and generally does not reconsider previous choices. Dynamic programming solves and stores subproblem results and considers combinations of subproblems. Greedy algorithms are usually simpler and faster when their greedy-choice property is valid, while dynamic programming is more broadly applicable."
    },
    {
        "question": "Why does a greedy algorithm not always give an optimal solution?",
        "expected_answer": "A locally optimal choice does not always lead to the globally optimal solution. Greedy algorithms work correctly only for problems that have the required greedy-choice property. For problems without this property, making the best immediate choice can prevent a better combination of choices later."
    },
    {
        "question": "What is the activity selection problem?",
        "expected_answer": "The activity selection problem asks us to select the maximum number of activities that do not overlap, given their start and finish times. The standard greedy solution sorts activities by their finishing time and repeatedly selects the next activity whose start time is after or equal to the finish time of the previously selected activity."
    },
    {
        "question": "Why does the earliest-finish-time strategy work for activity selection?",
        "expected_answer": "Choosing the activity that finishes earliest leaves the maximum possible remaining time for future activities. This greedy choice can be proven to be safe because replacing the first selected activity with the earliest-finishing compatible activity cannot reduce the number of activities that can be selected afterward."
    },
    {
        "question": "What is the fractional knapsack problem?",
        "expected_answer": "Fractional knapsack allows us to take complete or partial amounts of items. Each item has a value and weight, and the goal is to maximize total value within a given capacity. A greedy strategy that selects items in decreasing order of value-to-weight ratio gives an optimal solution."
    },
    {
        "question": "Why does greedy work for fractional knapsack?",
        "expected_answer": "Because fractions of items can be taken, selecting the item with the highest value-to-weight ratio always gives the greatest immediate value per unit of capacity. We can continue taking fractions until the capacity is full, and this produces an optimal solution."
    },
    {
        "question": "What is breadth-first search used for?",
        "expected_answer": "Breadth-first search is used to traverse graphs level by level. It is especially useful for finding the shortest path in an unweighted graph, finding nodes at a particular distance, and solving problems where states are explored in increasing number of steps."
    },
    {
        "question": "What is depth-first search commonly used for?",
        "expected_answer": "DFS is commonly used for graph traversal, connected components, cycle detection, topological sorting, path exploration, and backtracking problems. It explores one path deeply before returning and exploring another path."
    },
    {
        "question": "How can BFS find the shortest path in an unweighted graph?",
        "expected_answer": "BFS starts from the source and visits all vertices at distance one, then distance two, and so on. Because every edge has equal cost, the first time a vertex is reached, the number of edges used is the minimum possible. Therefore, BFS can find shortest paths in O(V + E) time."
    },
    {
        "question": "What is a topological sort?",
        "expected_answer": "A topological sort is a linear ordering of the vertices of a directed acyclic graph such that for every directed edge from vertex A to vertex B, A appears before B. It is commonly used for scheduling tasks and resolving dependencies."
    },
    {
        "question": "How can topological sorting be implemented?",
        "expected_answer": "Topological sorting can be implemented using DFS or Kahn's algorithm. The DFS method records vertices according to finishing times. Kahn's algorithm repeatedly selects vertices with zero incoming degree and removes their outgoing edges."
    },
    {
        "question": "What is Kahn's algorithm?",
        "expected_answer": "Kahn's algorithm is a BFS-based method for topological sorting. It calculates the in-degree of each vertex, places all vertices with zero in-degree into a queue, and repeatedly removes them while reducing the in-degree of their neighbors. If not all vertices are processed, the graph contains a cycle."
    },
    {
        "question": "What is the main limitation of Dijkstra's algorithm?",
        "expected_answer": "Dijkstra's algorithm assumes that edge weights are non-negative. If negative-weight edges are present, a vertex that was previously considered finalized may later have a shorter path, which violates the assumption used by Dijkstra's algorithm."
    },
    {
        "question": "What algorithm can handle negative edge weights?",
        "expected_answer": "Bellman-Ford can handle graphs containing negative edge weights and can also detect reachable negative-weight cycles. For all-pairs shortest paths, Floyd-Warshall can also handle negative edges as long as there are no negative cycles."
    },
    {
        "question": "What is the difference between Dijkstra and Bellman-Ford?",
        "expected_answer": "Dijkstra is generally faster but requires all edge weights to be non-negative. Bellman-Ford is slower but supports negative-weight edges and can detect negative-weight cycles. Therefore, the choice depends mainly on the properties of the graph."
    },
    {
        "question": "What is the time complexity of Floyd-Warshall?",
        "expected_answer": "Floyd-Warshall has O(V³) time complexity because it considers every possible intermediate vertex for every pair of source and destination vertices. Its space complexity is O(V²) when storing the distance matrix."
    },
    {
        "question": "What is Kruskal's algorithm?",
        "expected_answer": "Kruskal's algorithm finds a minimum spanning tree by sorting all graph edges by increasing weight and adding an edge if it does not create a cycle. A Union-Find data structure is commonly used to determine whether two vertices are already connected."
    },
    {
        "question": "What is Prim's algorithm?",
        "expected_answer": "Prim's algorithm finds a minimum spanning tree by starting with one vertex and repeatedly selecting the minimum-weight edge that connects a vertex inside the current tree to a vertex outside it. A priority queue is commonly used to efficiently find the next minimum edge."
    },
    {
        "question": "What is the difference between Prim's and Kruskal's algorithms?",
        "expected_answer": "Prim's algorithm grows a single tree from a starting vertex, selecting the cheapest edge that expands the tree. Kruskal's algorithm considers all edges globally in increasing order and joins different components while avoiding cycles. Both produce a minimum spanning tree for a connected weighted undirected graph."
    },
    {
        "question": "What is Union-Find used for in algorithms?",
        "expected_answer": "Union-Find, or Disjoint Set Union, is used to efficiently maintain groups of connected elements. It supports finding the representative of a set and merging two sets. It is especially useful in Kruskal's algorithm for detecting whether adding an edge would create a cycle."
    },
    {
        "question": "What is path compression?",
        "expected_answer": "Path compression is an optimization for the Union-Find data structure. During a find operation, it makes each visited node point directly to the representative of its set. This greatly reduces the height of the structure and makes future find operations faster."
    },
    {
        "question": "What is union by rank?",
        "expected_answer": "Union by rank is an optimization in Union-Find where the root of the smaller tree is attached below the root of the larger-rank tree. This prevents the resulting structure from becoming unnecessarily tall and improves the efficiency of future operations."
    },
    {
        "question": "What is backtracking with pruning?",
        "expected_answer": "Backtracking with pruning avoids exploring branches that cannot produce a valid solution. As soon as a partial solution violates a constraint or cannot lead to a useful result, the algorithm stops exploring that branch and returns to an earlier decision."
    },
    {
        "question": "How is the N-Queens problem solved using backtracking?",
        "expected_answer": "The N-Queens problem can be solved by placing one queen in each row and checking whether the selected column and diagonals are safe. If a placement causes a conflict, the algorithm removes the queen and tries another position. This process continues until all queens are placed successfully or all possibilities are exhausted."
    },
    {
        "question": "What is branch and bound?",
        "expected_answer": "Branch and bound is an optimization technique that divides a problem into smaller branches and calculates a bound on the best solution that each branch can produce. If the bound shows that a branch cannot improve the current best solution, that branch is discarded."
    },
    {
        "question": "What is the difference between backtracking and branch and bound?",
        "expected_answer": "Backtracking generally removes partial solutions that violate constraints, while branch and bound removes branches that cannot produce a better objective value than the best solution already found. Backtracking is common in constraint problems, while branch and bound is often used for optimization problems."
    },
    {
        "question": "What is amortized analysis?",
        "expected_answer": "Amortized analysis determines the average cost of operations over a sequence of operations. It allows some individual operations to be expensive as long as the total cost over many operations remains efficient. Dynamic array resizing is a common example."
    },
    {
        "question": "Why is O(n log n) generally better than O(n²)?",
        "expected_answer": "O(n log n) grows much more slowly than O(n²) as the input size increases. For small inputs the difference may not be significant, but for large datasets an O(n log n) algorithm usually performs much better and scales more effectively."
    },
    {
        "question": "What is a brute-force algorithm?",
        "expected_answer": "A brute-force algorithm tries all possible solutions or systematically checks every possibility without using significant problem-specific optimization. It is usually simple and easy to implement but can become very slow as the input size increases."
    },
    {
        "question": "When is a brute-force approach useful?",
        "expected_answer": "Brute force is useful when the input size is small, when simplicity is more important than performance, or when developing a reference solution to verify an optimized algorithm. It can also be useful when no practical optimized solution is known."
    },
    {
        "question": "What is algorithm optimization?",
        "expected_answer": "Algorithm optimization is the process of improving an algorithm so that it uses less time, memory, or other resources while maintaining correctness. Optimization can involve choosing a better algorithm, using a better data structure, removing redundant operations, or reducing repeated calculations."
    },
    {
        "question": "How do you choose an appropriate algorithm for a problem?",
        "expected_answer": "I first understand the problem requirements and constraints, including input size, expected output, time limits, and memory limits. Then I consider suitable algorithms and data structures, compare their complexities, and choose one that provides the required correctness and performance."
    },
    {
        "question": "What is the difference between best-case, average-case, and worst-case analysis?",
        "expected_answer": "Best-case analysis describes the minimum work required for favorable input. Average-case analysis estimates the expected work over typical inputs or an assumed input distribution. Worst-case analysis describes the maximum work required for any valid input of a given size."
    },
    {
        "question": "Why is space complexity important when designing an algorithm?",
        "expected_answer": "Space complexity is important because memory is a limited resource. An algorithm that is fast but requires excessive memory may not work for large inputs. Therefore, we often need to balance time and memory to create a practical solution."
    },
    {
        "question": "What is an in-place algorithm?",
        "expected_answer": "An in-place algorithm performs most of its operations directly on the input data and uses only a small amount of additional memory. For example, insertion sort is commonly implemented in-place. The exact memory usage can depend on the implementation."
    },
    {
        "question": "What is the difference between an iterative and recursive solution?",
        "expected_answer": "An iterative solution uses loops to repeatedly perform operations, while a recursive solution uses function calls to solve smaller versions of the same problem. Recursive solutions can be easier to understand for problems such as tree traversal, but they may use additional stack memory."
    },
    {
        "question": "How can recursion cause stack overflow?",
        "expected_answer": "Each recursive function call uses space on the call stack. If recursion goes too deep, especially when there is no proper base case or the input is very large, the stack can run out of available memory and cause a stack overflow."
    },
    {
        "question": "What is a recurrence relation in algorithm analysis?",
        "expected_answer": "A recurrence relation describes the running time of a recursive algorithm in terms of the running time for smaller input sizes. For example, merge sort has T(n) = 2T(n/2) + O(n), which represents two recursive calls and linear work for merging."
    },
    {
        "question": "What is the difference between deterministic and randomized algorithms?",
        "expected_answer": "A deterministic algorithm follows the same sequence of operations for the same input and therefore produces predictable behavior. A randomized algorithm uses random choices during execution, so its behavior or running time can vary between executions even for the same input."
    },
    {
        "question": "Why can randomized algorithms be useful?",
        "expected_answer": "Randomized algorithms can reduce the likelihood of consistently encountering bad input cases. For example, randomized pivot selection in quick sort makes it unlikely that the algorithm will repeatedly choose extremely poor pivots, improving expected performance."
    },
    {
        "question": "What is a greedy-choice property?",
        "expected_answer": "The greedy-choice property means that a globally optimal solution can be reached by making a locally optimal choice at each step without needing to reconsider previous choices. Problems such as activity selection have this property, which allows a greedy algorithm to produce an optimal solution."
    },
    {
        "question": "What is optimal substructure?",
        "expected_answer": "Optimal substructure means that an optimal solution to a problem contains optimal solutions to its subproblems. This property is important in dynamic programming and is also present in some greedy problems. It allows a larger optimal solution to be constructed from smaller optimal solutions."
    },
    {
        "question": "Why should algorithm complexity be considered before implementation?",
        "expected_answer": "Considering complexity before implementation helps avoid building a solution that will not scale. An algorithm that works for 100 elements may become unusable for millions of elements if it has poor complexity. Understanding the constraints helps us choose a suitable approach from the beginning."
    }
]
}