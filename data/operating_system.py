questions = {

    "Easy": [

        {
            "question": "What is an Operating System?",
            "expected_answer": "An Operating System is system software that manages computer hardware and software resources and provides services for application programs."
        },

        {
            "question": "What are the main functions of an Operating System?",
            "expected_answer": "The main functions include process management, memory management, file management, device management, security, and providing an interface between users and hardware."
        },

        {
            "question": "What is a kernel?",
            "expected_answer": "The kernel is the core part of an Operating System that manages hardware resources and provides essential services to applications."
        },

        {
            "question": "What is a process?",
            "expected_answer": "A process is a program that is currently executing, along with its associated resources and execution state."
        },

        {
            "question": "What is a program?",
            "expected_answer": "A program is a set of instructions stored on a storage device that can be executed by a computer."
        },

        {
            "question": "What is the difference between a program and a process?",
            "expected_answer": "A program is a passive set of instructions, while a process is an actively executing instance of a program."
        },

        {
            "question": "What is a thread?",
            "expected_answer": "A thread is the smallest unit of CPU execution within a process. Multiple threads can exist within the same process and share its resources."
        },

        {
            "question": "What is multitasking?",
            "expected_answer": "Multitasking is the ability of an Operating System to manage multiple tasks or processes so they can make progress during the same period."
        },

        {
            "question": "What is multiprocessing?",
            "expected_answer": "Multiprocessing is the use of multiple CPU cores or processors to execute multiple processes or threads concurrently."
        },

        {
            "question": "What is multithreading?",
            "expected_answer": "Multithreading is the execution of multiple threads within a process, allowing tasks to run concurrently and share process resources."
        },

        {
            "question": "What is process scheduling?",
            "expected_answer": "Process scheduling is the Operating System mechanism for deciding which ready process or thread should receive CPU time."
        },

        {
            "question": "What is a scheduler?",
            "expected_answer": "A scheduler is an Operating System component that selects processes or threads for execution according to a scheduling policy."
        },

        {
            "question": "What is memory management?",
            "expected_answer": "Memory management is the Operating System function responsible for allocating, tracking, protecting, and releasing main memory for processes."
        },

        {
            "question": "What is virtual memory?",
            "expected_answer": "Virtual memory is a memory-management technique that allows processes to use an address space larger than available physical RAM by using secondary storage as part of the memory system."
        },

        {
            "question": "What is RAM?",
            "expected_answer": "RAM is volatile main memory used to store data and instructions that the CPU needs while programs are running."
        },

        {
            "question": "What is secondary storage?",
            "expected_answer": "Secondary storage is non-volatile storage such as SSDs and hard drives used to store data and programs persistently."
        },

        {
            "question": "What is a file system?",
            "expected_answer": "A file system is a method used by an Operating System to organize, store, name, and access files and directories on storage devices."
        },

        {
            "question": "What is a file?",
            "expected_answer": "A file is a named collection of data stored on a storage device and managed by the Operating System."
        },

        {
            "question": "What is a directory?",
            "expected_answer": "A directory is a structure used by a file system to organize and reference files and other directories."
        },

        {
            "question": "What is a system call?",
            "expected_answer": "A system call is a controlled interface through which a user program requests a service from the Operating System kernel."
        },

        {
            "question": "What is user mode?",
            "expected_answer": "User mode is a restricted CPU execution mode in which normal applications run with limited access to hardware and privileged operations."
        },

        {
            "question": "What is kernel mode?",
            "expected_answer": "Kernel mode is a privileged execution mode in which the Operating System can access hardware and perform protected operations."
        },

        {
            "question": "What is context switching?",
            "expected_answer": "Context switching is the process of saving the state of one running process or thread and restoring the state of another so the CPU can switch execution."
        },

        {
            "question": "What is CPU scheduling?",
            "expected_answer": "CPU scheduling is the process of selecting which ready process or thread should execute on the CPU next."
        },

        {
            "question": "What is FCFS scheduling?",
            "expected_answer": "First-Come, First-Served scheduling executes processes in the order they enter the ready queue."
        },

        {
            "question": "What is Round Robin scheduling?",
            "expected_answer": "Round Robin scheduling gives each ready process a fixed time slice called a quantum and cycles through the processes repeatedly."
        },

        {
            "question": "What is priority scheduling?",
            "expected_answer": "Priority scheduling selects processes for execution based on their assigned priorities."
        },

        {
            "question": "What is a deadlock?",
            "expected_answer": "A deadlock is a situation where two or more processes are permanently waiting for resources held by one another, so none of them can continue."
        },

        {
            "question": "What is starvation?",
            "expected_answer": "Starvation occurs when a process waits for an excessively long time because other processes continue to receive the resources or CPU time it needs."
        },

        {
            "question": "What is synchronization in Operating Systems?",
            "expected_answer": "Synchronization coordinates concurrent processes or threads so that shared resources are accessed safely and race conditions are avoided."
        },

        {
            "question": "What is a race condition?",
            "expected_answer": "A race condition occurs when the result of a program depends on the timing or ordering of concurrent operations accessing shared data."
        },

        {
            "question": "What is a critical section?",
            "expected_answer": "A critical section is a part of a program where shared resources are accessed and which must be protected from unsafe concurrent execution."
        },

        {
            "question": "What is a mutex?",
            "expected_answer": "A mutex is a synchronization mechanism that allows only one thread at a time to enter a protected critical section."
        },

        {
            "question": "What is a semaphore?",
            "expected_answer": "A semaphore is a synchronization mechanism based on a counter that can control access to shared resources by multiple processes or threads."
        },

        {
            "question": "What is paging?",
            "expected_answer": "Paging is a memory-management technique that divides virtual memory into fixed-size pages and physical memory into fixed-size frames."
        },

        {
            "question": "What is a page fault?",
            "expected_answer": "A page fault occurs when a process accesses a virtual-memory page that is not currently available in physical memory, requiring the Operating System to load it."
        },

        {
            "question": "What is segmentation?",
            "expected_answer": "Segmentation is a memory-management technique that divides a program's logical address space into variable-sized segments based on logical units such as code, data, or stack."
        },

        {
            "question": "What is fragmentation?",
            "expected_answer": "Fragmentation is inefficient use of memory caused by free or allocated memory being divided into portions that cannot be used effectively."
        },

        {
            "question": "What is internal fragmentation?",
            "expected_answer": "Internal fragmentation occurs when allocated memory contains unused space inside an allocated block."
        },

        {
            "question": "What is external fragmentation?",
            "expected_answer": "External fragmentation occurs when free memory is available but divided into small non-contiguous blocks, making large allocations difficult."
        },

        {
            "question": "What is swapping?",
            "expected_answer": "Swapping is a memory-management technique in which processes or portions of processes are moved between main memory and secondary storage."
        },

        {
            "question": "What is booting?",
            "expected_answer": "Booting is the process of starting a computer and loading the Operating System into memory so the system can begin normal operation."
        },

        {
            "question": "What is an interrupt?",
            "expected_answer": "An interrupt is a signal that causes the CPU to temporarily stop its current execution and handle an event that requires attention."
        },

        {
            "question": "What is an interrupt handler?",
            "expected_answer": "An interrupt handler is a routine in the Operating System that responds to a particular interrupt and performs the required processing."
        },

        {
            "question": "What is a device driver?",
            "expected_answer": "A device driver is software that allows the Operating System to communicate with and control a particular hardware device."
        },

        {
            "question": "What is I/O management?",
            "expected_answer": "I/O management is the Operating System function that controls communication between applications, the CPU, memory, and input/output devices."
        },

        {
            "question": "What is a buffer?",
            "expected_answer": "A buffer is a temporary area of memory used to hold data while it is being transferred between devices or between components operating at different speeds."
        },

        {
            "question": "What is caching?",
            "expected_answer": "Caching stores frequently accessed data in faster storage so that future accesses can be served more quickly."
        },

        {
            "question": "What is spooling?",
            "expected_answer": "Spooling temporarily stores data for a device or process so that work can be performed asynchronously, such as queuing print jobs."
        },

        {
            "question": "What is a shell?",
            "expected_answer": "A shell is a program that provides an interface through which users can interact with the Operating System, commonly by entering commands."
        },

        {
            "question": "What is a command-line interface?",
            "expected_answer": "A command-line interface is a text-based interface where users interact with the Operating System by entering commands."
        },

        {
            "question": "What is a graphical user interface?",
            "expected_answer": "A graphical user interface allows users to interact with a computer through visual elements such as windows, icons, menus, and buttons."
        },

        {
            "question": "What is a distributed Operating System?",
            "expected_answer": "A distributed Operating System manages resources across multiple connected computers and can provide users with an integrated view of the system."
        },

        {
            "question": "What is a real-time Operating System?",
            "expected_answer": "A real-time Operating System is designed to provide predictable responses within specified timing constraints, which is important in time-sensitive systems."
        },

        {
            "question": "What is an embedded Operating System?",
            "expected_answer": "An embedded Operating System is designed to operate on dedicated devices with specific functions and often has limited hardware resources."
        },

        {
            "question": "What is the difference between hard real-time and soft real-time systems?",
            "expected_answer": "In a hard real-time system, missing a timing deadline can be considered a system failure, while in a soft real-time system, occasional deadline misses are undesirable but may be tolerated."
        }

    ],

    "Medium": [
        {
        "question": "What are the different states of a process?",
        "expected_answer": "The common process states are new, ready, running, waiting or blocked, and terminated. A process moves between these states depending on events such as CPU allocation, I/O requests, and completion."
    },

    {
        "question": "What is a Process Control Block (PCB)?",
        "expected_answer": "A Process Control Block is an Operating System data structure that stores information about a process, such as its process ID, state, program counter, CPU registers, scheduling information, and memory-management information."
    },

    {
        "question": "What is the difference between a process and a thread?",
        "expected_answer": "A process is an independent execution unit with its own address space and resources, while threads are execution units within a process that share the process's address space and many resources."
    },

    {
        "question": "What are the advantages of multithreading?",
        "expected_answer": "Multithreading can improve responsiveness, allow concurrent execution, make better use of multicore processors, and reduce overhead compared with creating separate processes for closely related tasks."
    },

    {
        "question": "What is context switching and why is it expensive?",
        "expected_answer": "Context switching occurs when the CPU saves the state of one process or thread and restores the state of another. It adds overhead because the CPU must save and restore execution state instead of doing useful application work."
    },

    {
        "question": "What is the difference between preemptive and non-preemptive scheduling?",
        "expected_answer": "In preemptive scheduling, the Operating System can interrupt a running process and assign the CPU to another process. In non-preemptive scheduling, a running process keeps the CPU until it finishes, blocks, or voluntarily gives it up."
    },

    {
        "question": "How does First-Come, First-Served (FCFS) scheduling work?",
        "expected_answer": "FCFS schedules processes in the order they arrive in the ready queue. It is simple to implement, but a long process at the front can make shorter processes wait for a long time."
    },

    {
        "question": "What is the convoy effect in CPU scheduling?",
        "expected_answer": "The convoy effect occurs when a long CPU-bound process holds the CPU while many shorter processes wait behind it. It can reduce overall system efficiency and increase waiting time."
    },

    {
        "question": "How does Shortest Job First (SJF) scheduling work?",
        "expected_answer": "SJF selects the process with the smallest expected CPU burst next. It can minimize average waiting time when burst lengths are known or estimated, but long processes may experience starvation."
    },

    {
        "question": "What is Shortest Remaining Time First (SRTF)?",
        "expected_answer": "SRTF is the preemptive version of Shortest Job First. The process with the shortest remaining CPU burst is selected, and a running process can be preempted when a shorter job becomes available."
    },

    {
        "question": "How does Round Robin scheduling work?",
        "expected_answer": "Round Robin assigns each ready process a fixed time quantum and cycles through the ready queue. If a process does not finish within its quantum, it is preempted and placed back in the queue."
    },

    {
        "question": "What happens if the time quantum in Round Robin is too small?",
        "expected_answer": "A very small time quantum causes frequent context switches, increasing scheduling overhead. This can reduce CPU efficiency and leave less time for useful application work."
    },

    {
        "question": "What happens if the time quantum in Round Robin is too large?",
        "expected_answer": "If the time quantum is very large, Round Robin can behave similarly to FCFS because processes may complete before being preempted."
    },

    {
        "question": "What is priority scheduling?",
        "expected_answer": "Priority scheduling selects a process based on its priority value. Depending on the implementation, it can be preemptive or non-preemptive, and processes with low priority may suffer from starvation."
    },

    {
        "question": "What is aging in Operating System scheduling?",
        "expected_answer": "Aging is a technique used to prevent starvation by gradually increasing the priority of a process that has been waiting for a long time."
    },

    {
        "question": "What is throughput in CPU scheduling?",
        "expected_answer": "Throughput is the number of processes completed per unit of time. A scheduling algorithm with higher throughput can complete more work during a given period."
    },

    {
        "question": "What is turnaround time?",
        "expected_answer": "Turnaround time is the total time from when a process enters the system until it completes. It includes waiting time, CPU execution time, and time spent waiting for I/O or other events."
    },

    {
        "question": "What is waiting time?",
        "expected_answer": "Waiting time is the amount of time a process spends waiting in the ready queue for CPU allocation."
    },

    {
        "question": "What is response time?",
        "expected_answer": "Response time is the time from when a request or process is submitted until the system first begins responding or providing CPU service to it."
    },

    {
        "question": "What is the difference between waiting time and turnaround time?",
        "expected_answer": "Waiting time measures how long a process waits in the ready queue, while turnaround time measures the total elapsed time from process submission until completion."
    },

    {
        "question": "What is a race condition and how can it be prevented?",
        "expected_answer": "A race condition occurs when concurrent operations access shared data and the result depends on their timing. It can be prevented using synchronization mechanisms such as mutexes, semaphores, monitors, or other appropriate locking techniques."
    },

    {
        "question": "What is a critical-section problem?",
        "expected_answer": "The critical-section problem is the challenge of designing a protocol that allows concurrent processes or threads to safely access shared resources without causing inconsistent results."
    },

    {
        "question": "What are the requirements for a correct critical-section solution?",
        "expected_answer": "A correct solution should provide mutual exclusion, progress, and bounded waiting. Mutual exclusion prevents simultaneous access, progress ensures eligible processes can enter, and bounded waiting prevents indefinite postponement."
    },

    {
        "question": "What is mutual exclusion?",
        "expected_answer": "Mutual exclusion ensures that only one process or thread at a time can execute a critical section that accesses a particular shared resource."
    },

    {
        "question": "What is the difference between a mutex and a semaphore?",
        "expected_answer": "A mutex is primarily used for exclusive ownership of a resource, allowing one thread to hold the lock at a time. A semaphore is a synchronization counter that can be used for signaling or controlling access to one or more instances of a resource."
    },

    {
        "question": "What is a binary semaphore?",
        "expected_answer": "A binary semaphore is a semaphore whose value is typically restricted to 0 or 1. It can be used for synchronization and, in some designs, for mutual exclusion."
    },

    {
        "question": "What is a counting semaphore?",
        "expected_answer": "A counting semaphore maintains a non-negative count and is useful for controlling access to a resource with multiple available instances."
    },

    {
        "question": "What is a monitor in Operating Systems?",
        "expected_answer": "A monitor is a high-level synchronization construct that encapsulates shared data and the operations that access it, ensuring that only one thread executes monitor procedures at a time."
    },

    {
        "question": "What are the four necessary conditions for deadlock?",
        "expected_answer": "The four necessary conditions are mutual exclusion, hold and wait, no preemption, and circular wait. Deadlock can occur only when all four conditions exist simultaneously."
    },

    {
        "question": "What is the difference between deadlock and starvation?",
        "expected_answer": "In deadlock, a group of processes is permanently blocked because each is waiting for resources held by another. In starvation, a process waits indefinitely because scheduling or resource allocation repeatedly favors other processes."
    },

    {
        "question": "What is deadlock prevention?",
        "expected_answer": "Deadlock prevention ensures that at least one of the four necessary deadlock conditions cannot occur. This can be achieved by restricting resource allocation or process behavior."
    },

    {
        "question": "What is deadlock avoidance?",
        "expected_answer": "Deadlock avoidance dynamically examines resource-allocation requests and grants them only when doing so keeps the system in a safe state."
    },

    {
        "question": "What is the Banker's Algorithm?",
        "expected_answer": "The Banker's Algorithm is a deadlock-avoidance algorithm that checks whether granting a resource request would leave the system in a safe state before actually allocating the resources."
    },

    {
        "question": "What is a safe state in deadlock avoidance?",
        "expected_answer": "A system is in a safe state if there exists at least one order in which all processes can obtain their remaining required resources and finish without causing deadlock."
    },

    {
        "question": "What is deadlock detection?",
        "expected_answer": "Deadlock detection allows deadlocks to occur and periodically checks the system to determine whether a set of processes is deadlocked."
    },

    {
        "question": "What is deadlock recovery?",
        "expected_answer": "Deadlock recovery is the process of restoring the system after detecting a deadlock. Techniques include terminating selected processes or preempting resources when possible."
    },

    {
        "question": "What is virtual memory and why is it useful?",
        "expected_answer": "Virtual memory provides each process with a logical address space that can be larger than physical RAM. It allows more programs to run concurrently and provides memory isolation between processes."
    },

    {
        "question": "What is demand paging?",
        "expected_answer": "Demand paging loads a page into physical memory only when the process actually references it. If the required page is not present, a page fault occurs and the Operating System loads it from secondary storage."
    },

    {
        "question": "What happens during a page fault?",
        "expected_answer": "When a page fault occurs, the Operating System checks whether the memory reference is valid, finds a free frame or selects a victim page if necessary, loads the required page from storage, updates the page table, and resumes the interrupted instruction."
    },

    {
        "question": "What is a page replacement algorithm?",
        "expected_answer": "A page replacement algorithm determines which page should be removed from physical memory when a new page must be loaded and no free frame is available."
    },

    {
        "question": "What is FIFO page replacement?",
        "expected_answer": "FIFO page replacement removes the page that has been in memory for the longest time. It is simple but can sometimes produce more page faults when additional frames are allocated, a phenomenon known as Belady's anomaly."
    },

    {
        "question": "What is the LRU page replacement algorithm?",
        "expected_answer": "Least Recently Used replacement removes the page that has not been referenced for the longest time. It uses recent access history as an approximation of future behavior."
    },

    {
        "question": "What is thrashing?",
        "expected_answer": "Thrashing occurs when a system spends excessive time handling page faults and swapping pages instead of executing useful processes, usually because processes do not have enough physical memory for their active working sets."
    },

    {
        "question": "What is a page table?",
        "expected_answer": "A page table is a data structure used by the Operating System and memory-management hardware to map virtual page numbers to physical frame numbers."
    },

    {
        "question": "What is a Translation Lookaside Buffer (TLB)?",
        "expected_answer": "A TLB is a small, fast cache that stores recently used virtual-to-physical address translations so that memory accesses can avoid repeatedly consulting the page table."
    },

    {
        "question": "What is the difference between paging and segmentation?",
        "expected_answer": "Paging divides memory into fixed-size pages and frames, while segmentation divides a logical address space into variable-sized segments based on meaningful program components such as code, data, or stack."
    },

    {
        "question": "What is internal fragmentation in paging?",
        "expected_answer": "Internal fragmentation in paging occurs when the final allocated page of a process does not completely fill its physical frame, leaving some unused space inside the allocated memory."
    },

    {
        "question": "What is external fragmentation?",
        "expected_answer": "External fragmentation occurs when available free memory is divided into separate non-contiguous blocks, so a large allocation may fail even though the total amount of free memory is sufficient."
    },

    {
        "question": "What is a file allocation method?",
        "expected_answer": "A file allocation method determines how the blocks belonging to a file are organized on storage. Common approaches include contiguous allocation, linked allocation, and indexed allocation."
    },

    {
        "question": "What is contiguous file allocation?",
        "expected_answer": "Contiguous allocation stores a file in consecutive disk blocks. It provides efficient sequential and direct access but can suffer from external fragmentation and difficulty growing files."
    },

    {
        "question": "What is linked file allocation?",
        "expected_answer": "Linked allocation stores a file as a linked list of disk blocks, where each block points to the next block. It avoids external fragmentation but can make direct access inefficient."
    },

    {
        "question": "What is indexed file allocation?",
        "expected_answer": "Indexed allocation uses an index block containing pointers to the data blocks of a file. It supports direct access without requiring the file's blocks to be contiguous."
    },

    {
        "question": "What is a system call and why is it needed?",
        "expected_answer": "A system call provides a controlled interface between user programs and the Operating System kernel. It is needed because normal applications cannot directly perform privileged operations such as managing hardware or protected resources."
    },

    {
        "question": "What is the difference between user mode and kernel mode?",
        "expected_answer": "User mode restricts applications from performing privileged operations directly, while kernel mode gives the Operating System the privileges required to manage hardware, memory, processes, and other protected resources."
    },

    {
        "question": "What is IPC in Operating Systems?",
        "expected_answer": "IPC, or Inter-Process Communication, refers to mechanisms that allow processes to exchange data and coordinate their activities. Common IPC methods include pipes, message queues, shared memory, and sockets."
    },

    {
        "question": "What is shared memory IPC?",
        "expected_answer": "Shared memory IPC allows multiple processes to access a common region of memory for exchanging data. Because processes can access the same memory directly, synchronization is usually required to prevent race conditions."
    },

    {
        "question": "What is message passing in IPC?",
        "expected_answer": "Message passing allows processes to communicate by explicitly sending and receiving messages through Operating System mechanisms rather than directly sharing memory."
    },

    {
        "question": "What is the difference between shared memory and message passing?",
        "expected_answer": "Shared memory allows processes to communicate through a common memory region and usually requires synchronization, while message passing communicates through explicit send and receive operations managed by the Operating System or communication mechanism."
    },

    {
        "question": "What is a zombie process?",
        "expected_answer": "A zombie process is a process that has finished execution but still has an entry in the process table because its parent has not yet collected its termination status."
    },

    {
        "question": "What is an orphan process?",
        "expected_answer": "An orphan process is a process whose original parent has terminated while the child is still running. The Operating System assigns it to an appropriate process that can take responsibility for it."
    },

    {
        "question": "What is a daemon process?",
        "expected_answer": "A daemon is a background process that typically runs without direct user interaction and provides services such as logging, scheduling, networking, or system maintenance."
    },

    {
        "question": "What is process synchronization?",
        "expected_answer": "Process synchronization coordinates the execution of concurrent processes or threads so they can safely access shared resources and maintain consistent results."
    },

    {
        "question": "What is the difference between concurrency and parallelism?",
        "expected_answer": "Concurrency means multiple tasks can make progress during overlapping periods, while parallelism means multiple tasks are actually executing simultaneously, typically on multiple CPU cores."
    },

    {
        "question": "What is a CPU burst and an I/O burst?",
        "expected_answer": "A CPU burst is a period during which a process executes instructions on the CPU, while an I/O burst is a period during which the process waits for or performs input/output operations."
    },

    {
        "question": "Why does an Operating System use scheduling algorithms?",
        "expected_answer": "Scheduling algorithms help decide which process should use the CPU next. They aim to improve measures such as CPU utilization, throughput, response time, turnaround time, and fairness."
    },

    {
        "question": "What is CPU utilization?",
        "expected_answer": "CPU utilization is the percentage of time the CPU is busy performing useful work during a given period. Scheduling and workload management aim to keep the CPU efficiently utilized without harming responsiveness."
    },

    {
        "question": "What is a process scheduler's ready queue?",
        "expected_answer": "The ready queue contains processes or threads that are prepared to execute but are currently waiting for CPU time."
    },

    {
        "question": "What is long-term scheduling?",
        "expected_answer": "The long-term scheduler controls which jobs are admitted into the system for execution. It influences the degree of multiprogramming and the mix of CPU-bound and I/O-bound processes."
    },

    {
        "question": "What is short-term scheduling?",
        "expected_answer": "The short-term scheduler selects a process or thread from the ready queue to run on the CPU. It operates frequently and therefore must be efficient."
    },

    {
        "question": "What is medium-term scheduling?",
        "expected_answer": "The medium-term scheduler can temporarily remove processes from main memory and later bring them back, helping manage memory pressure and the degree of multiprogramming."
    },

    {
        "question": "What is the difference between a process scheduler and a dispatcher?",
        "expected_answer": "The scheduler selects which ready process should run, while the dispatcher performs the steps needed to give the selected process control of the CPU, including context switching and switching to the appropriate execution mode."
    }


    ],
    # Hard
    "Hard": [
    {
        "question": "How would you troubleshoot a system with very high CPU utilization?",
        "expected_answer": "I would identify the processes consuming the CPU, check whether the workload is expected, examine process states and scheduling behavior, and inspect application and system logs. I would then determine whether the issue is caused by an application, excessive concurrency, an inefficient process, or insufficient CPU capacity."
    },

    {
        "question": "How would you troubleshoot excessive memory usage on a system?",
        "expected_answer": "I would identify processes with high memory consumption, check memory and swap usage, inspect whether memory usage grows over time, and determine whether the cause is a legitimate workload, memory leak, excessive caching, or insufficient RAM."
    },

    {
        "question": "What is a memory leak?",
        "expected_answer": "A memory leak occurs when a program allocates memory but fails to release memory that it no longer needs. Over time, this can increase memory usage and eventually cause performance problems or allocation failures."
    },

    {
        "question": "How can a memory leak affect an Operating System?",
        "expected_answer": "A memory leak can gradually consume available memory, increase paging or swapping, reduce system performance, and potentially cause applications or the system to fail when sufficient memory cannot be allocated."
    },

    {
        "question": "Why can excessive context switching reduce performance?",
        "expected_answer": "Context switching requires saving and restoring CPU state and may also disturb CPU caches and translation caches. If switching happens too frequently, a larger portion of CPU time is spent on overhead instead of useful application work."
    },

    {
        "question": "How would you choose a CPU scheduling algorithm for an interactive system?",
        "expected_answer": "I would prioritize low response time and reasonable fairness. A preemptive algorithm such as Round Robin can provide responsive sharing of CPU time, while the time quantum must be chosen to balance responsiveness against context-switching overhead."
    },

    {
        "question": "Why can Shortest Job First provide low average waiting time?",
        "expected_answer": "Shortest Job First tends to execute shorter CPU bursts earlier, which reduces the amount of time short processes spend waiting behind long processes. Under ideal conditions with known burst lengths, it minimizes average waiting time."
    },

    {
        "question": "What is the main problem with Shortest Job First scheduling?",
        "expected_answer": "The exact future CPU burst length is usually unknown, so the Operating System must estimate it. Also, continuously arriving short jobs can cause long jobs to wait for an excessive amount of time."
    },

    {
        "question": "How can starvation be prevented in priority scheduling?",
        "expected_answer": "A common solution is aging, where the priority of a waiting process gradually increases. This eventually allows long-waiting processes to receive CPU time."
    },

    {
        "question": "How would you detect a deadlock using a resource-allocation graph?",
        "expected_answer": "I would represent processes and resource types as nodes and allocation and request relationships as edges. A cycle can indicate deadlock when each resource involved has a single instance; with multiple instances, additional analysis is required."
    },

    {
        "question": "Can a cycle in a resource-allocation graph always mean deadlock?",
        "expected_answer": "No. With multiple instances of resource types, a cycle does not necessarily mean deadlock. For single-instance resource types, a cycle indicates deadlock when the graph represents the relevant allocation and request relationships."
    },

    {
        "question": "How would you recover from a deadlock?",
        "expected_answer": "Possible recovery techniques include terminating selected processes, preempting resources when safe, or rolling back processes to earlier states. The choice depends on system requirements and the cost of losing work."
    },

    {
        "question": "Why is deadlock prevention sometimes impractical?",
        "expected_answer": "Prevention may require restrictive resource-allocation rules that reduce concurrency or resource utilization. In some systems, it is more practical to use avoidance, detection and recovery, or carefully designed application-level synchronization."
    },

    {
        "question": "What is livelock?",
        "expected_answer": "Livelock occurs when processes remain active and repeatedly change their states or respond to each other but make no useful progress. Unlike deadlock, the processes are not necessarily blocked."
    },

    {
        "question": "What is the difference between deadlock and livelock?",
        "expected_answer": "In deadlock, processes are blocked while waiting for resources or events. In livelock, processes continue executing but repeatedly react to each other without making meaningful progress."
    },

    {
        "question": "What is priority inversion?",
        "expected_answer": "Priority inversion occurs when a high-priority task is forced to wait for a lower-priority task holding a required resource, while medium-priority tasks may prevent the lower-priority task from running."
    },

    {
        "question": "How can priority inversion be handled?",
        "expected_answer": "Priority inheritance can temporarily raise the priority of the lower-priority task holding the required resource. Priority ceiling protocols are another approach for controlling priority-related blocking."
    },

    {
        "question": "What is the working-set concept in virtual memory?",
        "expected_answer": "The working set is the collection of pages a process is actively using during a particular period. Keeping enough of these pages in memory can reduce page faults and help prevent thrashing."
    },

    {
        "question": "How can an Operating System reduce thrashing?",
        "expected_answer": "The Operating System can reduce thrashing by giving processes sufficient frames, controlling the degree of multiprogramming, using working-set or page-fault-frequency techniques, and reducing memory pressure."
    },

    {
        "question": "Why does increasing the number of processes sometimes reduce performance?",
        "expected_answer": "More processes increase competition for CPU and memory resources. If memory becomes insufficient, page faults and swapping can increase, causing thrashing and reducing useful CPU work."
    },

    {
        "question": "What is Belady's anomaly?",
        "expected_answer": "Belady's anomaly is a situation in which increasing the number of available page frames causes more page faults for certain page-replacement algorithms, particularly FIFO."
    },

    {
        "question": "Why does LRU generally perform better than FIFO for many workloads?",
        "expected_answer": "LRU uses recent access history and assumes pages used recently are more likely to be used again soon. FIFO ignores how frequently or recently pages are accessed."
    },

    {
        "question": "Why is implementing exact LRU expensive?",
        "expected_answer": "Exact LRU requires tracking the ordering or timestamps of memory references, which can introduce significant hardware or software overhead. Practical systems therefore use approximations."
    },

    {
        "question": "What is demand paging and what are its main benefits?",
        "expected_answer": "Demand paging loads pages only when they are needed. It reduces initial memory usage and allows processes to use address spaces larger than physical memory, but page faults can introduce significant latency."
    },

    {
        "question": "What is copy-on-write?",
        "expected_answer": "Copy-on-write allows multiple processes or address spaces to initially share the same physical memory pages. A private copy is created only when one process attempts to modify a shared page."
    },

    {
        "question": "Why is copy-on-write useful when creating a process?",
        "expected_answer": "It avoids immediately copying all of the parent's memory. The parent and child can initially share pages, and only modified pages need to be copied, reducing memory usage and unnecessary copying."
    },

    {
        "question": "What is memory protection?",
        "expected_answer": "Memory protection prevents one process from improperly accessing another process's memory or protected Operating System memory. Hardware mechanisms such as page permissions and address translation help enforce these boundaries."
    },

    {
        "question": "What is address translation?",
        "expected_answer": "Address translation converts a virtual address generated by a process into a physical address in main memory. The Operating System and memory-management hardware cooperate to perform this translation."
    },

    {
        "question": "Why is a TLB important for virtual memory performance?",
        "expected_answer": "The TLB caches recently used virtual-to-physical address translations. A TLB hit avoids an additional page-table lookup, reducing the time required for memory access."
    },

    {
        "question": "What happens when a TLB miss occurs?",
        "expected_answer": "When a TLB miss occurs, the system must obtain the required address translation from the page table or another translation mechanism. The translation may then be inserted into the TLB for future accesses."
    },

    {
        "question": "What is a multi-level page table?",
        "expected_answer": "A multi-level page table divides the page table into multiple levels so that only the portions needed for a process's address space have to be allocated, reducing memory overhead for sparse address spaces."
    },

    {
        "question": "Why are page sizes important in virtual memory?",
        "expected_answer": "Page size affects page-table size, TLB coverage, internal fragmentation, and the amount of data transferred during a page fault. Larger pages can reduce page-table overhead but may increase wasted space."
    },

    {
        "question": "What is memory-mapped file I/O?",
        "expected_answer": "Memory-mapped file I/O maps a file or portion of a file into a process's virtual address space, allowing the program to access file contents through normal memory operations."
    },

    {
        "question": "What are the advantages of memory-mapped files?",
        "expected_answer": "Memory-mapped files can simplify file access and allow the Operating System to manage file data through virtual memory. They can also reduce explicit copying between application buffers and the file system."
    },

    {
        "question": "What is the difference between a system call and a function call?",
        "expected_answer": "A normal function call transfers control within the program or its libraries, while a system call requests a service from the Operating System kernel and may require a controlled transition to privileged execution."
    },

    {
        "question": "What happens during a system call?",
        "expected_answer": "A program places the system-call number and required arguments in the expected locations and executes a controlled entry instruction. The kernel validates the request, performs the operation, and returns a result to the program."
    },

    {
        "question": "Why should user programs not access hardware directly?",
        "expected_answer": "Direct unrestricted hardware access could allow one program to interfere with other programs or the Operating System. Privileged access through the kernel provides protection, isolation, and controlled resource management."
    },

    {
        "question": "What is a kernel panic or kernel crash?",
        "expected_answer": "A kernel panic or kernel crash occurs when the Operating System kernel encounters a condition from which it cannot safely continue. The system may stop, restart, or enter a recovery state depending on the Operating System."
    },

    {
        "question": "How would you troubleshoot a system that frequently freezes?",
        "expected_answer": "I would check CPU, memory, disk, and I/O utilization, inspect system and application logs, look for driver or hardware errors, check for deadlocks or resource exhaustion, and examine recent software or configuration changes."
    },

    {
        "question": "How would you troubleshoot very high disk I/O?",
        "expected_answer": "I would identify which processes are generating the I/O, determine whether the workload is sequential or random, inspect disk latency and queue depth, check memory pressure and swapping, and review application and system logs."
    },

    {
        "question": "What is disk scheduling?",
        "expected_answer": "Disk scheduling determines the order in which pending disk I/O requests are serviced. Its goal is generally to reduce access time and improve throughput while maintaining acceptable fairness."
    },

    {
        "question": "What is the SCAN disk scheduling algorithm?",
        "expected_answer": "SCAN services disk requests while moving the disk head in one direction and then reverses direction, similar to an elevator. It can provide more predictable waiting times than simple request ordering."
    },

    {
        "question": "What is C-SCAN disk scheduling?",
        "expected_answer": "C-SCAN services requests while moving the disk head in one direction. After reaching the end, it returns to the beginning without servicing requests during the return, providing more uniform waiting times."
    },

    {
        "question": "What is the difference between SCAN and C-SCAN?",
        "expected_answer": "SCAN services requests in both directions as the head moves back and forth, while C-SCAN services requests in one direction and makes a return trip to the beginning without servicing requests."
    },

    {
        "question": "What is the producer-consumer problem?",
        "expected_answer": "The producer-consumer problem involves producers adding data to a shared buffer and consumers removing it. Synchronization is required to prevent producers from overflowing the buffer and consumers from reading when it is empty."
    },

    {
        "question": "What is the readers-writers problem?",
        "expected_answer": "The readers-writers problem concerns shared data that can be read by multiple readers concurrently but should be protected from simultaneous conflicting writes. Synchronization must balance correctness and fairness."
    },

    {
        "question": "What is the dining philosophers problem?",
        "expected_answer": "The dining philosophers problem is a synchronization example where processes compete for multiple shared resources. Poor resource allocation can lead to deadlock or starvation."
    },

    {
        "question": "How can the dining philosophers deadlock be prevented?",
        "expected_answer": "Possible solutions include imposing an ordering on resource acquisition, allowing at most a limited number of philosophers to compete simultaneously, or using a centralized synchronization mechanism."
    },

    {
        "question": "What is a reentrant function and why is it important in concurrent systems?",
        "expected_answer": "A reentrant function can be safely interrupted and called again before the previous invocation finishes because it does not rely on unsafe shared mutable state. This property is useful in concurrent and interrupt-driven systems."
    },

    {
        "question": "What is the difference between a spinlock and a mutex?",
        "expected_answer": "A spinlock makes a waiting thread repeatedly check until the lock becomes available, consuming CPU time. A mutex can put the waiting thread to sleep, making it more suitable when the expected wait is longer."
    },

    {
        "question": "When is a spinlock useful?",
        "expected_answer": "A spinlock can be useful when the protected critical section is extremely short and the expected wait is shorter than the overhead of putting a thread to sleep and waking it."
    },

    {
        "question": "What is lock contention?",
        "expected_answer": "Lock contention occurs when multiple threads frequently compete for the same lock. High contention can reduce parallelism and increase waiting and synchronization overhead."
    },

    {
        "question": "How can lock contention be reduced?",
        "expected_answer": "Lock contention can be reduced by shortening critical sections, reducing shared mutable state, using finer-grained locks where appropriate, improving data partitioning, or choosing synchronization mechanisms suited to the workload."
    },

    {
        "question": "What is false sharing?",
        "expected_answer": "False sharing occurs when independent variables used by different CPU cores occupy the same cache line. Updates by one core can invalidate the cache line for another core, reducing performance even though the variables are logically unrelated."
    },

    {
        "question": "What is CPU affinity?",
        "expected_answer": "CPU affinity controls or influences which CPU cores a process or thread can execute on. It can improve cache locality and provide predictable CPU placement in some workloads."
    },

    {
        "question": "What is NUMA?",
        "expected_answer": "NUMA, or Non-Uniform Memory Access, is a multiprocessor architecture where memory access time depends on which processor and memory region are involved. Accessing local memory is generally faster than accessing remote memory."
    },

    {
        "question": "Why is NUMA awareness important for Operating Systems?",
        "expected_answer": "NUMA-aware scheduling and memory allocation can keep processes close to the memory they frequently access, reducing expensive remote-memory accesses and improving performance on large multiprocessor systems."
    },

    {
        "question": "What is a real-time scheduling system?",
        "expected_answer": "A real-time scheduling system schedules tasks according to timing requirements and aims to ensure that important tasks complete within their specified deadlines."
    },

    {
        "question": "What is the difference between hard and soft real-time scheduling requirements?",
        "expected_answer": "Hard real-time requirements treat missed deadlines as unacceptable or potentially catastrophic, while soft real-time systems tolerate occasional deadline misses with degraded service rather than complete failure."
    },

    {
        "question": "How does an Operating System provide process isolation?",
        "expected_answer": "The Operating System uses separate virtual address spaces, memory protection, privilege levels, controlled system calls, and resource-management mechanisms to prevent processes from improperly interfering with one another."
    },

    {
        "question": "How does an Operating System maintain security between processes?",
        "expected_answer": "It uses mechanisms such as user and kernel privilege levels, access permissions, process isolation, authentication and authorization, protected memory, and controlled access to system resources."
    },

    {
        "question": "What happens when a process terminates?",
        "expected_answer": "The Operating System releases the process's resources, records its termination status, and removes its active process state. If the parent has not collected the status, the process may temporarily remain as a zombie."
    },

    {
        "question": "Why are orphan and zombie processes different?",
        "expected_answer": "An orphan is still running but its original parent has terminated. A zombie has already terminated but remains in the process table because its parent has not yet collected its exit status."
    },

    {
        "question": "How would you design a system to avoid deadlocks when multiple resources are required?",
        "expected_answer": "I would establish a consistent resource-acquisition order, minimize resource holding time, avoid unnecessary nested locks, and use timeouts or deadlock-detection mechanisms where appropriate."
    },

    {
        "question": "How would you debug a multithreaded application with intermittent incorrect results?",
        "expected_answer": "I would look for shared mutable data, race conditions, unsafe synchronization, incorrect lock ordering, and timing-dependent behavior. I would use thread-aware debugging, logging, race-detection tools, and carefully designed reproducible tests."
    },

    {
        "question": "Why can adding more threads sometimes make a program slower?",
        "expected_answer": "Additional threads can increase synchronization overhead, context switching, lock contention, cache contention, and scheduling overhead. If the workload is not sufficiently parallel, these costs can outweigh the benefits of concurrency."
    },

    {
        "question": "How would you decide whether a workload should use multiple processes or multiple threads?",
        "expected_answer": "I would consider memory isolation, communication needs, fault isolation, CPU parallelism, shared-state requirements, and creation or synchronization overhead. Threads are useful for shared-memory concurrency, while processes provide stronger isolation."
    },

    {
        "question": "How can an Operating System improve system responsiveness under heavy load?",
        "expected_answer": "It can use appropriate scheduling priorities and time slicing, manage memory pressure, reduce unnecessary I/O, control background workloads, and ensure that interactive tasks receive timely CPU and I/O service."
    },

    {
        "question": "How would you investigate a sudden increase in page faults?",
        "expected_answer": "I would check available physical memory, process working sets, memory allocation patterns, swap activity, recent workload changes, and page-replacement behavior. I would determine whether the increase is caused by legitimate workload growth, memory pressure, or a memory leak."
    },

    {
        "question": "What factors affect Operating System performance?",
        "expected_answer": "Important factors include CPU utilization, memory capacity and access patterns, cache behavior, disk and network I/O, scheduling overhead, context switching, synchronization contention, workload characteristics, and resource-management policies."
    },

    {
        "question": "How does virtualization interact with an Operating System?",
        "expected_answer": "Virtualization allows multiple virtual machines to share physical hardware through a hypervisor. Each guest Operating System runs in an isolated virtual environment while the hypervisor manages access to CPU, memory, storage, and devices."
    },

    {
        "question": "What is a hypervisor?",
        "expected_answer": "A hypervisor is software or firmware that creates and manages virtual machines and controls their access to physical hardware resources."
    },

    {
        "question": "What is the difference between Type 1 and Type 2 hypervisors?",
        "expected_answer": "A Type 1 hypervisor runs directly on the physical hardware, while a Type 2 hypervisor runs on top of a host Operating System."
    },

    {
        "question": "How does an Operating System handle limited physical memory when many processes are running?",
        "expected_answer": "It can use virtual memory, paging, page replacement, memory reclamation, and process-management techniques. The goal is to maintain useful execution while controlling memory pressure and avoiding excessive swapping."
    },

    {
        "question": "What is the difference between swapping and paging?",
        "expected_answer": "Swapping traditionally refers to moving an entire process or large process state between memory and secondary storage, while paging moves fixed-size pages individually. Modern systems commonly rely heavily on paging."
    },

    {
        "question": "How would you troubleshoot a process that is stuck in a blocked state?",
        "expected_answer": "I would determine what event or resource the process is waiting for, inspect its system calls and I/O operations, check locks and synchronization objects, and examine relevant system logs and resource usage."
    },

    {
        "question": "How can an Operating System balance fairness and performance in CPU scheduling?",
        "expected_answer": "It can combine priorities, time slicing, aging, and workload-aware scheduling. The goal is to provide reasonable CPU access to processes while maintaining good throughput and responsiveness."
    },

    {
        "question": "Why is synchronization necessary even on multicore processors?",
        "expected_answer": "Multiple cores can execute threads simultaneously and access shared data concurrently. Without proper synchronization, operations can interleave unpredictably and cause race conditions, inconsistent data, or visibility problems."
    },

    {
        "question": "What is the purpose of atomic operations in concurrent programming?",
        "expected_answer": "Atomic operations perform a read-modify-write or similar operation as one indivisible action from the perspective of other threads. They can be used to implement synchronization and safely update shared state."
    },

    {
        "question": "What is a memory barrier or fence?",
        "expected_answer": "A memory barrier is a synchronization mechanism that constrains the ordering and visibility of memory operations between CPUs or threads. It helps ensure that concurrent code observes memory operations according to the required ordering rules."
    },

    {
        "question": "How would you explain the role of an Operating System in a modern application?",
        "expected_answer": "The Operating System provides applications with controlled access to CPU, memory, storage, networking, and devices. It also manages processes, security, file systems, communication, and resource sharing so applications do not need to manage hardware directly."
    }

]
}