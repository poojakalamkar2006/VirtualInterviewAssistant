questions = {

    # Easy
    "Easy": [

        {
            "question": "What is a DBMS?",
            "expected_answer": "A DBMS (Database Management System) is software used to create, store, organize, retrieve, update, and manage data in databases."
        },

        {
            "question": "What is a database?",
            "expected_answer": "A database is an organized collection of data that can be stored, accessed, managed, and updated efficiently."
        },

        {
            "question": "What is the difference between a database and a DBMS?",
            "expected_answer": "A database is the collection of stored data, while a DBMS is the software used to create, manage, access, and control that data."
        },

        {
            "question": "What are the main advantages of a DBMS?",
            "expected_answer": "A DBMS provides data security, integrity, controlled access, reduced redundancy, backup and recovery, concurrency control, and efficient data management."
        },

        {
            "question": "What is an RDBMS?",
            "expected_answer": "An RDBMS (Relational Database Management System) stores data in related tables consisting of rows and columns and generally uses SQL to manage the data."
        },

        {
            "question": "What is the difference between DBMS and RDBMS?",
            "expected_answer": "DBMS is a general term for database management software, while RDBMS specifically manages data using the relational model with tables and relationships."
        },

        {
            "question": "What is a table in a database?",
            "expected_answer": "A table is a structure used to store related data in rows and columns."
        },

        {
            "question": "What is a row in a database table?",
            "expected_answer": "A row represents one complete record or instance of data in a table."
        },

        {
            "question": "What is a column in a database table?",
            "expected_answer": "A column represents an attribute or property of the data stored in a table."
        },

        {
            "question": "What is a schema?",
            "expected_answer": "A schema is the logical structure or design of a database that defines tables, columns, relationships, constraints, and other database objects."
        },

        {
            "question": "What is a primary key?",
            "expected_answer": "A primary key is a column or combination of columns that uniquely identifies each row in a table. It cannot contain NULL values."
        },

        {
            "question": "What is a foreign key?",
            "expected_answer": "A foreign key is a column or set of columns that references a key in another table and is used to establish relationships between tables."
        },

        {
            "question": "What is a candidate key?",
            "expected_answer": "A candidate key is a minimal set of attributes that can uniquely identify each row in a table. A table can have multiple candidate keys."
        },

        {
            "question": "What is a super key?",
            "expected_answer": "A super key is any set of one or more attributes that uniquely identifies a row in a table. It may contain unnecessary attributes."
        },

        {
            "question": "What is an alternate key?",
            "expected_answer": "An alternate key is a candidate key that was not selected as the primary key."
        },

        {
            "question": "What is a composite key?",
            "expected_answer": "A composite key is a key made up of two or more columns that together uniquely identify a row."
        },

        {
            "question": "What is a unique key?",
            "expected_answer": "A unique key constraint ensures that values in a column or combination of columns are unique. NULL handling can depend on the database system."
        },

        {
            "question": "What is a constraint in DBMS?",
            "expected_answer": "A constraint is a rule applied to database data to maintain accuracy, consistency, and integrity."
        },

        {
            "question": "What are common types of database constraints?",
            "expected_answer": "Common constraints include PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, and DEFAULT."
        },

        {
            "question": "What is the NOT NULL constraint?",
            "expected_answer": "The NOT NULL constraint ensures that a column cannot contain NULL values."
        },

        {
            "question": "What is the CHECK constraint?",
            "expected_answer": "The CHECK constraint restricts values in a column according to a specified condition."
        },

        {
            "question": "What is the DEFAULT constraint?",
            "expected_answer": "The DEFAULT constraint provides a predefined value when no value is supplied for a column during insertion."
        },

        {
            "question": "What is data integrity?",
            "expected_answer": "Data integrity means maintaining the accuracy, consistency, validity, and reliability of data throughout its lifecycle."
        },

        {
            "question": "What is referential integrity?",
            "expected_answer": "Referential integrity ensures that foreign key values correctly reference existing rows in the related table, unless NULL or other permitted behavior applies."
        },

        {
            "question": "What is data redundancy?",
            "expected_answer": "Data redundancy occurs when the same data is unnecessarily stored in multiple places, which can increase storage usage and cause inconsistency."
        },

        {
            "question": "What is normalization?",
            "expected_answer": "Normalization is the process of organizing database data to reduce unnecessary redundancy and prevent data anomalies."
        },

        {
            "question": "What is denormalization?",
            "expected_answer": "Denormalization intentionally adds some redundancy to a database to improve read performance or simplify certain queries."
        },

        {
            "question": "What is 1NF?",
            "expected_answer": "First Normal Form requires each field to contain atomic values and prevents repeating groups or multi-valued attributes in a relational table."
        },

        {
            "question": "What is 2NF?",
            "expected_answer": "Second Normal Form requires a table to be in 1NF and ensures that non-key attributes depend on the whole candidate key, not only part of a composite key."
        },

        {
            "question": "What is 3NF?",
            "expected_answer": "Third Normal Form requires 2NF and removes inappropriate transitive dependencies so non-key attributes depend directly on candidate keys."
        },

        {
            "question": "What is BCNF?",
            "expected_answer": "BCNF is a stronger form of 3NF where every determinant must be a candidate key."
        },

        {
            "question": "What is SQL?",
            "expected_answer": "SQL (Structured Query Language) is used to define, query, manipulate, and control data in relational database systems."
        },

        {
            "question": "What is DDL?",
            "expected_answer": "DDL (Data Definition Language) contains commands used to define or modify database structures, such as CREATE, ALTER, and DROP."
        },

        {
            "question": "What is DML?",
            "expected_answer": "DML (Data Manipulation Language) contains commands used to retrieve or modify data, such as SELECT, INSERT, UPDATE, and DELETE."
        },

        {
            "question": "What is DCL?",
            "expected_answer": "DCL (Data Control Language) is used to control database access and permissions, commonly through GRANT and REVOKE."
        },

        {
            "question": "What is TCL?",
            "expected_answer": "TCL (Transaction Control Language) manages transactions using commands such as COMMIT, ROLLBACK, and SAVEPOINT."
        },

        {
            "question": "What is the difference between DELETE, DROP, and TRUNCATE?",
            "expected_answer": "DELETE removes selected rows, TRUNCATE removes all rows from a table while keeping its structure, and DROP removes the table itself."
        },

        {
            "question": "What is a view?",
            "expected_answer": "A view is a virtual table based on the result of a query. It generally stores the query definition rather than a separate copy of the underlying data."
        },

        {
            "question": "What is an index?",
            "expected_answer": "An index is a database structure that can speed up data retrieval by providing an efficient way to locate rows, although it adds storage and write overhead."
        },

        {
            "question": "Why are indexes used?",
            "expected_answer": "Indexes are mainly used to improve query performance by reducing the amount of data that must be examined to find matching rows."
        },

        {
            "question": "What is a transaction?",
            "expected_answer": "A transaction is a logical unit of database operations that should be completed according to defined consistency and reliability rules."
        },

        {
            "question": "What are ACID properties?",
            "expected_answer": "ACID stands for Atomicity, Consistency, Isolation, and Durability, which are properties used to ensure reliable transaction processing."
        },

        {
            "question": "What is atomicity?",
            "expected_answer": "Atomicity means that a transaction is treated as one unit: either all required operations succeed or the transaction is rolled back."
        },

        {
            "question": "What is consistency in ACID?",
            "expected_answer": "Consistency means that a successful transaction moves the database from one valid state to another while preserving defined integrity rules."
        },

        {
            "question": "What is isolation?",
            "expected_answer": "Isolation controls how the intermediate effects of concurrent transactions are exposed to one another."
        },

        {
            "question": "What is durability?",
            "expected_answer": "Durability means that once a transaction is successfully committed, its changes are preserved even after failures such as a system crash."
        },

        {
            "question": "What is NULL in a database?",
            "expected_answer": "NULL represents the absence of a value or an unknown value. It is different from zero, an empty string, or false."
        },

        {
            "question": "What is a relationship in a database?",
            "expected_answer": "A relationship describes how records in different tables are logically connected, usually through keys."
        },

        {
            "question": "What are the common types of relationships in DBMS?",
            "expected_answer": "The common relationships are one-to-one, one-to-many, and many-to-many."
        },

        {
            "question": "What is a one-to-one relationship?",
            "expected_answer": "In a one-to-one relationship, each record in one table is associated with at most one record in another table, and vice versa."
        },

        {
            "question": "What is a one-to-many relationship?",
            "expected_answer": "In a one-to-many relationship, one record in one table can be associated with multiple records in another table."
        },

        {
            "question": "What is a many-to-many relationship?",
            "expected_answer": "In a many-to-many relationship, multiple records in one table can relate to multiple records in another table, usually through a junction table."
        },

        {
            "question": "What is an ER model?",
            "expected_answer": "The Entity-Relationship model represents a database using entities, attributes, and relationships to describe its logical structure."
        },

        {
            "question": "What is an entity?",
            "expected_answer": "An entity is a distinguishable real-world object or concept about which data is stored, such as a student, employee, or product."
        },

        {
            "question": "What is an attribute?",
            "expected_answer": "An attribute is a property or characteristic that describes an entity, such as a student's name or employee's salary."
        },

        {
            "question": "What is a stored procedure?",
            "expected_answer": "A stored procedure is a named collection of SQL or procedural statements stored in the database and executed when called."
        },

        {
            "question": "What is a trigger?",
            "expected_answer": "A trigger is database logic that automatically executes when specified events occur, such as INSERT, UPDATE, or DELETE."
        },

        {
            "question": "What is a cursor in DBMS?",
            "expected_answer": "A cursor is a mechanism that allows database programs to process query results row by row when set-based processing is not sufficient."
        },

        {
            "question": "What is database security?",
            "expected_answer": "Database security protects data from unauthorized access, modification, disclosure, or destruction using authentication, authorization, encryption, and other controls."
        },

        {
            "question": "What is authentication in DBMS?",
            "expected_answer": "Authentication verifies the identity of a user or application attempting to access the database."
        },

        {
            "question": "What is authorization in DBMS?",
            "expected_answer": "Authorization determines what operations or database objects an authenticated user is allowed to access."
        }

    ],


    # Medium
    "Medium": [

        {
            "question": "What is functional dependency in DBMS?",
            "expected_answer": "A functional dependency describes a relationship where one set of attributes determines another set. It is written as X -> Y."
        },

        {
            "question": "What is a trivial functional dependency?",
            "expected_answer": "A functional dependency X -> Y is trivial when Y is a subset of X."
        },

        {
            "question": "What is a non-trivial functional dependency?",
            "expected_answer": "A functional dependency X -> Y is non-trivial when Y is not a subset of X."
        },

        {
            "question": "What is a partial dependency?",
            "expected_answer": "Partial dependency occurs when a non-key attribute depends on only part of a composite candidate key instead of the entire key."
        },

        {
            "question": "What is transitive dependency?",
            "expected_answer": "A transitive dependency occurs when a non-key attribute depends on another non-key attribute through a candidate key."
        },

        {
            "question": "Why is normalization important in DBMS?",
            "expected_answer": "Normalization reduces unnecessary data redundancy and helps prevent insertion, update, and deletion anomalies."
        },

        {
            "question": "What is an insertion anomaly?",
            "expected_answer": "An insertion anomaly occurs when data cannot be inserted without adding unrelated or unnecessary information."
        },

        {
            "question": "What is an update anomaly?",
            "expected_answer": "An update anomaly occurs when the same fact is stored in multiple places and changing it requires updating multiple rows, which can cause inconsistency."
        },

        {
            "question": "What is a deletion anomaly?",
            "expected_answer": "A deletion anomaly occurs when deleting one piece of information unintentionally removes other important information."
        },

        {
            "question": "What is the difference between 3NF and BCNF?",
            "expected_answer": "3NF allows certain dependencies where the dependent attribute is part of a candidate key, while BCNF requires every determinant to be a candidate key."
        },

        {
            "question": "What is lossless decomposition?",
            "expected_answer": "A decomposition is lossless when joining the decomposed tables recreates the original relation without generating incorrect or extra tuples."
        },

        {
            "question": "What is dependency preservation?",
            "expected_answer": "Dependency preservation means that all important functional dependencies can be enforced using the decomposed relations without requiring joins."
        },

        {
            "question": "What is a natural join?",
            "expected_answer": "A natural join automatically joins tables using columns with the same names and compatible data types and returns one copy of the common columns."
        },

        {
            "question": "What is an inner join?",
            "expected_answer": "An inner join returns only rows that have matching values in both joined tables."
        },

        {
            "question": "What is a left outer join?",
            "expected_answer": "A left outer join returns all rows from the left table and matching rows from the right table. Unmatched right-side values are represented as NULL."
        },

        {
            "question": "What is a right outer join?",
            "expected_answer": "A right outer join returns all rows from the right table and matching rows from the left table. Unmatched left-side values are represented as NULL."
        },

        {
            "question": "What is a full outer join?",
            "expected_answer": "A full outer join returns matching rows plus unmatched rows from both tables, using NULL for missing values."
        },

        {
            "question": "What is a self join?",
            "expected_answer": "A self join joins a table with itself, usually using different aliases to compare related rows within the same table."
        },

        {
            "question": "What is a cross join?",
            "expected_answer": "A cross join produces the Cartesian product, combining every row from one table with every row from the other table."
        },

        {
            "question": "What is the difference between WHERE and HAVING?",
            "expected_answer": "WHERE filters individual rows before grouping, while HAVING filters groups after GROUP BY and is commonly used with aggregate functions."
        },

        {
            "question": "What is GROUP BY in SQL?",
            "expected_answer": "GROUP BY groups rows with the same values in specified columns so aggregate functions can be applied to each group."
        },

        {
            "question": "What are aggregate functions in SQL?",
            "expected_answer": "Aggregate functions perform calculations over multiple rows, such as COUNT, SUM, AVG, MIN, and MAX."
        },

        {
            "question": "What is the difference between COUNT(*) and COUNT(column)?",
            "expected_answer": "COUNT(*) counts rows, while COUNT(column) counts only rows where that column is not NULL."
        },

        {
            "question": "What is a subquery?",
            "expected_answer": "A subquery is a query nested inside another SQL statement and can be used to provide values or rows to the outer query."
        },

        {
            "question": "What is a correlated subquery?",
            "expected_answer": "A correlated subquery depends on values from the outer query and is logically evaluated for each relevant row of the outer query."
        },

        {
            "question": "What is the difference between IN and EXISTS?",
            "expected_answer": "IN compares a value against a set of returned values, while EXISTS checks whether the subquery returns at least one row."
        },

        {
            "question": "What is a CTE in SQL?",
            "expected_answer": "A Common Table Expression is a temporary named result set defined using WITH that can be referenced within a SQL statement."
        },

        {
            "question": "What is a recursive CTE?",
            "expected_answer": "A recursive CTE refers to itself and is useful for querying hierarchical or graph-like data such as employee-manager relationships."
        },

        {
            "question": "What is a transaction schedule?",
            "expected_answer": "A transaction schedule is the order in which operations from one or more transactions are executed."
        },

        {
            "question": "What is a serial schedule?",
            "expected_answer": "A serial schedule executes transactions one after another without interleaving their operations."
        },

        {
            "question": "What is a concurrent schedule?",
            "expected_answer": "A concurrent schedule interleaves operations from multiple transactions to improve resource utilization and performance."
        },

        {
            "question": "What is serializability?",
            "expected_answer": "Serializability ensures that the result of a concurrent schedule is equivalent to the result of some serial execution of the transactions."
        },

        {
            "question": "What is conflict serializability?",
            "expected_answer": "A schedule is conflict-serializable if it can be transformed into a serial schedule by swapping non-conflicting operations."
        },

        {
            "question": "What is a precedence graph?",
            "expected_answer": "A precedence graph represents conflicts between transactions. A schedule is conflict-serializable if its precedence graph is acyclic."
        },

        {
            "question": "What is a recoverable schedule?",
            "expected_answer": "A recoverable schedule ensures that a transaction commits only after the transactions whose changes it has read have committed."
        },

        {
            "question": "What is a cascading rollback?",
            "expected_answer": "Cascading rollback occurs when one transaction's failure forces other transactions that read its uncommitted data to roll back."
        },

        {
            "question": "What is a cascadeless schedule?",
            "expected_answer": "A cascadeless schedule prevents transactions from reading uncommitted data, thereby avoiding cascading rollbacks."
        },

        {
            "question": "What is strict schedule in DBMS?",
            "expected_answer": "A strict schedule prevents other transactions from reading or modifying data written by an uncommitted transaction."
        },

        {
            "question": "What is concurrency control?",
            "expected_answer": "Concurrency control manages simultaneous transactions so that database consistency is maintained while allowing efficient concurrent execution."
        },

        {
            "question": "What is a lock in DBMS?",
            "expected_answer": "A lock is a concurrency-control mechanism that restricts how transactions can access shared data."
        },

        {
            "question": "What is a shared lock?",
            "expected_answer": "A shared lock allows a transaction to read a data item while preventing conflicting writes by other transactions."
        },

        {
            "question": "What is an exclusive lock?",
            "expected_answer": "An exclusive lock allows a transaction to modify a data item and prevents other transactions from obtaining conflicting locks on that item."
        },

        {
            "question": "What is two-phase locking?",
            "expected_answer": "Two-phase locking has a growing phase where locks are acquired and a shrinking phase where locks are released. It can ensure conflict serializability."
        },

        {
            "question": "What is strict two-phase locking?",
            "expected_answer": "Strict two-phase locking keeps exclusive locks until the transaction commits or aborts, helping prevent cascading rollback."
        },

        {
            "question": "What is deadlock in DBMS?",
            "expected_answer": "A deadlock occurs when transactions wait for each other indefinitely because each holds resources needed by another transaction."
        },

        {
            "question": "How can deadlocks be handled in DBMS?",
            "expected_answer": "Deadlocks can be handled using prevention, avoidance, detection and recovery, or timeout-based techniques."
        },

        {
            "question": "What is a dirty read?",
            "expected_answer": "A dirty read occurs when one transaction reads data written by another transaction before that transaction commits."
        },

        {
            "question": "What is a non-repeatable read?",
            "expected_answer": "A non-repeatable read occurs when the same row is read twice in one transaction and another committed transaction changes its value between the reads."
        },

        {
            "question": "What is a phantom read?",
            "expected_answer": "A phantom read occurs when repeated execution of a query returns a different set of rows because another transaction inserted, deleted, or changed rows matching the query condition."
        },

        {
            "question": "What are isolation levels in DBMS?",
            "expected_answer": "Common isolation levels are Read Uncommitted, Read Committed, Repeatable Read, and Serializable. They provide different guarantees against concurrency anomalies."
        },

        {
            "question": "What is Read Uncommitted isolation?",
            "expected_answer": "Read Uncommitted allows a transaction to read uncommitted changes from other transactions, so dirty reads can occur."
        },

        {
            "question": "What is Read Committed isolation?",
            "expected_answer": "Read Committed prevents reading uncommitted data, although repeated reads may return different committed values."
        },

        {
            "question": "What is Repeatable Read isolation?",
            "expected_answer": "Repeatable Read generally ensures that rows read during a transaction remain stable for repeated reads, although exact phantom-read behavior can depend on the DBMS."
        },

        {
            "question": "What is Serializable isolation?",
            "expected_answer": "Serializable provides the strongest standard transaction isolation and makes concurrent execution behave like some serial ordering of transactions."
        },

        {
            "question": "What is an index scan?",
            "expected_answer": "An index scan uses an index to locate relevant rows instead of examining every row in the table."
        },

        {
            "question": "What is a clustered index?",
            "expected_answer": "A clustered index determines the physical or primary storage order of table rows in database systems that support that concept, so a table generally has at most one."
        },

        {
            "question": "What is a non-clustered index?",
            "expected_answer": "A non-clustered index is a separate index structure that stores indexed values and references to the corresponding table rows."
        },

        {
            "question": "What is a composite index?",
            "expected_answer": "A composite index is an index created on multiple columns. Its column order affects which queries can use it efficiently."
        },

        {
            "question": "What is a covering index?",
            "expected_answer": "A covering index contains all columns needed by a query, allowing the database to answer the query from the index without accessing the base table in some cases."
        },

        {
            "question": "What is index selectivity?",
            "expected_answer": "Index selectivity describes how effectively an index distinguishes rows. Higher selectivity generally means fewer matching rows for a value."
        },

        {
            "question": "Why can too many indexes reduce performance?",
            "expected_answer": "Indexes consume storage and must be maintained during INSERT, UPDATE, and DELETE operations, so excessive indexes can slow writes."
        },

        {
            "question": "What is a B-tree index?",
            "expected_answer": "A B-tree is a balanced tree structure commonly used for database indexes because it supports efficient searches, insertions, deletions, and range queries."
        },

        {
            "question": "What is a B+ tree?",
            "expected_answer": "A B+ tree is a balanced tree where actual indexed data references are typically stored at leaf nodes, which are commonly linked to support efficient range scans."
        },

        {
            "question": "Why are B+ trees commonly used for database indexes?",
            "expected_answer": "B+ trees provide balanced search performance, high fan-out, and efficient sequential and range access through their linked leaf nodes."
        },

        {
            "question": "What is query optimization?",
            "expected_answer": "Query optimization is the process of choosing an efficient execution plan for a SQL query to reduce resource usage and execution time."
        },

        {
            "question": "What is an execution plan?",
            "expected_answer": "An execution plan describes how the database engine intends to execute a query, including operations such as scans, joins, sorting, and index usage."
        },

        {
            "question": "What is a full table scan?",
            "expected_answer": "A full table scan reads rows across the table to find matching records rather than using an index to locate them directly."
        },

        {
            "question": "What factors affect SQL query performance?",
            "expected_answer": "Factors include indexes, data size, query structure, join strategy, statistics, filtering, sorting, hardware resources, and the database execution plan."
        },

        {
            "question": "What is database partitioning?",
            "expected_answer": "Partitioning divides a large table or index into smaller logical or physical partitions to improve manageability and sometimes query performance."
        },

        {
            "question": "What is horizontal partitioning?",
            "expected_answer": "Horizontal partitioning divides a table by rows, with different partitions containing different subsets of records."
        },

        {
            "question": "What is vertical partitioning?",
            "expected_answer": "Vertical partitioning divides a table by columns, storing different groups of columns separately while preserving their relationship."
        },

        {
            "question": "What is database replication?",
            "expected_answer": "Replication maintains copies of database data on multiple servers to improve availability, scalability, or fault tolerance."
        },

        {
            "question": "What is the difference between synchronous and asynchronous replication?",
            "expected_answer": "Synchronous replication waits for required replicas to acknowledge changes before completion, while asynchronous replication allows the primary to continue without waiting for all replicas."
        },

        {
            "question": "What is database sharding?",
            "expected_answer": "Sharding distributes database data across multiple independent servers or partitions, usually based on a shard key, to scale storage and workload."
        },

        {
            "question": "What is a database transaction log?",
            "expected_answer": "A transaction log records database changes and transaction information so the DBMS can support recovery, rollback, and durability."
        },

        {
            "question": "What is write-ahead logging?",
            "expected_answer": "Write-ahead logging requires the relevant log record to be persisted before the corresponding changed data is written to stable storage."
        },

        {
            "question": "What is checkpointing in DBMS?",
            "expected_answer": "A checkpoint records a known recovery point and helps reduce the amount of log that must be processed after a database failure."
        },

        {
            "question": "What is database recovery?",
            "expected_answer": "Database recovery restores the database to a consistent state after failures using mechanisms such as logs, checkpoints, undo, and redo."
        },

        {
            "question": "What is the difference between undo and redo?",
            "expected_answer": "Undo reverses changes that should not remain, while redo reapplies committed changes that may not yet have been written to the database storage."
        },

        {
            "question": "What is a materialized view?",
            "expected_answer": "A materialized view stores the result of a query physically and can improve read performance, but it must be refreshed when underlying data changes."
        },

        {
            "question": "What is database connection pooling?",
            "expected_answer": "Connection pooling maintains reusable database connections so applications can avoid repeatedly creating and closing connections."
        },

        {
            "question": "What is cascading referential action?",
            "expected_answer": "Cascading actions automatically propagate operations such as DELETE or UPDATE from a referenced row to related foreign-key rows according to the defined constraint."
        },

        {
            "question": "What is a surrogate key?",
            "expected_answer": "A surrogate key is an artificial identifier, such as an auto-generated integer or UUID, created specifically to uniquely identify rows."
        },

        {
            "question": "What is a natural key?",
            "expected_answer": "A natural key is a real-world attribute or combination of attributes that naturally identifies a record, such as a government-issued identifier."
        },

        {
            "question": "What is the difference between a primary key and a unique key?",
            "expected_answer": "A primary key identifies the main unique identity of rows and cannot be NULL, while a UNIQUE constraint also enforces uniqueness but NULL behavior depends on the DBMS."
        },

        {
            "question": "What is an updatable view?",
            "expected_answer": "An updatable view is a view through which the DBMS permits certain INSERT, UPDATE, or DELETE operations on the underlying tables."
        },

        {
            "question": "What is database cardinality?",
            "expected_answer": "Cardinality describes the number of rows in a relation or, in relationship modeling, the number of entity instances that can participate in a relationship."
        },

        {
            "question": "What is database degree?",
            "expected_answer": "The degree of a relation is the number of attributes or columns in that relation."
        },

        {
            "question": "What is an entity integrity constraint?",
            "expected_answer": "Entity integrity requires every row to have a valid primary key value, meaning the primary key cannot be NULL."
        },

        {
            "question": "What is the difference between schema and instance?",
            "expected_answer": "A schema describes the structure of a database, while an instance is the actual data stored in the database at a particular point in time."
        },

        {
            "question": "What is data independence?",
            "expected_answer": "Data independence is the ability to change one level of database structure without requiring changes at the next higher level."
        },

        {
            "question": "What is physical data independence?",
            "expected_answer": "Physical data independence allows changes to physical storage or access methods without changing the logical database structure."
        },

        {
            "question": "What is logical data independence?",
            "expected_answer": "Logical data independence allows changes to the logical schema without requiring changes to external views or application programs."
        },

        {
            "question": "What is the three-schema architecture?",
            "expected_answer": "The three-schema architecture separates databases into external, conceptual, and internal levels to provide abstraction and data independence."
        },

        {
            "question": "What is the external level in DBMS architecture?",
            "expected_answer": "The external level represents user-specific views of the database and hides details that are not required by particular users or applications."
        },

        {
            "question": "What is the conceptual level in DBMS architecture?",
            "expected_answer": "The conceptual level describes the overall logical structure of the database, including entities, relationships, constraints, and data types."
        },

        {
            "question": "What is the internal level in DBMS architecture?",
            "expected_answer": "The internal level describes how database data is physically stored, including storage structures, files, indexes, and access paths."
        }

    ],


        # Hard
        
    "Hard": [

        {
            "question": "How does a DBMS ensure atomicity during a system crash?",
            "expected_answer": "The DBMS uses recovery mechanisms such as transaction logs, undo operations, and recovery protocols to ensure incomplete transactions are rolled back."
        },

        {
            "question": "How does write-ahead logging support database recovery?",
            "expected_answer": "Write-ahead logging ensures log records describing changes reach stable storage before the corresponding data pages, allowing the DBMS to undo or redo operations after failure."
        },

        {
            "question": "What is the ARIES recovery algorithm?",
            "expected_answer": "ARIES is a recovery algorithm based on write-ahead logging. It uses analysis, redo, and undo phases to recover a database after a crash."
        },

        {
            "question": "What are the three phases of ARIES recovery?",
            "expected_answer": "ARIES recovery consists of analysis, redo, and undo. Analysis determines the state at failure, redo repeats necessary changes, and undo reverses incomplete transactions."
        },

        {
            "question": "What is a dirty page in database recovery?",
            "expected_answer": "A dirty page is a database page in memory that has been modified but whose updated contents have not yet been written to persistent storage."
        },

        {
            "question": "What is steal and no-steal buffer management?",
            "expected_answer": "Steal allows uncommitted changes to be written to disk, requiring undo during recovery. No-steal prevents this but may require more memory."
        },

        {
            "question": "What is force and no-force buffer management?",
            "expected_answer": "Force writes all modified pages of a committed transaction to storage at commit, while no-force allows them to be written later and therefore relies more on redo recovery."
        },

        {
            "question": "Why are undo and redo both needed in database recovery?",
            "expected_answer": "Undo removes effects of incomplete transactions, while redo restores committed changes that may not have reached persistent storage before a crash."
        },

        {
            "question": "What is a fuzzy checkpoint?",
            "expected_answer": "A fuzzy checkpoint allows transactions to continue while checkpoint information is collected, avoiding the need to stop normal database processing."
        },

        {
            "question": "What is cascading rollback and how can it be prevented?",
            "expected_answer": "Cascading rollback occurs when transactions depend on uncommitted data. Strict or cascadeless schedules prevent transactions from reading such data."
        },

        {
            "question": "Why is conflict serializability important?",
            "expected_answer": "Conflict serializability ensures that concurrent transactions produce a result equivalent to some serial execution, helping preserve database consistency."
        },

        {
            "question": "What is view serializability?",
            "expected_answer": "View serializability considers whether a concurrent schedule is view-equivalent to a serial schedule based on reads-from relationships and final writes."
        },

        {
            "question": "What is the difference between conflict and view serializability?",
            "expected_answer": "Conflict serializability is based on conflicting operation order, while view serializability uses equivalent reads and final writes. Every conflict-serializable schedule is view-serializable."
        },

        {
            "question": "Can a schedule be view-serializable but not conflict-serializable?",
            "expected_answer": "Yes. View serializability is more general and includes some schedules that are not conflict-serializable, especially schedules involving blind writes."
        },

        {
            "question": "What is a blind write?",
            "expected_answer": "A blind write occurs when a transaction writes a data item without first reading its current value."
        },

        {
            "question": "How does two-phase locking guarantee conflict serializability?",
            "expected_answer": "Two-phase locking prevents a transaction from acquiring new locks after it begins releasing locks, which imposes an ordering on conflicting operations and guarantees conflict serializability."
        },

        {
            "question": "What is conservative two-phase locking?",
            "expected_answer": "Conservative two-phase locking requires a transaction to acquire all required locks before it begins execution, preventing deadlocks caused by lock acquisition."
        },

        {
            "question": "What is rigorous two-phase locking?",
            "expected_answer": "Rigorous two-phase locking keeps both shared and exclusive locks until the transaction commits or aborts."
        },

        {
            "question": "What is lock conversion?",
            "expected_answer": "Lock conversion changes a lock from one type to another, such as upgrading a shared lock to an exclusive lock or downgrading an exclusive lock."
        },

        {
            "question": "What is lock escalation?",
            "expected_answer": "Lock escalation replaces many fine-grained locks with a coarser lock, such as replacing many row locks with a table lock, to reduce lock-management overhead."
        },

        {
            "question": "What is a deadlock wait-for graph?",
            "expected_answer": "A wait-for graph represents transactions as nodes and waiting relationships as directed edges. A cycle indicates a deadlock."
        },

        {
            "question": "What is deadlock prevention?",
            "expected_answer": "Deadlock prevention uses rules that make at least one necessary deadlock condition impossible, often by controlling how transactions acquire or wait for locks."
        },

        {
            "question": "What is deadlock detection and recovery?",
            "expected_answer": "The DBMS periodically detects cycles in transaction wait relationships and resolves a deadlock by aborting or rolling back one or more transactions."
        },

        {
            "question": "What is the difference between deadlock prevention and deadlock detection?",
            "expected_answer": "Prevention attempts to stop deadlocks from forming, while detection allows them to occur and later identifies and resolves them."
        },

        {
            "question": "What is starvation in concurrency control?",
            "expected_answer": "Starvation occurs when a transaction repeatedly waits or is denied resources and therefore cannot make progress for an indefinitely long time."
        },

        {
            "question": "What is MVCC?",
            "expected_answer": "MVCC, or Multi-Version Concurrency Control, maintains multiple versions of data so readers can often access a consistent version without blocking writers."
        },

        {
            "question": "How does MVCC reduce read-write blocking?",
            "expected_answer": "MVCC allows readers to access an appropriate committed version while writers create newer versions, reducing the need for readers and writers to block each other."
        },

        {
            "question": "What is snapshot isolation?",
            "expected_answer": "Snapshot isolation allows a transaction to read from a consistent snapshot of committed data while other transactions continue executing concurrently."
        },

        {
            "question": "How is snapshot isolation different from serializable isolation?",
            "expected_answer": "Snapshot isolation provides consistent snapshots but can allow certain anomalies such as write skew, while serializable isolation provides stronger guarantees equivalent to serial execution."
        },

        {
            "question": "What is write skew?",
            "expected_answer": "Write skew is a concurrency anomaly where two transactions read overlapping data and independently make changes that together violate a business constraint."
        },

        {
            "question": "What is phantom protection in serializable isolation?",
            "expected_answer": "Serializable systems prevent concurrent transactions from creating results that behave as if matching rows were unexpectedly inserted, deleted, or changed during another transaction."
        },

        {
            "question": "What is a lost update?",
            "expected_answer": "A lost update occurs when concurrent transactions modify the same data and one transaction unintentionally overwrites changes made by another."
        },

        {
            "question": "What is optimistic concurrency control?",
            "expected_answer": "Optimistic concurrency control assumes conflicts are uncommon, allows transactions to proceed without heavy locking, and checks for conflicts before commit."
        },

        {
            "question": "What is pessimistic concurrency control?",
            "expected_answer": "Pessimistic concurrency control assumes conflicts may occur and uses locks or similar mechanisms to prevent conflicting operations."
        },

        {
            "question": "When would optimistic concurrency control be preferred?",
            "expected_answer": "It can be useful when conflicts are relatively rare and transactions would otherwise spend significant time waiting for locks."
        },

        {
            "question": "What is a functional dependency closure?",
            "expected_answer": "The closure of a set of attributes is the set of all attributes that can be functionally determined from that set using the given functional dependencies."
        },

        {
            "question": "How is attribute closure used to find candidate keys?",
            "expected_answer": "If the closure of an attribute set contains all attributes of the relation, that set is a super key. A minimal such set is a candidate key."
        },

        {
            "question": "What is a minimal cover of functional dependencies?",
            "expected_answer": "A minimal cover is an equivalent set of functional dependencies with a single attribute on each right side and no redundant dependencies or unnecessary attributes."
        },

        {
            "question": "Why is BCNF sometimes not dependency preserving?",
            "expected_answer": "Decomposing a relation into BCNF may remove dependencies that cannot be enforced within individual decomposed relations without performing joins."
        },

        {
            "question": "Why can 3NF be preferred over BCNF?",
            "expected_answer": "3NF may preserve functional dependencies while BCNF can require decompositions that lose dependency preservation."
        },

        {
            "question": "What is 4NF?",
            "expected_answer": "Fourth Normal Form addresses multivalued dependencies and requires that non-trivial multivalued dependencies have a superkey as their determinant."
        },

        {
            "question": "What is a multivalued dependency?",
            "expected_answer": "A multivalued dependency occurs when one attribute determines a set of independent values of another attribute, represented as X ->> Y."
        },

        {
            "question": "What is 5NF?",
            "expected_answer": "Fifth Normal Form deals with join dependencies and requires that every non-trivial join dependency is implied by candidate keys."
        },

        {
            "question": "What is a join dependency?",
            "expected_answer": "A join dependency specifies that a relation can be reconstructed by joining multiple projections of that relation."
        },

        {
            "question": "What is relational algebra?",
            "expected_answer": "Relational algebra is a procedural query language using operations such as selection, projection, union, difference, Cartesian product, and joins."
        },

        {
            "question": "What is relational calculus?",
            "expected_answer": "Relational calculus is a non-procedural query formalism that describes what data should be retrieved rather than specifying the exact sequence of operations."
        },

        {
            "question": "What is the difference between relational algebra and relational calculus?",
            "expected_answer": "Relational algebra specifies how to obtain results using operations, while relational calculus specifies what results are required."
        },

        {
            "question": "What is query equivalence?",
            "expected_answer": "Two queries are equivalent when they produce the same result for every valid database state."
        },

        {
            "question": "What are heuristic query optimization techniques?",
            "expected_answer": "Common heuristics include applying selections early, projecting only required columns, reducing intermediate results, and choosing efficient join orders."
        },

        {
            "question": "Why is join order important in query optimization?",
            "expected_answer": "Different join orders can produce very different intermediate result sizes and execution costs, so choosing an efficient order can greatly improve performance."
        },

        {
            "question": "What is predicate pushdown?",
            "expected_answer": "Predicate pushdown applies filtering conditions as early as possible so fewer rows need to be processed by later query operations."
        },

        {
            "question": "What is projection pushdown?",
            "expected_answer": "Projection pushdown retrieves only required columns as early as possible, reducing the amount of data processed and transferred."
        },

        {
            "question": "What is a hash join?",
            "expected_answer": "A hash join builds a hash structure on one input and uses it to efficiently find matching rows from the other input, especially for equality joins."
        },

        {
            "question": "What is a nested-loop join?",
            "expected_answer": "A nested-loop join compares rows from one relation with rows from another relation. An index on the inner relation can make it efficient for some workloads."
        },

        {
            "question": "What is a sort-merge join?",
            "expected_answer": "A sort-merge join sorts both inputs on the join key and then scans them to efficiently find matching rows."
        },

        {
            "question": "When can a hash join be better than a nested-loop join?",
            "expected_answer": "A hash join can be effective for large inputs and equality joins when suitable memory is available and indexed nested-loop access is not efficient."
        },

        {
            "question": "What is index-only scan?",
            "expected_answer": "An index-only scan answers a query using only information available in the index, avoiding access to the base table when the database can verify visibility and required columns."
        },

        {
            "question": "Why might a database choose a sequential scan instead of an index scan?",
            "expected_answer": "If a large percentage of rows must be retrieved or the table is small, a sequential scan may have lower cost than performing many random index lookups."
        },

        {
            "question": "What is database statistics in query optimization?",
            "expected_answer": "Database statistics describe data distribution, row counts, and other characteristics that the optimizer uses to estimate query costs and choose execution plans."
        },

        {
            "question": "What is cardinality estimation?",
            "expected_answer": "Cardinality estimation predicts how many rows an operation such as a filter or join will produce, helping the optimizer choose an efficient execution plan."
        },

        {
            "question": "What happens when cardinality estimates are inaccurate?",
            "expected_answer": "Incorrect estimates can cause the optimizer to choose poor join orders, join algorithms, access paths, or memory allocations, resulting in slower queries."
        },

        {
            "question": "What is a covering index and what is its trade-off?",
            "expected_answer": "A covering index contains all columns needed by a query and can avoid table access, but it increases index size and write-maintenance cost."
        },

        {
            "question": "Why does column order matter in a composite index?",
            "expected_answer": "The leading columns determine which filtering, sorting, and range conditions can efficiently use the index."
        },

        {
            "question": "What is the leftmost-prefix principle?",
            "expected_answer": "For many B-tree composite indexes, queries can efficiently use the index when they constrain the leading columns of the index in their defined order."
        },

        {
            "question": "What is a partial or filtered index?",
            "expected_answer": "A partial or filtered index indexes only rows satisfying a specified condition, reducing index size and maintenance cost when supported by the DBMS."
        },

        {
            "question": "What is an index selectivity problem?",
            "expected_answer": "An index with low selectivity matches many rows for a value, so using it may provide little benefit compared with scanning a large portion of the table."
        },

        {
            "question": "What is table partition pruning?",
            "expected_answer": "Partition pruning allows the database to access only relevant partitions based on query conditions instead of scanning every partition."
        },

        {
            "question": "What is horizontal sharding?",
            "expected_answer": "Horizontal sharding distributes different rows of the same logical table across multiple database servers or shards."
        },

        {
            "question": "What is a shard key?",
            "expected_answer": "A shard key determines how records are distributed among shards. A good key provides balanced distribution and supports common query patterns."
        },

        {
            "question": "What is a hot shard?",
            "expected_answer": "A hot shard receives disproportionately high traffic or data compared with other shards, creating a performance bottleneck."
        },

        {
            "question": "What is cross-shard querying?",
            "expected_answer": "Cross-shard querying requires retrieving or combining data from multiple shards, which can increase network traffic and query complexity."
        },

        {
            "question": "What is replication lag?",
            "expected_answer": "Replication lag is the delay between a change being committed on a primary database and that change becoming visible on a replica."
        },

        {
            "question": "What problems can replication lag cause?",
            "expected_answer": "Replication lag can cause stale reads, inconsistent user experiences, incorrect read-after-write behavior, and complications in failover."
        },

        {
            "question": "What is read-after-write consistency?",
            "expected_answer": "Read-after-write consistency ensures that after an application successfully writes data, subsequent reads observe that write rather than an older version."
        },

        {
            "question": "What is quorum-based replication?",
            "expected_answer": "Quorum-based replication requires a sufficient number of replicas to acknowledge reads or writes so that overlapping quorums provide consistency guarantees."
        },

        {
            "question": "What is eventual consistency?",
            "expected_answer": "Eventual consistency means that replicas may temporarily contain different values but will converge to the same state if updates stop."
        },

        {
            "question": "What is CAP theorem?",
            "expected_answer": "CAP theorem states that during a network partition, a distributed data system cannot simultaneously guarantee both strong consistency and availability."
        },

        {
            "question": "What does partition tolerance mean in CAP theorem?",
            "expected_answer": "Partition tolerance means the system continues operating despite communication failures that divide nodes into disconnected groups."
        },

        {
            "question": "What is the difference between ACID and BASE?",
            "expected_answer": "ACID emphasizes strong transaction guarantees, while BASE generally favors availability and eventual consistency in distributed systems."
        },

        {
            "question": "What is two-phase commit?",
            "expected_answer": "Two-phase commit is a distributed transaction protocol with prepare and commit phases that coordinates multiple participants so they commit or abort consistently."
        },

        {
            "question": "What is the main weakness of two-phase commit?",
            "expected_answer": "Two-phase commit can block participants while waiting for the coordinator and can be affected by coordinator or network failures."
        },

        {
            "question": "What is a distributed deadlock?",
            "expected_answer": "A distributed deadlock occurs when transactions or processes on different database nodes wait for one another in a cycle."
        },

        {
            "question": "What is database horizontal scaling?",
            "expected_answer": "Horizontal scaling adds more database servers or nodes to distribute workload, storage, or requests instead of relying on a larger single server."
        },

        {
            "question": "What is database vertical scaling?",
            "expected_answer": "Vertical scaling increases the resources of an existing database server, such as CPU, memory, or storage capacity."
        },

        {
            "question": "What is connection pool exhaustion?",
            "expected_answer": "Connection pool exhaustion occurs when all available database connections are in use, causing new requests to wait or fail until connections are released."
        },

        {
            "question": "How can connection pool exhaustion be diagnosed?",
            "expected_answer": "Check pool usage, connection wait times, long-running queries, leaked connections, transaction duration, and application traffic patterns."
        },

        {
            "question": "What is database connection leakage?",
            "expected_answer": "Connection leakage occurs when application code fails to properly release database connections, gradually exhausting the available connection pool."
        },

        {
            "question": "What is database failover?",
            "expected_answer": "Failover is the process of switching database operations from a failed primary server to an available replica or standby system."
        },

        {
            "question": "What challenges occur during database failover?",
            "expected_answer": "Challenges include data loss risk, replication lag, stale connections, split-brain scenarios, DNS or routing changes, and application reconnection handling."
        },

        {
            "question": "What is split brain in database systems?",
            "expected_answer": "Split brain occurs when multiple nodes incorrectly believe they are the authoritative primary at the same time, potentially causing conflicting writes."
        },

        {
            "question": "What is database backup versus replication?",
            "expected_answer": "Replication maintains additional copies for availability or scaling, while backups provide recoverable historical copies for restoring data after corruption, deletion, or other failures."
        },

        {
            "question": "Why is replication not a replacement for backups?",
            "expected_answer": "Replication can copy accidental updates, deletions, or corruption to replicas, while backups can provide an earlier recoverable version."
        },

        {
            "question": "What is point-in-time recovery?",
            "expected_answer": "Point-in-time recovery restores a database to a chosen time using a base backup together with transaction logs or equivalent recovery information."
        },

        {
            "question": "What is a hot backup?",
            "expected_answer": "A hot backup is performed while the database remains available for normal operations, using mechanisms that maintain a consistent recoverable backup."
        },

        {
            "question": "What is a cold backup?",
            "expected_answer": "A cold backup is taken while the database is stopped or otherwise made unavailable for normal writes, simplifying consistency at the cost of downtime."
        },

        {
            "question": "How would you troubleshoot a suddenly slow SQL query?",
            "expected_answer": "Inspect the execution plan, indexes, statistics, row estimates, locks, query changes, data growth, resource usage, and recent database or application changes."
        },

        {
            "question": "How would you troubleshoot database CPU usage reaching 100 percent?",
            "expected_answer": "Identify expensive queries, inspect execution plans, check query frequency and concurrency, examine missing or inefficient indexes, and verify whether workload or configuration changed."
        },

        {
            "question": "How would you troubleshoot database lock contention?",
            "expected_answer": "Identify blocking and waiting transactions, inspect long-running transactions and queries, determine the conflicting resources, and optimize transaction scope or indexing."
        },

        {
            "question": "Why can an index make a query slower?",
            "expected_answer": "An index may be slower when many rows match, when random lookups are expensive, or when maintaining the index adds significant overhead compared with a sequential scan."
        },

        {
            "question": "How would you design a database for millions of users?",
            "expected_answer": "Start with a normalized design and proper indexes, then consider caching, read replicas, partitioning, sharding, connection pooling, backups, monitoring, and workload-specific optimization."
        },

        {
            "question": "How would you prevent duplicate records in a high-concurrency system?",
            "expected_answer": "Use appropriate UNIQUE constraints or keys at the database level and combine them with transactions or concurrency-safe application logic."
        },

        {
            "question": "Why should important business rules be enforced at the database level?",
            "expected_answer": "Database constraints provide a centralized guarantee that remains effective even when multiple applications or services modify the same data."
        },

        {
            "question": "What is idempotency in database operations?",
            "expected_answer": "An operation is idempotent when performing it multiple times produces the same intended final state as performing it once."
        },

        {
            "question": "How can idempotency prevent duplicate transactions?",
            "expected_answer": "A unique idempotency key or business identifier can ensure repeated requests are recognized as the same operation instead of creating duplicate records."
        },

        {
            "question": "What is optimistic locking?",
            "expected_answer": "Optimistic locking detects concurrent modifications using a version number or timestamp and rejects an update when the stored version no longer matches."
        },

        {
            "question": "What is pessimistic locking?",
            "expected_answer": "Pessimistic locking acquires database locks before modifying data so conflicting transactions are prevented from changing the same resource concurrently."
        },

        {
            "question": "When should optimistic locking be preferred over pessimistic locking?",
            "expected_answer": "Optimistic locking is often preferred when conflicts are relatively rare and avoiding long-held database locks improves scalability."
        },

        {
            "question": "How can database transactions become a performance problem?",
            "expected_answer": "Long transactions can hold locks, consume connections, increase contention, delay cleanup, and increase the amount of work required during rollback or recovery."
        },

        {
            "question": "Why should transactions usually be kept short?",
            "expected_answer": "Short transactions reduce lock duration, contention, connection usage, failure impact, and the amount of work required if rollback occurs."
        },

        {
            "question": "What is a savepoint in a transaction?",
            "expected_answer": "A savepoint marks a point within a transaction so the transaction can roll back to that point without necessarily aborting the entire transaction."
        },

        {
            "question": "What happens if a transaction fails after modifying multiple tables?",
            "expected_answer": "If the transaction is rolled back, its changes should be undone according to the database transaction and recovery mechanisms, preserving atomicity."
        },

        {
            "question": "Why can normalization hurt read performance?",
            "expected_answer": "Highly normalized designs may require more joins to reconstruct information, increasing query complexity and sometimes read latency."
        },

        {
            "question": "When is denormalization useful?",
            "expected_answer": "Denormalization can be useful for read-heavy workloads when reducing joins or repeated computation provides meaningful performance benefits and controlled redundancy is acceptable."
        },

        {
            "question": "What are the risks of denormalization?",
            "expected_answer": "Denormalization increases redundancy and can cause inconsistent data unless updates are carefully controlled."
        },

        {
            "question": "What is database schema migration?",
            "expected_answer": "A schema migration is a controlled change to database structure, such as adding columns, modifying tables, or creating indexes, usually managed through versioned migration scripts."
        },

        {
            "question": "What is a zero-downtime database migration?",
            "expected_answer": "It is a migration designed so applications can continue operating while schema changes are introduced gradually, often using backward-compatible changes and staged deployment."
        },

        {
            "question": "What is the expand-and-contract migration pattern?",
            "expected_answer": "The expand phase introduces backward-compatible schema changes, applications migrate gradually, and the contract phase removes the old structure after it is no longer needed."
        },

        {
            "question": "How can a database migration be made safer?",
            "expected_answer": "Use backups, tested migration scripts, backward-compatible changes, staged deployment, monitoring, rollback planning, and validation on representative data."
        },

        {
            "question": "What is database auditing?",
            "expected_answer": "Database auditing records important access and modification activities so organizations can monitor usage, investigate incidents, and meet compliance requirements."
        },

        {
            "question": "What is row-level security?",
            "expected_answer": "Row-level security restricts which rows a user or role can access based on defined security policies."
        },

        {
            "question": "Why should database credentials not be hard-coded in applications?",
            "expected_answer": "Hard-coded credentials can be exposed through source code or repositories. Secrets should instead be managed using secure configuration or secret-management systems."
        },

        {
            "question": "What is SQL injection and how does a DBMS application prevent it?",
            "expected_answer": "SQL injection occurs when untrusted input changes query structure. Parameterized queries or prepared statements prevent input from being interpreted as SQL code."
        },

        {
            "question": "Why are prepared statements safer than string concatenation?",
            "expected_answer": "Prepared statements separate SQL structure from user-supplied values, preventing input values from being interpreted as executable SQL syntax."
        },

        {
            "question": "What is a database connection timeout?",
            "expected_answer": "A connection timeout limits how long an application waits to establish a database connection before treating the attempt as failed."
        },

        {
            "question": "What is query timeout and why is it important?",
            "expected_answer": "A query timeout limits how long a query may execute. It prevents excessively long operations from consuming resources indefinitely."
        },

        {
            "question": "What is backpressure in a database-backed application?",
            "expected_answer": "Backpressure limits incoming work when the database cannot process requests quickly enough, preventing queues, connections, and resources from becoming exhausted."
        },

        {
            "question": "What is the N+1 query problem?",
            "expected_answer": "The N+1 problem occurs when an application executes one query to fetch a list and then performs another query for each returned item, causing excessive database calls."
        },

        {
            "question": "How can the N+1 query problem be solved?",
            "expected_answer": "It can often be reduced using joins, batch queries, eager loading, appropriate prefetching, or carefully designed data-access patterns."
        },

        {
            "question": "Why can SELECT * be problematic in production systems?",
            "expected_answer": "SELECT * can retrieve unnecessary data, increase network and memory usage, reduce the benefit of covering indexes, and make applications sensitive to schema changes."
        },

        {
            "question": "What is a sargable query condition?",
            "expected_answer": "A sargable condition allows the database to use an index efficiently for filtering rather than applying a function or transformation that prevents useful index access."
        },

        {
            "question": "Why can applying a function to an indexed column hurt performance?",
            "expected_answer": "Applying a function may prevent the database from using a normal index efficiently because the stored indexed values no longer directly match the search expression."
        },

        {
            "question": "How would you optimize a query that filters millions of rows?",
            "expected_answer": "Inspect the execution plan, add or improve suitable indexes, make predicates sargable, reduce selected columns, filter early, and verify statistics and data distribution."
        },

        {
            "question": "What is a database deadlock example?",
            "expected_answer": "Transaction A locks row 1 and waits for row 2 while transaction B locks row 2 and waits for row 1. Neither can continue, creating a deadlock."
        },

        {
            "question": "How can applications reduce the chance of database deadlocks?",
            "expected_answer": "Access resources in a consistent order, keep transactions short, use appropriate indexes, avoid unnecessary locks, and implement safe retry handling where appropriate."
        },

        {
            "question": "Why should deadlock retries use caution?",
            "expected_answer": "Blind retries can repeatedly recreate contention. Applications should use bounded retries, appropriate backoff, and ensure operations are safe to retry."
        },

        {
            "question": "What is a phantom problem in database concurrency?",
            "expected_answer": "The phantom problem occurs when a transaction repeats a range query and finds new or missing rows because another concurrent transaction changed rows matching that range."
        },

        {
            "question": "How does serializable isolation affect performance?",
            "expected_answer": "Serializable isolation provides strong consistency guarantees but can increase locking, blocking, conflict detection, or retry overhead and therefore reduce concurrency."
        },

        {
            "question": "How would you choose an isolation level for a financial transaction?",
            "expected_answer": "Choose based on the required correctness guarantees, business invariants, workload, and DBMS behavior. Stronger isolation may be required for operations involving critical consistency constraints."
        },

        {
            "question": "What is eventual consistency and when can it be acceptable?",
            "expected_answer": "Eventual consistency allows temporary differences between replicas and can be acceptable when immediate consistency is not required and availability or scalability is more important."
        },

        {
            "question": "What is the difference between a primary database and a read replica?",
            "expected_answer": "A primary generally accepts writes and coordinates authoritative state, while a read replica maintains a copy used mainly for read workloads and may lag behind the primary."
        },

        {
            "question": "How can read replicas improve database scalability?",
            "expected_answer": "Read replicas distribute read workloads across multiple database servers, reducing pressure on the primary when the workload is read-heavy."
        },

        {
            "question": "What is the risk of sending immediately-after-write reads to replicas?",
            "expected_answer": "Replication lag can cause the read to return stale data even though the write has already succeeded on the primary."
        },

        {
            "question": "What is database caching?",
            "expected_answer": "Database caching stores frequently accessed data in a faster cache layer to reduce repeated database queries and improve application response time."
        },

        {
            "question": "What is cache invalidation in database-backed systems?",
            "expected_answer": "Cache invalidation removes or updates cached data when the underlying database data changes so stale values are not served."
        },

        {
            "question": "What is a cache stampede?",
            "expected_answer": "A cache stampede occurs when many requests simultaneously miss an expired cache entry and overload the database by requesting the same data."
        },

        
    ]
}