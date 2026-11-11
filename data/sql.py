questions = {
  
  "Easy": [

    {
        "question": "What is SQL?",
        "expected_answer": "SQL stands for Structured Query Language. It is used to create, read, update, and manage data in relational databases."
    },

    {
        "question": "What is a database?",
        "expected_answer": "A database is an organized collection of data that can be stored, accessed, and managed efficiently."
    },

    {
        "question": "What is a relational database?",
        "expected_answer": "A relational database stores data in tables made of rows and columns, with relationships between tables."
    },

    {
        "question": "What is a table in SQL?",
        "expected_answer": "A table is a database object that stores related data in rows and columns."
    },

    {
        "question": "What is a row in SQL?",
        "expected_answer": "A row represents one record or instance of data in a table."
    },

    {
        "question": "What is a column in SQL?",
        "expected_answer": "A column represents a particular attribute or field of the data stored in a table."
    },

    {
        "question": "What is a primary key?",
        "expected_answer": "A primary key uniquely identifies each row in a table. It cannot contain duplicate or NULL values."
    },

    {
        "question": "What is a foreign key?",
        "expected_answer": "A foreign key is a column or set of columns that references a key in another table to establish a relationship between tables."
    },

    {
        "question": "What is a unique key?",
        "expected_answer": "A UNIQUE constraint ensures that values in a column or group of columns are not duplicated."
    },

    {
        "question": "What is NULL in SQL?",
        "expected_answer": "NULL represents a missing, unknown, or unavailable value. It is different from zero, an empty string, or false."
    },

    {
        "question": "What is the difference between NULL and 0?",
        "expected_answer": "NULL means the value is missing or unknown, while 0 is an actual numeric value."
    },

    {
        "question": "What is the SELECT statement?",
        "expected_answer": "SELECT is used to retrieve data from one or more database tables."
    },

    {
        "question": "What is the WHERE clause?",
        "expected_answer": "The WHERE clause filters rows based on a specified condition."
    },

    {
        "question": "What is the FROM clause?",
        "expected_answer": "The FROM clause specifies the table or tables from which data should be retrieved."
    },

    {
        "question": "What is the ORDER BY clause?",
        "expected_answer": "ORDER BY sorts query results in ascending or descending order based on one or more columns."
    },

    {
        "question": "What is ASC in SQL?",
        "expected_answer": "ASC means ascending order. It is the default sorting direction for ORDER BY in most SQL implementations."
    },

    {
        "question": "What is DESC in SQL?",
        "expected_answer": "DESC means descending order and is used to sort query results from higher to lower values."
    },

    {
        "question": "What is the DISTINCT keyword?",
        "expected_answer": "DISTINCT removes duplicate rows from the result of a SELECT query."
    },

    {
        "question": "What is the INSERT statement?",
        "expected_answer": "INSERT is used to add new rows of data to a table."
    },

    {
        "question": "What is the UPDATE statement?",
        "expected_answer": "UPDATE is used to modify existing rows in a table."
    },

    {
        "question": "What is the DELETE statement?",
        "expected_answer": "DELETE removes selected rows from a table based on a condition."
    },

    {
        "question": "What is the difference between DELETE and DROP?",
        "expected_answer": "DELETE removes rows from a table, while DROP removes the database object itself, such as the table."
    },

    {
        "question": "What is the difference between DELETE and TRUNCATE?",
        "expected_answer": "DELETE can remove selected rows using a WHERE condition, while TRUNCATE removes all rows from a table more directly."
    },

    {
        "question": "What is the CREATE TABLE statement?",
        "expected_answer": "CREATE TABLE is used to create a new table and define its columns, data types, and constraints."
    },

    {
        "question": "What is the ALTER TABLE statement?",
        "expected_answer": "ALTER TABLE is used to modify the structure of an existing table, such as adding or removing columns."
    },

    {
        "question": "What is the DROP TABLE statement?",
        "expected_answer": "DROP TABLE permanently removes a table and its stored data from the database."
    },

    {
        "question": "What is a SQL constraint?",
        "expected_answer": "A constraint is a rule applied to database columns to maintain valid and consistent data."
    },

    {
        "question": "What is the NOT NULL constraint?",
        "expected_answer": "NOT NULL requires a column to contain a value and prevents NULL values from being stored in that column."
    },

    {
        "question": "What is the DEFAULT constraint?",
        "expected_answer": "DEFAULT provides a value automatically when an INSERT statement does not specify a value for that column."
    },

    {
        "question": "What is the CHECK constraint?",
        "expected_answer": "CHECK restricts column values by requiring them to satisfy a specified condition."
    },

    {
        "question": "What is a SQL operator?",
        "expected_answer": "A SQL operator is a symbol or keyword used to perform comparisons, calculations, logical operations, or other expressions."
    },

    {
        "question": "What are comparison operators in SQL?",
        "expected_answer": "Comparison operators such as =, <>, <, >, <=, and >= compare values in SQL conditions."
    },

    {
        "question": "What are logical operators in SQL?",
        "expected_answer": "AND, OR, and NOT are logical operators used to combine or reverse conditions in SQL queries."
    },

    {
        "question": "What is the LIKE operator?",
        "expected_answer": "LIKE is used to search for a specified pattern in text values."
    },

    {
        "question": "What is the purpose of the % wildcard in SQL?",
        "expected_answer": "The % wildcard in a LIKE pattern represents zero or more characters."
    },

    {
        "question": "What is the purpose of the _ wildcard in SQL?",
        "expected_answer": "The _ wildcard in a LIKE pattern represents exactly one character."
    },

    {
        "question": "What is the IN operator?",
        "expected_answer": "IN checks whether a value matches any value in a specified list or result set."
    },

    {
        "question": "What is the BETWEEN operator?",
        "expected_answer": "BETWEEN checks whether a value falls within a specified inclusive range."
    },

    {
        "question": "What is the IS NULL operator?",
        "expected_answer": "IS NULL checks whether a value is NULL."
    },

    {
        "question": "What is an aggregate function?",
        "expected_answer": "An aggregate function performs a calculation on multiple rows and returns a single result, such as COUNT, SUM, AVG, MIN, or MAX."
    },

    {
        "question": "What does COUNT() do in SQL?",
        "expected_answer": "COUNT() returns the number of rows or non-NULL values depending on how it is used."
    },

    {
        "question": "What does SUM() do in SQL?",
        "expected_answer": "SUM() calculates the total of numeric values in a column."
    },

    {
        "question": "What does AVG() do in SQL?",
        "expected_answer": "AVG() calculates the average of numeric values."
    },

    {
        "question": "What does MIN() do in SQL?",
        "expected_answer": "MIN() returns the smallest value from the selected values."
    },

    {
        "question": "What does MAX() do in SQL?",
        "expected_answer": "MAX() returns the largest value from the selected values."
    },

    {
        "question": "What is GROUP BY?",
        "expected_answer": "GROUP BY groups rows with the same values so aggregate functions can be applied to each group."
    },

    {
        "question": "What is HAVING?",
        "expected_answer": "HAVING filters groups produced by GROUP BY, usually using aggregate conditions."
    },

    {
        "question": "What is the difference between WHERE and HAVING?",
        "expected_answer": "WHERE filters individual rows before grouping, while HAVING filters groups after GROUP BY is applied."
    },

    {
        "question": "What is a SQL JOIN?",
        "expected_answer": "A JOIN combines rows from two or more tables based on a related column or condition."
    },

    {
        "question": "What is an INNER JOIN?",
        "expected_answer": "INNER JOIN returns only rows where matching values exist in both joined tables."
    },

    {
        "question": "What is a LEFT JOIN?",
        "expected_answer": "LEFT JOIN returns all rows from the left table and matching rows from the right table. Unmatched right-side values become NULL."
    },

    {
        "question": "What is a RIGHT JOIN?",
        "expected_answer": "RIGHT JOIN returns all rows from the right table and matching rows from the left table."
    },

    {
        "question": "What is a FULL OUTER JOIN?",
        "expected_answer": "FULL OUTER JOIN returns matching rows and also unmatched rows from both tables, with NULLs where no match exists."
    },

    {
        "question": "What is a CROSS JOIN?",
        "expected_answer": "CROSS JOIN produces the Cartesian product, combining every row from one table with every row from another."
    },

    {
        "question": "What is a self join?",
        "expected_answer": "A self join joins a table with itself, usually using different aliases to compare related rows within the same table."
    },

    {
        "question": "What is an alias in SQL?",
        "expected_answer": "An alias is a temporary name given to a table or column to make a query easier to read or reference."
    },

    {
        "question": "What is a subquery?",
        "expected_answer": "A subquery is a query written inside another SQL query. It can be used in clauses such as WHERE, FROM, or SELECT."
    },

    {
        "question": "What is a view?",
        "expected_answer": "A view is a virtual table based on the result of a SQL query. It usually stores the query definition rather than a separate copy of the data."
    },

    {
        "question": "What is an index in SQL?",
        "expected_answer": "An index is a database structure that can speed up data retrieval, but it can require additional storage and may slow writes."
    },

    {
        "question": "What is a transaction in SQL?",
        "expected_answer": "A transaction is a logical unit of database operations that should be completed successfully as a whole or rolled back."
    },

    {
        "question": "What are ACID properties?",
        "expected_answer": "ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties help ensure reliable transaction processing."
    },

    {
        "question": "What is COMMIT?",
        "expected_answer": "COMMIT permanently saves the changes made by the current transaction."
    },

    {
        "question": "What is ROLLBACK?",
        "expected_answer": "ROLLBACK undoes changes made by the current transaction that have not been committed."
    },

    {
        "question": "What is SQL injection?",
        "expected_answer": "SQL injection is a security vulnerability where malicious SQL input changes the intended database query. Parameterized queries help prevent it."
    },

    {
        "question": "What is the difference between SQL and MySQL?",
        "expected_answer": "SQL is a language used to work with relational databases, while MySQL is a relational database management system that supports SQL."
    },

    {
        "question": "What is a DBMS?",
        "expected_answer": "A DBMS is software used to create, store, retrieve, update, and manage data in databases."
    },

    {
        "question": "What is DDL?",
        "expected_answer": "DDL stands for Data Definition Language. It includes commands such as CREATE, ALTER, and DROP for defining database structures."
    },

    {
        "question": "What is DML?",
        "expected_answer": "DML stands for Data Manipulation Language. It includes commands such as INSERT, UPDATE, and DELETE for modifying data."
    },

    {
        "question": "What is DCL?",
        "expected_answer": "DCL stands for Data Control Language. It includes commands such as GRANT and REVOKE for controlling database permissions."
    },

    {
        "question": "What is TCL?",
        "expected_answer": "TCL stands for Transaction Control Language. Commands such as COMMIT and ROLLBACK are used to manage transactions."
    }

],

 #Medium

    "Medium": [

    {
        "question": "What is the difference between INNER JOIN and LEFT JOIN?",
        "expected_answer": "INNER JOIN returns only matching rows from both tables, while LEFT JOIN returns all rows from the left table and matching rows from the right table."
    },

    {
        "question": "What is the difference between WHERE and ON in a JOIN?",
        "expected_answer": "ON defines how rows are matched during the join, while WHERE filters rows after the join result is formed."
    },

    {
        "question": "What is a natural join?",
        "expected_answer": "A NATURAL JOIN automatically joins tables using columns with the same names and compatible data types. It should be used carefully because schema changes can affect the join."
    },

    {
        "question": "What is the difference between UNION and UNION ALL?",
        "expected_answer": "UNION combines result sets and removes duplicate rows, while UNION ALL combines them without removing duplicates and is usually faster."
    },

    {
        "question": "What are the requirements for using UNION?",
        "expected_answer": "The queries combined with UNION should return the same number of columns, with compatible data types in corresponding positions."
    },

    {
        "question": "What is a correlated subquery?",
        "expected_answer": "A correlated subquery depends on values from the outer query and is evaluated in relation to each row processed by the outer query."
    },

    {
        "question": "What is the difference between a subquery and a correlated subquery?",
        "expected_answer": "A normal subquery can execute independently of the outer query, while a correlated subquery references columns from the outer query."
    },

    {
        "question": "What is the difference between IN and EXISTS?",
        "expected_answer": "IN compares a value against a set of values, while EXISTS checks whether the subquery returns at least one row. EXISTS can be efficient for existence checks."
    },

    {
        "question": "What is a Common Table Expression (CTE)?",
        "expected_answer": "A CTE is a temporary named result set defined using WITH. It improves query readability and can simplify complex queries."
    },

    {
        "question": "What is a recursive CTE?",
        "expected_answer": "A recursive CTE refers to itself and is useful for hierarchical or tree-like data such as employee-manager relationships."
    },

    {
        "question": "What is a window function?",
        "expected_answer": "A window function performs calculations across related rows without collapsing them into one row per group."
    },

    {
        "question": "What is the difference between GROUP BY and window functions?",
        "expected_answer": "GROUP BY combines rows into groups and returns fewer rows, while window functions calculate across related rows while preserving individual rows."
    },

    {
        "question": "What does ROW_NUMBER() do?",
        "expected_answer": "ROW_NUMBER() assigns a unique sequential number to rows within each specified window partition and ordering."
    },

    {
        "question": "What is the difference between RANK() and DENSE_RANK()?",
        "expected_answer": "RANK() gives the same rank to ties and leaves gaps afterward, while DENSE_RANK() gives the same rank to ties without leaving gaps."
    },

    {
        "question": "How can you find the second highest salary using SQL?",
        "expected_answer": "One approach is to use a subquery with MAX below the maximum salary, or use DENSE_RANK() or ORDER BY with an appropriate limit or offset."
    },

    {
        "question": "How can you find duplicate values in a column?",
        "expected_answer": "Use GROUP BY on the column and HAVING COUNT(*) > 1 to identify values that occur more than once."
    },

    {
        "question": "How can you remove duplicate rows while keeping one record?",
        "expected_answer": "A common approach is to use ROW_NUMBER() to identify duplicates within each group and then delete rows whose row number is greater than one."
    },

    {
        "question": "How do you find employees whose salary is greater than the average salary?",
        "expected_answer": "Use a subquery to calculate the average salary and compare each employee's salary against that result."
    },

    {
        "question": "How do you find the highest salary in each department?",
        "expected_answer": "Use GROUP BY with MAX() for the salary, or use a window function such as RANK() or ROW_NUMBER() when employee details are also required."
    },

    {
        "question": "How do you find employees who do not have a department?",
        "expected_answer": "Use a LEFT JOIN and filter rows where the department key from the joined table is NULL, or check for NULL directly if the employee table stores the relationship."
    },

    {
        "question": "What is NULL-safe comparison in SQL?",
        "expected_answer": "NULL cannot be compared using normal equality because NULL represents an unknown value. IS NULL, IS NOT NULL, or database-specific NULL-safe operators should be used."
    },

    {
        "question": "What does COALESCE() do?",
        "expected_answer": "COALESCE() returns the first non-NULL value from the supplied expressions."
    },

    {
        "question": "What is the difference between COUNT(*) and COUNT(column)?",
        "expected_answer": "COUNT(*) counts rows, while COUNT(column) counts only rows where that column is not NULL."
    },

    {
        "question": "What is the difference between CHAR and VARCHAR?",
        "expected_answer": "CHAR stores fixed-length character values, while VARCHAR stores variable-length values and generally uses storage based on the actual length."
    },

    {
        "question": "What is a composite key?",
        "expected_answer": "A composite key uses two or more columns together to uniquely identify a row."
    },

    {
        "question": "What is referential integrity?",
        "expected_answer": "Referential integrity ensures that foreign-key values correctly reference existing rows in the related parent table, subject to defined constraints."
    },

    {
        "question": "What is CASCADE in a foreign key?",
        "expected_answer": "CASCADE automatically propagates certain changes, such as updates or deletes, from a referenced parent row to related child rows."
    },

    {
        "question": "What is the difference between ON DELETE CASCADE and ON DELETE SET NULL?",
        "expected_answer": "ON DELETE CASCADE deletes related child rows, while ON DELETE SET NULL changes the foreign-key value in child rows to NULL when allowed."
    },

    {
        "question": "What is an index and why is it used?",
        "expected_answer": "An index is a data structure that can speed up searches, joins, and sorting on indexed columns, but it requires storage and can add write overhead."
    },

    {
        "question": "When can an index hurt database performance?",
        "expected_answer": "Indexes can slow INSERT, UPDATE, and DELETE operations because the indexes must also be maintained. Too many indexes also consume storage."
    },

    {
        "question": "What is a composite index?",
        "expected_answer": "A composite index is an index created on multiple columns. Its usefulness often depends on the order of those columns and the query conditions."
    },

    {
        "question": "What is a clustered index?",
        "expected_answer": "A clustered index determines how table data is physically or logically organized according to the database system. Typically, a table has at most one clustered ordering."
    },

    {
        "question": "What is a covering index?",
        "expected_answer": "A covering index contains all columns needed by a query, allowing the database to answer the query from the index without accessing the base table in some systems."
    },

    {
        "question": "What is query optimization?",
        "expected_answer": "Query optimization is the process of choosing an efficient execution strategy for a SQL query, such as appropriate indexes, join methods, and access paths."
    },

    {
        "question": "What is an execution plan?",
        "expected_answer": "An execution plan describes how the database intends to execute a query, including scans, joins, sorting, filtering, and index usage."
    },

    {
        "question": "What is a full table scan?",
        "expected_answer": "A full table scan reads many or all rows of a table to find matching data. It can be expensive for large tables but may be efficient for queries returning many rows."
    },

    {
        "question": "What is a SARGable query?",
        "expected_answer": "A SARGable query allows the database to use an index efficiently for a search condition instead of applying a transformation that prevents efficient index usage."
    },

    {
        "question": "Why can SELECT * be inefficient?",
        "expected_answer": "SELECT * retrieves every column, which can increase I/O, network traffic, and processing. Selecting only required columns is usually more efficient."
    },

    {
        "question": "What is a transaction isolation level?",
        "expected_answer": "An isolation level controls how much one transaction can observe changes made by other concurrent transactions."
    },

    {
        "question": "What is a dirty read?",
        "expected_answer": "A dirty read occurs when a transaction reads data written by another transaction before that transaction has committed."
    },

    {
        "question": "What is a non-repeatable read?",
        "expected_answer": "A non-repeatable read occurs when the same row is read twice in one transaction and another transaction changes the row between the reads."
    },

    {
        "question": "What is a phantom read?",
        "expected_answer": "A phantom read occurs when repeated execution of a range query returns additional or missing rows because another transaction inserted or deleted matching rows."
    },

    {
        "question": "What is the difference between COMMIT and ROLLBACK?",
        "expected_answer": "COMMIT permanently saves the transaction's changes, while ROLLBACK undoes changes that have not been committed."
    },

    {
        "question": "What is a savepoint?",
        "expected_answer": "A savepoint marks a point inside a transaction so that part of the transaction can be rolled back without undoing the entire transaction."
    },

    {
        "question": "What is a stored procedure?",
        "expected_answer": "A stored procedure is a named collection of SQL statements stored and executed by the database server, often with parameters."
    },

    {
        "question": "What is a SQL trigger?",
        "expected_answer": "A trigger is database logic that automatically executes when specified events occur, such as INSERT, UPDATE, or DELETE."
    },

    {
        "question": "What is the difference between a stored procedure and a function?",
        "expected_answer": "A stored procedure is generally invoked as an operation and may perform multiple actions, while a function is designed to return a value and can often be used within expressions."
    },

    {
        "question": "What is a materialized view?",
        "expected_answer": "A materialized view stores the result of a query physically and can improve read performance, but it must be refreshed to keep its data current."
    },

    {
        "question": "What is a deadlock in a database?",
        "expected_answer": "A deadlock occurs when transactions wait for locks held by each other, so none can continue. Database systems typically detect and resolve deadlocks by aborting or rolling back a transaction."
    },

    {
        "question": "How can SQL query performance be improved?",
        "expected_answer": "Use appropriate indexes, select only required columns, filter efficiently, avoid unnecessary joins, inspect execution plans, and optimize queries based on actual workload and data."
    }

],

#Hard

    "Hard": [

    {
        "question": "What is the logical execution order of a SQL query?",
        "expected_answer": "The logical order is generally FROM, JOIN, WHERE, GROUP BY, HAVING, SELECT, DISTINCT, ORDER BY, and finally LIMIT or OFFSET where supported."
    },

    {
        "question": "Why can a column alias usually not be used in the WHERE clause?",
        "expected_answer": "WHERE is logically evaluated before SELECT, so the SELECT alias has not yet been defined at the WHERE stage."
    },

    {
        "question": "How do you find the top three salaries in each department?",
        "expected_answer": "Use a window function such as DENSE_RANK() partitioned by department and ordered by salary descending, then filter for ranks up to three."
    },

    {
        "question": "How do you find the nth highest salary?",
        "expected_answer": "Use DENSE_RANK() or ROW_NUMBER() with salary ordered descending and filter for the required rank. The choice depends on how ties should be handled."
    },

    {
        "question": "How do you find employees who earn more than their department average?",
        "expected_answer": "Calculate the department average using a window function or grouped subquery and compare each employee's salary with that department-level average."
    },

    {
        "question": "How do you find the highest-paid employee in every department including ties?",
        "expected_answer": "Use DENSE_RANK() partitioned by department and ordered by salary descending, then select rows where the rank is one."
    },

    {
        "question": "How can you calculate a running total in SQL?",
        "expected_answer": "Use SUM() as a window function with an ORDER BY clause, such as SUM(amount) OVER (ORDER BY date), to calculate a cumulative total."
    },

    {
        "question": "How can you calculate a moving average in SQL?",
        "expected_answer": "Use AVG() as a window function with an ordered window frame that specifies the number of preceding and current rows to include."
    },

    {
        "question": "What is a window frame?",
        "expected_answer": "A window frame defines the subset of rows considered by a window function for the current row, such as rows between a specified number of preceding and following rows."
    },

    {
        "question": "What is the difference between ROWS and RANGE in a window frame?",
        "expected_answer": "ROWS defines a physical number of rows, while RANGE defines a logical range based on the ordering values. Their results can differ when duplicate ordering values exist."
    },

    {
        "question": "How do you find the first and last record for each group?",
        "expected_answer": "Use ROW_NUMBER(), FIRST_VALUE(), or LAST_VALUE() with an appropriate PARTITION BY and ORDER BY clause depending on the required result."
    },

    {
        "question": "What is the difference between FIRST_VALUE() and MIN()?",
        "expected_answer": "MIN() returns the smallest value, while FIRST_VALUE() returns the value from the first row according to the specified window ordering."
    },

    {
        "question": "What is a recursive CTE used for?",
        "expected_answer": "A recursive CTE is used for hierarchical or graph-like data, such as organizational structures, category trees, and parent-child relationships."
    },

    {
        "question": "How can you detect cycles in hierarchical data using SQL?",
        "expected_answer": "A recursive query can track visited identifiers and stop or flag recursion when an identifier appears again, preventing infinite traversal."
    },

    {
        "question": "What is a lateral join?",
        "expected_answer": "A lateral join allows a subquery in the FROM clause to reference columns from preceding tables in the same FROM clause. Syntax and support vary by database."
    },

    {
        "question": "What is a correlated subquery performance problem?",
        "expected_answer": "A correlated subquery may be evaluated repeatedly for rows from the outer query, which can become expensive. Joins, aggregation, or window functions may provide better plans."
    },

    {
        "question": "When should you use a window function instead of GROUP BY?",
        "expected_answer": "Use a window function when calculations such as ranking or running totals are needed while retaining individual rows. Use GROUP BY when rows should be collapsed into groups."
    },

    {
        "question": "What is query plan cardinality estimation?",
        "expected_answer": "Cardinality estimation predicts how many rows each query operation will produce. The optimizer uses these estimates to choose efficient execution strategies."
    },

    {
        "question": "What is a cost-based optimizer?",
        "expected_answer": "A cost-based optimizer evaluates possible execution plans and estimates their costs using statistics, indexes, table sizes, and other information before choosing a plan."
    },

    {
        "question": "What is an index scan?",
        "expected_answer": "An index scan reads entries from an index to locate required data. It can be efficient when the index significantly reduces the amount of data that must be examined."
    },

    {
        "question": "What is an index seek?",
        "expected_answer": "An index seek directly navigates an index to locate matching values, usually making it more targeted than scanning a large portion of the index."
    },

    {
        "question": "Why might a database ignore an available index?",
        "expected_answer": "The optimizer may ignore an index when a table is small, many rows match, statistics are unfavorable, the condition is not index-friendly, or another plan has lower estimated cost."
    },

    {
        "question": "What is selectivity in database indexing?",
        "expected_answer": "Selectivity describes how effectively a condition distinguishes rows. Highly selective conditions match fewer rows and are often better candidates for index access."
    },

    {
        "question": "What is the leftmost-prefix rule for composite indexes?",
        "expected_answer": "For an index on multiple columns, queries can generally use the index efficiently starting from the leading indexed columns, depending on the database optimizer."
    },

    {
        "question": "Why can applying a function to an indexed column hurt performance?",
        "expected_answer": "Applying a function may prevent the optimizer from using a normal index efficiently because the indexed values no longer directly match the search condition."
    },

    {
        "question": "What is a covering index?",
        "expected_answer": "A covering index contains all columns required by a query, allowing the database to answer the query from the index without accessing the base table in supported cases."
    },

    {
        "question": "What is a partial or filtered index?",
        "expected_answer": "A partial or filtered index stores entries only for rows satisfying a specified condition, reducing index size and potentially improving queries that use the same condition."
    },

    {
        "question": "What is a composite index and how should its column order be chosen?",
        "expected_answer": "A composite index contains multiple columns. Column order should reflect common filtering, joining, sorting, and grouping patterns while considering selectivity and query workload."
    },

    {
        "question": "What is a deadlock in SQL transactions?",
        "expected_answer": "A deadlock occurs when two or more transactions wait for locks held by each other, so none can proceed. The database usually detects the cycle and aborts one transaction."
    },

    {
        "question": "How can database deadlocks be reduced?",
        "expected_answer": "Keep transactions short, access tables and rows in a consistent order, avoid unnecessary locks, use appropriate indexes, and retry aborted transactions when appropriate."
    },

    {
        "question": "What is optimistic concurrency control?",
        "expected_answer": "Optimistic concurrency assumes conflicts are uncommon and allows transactions to proceed without holding extensive locks, checking for conflicts before committing changes."
    },

    {
        "question": "What is pessimistic concurrency control?",
        "expected_answer": "Pessimistic concurrency assumes conflicts are likely and uses locks to prevent other transactions from modifying or accessing data in conflicting ways."
    },

    {
        "question": "What is MVCC?",
        "expected_answer": "MVCC stands for Multi-Version Concurrency Control. It maintains multiple versions of data so transactions can often read a consistent snapshot without blocking writers."
    },

    {
        "question": "What is a lost update?",
        "expected_answer": "A lost update occurs when two transactions read the same data and later overwrite each other's changes, causing one update to be lost."
    },

    {
        "question": "What is write skew?",
        "expected_answer": "Write skew is a concurrency anomaly where two transactions read overlapping data, make individually valid decisions, and together violate a business constraint."
    },

    {
        "question": "What is serializability?",
        "expected_answer": "Serializability means that the result of concurrent transactions is equivalent to some valid serial execution of those transactions."
    },

    {
        "question": "What is conflict serializability?",
        "expected_answer": "A schedule is conflict-serializable if its conflicting operations can be reordered into a serial schedule without changing the result."
    },

    {
        "question": "What is a phantom read and how can it be prevented?",
        "expected_answer": "A phantom read occurs when a repeated range query sees new or missing rows due to another transaction. Stronger isolation or appropriate range/key-range locking can prevent it."
    },

    {
        "question": "What is the difference between Repeatable Read and Serializable isolation?",
        "expected_answer": "Repeatable Read generally prevents changes to rows already read, while Serializable provides the strongest standard isolation and prevents conflicting concurrent operations that would violate serial execution."
    },

    {
        "question": "What is an execution plan and how do you use it to debug a slow query?",
        "expected_answer": "An execution plan shows how the database executes a query. Inspect scans, joins, estimated versus actual rows, sorting, filtering, and expensive operations to identify bottlenecks."
    },

    {
        "question": "What is the N+1 query problem?",
        "expected_answer": "The N+1 problem occurs when an application runs one query to retrieve parent records and then one additional query for each parent, causing excessive database calls."
    },

    {
        "question": "How can the N+1 query problem be solved?",
        "expected_answer": "Use joins, batching, eager loading, IN queries, or other set-based operations to retrieve related data in fewer database queries."
    },

    {
        "question": "Why are set-based SQL operations usually preferred over row-by-row processing?",
        "expected_answer": "Set-based operations allow the database optimizer to process many rows efficiently and often reduce network communication and procedural overhead."
    },

    {
        "question": "What is a transaction boundary and why is it important?",
        "expected_answer": "A transaction boundary defines which operations belong to one atomic transaction. Proper boundaries help maintain consistency while avoiding unnecessarily long locks."
    },

    {
        "question": "What is an idempotent SQL operation?",
        "expected_answer": "An operation is idempotent when repeating it produces the same final state as executing it once, which is useful for safe retries in distributed systems."
    },

    {
        "question": "How can you safely prevent duplicate records during concurrent inserts?",
        "expected_answer": "Use an appropriate UNIQUE constraint or unique index and handle duplicate-key conflicts rather than relying only on application-side checks."
    },

    {
        "question": "What is an upsert?",
        "expected_answer": "An upsert inserts a row when it does not exist and updates an existing row when a matching key already exists. The exact syntax depends on the database."
    },

    {
        "question": "What is SQL injection and how should it be prevented in applications?",
        "expected_answer": "SQL injection occurs when untrusted input changes the intended SQL command. Use parameterized queries or prepared statements and avoid constructing SQL by string concatenation."
    },

    {
        "question": "What is the difference between a transaction rollback and a database recovery operation?",
        "expected_answer": "A rollback undoes changes belonging to a transaction, while database recovery restores consistency after failures using mechanisms such as logs, checkpoints, undo, and redo."
    },

    {
        "question": "How would you troubleshoot a SQL query that suddenly became slow?",
        "expected_answer": "Check the execution plan, changed statistics, indexes, data growth, locking, resource usage, parameter behavior, and recent schema or query changes before selecting an optimization."
    },

    {
        "question": "How would you optimize a query running against millions of rows?",
        "expected_answer": "Analyze the execution plan, filter early, select only required columns, add appropriate indexes, optimize joins, avoid unnecessary sorting, and verify improvements using realistic data."
    },

    {
        "question": "What is the difference between OLTP and OLAP databases?",
        "expected_answer": "OLTP systems handle frequent transactional operations with many small reads and writes, while OLAP systems are optimized for large analytical queries and aggregations."
    },

    {
        "question": "Why can denormalization improve SQL query performance?",
        "expected_answer": "Denormalization can reduce joins and repeated lookups by storing some redundant data, potentially improving reads at the cost of additional storage and more complex updates."
    },

    {
        "question": "What are common mistakes when optimizing SQL queries?",
        "expected_answer": "Common mistakes include adding unnecessary indexes, optimizing without checking execution plans, using SELECT *, ignoring data distribution, and changing queries without measuring the actual impact."
    }

]
}
  