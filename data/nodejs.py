questions = {

    "Easy": [

        {
            "question": "What is Node.js?",
            "expected_answer": "Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine that allows JavaScript to run outside the browser, commonly for server-side applications."
        },

        {
            "question": "Is Node.js a programming language?",
            "expected_answer": "No. Node.js is a JavaScript runtime environment. JavaScript is the programming language that runs inside Node.js."
        },

        {
            "question": "What is the V8 engine?",
            "expected_answer": "V8 is Google's open-source JavaScript engine used by Chrome and Node.js to execute JavaScript code."
        },

        {
            "question": "Why is Node.js commonly used for backend development?",
            "expected_answer": "Node.js provides a fast JavaScript runtime, non-blocking I/O, a large package ecosystem, and allows developers to use JavaScript on both the frontend and backend."
        },

        {
            "question": "What is npm?",
            "expected_answer": "npm is the default package manager for Node.js. It is used to install, manage, update, and publish JavaScript packages."
        },

        {
            "question": "What is package.json?",
            "expected_answer": "package.json is a configuration file that stores information about a Node.js project, including its name, version, dependencies, scripts, and other project metadata."
        },

        {
            "question": "What is node_modules?",
            "expected_answer": "node_modules is the directory where npm installs the packages and their dependencies required by a Node.js project."
        },

        {
            "question": "What is the difference between dependencies and devDependencies?",
            "expected_answer": "dependencies are packages required by the application at runtime, while devDependencies are mainly packages needed during development, testing, or building."
        },

        {
            "question": "How do you initialize a Node.js project?",
            "expected_answer": "A Node.js project can be initialized using the command `npm init`, or `npm init -y` to create package.json with default values."
        },

        {
            "question": "How do you install a package using npm?",
            "expected_answer": "A package can be installed using `npm install package-name`. npm then adds the package to the project's dependencies by default."
        },

        {
            "question": "How do you install a package globally?",
            "expected_answer": "A package can be installed globally using `npm install -g package-name`, making its command-line tools available system-wide."
        },

        {
            "question": "How do you remove an npm package?",
            "expected_answer": "A package can be removed from a project using `npm uninstall package-name`."
        },

        {
            "question": "What is a Node.js module?",
            "expected_answer": "A module is a reusable unit of code that can expose functions, objects, or other values for use in other parts of a Node.js application."
        },

        {
            "question": "What is the CommonJS module system?",
            "expected_answer": "CommonJS is a traditional Node.js module system that commonly uses `require()` to import modules and `module.exports` or `exports` to expose values."
        },

        {
            "question": "What are ES modules in Node.js?",
            "expected_answer": "ES modules are the standard JavaScript module system using `import` and `export`. Node.js supports them with appropriate project configuration or `.mjs` files."
        },

        {
            "question": "What is the difference between require and import?",
            "expected_answer": "`require()` is commonly associated with CommonJS modules, while `import` is part of the standard ECMAScript module system."
        },

        {
            "question": "What is the Node.js event loop?",
            "expected_answer": "The event loop is the mechanism that allows Node.js to handle asynchronous operations without blocking the main JavaScript execution thread."
        },

        {
            "question": "What is non-blocking I/O?",
            "expected_answer": "Non-blocking I/O allows a program to start an input/output operation without waiting for it to finish before continuing with other work."
        },

        {
            "question": "What is asynchronous programming in Node.js?",
            "expected_answer": "Asynchronous programming allows operations such as file access, network requests, and database operations to complete without blocking the main JavaScript execution flow."
        },

        {
            "question": "What is a callback function?",
            "expected_answer": "A callback is a function passed to another function so that it can be executed later, commonly after an asynchronous operation completes."
        },

        {
            "question": "What is callback hell?",
            "expected_answer": "Callback hell refers to deeply nested callbacks that make asynchronous code difficult to read, maintain, and handle errors in."
        },

        {
            "question": "What is a Promise in Node.js?",
            "expected_answer": "A Promise represents the eventual completion or failure of an asynchronous operation and can be handled using `.then()`, `.catch()`, and `.finally()`."
        },

        {
            "question": "What is async/await?",
            "expected_answer": "async/await is JavaScript syntax for working with Promises in a more readable style. An `async` function returns a Promise, and `await` pauses that function until a Promise settles."
        },

        {
            "question": "What is the difference between synchronous and asynchronous code?",
            "expected_answer": "Synchronous code generally executes one operation at a time and waits for each operation to finish, while asynchronous code can start an operation and continue other work before that operation completes."
        },

        {
            "question": "What is the fs module in Node.js?",
            "expected_answer": "The `fs` module provides APIs for interacting with the file system, including reading, writing, updating, deleting, and managing files and directories."
        },

        {
            "question": "What is the path module in Node.js?",
            "expected_answer": "The `path` module provides utilities for working with file and directory paths in a platform-independent way."
        },

        {
            "question": "What is the http module?",
            "expected_answer": "The built-in `http` module provides APIs for creating HTTP servers and making HTTP requests."
        },

        {
            "question": "How do you create a basic HTTP server in Node.js?",
            "expected_answer": "A basic server can be created using `http.createServer()` and started with `server.listen()`."
        },

        {
            "question": "What is Express.js?",
            "expected_answer": "Express.js is a lightweight web framework for Node.js that provides features for building web servers, APIs, routing, middleware, and request handling."
        },

        {
            "question": "What is middleware in Express.js?",
            "expected_answer": "Middleware is a function that runs during the request-response cycle and can inspect or modify the request and response, perform actions, or pass control to the next middleware."
        },

        {
            "question": "What is routing in Express.js?",
            "expected_answer": "Routing defines how an application responds to requests for particular HTTP methods and URL paths."
        },

        {
            "question": "What are HTTP methods commonly used in Node.js APIs?",
            "expected_answer": "Common HTTP methods include GET for retrieving data, POST for creating or submitting data, PUT or PATCH for updates, and DELETE for removing data."
        },

        {
            "question": "What is REST API?",
            "expected_answer": "A REST API is an HTTP-based API designed around resources and standard HTTP methods, commonly using JSON to exchange data."
        },

        {
            "question": "What is JSON?",
            "expected_answer": "JSON is a lightweight text-based data format commonly used to exchange structured data between clients and servers."
        },

        {
            "question": "How do you send a JSON response in Express.js?",
            "expected_answer": "In Express.js, `res.json()` can be used to send a JavaScript value as a JSON response with the appropriate content type."
        },

        {
            "question": "What is req in Express.js?",
            "expected_answer": "`req` is the request object that contains information about the incoming HTTP request, such as parameters, query values, headers, and body data."
        },

        {
            "question": "What is res in Express.js?",
            "expected_answer": "`res` is the response object used by Express.js to send data, status codes, headers, or other responses back to the client."
        },

        {
            "question": "What is req.params?",
            "expected_answer": "`req.params` contains route parameters defined in an Express.js route, such as the `id` in `/users/:id`."
        },

        {
            "question": "What is req.query?",
            "expected_answer": "`req.query` contains query-string parameters from the URL, such as `?page=2&limit=10`."
        },

        {
            "question": "What is req.body?",
            "expected_answer": "`req.body` contains data sent in the request body, commonly JSON or form data, after the appropriate body-parsing middleware is configured."
        },

        {
            "question": "What is process in Node.js?",
            "expected_answer": "`process` is a global object that provides information about and control over the current Node.js process, including environment variables, arguments, and exit behavior."
        },

        {
            "question": "What is process.env?",
            "expected_answer": "`process.env` provides access to environment variables available to the current Node.js process."
        },

        {
            "question": "What is the purpose of environment variables?",
            "expected_answer": "Environment variables store configuration values outside the source code, such as database URLs, ports, and application settings."
        },

        {
            "question": "What is the difference between Node.js and a browser JavaScript environment?",
            "expected_answer": "Node.js provides server-side capabilities such as file-system and network APIs, while browser JavaScript runs in a web-page environment with browser-specific APIs such as the DOM."
        },

        {
            "question": "What is a buffer in Node.js?",
            "expected_answer": "A Buffer is a Node.js object used to work with raw binary data, such as data received from files, network connections, or streams."
        },

        {
            "question": "What are streams in Node.js?",
            "expected_answer": "Streams provide a way to process data incrementally as it becomes available instead of loading the entire data set into memory at once."
        },

        {
            "question": "What are the main types of Node.js streams?",
            "expected_answer": "The main stream types are Readable, Writable, Duplex, and Transform streams."
        },

        {
            "question": "What is a Readable stream?",
            "expected_answer": "A Readable stream represents a source from which data can be consumed, such as a file or incoming network data."
        },

        {
            "question": "What is a Writable stream?",
            "expected_answer": "A Writable stream represents a destination to which data can be written, such as a file or outgoing network connection."
        },

        {
            "question": "What is a Duplex stream?",
            "expected_answer": "A Duplex stream can both read and write data, such as a network socket."
        },

        {
            "question": "What is a Transform stream?",
            "expected_answer": "A Transform stream is a type of Duplex stream that can modify or transform data as it passes through."
        },

        {
            "question": "What is npm script?",
            "expected_answer": "An npm script is a command defined in the `scripts` section of package.json and can be executed using commands such as `npm run start`."
        },

        {
            "question": "What is package-lock.json?",
            "expected_answer": "package-lock.json records the exact dependency versions and dependency tree installed for a project, helping make installations reproducible."
        },

        {
            "question": "What is the difference between npm install and npm ci?",
            "expected_answer": "`npm install` can update the lock file when needed, while `npm ci` installs exactly from the lock file and is commonly used for clean, reproducible CI or deployment installs."
        },

        {
            "question": "What is nodemon?",
            "expected_answer": "Nodemon is a development utility that automatically restarts a Node.js application when files in the project change."
        },

        {
            "question": "What is the purpose of the .gitignore file in a Node.js project?",
            "expected_answer": "It specifies files and directories Git should ignore, commonly including `node_modules`, environment files containing secrets, logs, and generated build files."
        },

        {
            "question": "How can errors be handled in Node.js?",
            "expected_answer": "Errors can be handled using callbacks, Promise rejection handling, try/catch with async/await, and appropriate application-level error-handling middleware."
        },

        {
            "question": "What is the difference between throw and return in error handling?",
            "expected_answer": "`throw` raises an exception that must be handled by appropriate error-handling logic, while `return` simply returns a value from a function and does not itself signal an exception."
        },

        {
            "question": "What is an environment such as development or production in Node.js?",
            "expected_answer": "An environment represents the context in which an application runs, such as development, testing, or production, and can be used to control configuration and behavior."
        },

        {
            "question": "What is the default port commonly used by Node.js applications?",
            "expected_answer": "Node.js does not require a single default application port. Developers commonly choose ports such as 3000 for local development."
        }

    ],
 #Medium
 "Medium":[

   {
        "question": "How does the Node.js event loop work?",
        "expected_answer": "The event loop allows Node.js to handle asynchronous operations by processing callbacks and events while JavaScript execution remains on the main thread. Operations such as I/O can be handled outside the JavaScript call stack and their callbacks are processed when ready."
    },

    {
        "question": "Why is Node.js considered single-threaded?",
        "expected_answer": "Node.js executes JavaScript code on a main thread, but it can still handle many concurrent operations using asynchronous I/O and system or libuv worker threads for certain tasks."
    },

    {
        "question": "Does Node.js support multiple threads?",
        "expected_answer": "Yes. Node.js can use worker threads for CPU-intensive JavaScript work, and its underlying runtime can use a thread pool for certain asynchronous operations. The main JavaScript execution thread remains event-driven."
    },

    {
        "question": "What is libuv in Node.js?",
        "expected_answer": "libuv is a cross-platform library used by Node.js for asynchronous I/O, the event loop, networking, and a worker thread pool for certain operations."
    },

    {
        "question": "What is the Node.js thread pool?",
        "expected_answer": "The libuv thread pool provides worker threads for certain operations that would otherwise block the main event loop, such as some file-system, DNS, and cryptographic operations."
    },

    {
        "question": "What is the difference between CPU-bound and I/O-bound tasks?",
        "expected_answer": "CPU-bound tasks spend most of their time performing computation, while I/O-bound tasks spend significant time waiting for operations such as files, databases, or networks to complete."
    },

    {
        "question": "Why can CPU-intensive operations be a problem in Node.js?",
        "expected_answer": "Long CPU-intensive JavaScript operations can block the main event loop, preventing it from processing other requests and reducing application responsiveness."
    },

    {
        "question": "How can CPU-intensive work be handled in Node.js?",
        "expected_answer": "CPU-intensive work can be moved to worker threads, separate processes, or external services so that the main event loop remains responsive."
    },

    {
        "question": "What are Worker Threads in Node.js?",
        "expected_answer": "Worker Threads allow JavaScript code to run in separate threads. They are useful for CPU-intensive tasks because they can perform computation without blocking the main JavaScript thread."
    },

    {
        "question": "What is the difference between worker_threads and child_process?",
        "expected_answer": "Worker Threads run JavaScript in separate threads within the same process, while child_process creates separate operating-system processes. Processes provide stronger isolation but generally have higher communication overhead."
    },

    {
        "question": "What is the cluster module in Node.js?",
        "expected_answer": "The cluster module allows multiple Node.js processes to run and share server connections, which can help use multiple CPU cores for handling network workloads."
    },

    {
        "question": "What is the difference between clustering and worker threads?",
        "expected_answer": "Clustering uses multiple processes and provides stronger isolation, while worker threads use multiple threads within a process and can share certain memory structures more efficiently."
    },

    {
        "question": "What is middleware chaining in Express.js?",
        "expected_answer": "Middleware chaining means multiple middleware functions process a request in sequence. A middleware can perform work and call `next()` to pass control to the next middleware."
    },

    {
        "question": "What happens if Express middleware does not call next() or send a response?",
        "expected_answer": "The request can remain unresolved because control is not passed to the next middleware and no response is sent to the client."
    },

    {
        "question": "What is error-handling middleware in Express.js?",
        "expected_answer": "Error-handling middleware is middleware designed to process application errors. It uses four parameters: `(err, req, res, next)` and can send an appropriate response or pass the error onward."
    },

    {
        "question": "How do you handle asynchronous errors in Express.js?",
        "expected_answer": "Asynchronous errors should be passed to Express's error-handling mechanism, commonly using `next(error)` or appropriate Promise rejection handling. Modern Express versions can also handle rejected route-handler Promises."
    },

    {
        "question": "What is route parameter validation?",
        "expected_answer": "Route parameter validation checks whether values supplied in URL parameters meet expected requirements, such as type, format, range, or allowed values, before processing the request."
    },

    {
        "question": "What is the difference between route parameters and query parameters?",
        "expected_answer": "Route parameters identify values embedded in the URL path, such as `/users/10`, while query parameters provide optional values after `?`, such as `/users?page=2`."
    },

    {
        "question": "How can you parse JSON request bodies in Express.js?",
        "expected_answer": "Express provides built-in JSON parsing middleware using `express.json()`. After enabling it, parsed JSON data is available through `req.body`."
    },

    {
        "question": "What is CORS?",
        "expected_answer": "CORS, or Cross-Origin Resource Sharing, is a browser security mechanism that controls whether a web page from one origin can access resources from another origin."
    },

    {
        "question": "How can CORS be configured in an Express application?",
        "expected_answer": "CORS can be configured by sending appropriate HTTP response headers or by using middleware such as the `cors` package to specify allowed origins, methods, headers, and credentials."
    },

    {
        "question": "What is a RESTful route design?",
        "expected_answer": "RESTful route design represents resources through URLs and uses HTTP methods according to their intended semantics, such as GET for retrieval, POST for creation, PUT or PATCH for updates, and DELETE for removal."
    },

    {
        "question": "What is API versioning?",
        "expected_answer": "API versioning allows different versions of an API to coexist so changes can be introduced without immediately breaking existing clients. Versioning can be implemented through URL paths, headers, or other agreed conventions."
    },

    {
        "question": "What is authentication?",
        "expected_answer": "Authentication is the process of verifying the identity of a user or system, such as through a username and password, token, certificate, or other credential."
    },

    {
        "question": "What is authorization?",
        "expected_answer": "Authorization determines what an authenticated user or system is allowed to access or perform."
    },

    {
        "question": "What is the difference between authentication and authorization?",
        "expected_answer": "Authentication verifies who the user is, while authorization determines what that authenticated user is permitted to do."
    },

    {
        "question": "What is JWT?",
        "expected_answer": "JWT, or JSON Web Token, is a compact token format commonly used to transmit signed claims between parties. It can be used for stateless authentication when designed and validated correctly."
    },

    {
        "question": "What are the main parts of a JWT?",
        "expected_answer": "A JWT commonly contains three Base64URL-encoded parts separated by dots: header, payload, and signature."
    },

    {
        "question": "Should sensitive information be stored in a JWT payload?",
        "expected_answer": "No. A normal JWT payload is encoded rather than encrypted, so its contents can be decoded by someone who has the token. Sensitive information should not be placed there unless appropriate encryption is used."
    },

    {
        "question": "What is session-based authentication?",
        "expected_answer": "In session-based authentication, the server creates a session after successful login and associates it with the user. The client typically sends a session identifier with subsequent requests."
    },

    {
        "question": "What is the difference between sessions and JWT-based authentication?",
        "expected_answer": "Session authentication commonly stores session state on the server, while JWT-based authentication can carry signed authentication claims in the token. Each approach has different trade-offs for revocation, storage, and scalability."
    },

    {
        "question": "Why should passwords not be stored directly in a Node.js database?",
        "expected_answer": "Plain-text passwords are highly sensitive and should not be stored directly. Passwords should be securely hashed using a suitable password-hashing algorithm and verified using the stored hash."
    },

    {
        "question": "What is password hashing?",
        "expected_answer": "Password hashing converts a password into a one-way cryptographic representation using a password-hashing algorithm. During login, the supplied password is verified against the stored hash."
    },

    {
        "question": "What is salting in password hashing?",
        "expected_answer": "A salt is unique random data added during password hashing. It makes identical passwords produce different hashes and helps defend against precomputed hash attacks."
    },

    {
        "question": "What is environment-based configuration in Node.js?",
        "expected_answer": "Environment-based configuration stores settings such as database URLs, API keys, and ports outside the application code, commonly using environment variables."
    },

    {
        "question": "Why should secrets not be hard-coded in Node.js source code?",
        "expected_answer": "Hard-coded secrets can accidentally be committed to source-control repositories or exposed to developers and systems that should not have access. Environment variables or secure secret-management systems are safer approaches."
    },

    {
        "question": "What is dotenv?",
        "expected_answer": "dotenv is a package commonly used during development to load environment variables from a `.env` file into `process.env`."
    },

    {
        "question": "What is a stream backpressure problem?",
        "expected_answer": "Backpressure occurs when a data producer generates data faster than the consumer can process it. Streams provide mechanisms such as buffering and flow control to prevent uncontrolled memory growth."
    },

    {
        "question": "How can streams improve memory efficiency?",
        "expected_answer": "Streams process data in smaller chunks instead of loading an entire large resource into memory, which can reduce memory usage for files, network data, and other large inputs."
    },

    {
        "question": "What is a pipe in Node.js streams?",
        "expected_answer": "The `pipe()` method connects a readable stream to a writable stream so that data can flow automatically from the source to the destination while applying stream flow control."
    },

    {
        "question": "What is an EventEmitter in Node.js?",
        "expected_answer": "EventEmitter is a Node.js mechanism for creating and handling custom events. Objects can emit named events and listeners can register functions to respond to them."
    },

    {
        "question": "How does EventEmitter work?",
        "expected_answer": "Listeners are registered for event names using methods such as `on()`, and an event can be triggered using `emit()`, causing the registered listeners to execute."
    },

    {
        "question": "What is the difference between on() and once() in EventEmitter?",
        "expected_answer": "`on()` registers a listener that can run every time the event occurs, while `once()` registers a listener that automatically removes itself after the first occurrence."
    },

    {
        "question": "What is an event-driven architecture?",
        "expected_answer": "Event-driven architecture organizes application behavior around events. Components produce events and other components react to those events, allowing parts of the system to operate with loose coupling."
    },

    {
        "question": "What is the purpose of the Node.js URL module?",
        "expected_answer": "The URL module provides APIs for parsing, constructing, and manipulating URLs and their components."
    },

    {
        "question": "What is the purpose of the crypto module in Node.js?",
        "expected_answer": "The built-in crypto module provides cryptographic functionality such as hashing, encryption-related operations, digital signatures, random data generation, and key management."
    },

    {
        "question": "What is the purpose of the os module in Node.js?",
        "expected_answer": "The `os` module provides operating-system-related information such as CPU details, memory information, platform information, and network interfaces."
    },

    {
        "question": "What is the purpose of the child_process module?",
        "expected_answer": "The `child_process` module allows a Node.js application to create and manage operating-system child processes and communicate with them."
    },

    {
        "question": "What is spawn() in Node.js?",
        "expected_answer": "`spawn()` starts a child process and provides streams for communicating with its standard input, output, and error streams. It is useful for processes that produce or consume data over time."
    },

    {
        "question": "What is exec() in Node.js?",
        "expected_answer": "`exec()` runs a command in a shell and collects its output, making it convenient for commands where the output can reasonably be buffered in memory."
    },

    {
        "question": "What is the difference between exec() and spawn()?",
        "expected_answer": "`exec()` runs a command through a shell and buffers its output, while `spawn()` starts a process and exposes streams for handling output incrementally."
    },

    {
        "question": "What is graceful shutdown in Node.js?",
        "expected_answer": "Graceful shutdown means stopping a Node.js application in an orderly way by stopping new requests, allowing active work to finish when possible, closing connections, and then exiting."
    },

    {
        "question": "Why is graceful shutdown important?",
        "expected_answer": "It helps prevent incomplete requests, lost data, abrupt connection failures, and resource leaks when an application is restarted, deployed, or terminated."
    },

    {
        "question": "What is process.nextTick()?",
        "expected_answer": "`process.nextTick()` schedules a callback to run after the current operation completes but before the event loop continues to later phases."
    },

    {
        "question": "What is setImmediate() in Node.js?",
        "expected_answer": "`setImmediate()` schedules a callback to execute during the check phase of the Node.js event loop, after the current poll phase."
    },

    {
        "question": "What is the difference between process.nextTick() and setImmediate()?",
        "expected_answer": "`process.nextTick()` callbacks are processed before the event loop continues to later phases, while `setImmediate()` schedules work for the check phase. Excessive nextTick usage can delay other event-loop work."
    },

    {
        "question": "What is an unhandled Promise rejection?",
        "expected_answer": "An unhandled Promise rejection occurs when a Promise rejects and no appropriate rejection handler is attached. Applications should handle expected failures and configure appropriate process-level monitoring."
    },

    {
        "question": "What is an uncaught exception?",
        "expected_answer": "An uncaught exception is an exception that reaches the top level without being handled. It can leave the application in an unsafe state, so robust applications should log the failure and use an appropriate recovery or restart strategy."
    },

    {
        "question": "How can Node.js applications be made more secure?",
        "expected_answer": "Security measures include validating input, using secure authentication, protecting secrets, applying authorization checks, preventing injection attacks, configuring CORS carefully, using HTTPS, updating dependencies, and applying secure HTTP headers."
    },

    {
        "question": "What is input validation in a Node.js API?",
        "expected_answer": "Input validation checks incoming request data against expected types, formats, ranges, and business rules before the application processes it."
    },

    {
        "question": "Why is input validation important in Node.js applications?",
        "expected_answer": "It prevents invalid or malicious data from reaching application logic and downstream systems, reducing bugs and security risks such as injection and unexpected behavior."
    },

    {
        "question": "What is rate limiting?",
        "expected_answer": "Rate limiting restricts how many requests a client can make during a defined period. It can help protect APIs from abuse, excessive traffic, and certain denial-of-service patterns."
    },

    {
        "question": "What is caching in a Node.js application?",
        "expected_answer": "Caching stores frequently needed data in a faster-access location so repeated requests can be served more quickly and with less load on databases or other backend services."
    },

    {
        "question": "Where can caching be implemented in a Node.js application?",
        "expected_answer": "Caching can be implemented in application memory, reverse proxies, CDNs, or external systems such as Redis, depending on the data, consistency requirements, and deployment architecture."
    },

    {
        "question": "What is connection pooling?",
        "expected_answer": "Connection pooling maintains a reusable set of database connections so requests can borrow and return connections instead of creating a new connection for every operation."
    },

    {
        "question": "Why is database connection pooling useful in Node.js?",
        "expected_answer": "It reduces the overhead of repeatedly creating database connections and allows controlled reuse of connections when many requests are handled concurrently."
    },

    {
        "question": "How should a Node.js application handle database errors?",
        "expected_answer": "Database errors should be caught and logged appropriately, meaningful safe responses should be returned to clients, and transactions or retries should be used where appropriate without exposing sensitive internal details."
    },

    {
        "question": "What is horizontal scaling in Node.js?",
        "expected_answer": "Horizontal scaling means running multiple instances of a Node.js application and distributing traffic among them, commonly through a load balancer."
    },

    {
        "question": "What is vertical scaling?",
        "expected_answer": "Vertical scaling means increasing the CPU, memory, or other resources available to an existing server or application instance."
    },

    {
        "question": "Why can Node.js applications benefit from horizontal scaling?",
        "expected_answer": "Multiple application instances can use additional CPU resources and handle more concurrent traffic while improving availability when combined with suitable load balancing and shared state management."
    },

    {
        "question": "What problem can occur when sessions are stored only in application memory during horizontal scaling?",
        "expected_answer": "A user's next request may reach a different application instance that does not contain the original session. Shared session storage or an appropriate load-balancing strategy can solve this problem."
    },

    {
        "question": "What is a reverse proxy in front of a Node.js application?",
        "expected_answer": "A reverse proxy receives client requests and forwards them to Node.js application servers. It can provide TLS termination, load balancing, caching, compression, routing, and other infrastructure features."
    },

    {
        "question": "What is logging in a Node.js application?",
        "expected_answer": "Logging records useful information about application behavior, requests, errors, and system events so developers and operators can monitor and troubleshoot the application."
    },

    {
        "question": "What should production logs contain?",
        "expected_answer": "Production logs should contain useful contextual information such as timestamps, severity, request or correlation identifiers, relevant error details, and operational events without exposing passwords, tokens, or other sensitive data."
    },

    {
        "question": "What is a health-check endpoint?",
        "expected_answer": "A health-check endpoint provides information about whether an application instance is running and, depending on its design, whether important dependencies are available."
    },

    {
        "question": "What is the difference between liveness and readiness checks?",
        "expected_answer": "A liveness check indicates whether an application instance should be considered alive, while a readiness check indicates whether it is prepared to receive traffic."
    },

    {
        "question": "How can a Node.js API improve response performance?",
        "expected_answer": "Performance can be improved by avoiding blocking operations, optimizing database queries, using caching, streaming large responses, reducing unnecessary computation, using connection pooling, and scaling appropriately."
    },

    {
        "question": "How would you debug a slow Node.js API?",
        "expected_answer": "I would measure request latency, identify slow routes, inspect database and external-service timings, check event-loop delay and CPU usage, examine memory and I/O, and use profiling or tracing tools to locate the bottleneck."
    },

    {
        "question": "What is event-loop blocking?",
        "expected_answer": "Event-loop blocking occurs when synchronous or CPU-intensive work keeps the main JavaScript thread busy for too long, preventing it from processing other callbacks and incoming requests."
    },

    {
        "question": "How can synchronous APIs cause problems in a Node.js server?",
        "expected_answer": "Synchronous APIs can block the event loop while they wait for an operation to complete. In a server handling many requests, this can delay unrelated requests and reduce throughput."
    },

    {
        "question": "What is the purpose of async error handling in Node.js?",
        "expected_answer": "Async error handling ensures failures from asynchronous operations are captured and handled instead of becoming unhandled rejections or causing inconsistent application behavior."
    },

    {
        "question": "How do Promise.all() and Promise.allSettled() differ?",
        "expected_answer": "Promise.all() fulfills only when all Promises fulfill and rejects when one rejects. Promise.allSettled() waits for every Promise and reports the fulfillment or rejection status of each."
    },

    {
        "question": "When should Promise.all() be used?",
        "expected_answer": "Promise.all() is useful when multiple independent asynchronous operations can run concurrently and the overall operation should fail if any required operation fails."
    },

    {
        "question": "What is the benefit of running independent asynchronous operations concurrently?",
        "expected_answer": "Concurrent asynchronous operations can reduce total waiting time when the operations are independent, because their I/O delays can overlap instead of occurring sequentially."
    },

    {
        "question": "What is the difference between sequential and concurrent Promise execution?",
        "expected_answer": "Sequential execution waits for one asynchronous operation before starting the next, while concurrent execution starts independent operations together and waits for their results collectively."
    },

    {
        "question": "What is dependency management in Node.js?",
        "expected_answer": "Dependency management involves declaring, installing, updating, locking, and auditing packages required by an application."
    },

    {
        "question": "Why should Node.js dependencies be kept updated?",
        "expected_answer": "Updates can provide security fixes, bug fixes, compatibility improvements, and performance improvements. Updates should still be tested because they can introduce breaking changes."
    },

    {
        "question": "What is semantic versioning?",
        "expected_answer": "Semantic versioning commonly uses MAJOR.MINOR.PATCH. Major versions may contain breaking changes, minor versions generally add backward-compatible features, and patch versions generally contain backward-compatible fixes."
    },

    {
        "question": "What is npm audit?",
        "expected_answer": "`npm audit` checks project dependencies against known security vulnerabilities and reports packages that may require updates or other remediation."
    }

],

"Hard": [

    {
        "question": "What are the phases of the Node.js event loop?",
        "expected_answer": "The event loop processes phases such as timers, pending callbacks, poll, check, and close callbacks. Each phase handles a specific category of asynchronous work."
    },

    {
        "question": "What is the difference between the microtask queue and the event loop phases?",
        "expected_answer": "Microtasks such as Promise callbacks are processed between event-loop phases, while phases handle categories such as timers, I/O, and check callbacks. Node.js also gives process.nextTick callbacks special priority."
    },

    {
        "question": "Why can process.nextTick() be dangerous?",
        "expected_answer": "Too many recursive process.nextTick callbacks can prevent the event loop from reaching I/O and other phases, causing event-loop starvation."
    },

    {
        "question": "What is event-loop starvation in Node.js?",
        "expected_answer": "Event-loop starvation occurs when callbacks continuously occupy the event loop and prevent other work, such as I/O and timers, from being processed promptly."
    },

    {
        "question": "How would you detect event-loop blocking in a Node.js application?",
        "expected_answer": "I would monitor event-loop delay or lag, inspect CPU usage and profiling data, and look for synchronous operations or CPU-heavy JavaScript running on the main thread."
    },

    {
        "question": "Why can a single-threaded Node.js server still handle many concurrent requests?",
        "expected_answer": "Node.js uses non-blocking I/O and an event loop, allowing one JavaScript thread to start asynchronous operations and process their callbacks while I/O is in progress."
    },

    {
        "question": "What happens when CPU-intensive JavaScript runs on the Node.js main thread?",
        "expected_answer": "It blocks the event loop, delaying other requests, timers, and callbacks. CPU-heavy work should be moved to worker threads or separate processes when appropriate."
    },

    {
        "question": "How do worker threads communicate with each other?",
        "expected_answer": "Worker threads can communicate using message passing with parentPort and worker threads. They can also use SharedArrayBuffer and Atomics when shared memory is required."
    },

    {
        "question": "What is SharedArrayBuffer in Node.js?",
        "expected_answer": "SharedArrayBuffer provides memory that can be shared between worker threads. Atomics can be used to coordinate access to shared memory safely."
    },

    {
        "question": "What is the purpose of Atomics in worker threads?",
        "expected_answer": "Atomics provide operations for safely coordinating access to shared memory between threads and can be used for synchronization."
    },

    {
        "question": "When would you use worker_threads instead of child_process?",
        "expected_answer": "I would use worker_threads mainly for CPU-intensive JavaScript that can benefit from threads and shared memory. child_process is more suitable for running separate processes or external programs."
    },

    {
        "question": "How does Node.js cluster help scale an application?",
        "expected_answer": "Cluster allows multiple Node.js worker processes to run, commonly using multiple CPU cores so the application can handle more concurrent workloads."
    },

    {
        "question": "What is the difference between clustering and horizontal scaling?",
        "expected_answer": "Clustering creates multiple processes on one machine, while horizontal scaling runs application instances across multiple machines or containers."
    },

    {
        "question": "How would you design a Node.js application for horizontal scaling?",
        "expected_answer": "I would keep application instances stateless, use shared external storage for sessions and data, place instances behind a load balancer, and design shared services carefully."
    },

    {
        "question": "Why should sessions generally not be stored only in application memory in a scaled Node.js application?",
        "expected_answer": "Different requests may reach different instances, so in-memory sessions can become inconsistent. A shared session store such as Redis can provide common session state."
    },

    {
        "question": "What is stream backpressure and how do you handle it?",
        "expected_answer": "Backpressure occurs when a writable destination cannot consume data as quickly as it is produced. Node.js streams can manage this through mechanisms such as pipe() and drain events."
    },

    {
        "question": "Why are streams useful for processing large files?",
        "expected_answer": "Streams process data incrementally instead of loading the entire file into memory, which reduces memory usage and can improve responsiveness."
    },

    {
        "question": "What is a Transform stream?",
        "expected_answer": "A Transform stream is both readable and writable and modifies or processes data as it passes through the stream."
    },

    {
        "question": "What happens if a stream is not handling backpressure correctly?",
        "expected_answer": "Data can accumulate faster than it is consumed, increasing memory usage and potentially causing poor performance or memory exhaustion."
    },

    {
        "question": "How would you investigate a memory leak in Node.js?",
        "expected_answer": "I would monitor memory usage over time, take heap snapshots, compare retained objects, inspect references, and use profiling tools to identify objects that are unnecessarily retained."
    },

    {
        "question": "What is a memory leak in a Node.js application?",
        "expected_answer": "A memory leak occurs when objects that are no longer needed remain reachable and therefore cannot be reclaimed by the garbage collector."
    },

    {
        "question": "What are common causes of memory leaks in Node.js?",
        "expected_answer": "Common causes include growing global collections, uncleared timers, event listeners that are never removed, caches without limits, and references that unintentionally keep objects alive."
    },

    {
        "question": "What is garbage collection in Node.js?",
        "expected_answer": "Garbage collection automatically reclaims memory occupied by objects that are no longer reachable by the application."
    },

    {
        "question": "What is the V8 heap?",
        "expected_answer": "The V8 heap is the memory area managed by the V8 JavaScript engine for objects and other JavaScript data used by a Node.js process."
    },

    {
        "question": "How would you troubleshoot an API that becomes slower over time?",
        "expected_answer": "I would monitor latency, CPU, memory, event-loop delay, database performance, external calls, and heap usage, then use profiling and logs to identify the growing bottleneck."
    },

    {
        "question": "How would you troubleshoot high CPU usage in Node.js?",
        "expected_answer": "I would inspect CPU profiles, event-loop delay, request patterns, synchronous operations, expensive algorithms, and worker or process usage to identify the CPU-intensive code."
    },

    {
        "question": "What is event-loop lag and why does it matter?",
        "expected_answer": "Event-loop lag measures how much scheduled work is delayed because the event loop is busy. High lag indicates that requests and other asynchronous tasks may become slow."
    },

    {
        "question": "How can synchronous APIs hurt a production Node.js server?",
        "expected_answer": "Synchronous APIs block the event loop until they finish, preventing the server from processing other JavaScript callbacks during that time."
    },

    {
        "question": "How would you design error handling for an Express application?",
        "expected_answer": "I would use centralized error-handling middleware, validate inputs, handle expected errors explicitly, avoid exposing sensitive details, and log unexpected errors with useful context."
    },

    {
        "question": "What is centralized error handling?",
        "expected_answer": "Centralized error handling routes application errors to a common handler instead of duplicating response logic across every route."
    },

    {
        "question": "How should asynchronous errors be handled in Express?",
        "expected_answer": "Async route handlers should ensure rejected promises reach the application's error-handling middleware, either through framework support or an appropriate async wrapper."
    },

    {
        "question": "Why should production APIs avoid returning raw error stacks?",
        "expected_answer": "Stack traces can expose internal implementation details, file paths, dependencies, and other information useful to attackers. Clients should receive controlled error responses."
    },

    {
        "question": "How would you prevent sensitive information from appearing in Node.js logs?",
        "expected_answer": "I would avoid logging passwords, tokens, session identifiers, and unnecessary personal data, and use structured logging with appropriate redaction."
    },

    {
        "question": "What is structured logging?",
        "expected_answer": "Structured logging stores log information in a consistent machine-readable format, such as JSON, making logs easier to search, analyze, and correlate."
    },

    {
        "question": "What security risks should be considered when accepting user input in Node.js?",
        "expected_answer": "Important risks include injection attacks, path traversal, prototype pollution, command injection, unsafe file handling, malformed data, and denial-of-service conditions."
    },

    {
        "question": "What is command injection in Node.js?",
        "expected_answer": "Command injection occurs when untrusted input is incorporated into operating-system commands in an unsafe way, allowing unintended commands to execute."
    },

    {
        "question": "How can command injection be prevented in Node.js?",
        "expected_answer": "Avoid constructing shell commands from untrusted input, validate and restrict inputs, prefer direct process APIs when possible, and use safe argument handling."
    },

    {
        "question": "What is path traversal?",
        "expected_answer": "Path traversal is an attack where crafted paths such as ../ are used to access files outside the intended directory."
    },

    {
        "question": "How can path traversal be prevented?",
        "expected_answer": "Validate and normalize paths, restrict access to an intended directory, reject unsafe path components, and verify that the resolved path remains inside the allowed location."
    },

    {
        "question": "What is prototype pollution in JavaScript?",
        "expected_answer": "Prototype pollution occurs when an attacker modifies object prototypes through unsafe object manipulation, potentially changing behavior across many objects."
    },

    {
        "question": "How can a Node.js application reduce prototype pollution risks?",
        "expected_answer": "Use maintained dependencies, validate input, avoid unsafe deep-merging of untrusted objects, and restrict dangerous property names and object manipulation."
    },

    {
        "question": "What is SSRF and how can a Node.js application be affected by it?",
        "expected_answer": "SSRF occurs when a server is tricked into making requests to unintended destinations. A Node.js application that fetches user-controlled URLs can be vulnerable."
    },

    {
        "question": "How can SSRF be mitigated?",
        "expected_answer": "Validate destination URLs, restrict allowed hosts and protocols, block internal network ranges where appropriate, and avoid blindly requesting user-provided URLs."
    },

    {
        "question": "How would you securely implement file uploads in Node.js?",
        "expected_answer": "Validate file size and type, restrict filenames and paths, store files outside executable locations when appropriate, generate safe names, and scan or process files as required."
    },

    {
        "question": "How should passwords be stored in a Node.js application?",
        "expected_answer": "Passwords should be stored using a strong password-hashing algorithm such as Argon2 or bcrypt with appropriate parameters and salts. Plain-text passwords should never be stored."
    },

    {
        "question": "How can JWT-based authentication be made safer?",
        "expected_answer": "Use strong signing keys, validate signatures and claims, keep token lifetimes appropriate, protect refresh tokens, rotate or revoke credentials when necessary, and avoid storing sensitive data in JWT payloads."
    },

    {
        "question": "What is token rotation?",
        "expected_answer": "Token rotation replaces a refresh token with a new one when it is used, allowing suspicious reuse of an old token to be detected or rejected."
    },

    {
        "question": "What is the difference between authentication and authorization in a secure API?",
        "expected_answer": "Authentication verifies who the user is, while authorization determines what that authenticated user is allowed to access or perform."
    },

    {
        "question": "How would you protect an API from brute-force attacks?",
        "expected_answer": "Use rate limiting, account or IP controls where appropriate, strong password policies, monitoring, progressive delays or temporary blocking, and secure authentication mechanisms."
    },

    {
        "question": "What is an idempotent API operation?",
        "expected_answer": "An idempotent operation can be performed multiple times with the same intended result as performing it once, which is useful when safely retrying requests."
    },

    {
        "question": "Why are idempotency keys useful in APIs?",
        "expected_answer": "They allow a server to recognize repeated requests and avoid performing the same operation multiple times, which is useful for retrying operations such as payments."
    },

    {
        "question": "How would you implement request timeouts in Node.js?",
        "expected_answer": "I would configure appropriate timeouts for incoming requests and outgoing network calls so stalled operations do not consume resources indefinitely."
    },

    {
        "question": "Why should outgoing HTTP requests have timeouts?",
        "expected_answer": "Without timeouts, a slow or unavailable dependency can keep resources occupied for too long and reduce application capacity."
    },

    {
        "question": "How should a Node.js service handle temporary failures from another service?",
        "expected_answer": "It can use bounded retries with backoff, timeouts, circuit breakers, and appropriate fallback behavior while avoiding uncontrolled retry storms."
    },

    {
        "question": "What is exponential backoff?",
        "expected_answer": "Exponential backoff increases the delay between retries, reducing pressure on an overloaded or temporarily unavailable service."
    },

    {
        "question": "What is a circuit breaker pattern?",
        "expected_answer": "A circuit breaker temporarily stops calls to a failing dependency after repeated failures, allowing the dependency and application to recover before calls resume."
    },

    {
        "question": "How would you make a Node.js API resilient to database failures?",
        "expected_answer": "Use connection pooling, timeouts, transactions where needed, bounded retries for safe operations, clear error handling, health checks, monitoring, and graceful degradation where possible."
    },

    {
        "question": "What is database connection pooling?",
        "expected_answer": "Connection pooling maintains reusable database connections so requests do not need to establish a new connection for every operation."
    },

    {
        "question": "Why can creating a new database connection for every request be a problem?",
        "expected_answer": "Connection creation adds overhead and can exhaust database or application resources when request volume increases."
    },

    {
        "question": "How would you prevent a Node.js application from exhausting its database connection pool?",
        "expected_answer": "Configure appropriate pool limits, release connections correctly, avoid unnecessarily long transactions, monitor pool usage, and investigate slow queries."
    },

    {
        "question": "What is graceful shutdown in a production Node.js service?",
        "expected_answer": "Graceful shutdown stops accepting new work, allows active requests to finish when possible, closes connections and resources, and then terminates the process."
    },

    {
        "question": "Why is graceful shutdown important during deployment?",
        "expected_answer": "It reduces dropped requests and incomplete operations when application instances are restarted, replaced, or deployed."
    },

    {
        "question": "How should a Node.js application respond to SIGTERM?",
        "expected_answer": "The application should begin graceful shutdown, stop accepting new work, finish or safely cancel active operations, close resources, and exit within a controlled timeout."
    },

    {
        "question": "What is a health-check endpoint in a production Node.js service?",
        "expected_answer": "A health-check endpoint reports whether the service is functioning sufficiently for a load balancer or orchestrator to make routing or restart decisions."
    },

    {
        "question": "What is the difference between liveness and readiness checks?",
        "expected_answer": "Liveness indicates whether the process should remain running, while readiness indicates whether the service is currently ready to receive traffic."
    },

    {
        "question": "Why should readiness checks change during graceful shutdown?",
        "expected_answer": "The service should become unready so new traffic is stopped or reduced while existing requests are allowed to finish."
    },

    {
        "question": "How would you design a Node.js service for observability?",
        "expected_answer": "I would use structured logs, metrics, traces, request identifiers, health checks, error monitoring, and measurements such as latency, throughput, CPU, memory, and event-loop delay."
    },

    {
        "question": "What is distributed tracing?",
        "expected_answer": "Distributed tracing follows a request across multiple services and records timing and relationships between operations, helping identify where latency or failures occur."
    },

    {
        "question": "What is a correlation ID?",
        "expected_answer": "A correlation ID is an identifier attached to related requests and logs so activity belonging to one operation can be traced across components."
    },

    {
        "question": "How would you prevent duplicate processing in a Node.js message consumer?",
        "expected_answer": "Use idempotent processing, unique identifiers, deduplication records, appropriate transaction boundaries, and acknowledgment only after successful processing."
    },

    {
        "question": "What is the difference between at-most-once and at-least-once message delivery?",
        "expected_answer": "At-most-once avoids duplicate delivery but may lose messages, while at-least-once aims to avoid loss but may deliver a message more than once."
    },

    {
        "question": "Why must consumers be idempotent with at-least-once delivery?",
        "expected_answer": "Because the same message may be delivered multiple times, repeated processing must not incorrectly apply the operation multiple times."
    },

    {
        "question": "What is the purpose of a message queue in a Node.js architecture?",
        "expected_answer": "A message queue decouples producers from consumers and allows work to be processed asynchronously, improving resilience and controlling workload spikes."
    },

    {
        "question": "How would you handle a sudden traffic spike in a Node.js application?",
        "expected_answer": "I would use load balancing, horizontal scaling, caching, connection limits, queues for background work, rate limiting, and monitoring while identifying the main bottleneck."
    },

    {
        "question": "What is load shedding?",
        "expected_answer": "Load shedding intentionally rejects or defers some work when a system is overloaded so that critical operations can continue and the system remains responsive."
    },

    {
        "question": "What is caching and what consistency problem can it create?",
        "expected_answer": "Caching stores reusable data closer to consumers to reduce latency and load. The challenge is keeping cached data sufficiently consistent with the underlying source."
    },

    {
        "question": "How can cache invalidation be handled?",
        "expected_answer": "Common approaches include expiration times, explicit invalidation after writes, versioned keys, write-through strategies, or cache-aside patterns."
    },

    {
        "question": "What is the cache-aside pattern?",
        "expected_answer": "The application first checks the cache, reads from the database on a miss, and then stores the retrieved result in the cache."
    },

    {
        "question": "How would you prevent a cache stampede?",
        "expected_answer": "Use techniques such as randomized expiration, request coalescing, locking, prewarming, or controlled refresh so many requests do not regenerate the same expired data simultaneously."
    },

    {
        "question": "How would you design a real-time feature in Node.js?",
        "expected_answer": "Depending on requirements, I might use WebSockets or Server-Sent Events, manage connection state carefully, handle reconnection, authenticate clients, and scale connection handling appropriately."
    },

    {
        "question": "What is the difference between WebSockets and Server-Sent Events?",
        "expected_answer": "WebSockets provide bidirectional communication, while Server-Sent Events primarily provide a persistent server-to-client event stream over HTTP."
    },

    {
        "question": "How would you secure a WebSocket connection?",
        "expected_answer": "Authenticate the connection, authorize actions, validate messages, enforce size and rate limits, use secure transport, and close connections that violate security rules."
    },

    {
        "question": "How would you test a Node.js application under high load?",
        "expected_answer": "I would use load-testing tools to generate realistic traffic and monitor latency, throughput, errors, CPU, memory, database usage, and event-loop delay."
    },

    {
        "question": "What is the difference between throughput and latency in a Node.js API?",
        "expected_answer": "Throughput measures how much work the system completes over time, while latency measures how long an individual request or operation takes."
    },

    {
        "question": "How would you optimize a slow Node.js API?",
        "expected_answer": "I would measure first, then investigate database queries, external calls, CPU-heavy code, event-loop blocking, serialization, network latency, caching, and unnecessary work."
    },

    {
        "question": "What is zero-downtime deployment?",
        "expected_answer": "Zero-downtime deployment updates application instances while maintaining service availability, commonly by gradually replacing or updating instances behind a load balancer."
    },

    {
        "question": "What should a Node.js application do when an unexpected fatal error occurs?",
        "expected_answer": "It should record useful diagnostic information, avoid continuing in an unsafe state, perform necessary cleanup when possible, and allow a supervisor or orchestrator to restart it."
    },

    {
        "question": "Why should uncaught exceptions not simply be ignored?",
        "expected_answer": "They can leave the application in an unknown or inconsistent state. Continuing blindly may cause incorrect behavior or data corruption."
    },

    {
        "question": "How would you structure a large Node.js application?",
        "expected_answer": "I would separate concerns such as routes, controllers, services, data access, validation, configuration, middleware, and infrastructure while keeping dependencies manageable and testable."
    },

    {
        "question": "What is dependency injection and why can it help Node.js applications?",
        "expected_answer": "Dependency injection supplies required dependencies from outside a component, making code easier to test, replace, and maintain."
    },

    {
        "question": "How would you safely manage configuration across development, testing, and production?",
        "expected_answer": "Use environment-specific configuration, environment variables or a secure configuration system, validation at startup, and separate secrets from source code."
    },

    {
        "question": "How would you investigate a Node.js application that crashes intermittently in production?",
        "expected_answer": "I would inspect logs, crash reports, memory and CPU metrics, unhandled errors, dependency failures, resource limits, recent deployments, and reproduce the failure using production-like conditions."
    },

    {
        "question": "How would you design a Node.js API to remain reliable when a dependency becomes slow?",
        "expected_answer": "Use timeouts, bounded concurrency, circuit breakers, limited retries with backoff, caching where appropriate, and fallback or degraded behavior for non-critical operations."
    },

    {
        "question": "What is bounded concurrency?",
        "expected_answer": "Bounded concurrency limits how many asynchronous operations run simultaneously, preventing uncontrolled work from exhausting CPU, memory, connections, or other resources."
    },

    {
        "question": "Why can Promise.all() be dangerous with a very large number of operations?",
        "expected_answer": "Starting too many operations simultaneously can consume excessive memory, connections, CPU, or external-service capacity. Bounded concurrency may be safer."
    },

    {
        "question": "How would you process one million records efficiently in Node.js?",
        "expected_answer": "I would process records in batches or streams, use bounded concurrency, avoid loading everything into memory, optimize database access, and monitor resource usage."
    },

    {
        "question": "How would you safely retry a failed API request?",
        "expected_answer": "Use timeouts, a limited retry count, exponential backoff with jitter, and retry only operations and errors that are safe or explicitly designed to be retried."
    },

    {
        "question": "What is retry jitter and why is it useful?",
        "expected_answer": "Jitter adds controlled randomness to retry delays, reducing the chance that many clients retry at exactly the same time."
    },

    {
        "question": "What is graceful degradation?",
        "expected_answer": "Graceful degradation means reducing or disabling non-critical functionality when dependencies or resources fail while keeping essential functionality available."
    },

    {
        "question": "How would you design a production-ready Node.js API?",
        "expected_answer": "I would include validation, authentication and authorization, centralized errors, timeouts, rate limiting, logging, metrics, health checks, secure configuration, database controls, testing, and graceful shutdown."
    }

]
    
}