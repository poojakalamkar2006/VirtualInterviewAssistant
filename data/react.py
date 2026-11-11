questions = {

    "Easy": [

        {
            "question": "What is React?",
            "expected_answer": "React is a JavaScript library developed by Meta for building interactive user interfaces using reusable components."
        },

        {
            "question": "Why is React used?",
            "expected_answer": "React is used to build interactive and maintainable user interfaces by organizing the UI into reusable components."
        },

        {
            "question": "Is React a programming language?",
            "expected_answer": "No. React is a JavaScript library used mainly for building user interfaces."
        },

        {
            "question": "What is a React component?",
            "expected_answer": "A component is a reusable piece of UI that can contain its own structure, logic, and behavior."
        },

        {
            "question": "What is a functional component?",
            "expected_answer": "A functional component is a JavaScript function that returns React elements describing what should appear on the screen."
        },

        {
            "question": "What is JSX?",
            "expected_answer": "JSX is a JavaScript syntax extension that allows developers to write HTML-like markup inside JavaScript."
        },

        {
            "question": "Why is JSX used in React?",
            "expected_answer": "JSX makes React UI code easier to read by allowing markup and JavaScript logic to be written together."
        },

        {
            "question": "Can browsers directly understand JSX?",
            "expected_answer": "No. JSX must be transformed into regular JavaScript by a build tool before the browser can execute it."
        },

        {
            "question": "What is a React element?",
            "expected_answer": "A React element is an object describing what should be rendered in the user interface."
        },

        {
            "question": "What are props in React?",
            "expected_answer": "Props are read-only values passed from a parent component to a child component."
        },

        {
            "question": "Can a component modify its props?",
            "expected_answer": "No. Props should be treated as read-only by the component receiving them."
        },

        {
            "question": "What is state in React?",
            "expected_answer": "State is data managed by a component that can change over time and cause the component to render again."
        },

        {
            "question": "What is useState?",
            "expected_answer": "useState is a React Hook that allows functional components to create and update state."
        },

        {
            "question": "What does useState return?",
            "expected_answer": "useState returns the current state value and a function that can be used to update that state."
        },

        {
            "question": "What is the difference between props and state?",
            "expected_answer": "Props are passed into a component by its parent, while state is managed by the component and can change over time."
        },

        {
            "question": "What is a React Hook?",
            "expected_answer": "A Hook is a React function that allows functional components to use features such as state, effects, and context."
        },

        {
            "question": "What is useEffect?",
            "expected_answer": "useEffect is a React Hook used to synchronize a component with external systems such as APIs, timers, or event listeners."
        },

        {
            "question": "What is useRef?",
            "expected_answer": "useRef stores a mutable value that persists between renders without causing a re-render when the value changes."
        },

        {
            "question": "What is conditional rendering?",
            "expected_answer": "Conditional rendering means displaying different UI depending on whether a condition is true or false."
        },

        {
            "question": "How do you render a list in React?",
            "expected_answer": "Lists are commonly rendered using JavaScript's map() method to create React elements for each item."
        },

        {
            "question": "Why are keys used in React lists?",
            "expected_answer": "Keys help React identify individual list items so it can efficiently update, add, or remove them."
        },

        {
            "question": "What makes a good key in React?",
            "expected_answer": "A good key is stable and unique among the items in the same list, such as a database ID."
        },

        {
            "question": "What is the virtual DOM?",
            "expected_answer": "The virtual DOM is an in-memory representation of the UI that React uses to determine necessary updates to the actual DOM."
        },

        {
            "question": "What is reconciliation in React?",
            "expected_answer": "Reconciliation is the process React uses to compare the previous and new UI descriptions and determine what needs to be updated."
        },

        {
            "question": "What is the DOM?",
            "expected_answer": "The DOM is the browser's object representation of an HTML document that JavaScript can access and modify."
        },

        {
            "question": "What is event handling in React?",
            "expected_answer": "Event handling in React uses event props such as onClick, onChange, and onSubmit to respond to user actions."
        },

        {
            "question": "What is the onClick event?",
            "expected_answer": "The onClick event is used to run a function when a user clicks an element such as a button."
        },

        {
            "question": "What is the onChange event?",
            "expected_answer": "The onChange event is commonly used to detect changes in form controls such as input fields and select elements."
        },

        {
            "question": "What is a controlled component?",
            "expected_answer": "A controlled component is a form element whose value is controlled by React state."
        },

        {
            "question": "What is an uncontrolled component?",
            "expected_answer": "An uncontrolled component stores its current value in the DOM rather than directly controlling it with React state."
        },

        {
            "question": "What is a React Fragment?",
            "expected_answer": "A React Fragment allows multiple elements to be returned without adding an unnecessary DOM element."
        },

        {
            "question": "What is the purpose of <>...</> in React?",
            "expected_answer": "The <>...</> syntax is shorthand for a React Fragment and lets multiple elements be returned without an extra DOM wrapper."
        },

        {
            "question": "What is lifting state up?",
            "expected_answer": "Lifting state up means moving shared state to the nearest common parent so multiple child components can use it."
        },

        {
            "question": "What is prop drilling?",
            "expected_answer": "Prop drilling means passing props through multiple components just to reach a deeply nested component."
        },

        {
            "question": "What is React Context?",
            "expected_answer": "React Context allows values to be shared with components at different levels without passing props through every intermediate component."
        },

        {
            "question": "What is createContext?",
            "expected_answer": "createContext creates a Context object that can be used to provide and consume shared values in a React component tree."
        },

        {
            "question": "What is a Context Provider?",
            "expected_answer": "A Context Provider supplies a value to components below it in the React component tree."
        },

        {
            "question": "What is React Router?",
            "expected_answer": "React Router is a library commonly used to handle navigation and URL-based routing in React applications."
        },

        {
            "question": "What is a single-page application?",
            "expected_answer": "A single-page application loads the main application once and dynamically updates its UI as the user navigates."
        },

        {
            "question": "How can React call an API?",
            "expected_answer": "React can call APIs using fetch(), Axios, or other HTTP libraries, commonly from an effect or a data-fetching solution."
        },

        {
            "question": "What is fetch()?",
            "expected_answer": "fetch() is a browser API used to make HTTP requests and retrieve data from servers."
        },

        {
            "question": "What is a React form?",
            "expected_answer": "A React form is a form whose input values, validation, and submission can be managed using React components and event handlers."
        },

        {
            "question": "What is the onSubmit event?",
            "expected_answer": "The onSubmit event is used to handle form submission and can be used to validate or send form data."
        },

        {
            "question": "What is React.StrictMode?",
            "expected_answer": "StrictMode is a development feature that helps identify potential problems and unsafe patterns in React applications."
        },

        {
            "question": "What is npm?",
            "expected_answer": "npm is a package manager for JavaScript that is commonly used to install dependencies and run project scripts."
        },

        {
            "question": "What is package.json?",
            "expected_answer": "package.json contains information about a JavaScript project, including dependencies, scripts, and project metadata."
        },

        {
            "question": "What is ReactDOM?",
            "expected_answer": "ReactDOM provides APIs that allow React applications to interact with and render into the browser DOM."
        },

        {
            "question": "What is createRoot()?",
            "expected_answer": "createRoot() creates a React root connected to a DOM element and is used to render a React application."
        },

        {
            "question": "What is component re-rendering?",
            "expected_answer": "A component re-renders when React needs to calculate its UI again because relevant state, props, context, or another update has changed."
        },

        {
            "question": "What is the difference between React and JavaScript?",
            "expected_answer": "JavaScript is a programming language, while React is a JavaScript library mainly used to build user interfaces."
        },

        {
            "question": "What is the difference between React and HTML?",
            "expected_answer": "HTML defines the structure of web content, while React is a JavaScript library used to create dynamic and reusable user interfaces."
        },

        {
            "question": "What is a reusable component?",
            "expected_answer": "A reusable component is a component designed to be used in multiple places with different data or configuration."
        }

    ],

  #  Medium

      "Medium": [

    {
        "question": "What is the difference between props and state in React?",
        "expected_answer": "Props are read-only values passed from a parent component, while state is data managed by a component that can change over time and cause re-rendering."
    },

    {
        "question": "What happens when state changes in React?",
        "expected_answer": "When state changes, React schedules the component to re-render so the UI can reflect the new state."
    },

    {
        "question": "Why should state not be modified directly?",
        "expected_answer": "Direct mutation can prevent React from detecting changes correctly and can lead to unpredictable UI behavior. State should be updated using its setter or appropriate state-management method."
    },

    {
        "question": "What is the functional form of setState?",
        "expected_answer": "The functional form receives the previous state and calculates the next state, such as setCount(prev => prev + 1). It is useful when the new state depends on the previous state."
    },

    {
        "question": "Why does React batch state updates?",
        "expected_answer": "React batches multiple state updates to reduce unnecessary renders and improve performance."
    },

    {
        "question": "What is the difference between useState and useReducer?",
        "expected_answer": "useState is convenient for simple state, while useReducer is useful when state transitions are more complex or depend on multiple related actions."
    },

    {
        "question": "How does useReducer work?",
        "expected_answer": "useReducer manages state through a reducer function that receives the current state and an action and returns the next state."
    },

    {
        "question": "What is a reducer function in React?",
        "expected_answer": "A reducer is a function that determines the next state based on the current state and an action."
    },

    {
        "question": "What is useEffect used for?",
        "expected_answer": "useEffect is used to synchronize a component with external systems such as APIs, subscriptions, timers, or browser APIs."
    },

    {
        "question": "What is the dependency array in useEffect?",
        "expected_answer": "The dependency array tells React when an effect should be re-run based on changes to the specified reactive values."
    },

    {
        "question": "What happens if useEffect has an empty dependency array?",
        "expected_answer": "The effect does not re-run because of dependency changes. In common cases it runs after the initial mount, with cleanup when the component is removed."
    },

    {
        "question": "What is cleanup in useEffect?",
        "expected_answer": "Cleanup is a function returned from an effect to remove subscriptions, timers, event listeners, or other resources when the effect is re-synchronized or the component is removed."
    },

    {
        "question": "Can useEffect return a value other than a cleanup function?",
        "expected_answer": "No. An effect callback should return either nothing or a cleanup function. It should not return arbitrary values."
    },

    {
        "question": "What is useMemo?",
        "expected_answer": "useMemo caches the result of a calculation between renders until its dependencies change. It can avoid expensive recalculations when used appropriately."
    },

    {
        "question": "What is useCallback?",
        "expected_answer": "useCallback caches a function reference between renders until its dependencies change. It can help when function identity affects child rendering or another dependency."
    },

    {
        "question": "What is the difference between useMemo and useCallback?",
        "expected_answer": "useMemo memoizes a calculated value, while useCallback memoizes a function reference."
    },

    {
        "question": "What is React.memo?",
        "expected_answer": "React.memo can skip re-rendering a component when its props have not changed according to its comparison."
    },

    {
        "question": "When should React.memo be used?",
        "expected_answer": "It should be used when preventing unnecessary renders provides a measurable benefit, especially for components that render often with unchanged props."
    },

    {
        "question": "What is prop drilling?",
        "expected_answer": "Prop drilling means passing data through several intermediate components only so that a deeply nested component can receive it."
    },

    {
        "question": "How can prop drilling be reduced?",
        "expected_answer": "Prop drilling can be reduced using Context, component composition, or an appropriate state-management solution."
    },

    {
        "question": "What is the React Context API?",
        "expected_answer": "Context provides a way to make values available to components deeper in the tree without passing them through every intermediate component."
    },

    {
        "question": "What are the disadvantages of using Context?",
        "expected_answer": "Context can make data flow less explicit and broad context updates can cause many consumers to re-render. It should be used for suitable shared values rather than all application state."
    },

    {
        "question": "What is a custom Hook?",
        "expected_answer": "A custom Hook is a reusable JavaScript function whose name starts with use and that can call other Hooks to share stateful logic between components."
    },

    {
        "question": "Why are custom Hooks useful?",
        "expected_answer": "Custom Hooks allow reusable stateful logic to be extracted from components without duplicating the same logic."
    },

    {
        "question": "What are the Rules of Hooks?",
        "expected_answer": "Hooks should be called only at the top level of React functions and only from React function components or custom Hooks."
    },

    {
        "question": "Why can't Hooks normally be called inside loops or conditions?",
        "expected_answer": "React relies on the consistent order of Hook calls to associate Hook state correctly with each component render."
    },

    {
        "question": "What is lifting state up?",
        "expected_answer": "Lifting state up means moving shared state to the closest common parent so multiple child components can use the same source of truth."
    },

    {
        "question": "What is derived state?",
        "expected_answer": "Derived state is information that can be calculated from existing props or state. It is usually better calculated during rendering rather than stored separately."
    },

    {
        "question": "Why should unnecessary derived state be avoided?",
        "expected_answer": "Storing values that can be calculated from existing data can create duplicated state and synchronization bugs."
    },

    {
        "question": "What is conditional rendering in React?",
        "expected_answer": "Conditional rendering means displaying different elements or components based on conditions using JavaScript expressions such as if, ternary operators, or logical operators."
    },

    {
        "question": "How do you render a list of components in React?",
        "expected_answer": "A list is commonly rendered using JavaScript methods such as map(), with each rendered item receiving a stable key."
    },

    {
        "question": "Why are keys important when rendering lists?",
        "expected_answer": "Keys help React identify which list items correspond to which components so it can update the UI efficiently when items are added, removed, or reordered."
    },

    {
        "question": "Why is using array index as a key sometimes problematic?",
        "expected_answer": "If list items are inserted, removed, or reordered, indexes can change and cause React to associate component state with the wrong item."
    },

    {
        "question": "What is reconciliation in React?",
        "expected_answer": "Reconciliation is React's process of comparing the previous rendered tree with the new one and determining the necessary UI updates."
    },

    {
        "question": "What is the virtual DOM?",
        "expected_answer": "The virtual DOM is an in-memory representation of UI elements that React uses as part of its rendering process to determine updates efficiently."
    },

    {
        "question": "Does React update the real DOM after every state change?",
        "expected_answer": "React re-renders the affected component tree and commits the necessary changes to the real DOM rather than blindly replacing the entire DOM."
    },

    {
        "question": "What causes a React component to re-render?",
        "expected_answer": "A component can re-render because its state changes, its parent renders with changed props, a consumed context value changes, or another subscribed external value changes."
    },

    {
        "question": "Does a parent re-render always mean every child must update the DOM?",
        "expected_answer": "No. React may re-render child components during reconciliation, but it commits only the necessary DOM changes. Memoization can also skip some child renders."
    },

    {
        "question": "What is a controlled component?",
        "expected_answer": "A controlled form component gets its current value from React state and updates that state through event handlers."
    },

    {
        "question": "What is an uncontrolled component?",
        "expected_answer": "An uncontrolled component stores its current form value in the DOM itself, commonly accessed using a ref."
    },

    {
        "question": "When should controlled components be preferred?",
        "expected_answer": "Controlled components are useful when React needs to validate, transform, conditionally display, or otherwise coordinate form values."
    },

    {
        "question": "What is the difference between controlled and uncontrolled forms?",
        "expected_answer": "Controlled forms keep input values in React state, while uncontrolled forms let the DOM maintain the values and React accesses them when needed."
    },

    {
        "question": "How do you handle multiple form inputs in React?",
        "expected_answer": "A common approach is to keep the values in an object and update the appropriate property using the input's name and value."
    },

    {
        "question": "How do you handle form submission in React?",
        "expected_answer": "Use an onSubmit handler on the form, call preventDefault() when appropriate, validate the data, and then perform the required action."
    },

    {
        "question": "How do you fetch API data in React?",
        "expected_answer": "API data can be fetched using fetch or another HTTP client, commonly inside an effect or through a framework-specific data-fetching mechanism."
    },

    {
        "question": "How should loading and error states be handled during API calls?",
        "expected_answer": "The UI should maintain clear loading, success, and error states so users know whether data is being fetched, displayed, or failed."
    },

    {
        "question": "Why can an API request inside useEffect cause stale data problems?",
        "expected_answer": "Multiple requests can finish in a different order from when they started, allowing an older response to overwrite newer data."
    },

    {
        "question": "How can an API request be cancelled in React?",
        "expected_answer": "With APIs that support it, an AbortController can be used to cancel an unnecessary request during cleanup or when a newer request replaces it."
    },

    {
        "question": "What is React Router used for?",
        "expected_answer": "React Router provides client-side routing so applications can display different components for different URLs without requiring a full page reload."
    },

    {
        "question": "What is a single-page application?",
        "expected_answer": "A single-page application loads the main application page and then updates the displayed UI dynamically as users navigate or interact with it."
    },

    {
        "question": "What is lazy loading in React?",
        "expected_answer": "Lazy loading allows a component or module to be loaded only when it is needed, commonly using React.lazy and Suspense."
    },

    {
        "question": "What is React Suspense?",
        "expected_answer": "Suspense lets React display a fallback UI while certain child content, such as a lazy-loaded component, is not yet ready."
    },

    {
        "question": "What is code splitting?",
        "expected_answer": "Code splitting divides application JavaScript into smaller chunks so users do not have to download all application code at once."
    },

    {
        "question": "How can React application performance be improved?",
        "expected_answer": "Performance can be improved by reducing unnecessary renders, optimizing expensive calculations, lazy-loading code, using stable keys, and avoiding unnecessary state."
    },

    {
        "question": "What is component composition in React?",
        "expected_answer": "Component composition means building complex interfaces by combining smaller components and passing content or behavior through props such as children."
    },

    {
        "question": "What is the children prop in React?",
        "expected_answer": "The children prop contains the content placed between a component's opening and closing tags and allows components to compose nested UI."
    },

    {
        "question": "What is the difference between state management and UI state?",
        "expected_answer": "UI state controls interface details such as open menus or selected tabs, while broader application state may represent data shared across multiple parts of an application."
    },

    {
        "question": "When should state be moved to a common parent?",
        "expected_answer": "State should be moved to a common parent when multiple components need to read or update the same piece of information."
    },

    {
        "question": "What is an error boundary in React?",
        "expected_answer": "An error boundary is a component that catches rendering errors in its child component tree and displays fallback UI instead of allowing the entire UI to fail."
    },

    {
        "question": "Can error boundaries catch errors from event handlers?",
        "expected_answer": "No. Error boundaries do not automatically catch errors from event handlers, asynchronous callbacks, or server-side code. Those errors need separate handling."
    },

    {
        "question": "What is StrictMode used for?",
        "expected_answer": "StrictMode enables additional development-time checks that help identify unsafe patterns and potential problems in React applications."
    },

    {
        "question": "What is the purpose of React DevTools?",
        "expected_answer": "React DevTools helps developers inspect component trees, props, state, and performance information while debugging React applications."
    }

],

#Hard

    "Hard": [

    {
        "question": "How does React reconciliation work internally at a high level?",
        "expected_answer": "React compares the newly returned element tree with the previous one and determines which parts need to be updated during the commit phase."
    },

    {
        "question": "What is the difference between the render phase and commit phase?",
        "expected_answer": "The render phase calculates what the UI should look like, while the commit phase applies the required changes to the DOM and runs appropriate effects."
    },

    {
        "question": "Why must React rendering be kept free of side effects?",
        "expected_answer": "React may render components multiple times or abandon a render before committing it. Side effects during rendering can therefore execute unexpectedly."
    },

    {
        "question": "What is concurrent rendering in React?",
        "expected_answer": "Concurrent rendering allows React to work on rendering without blocking the main thread for the entire operation and enables React to prioritize more important updates."
    },

    {
        "question": "What is a transition in React?",
        "expected_answer": "A transition marks an update as non-urgent so React can prioritize urgent interactions such as typing or clicking while rendering the transition in the background."
    },

    {
        "question": "What does startTransition do?",
        "expected_answer": "startTransition marks state updates inside its callback as non-urgent transition updates."
    },

    {
        "question": "What is useTransition?",
        "expected_answer": "useTransition provides a way to mark updates as transitions and gives the component an isPending value for displaying pending UI."
    },

    {
        "question": "What is useDeferredValue?",
        "expected_answer": "useDeferredValue lets a non-critical value update later so urgent UI interactions can remain responsive."
    },

    {
        "question": "What is the difference between useTransition and useDeferredValue?",
        "expected_answer": "useTransition marks a state update as non-urgent, while useDeferredValue lets a derived value lag behind an urgent value."
    },

    {
        "question": "Why can React render a component more than once?",
        "expected_answer": "Rendering can occur because of state or prop changes, parent renders, context changes, development checks, or concurrent rendering work."
    },

    {
        "question": "Why can StrictMode make a component appear to render twice in development?",
        "expected_answer": "StrictMode performs additional development-only checks that can invoke rendering and effect setup more than once to expose unsafe side effects."
    },

    {
        "question": "What is referential equality in React?",
        "expected_answer": "Referential equality compares whether two values are the same object or function reference rather than whether their contents are structurally equal."
    },

    {
        "question": "Why can inline objects cause unnecessary React re-renders?",
        "expected_answer": "A new object is created on every render, so its reference changes even when its contents are identical. Memoized children may therefore re-render."
    },

    {
        "question": "Why can inline functions cause unnecessary re-renders?",
        "expected_answer": "A new function reference is normally created on each render, which can cause memoized child components to receive changed props."
    },

    {
        "question": "When can useCallback make performance worse?",
        "expected_answer": "useCallback adds memoization overhead and complexity. Using it unnecessarily can make code harder to understand without providing a meaningful performance benefit."
    },

    {
        "question": "When can useMemo make performance worse?",
        "expected_answer": "useMemo has its own memory and comparison overhead. It can add complexity when the calculation is already inexpensive."
    },

    {
        "question": "How would you investigate unnecessary React re-renders?",
        "expected_answer": "Use React DevTools Profiler, inspect state and prop changes, check context updates, and identify unstable object or function references."
    },

    {
        "question": "What is the React Profiler used for?",
        "expected_answer": "The Profiler helps measure component rendering behavior and identify components or interactions that contribute significantly to rendering time."
    },

    {
        "question": "What is state colocation?",
        "expected_answer": "State colocation means keeping state as close as possible to the components that actually need it instead of placing all state at the application root."
    },

    {
        "question": "Why is state colocation useful for performance?",
        "expected_answer": "Keeping state local limits the number of components affected by updates and can reduce unnecessary rendering."
    },

    {
        "question": "How would you design state for a large React application?",
        "expected_answer": "Keep local UI state local, lift shared state only when necessary, use Context for suitable shared values, and use a dedicated state solution when application-wide state becomes complex."
    },

    {
        "question": "What is the difference between server state and client state?",
        "expected_answer": "Server state comes from remote systems and requires fetching, caching, synchronization, and error handling. Client state represents local application or UI information."
    },

    {
        "question": "Why should server data not always be stored directly in global React state?",
        "expected_answer": "Server data has concerns such as caching, refetching, synchronization, stale data, and request deduplication that are often better handled by specialized data-fetching tools."
    },

    {
        "question": "How can race conditions occur during React API requests?",
        "expected_answer": "If multiple requests are started before earlier ones finish, responses may arrive out of order and an older response can overwrite newer data."
    },

    {
        "question": "How can stale API responses be prevented?",
        "expected_answer": "Requests can be cancelled with AbortController, or the application can track request identity and ignore responses that are no longer current."
    },

    {
        "question": "How would you prevent setting state after an obsolete request finishes?",
        "expected_answer": "Use request cancellation or maintain a request identifier so only the latest active request is allowed to update the state."
    },

    {
        "question": "How should authentication state be handled in React?",
        "expected_answer": "Authentication state should have a clear source of truth, protected routes or authorization checks, loading handling, and secure token/session handling appropriate to the application."
    },

    {
        "question": "Why is storing sensitive authentication tokens in localStorage risky?",
        "expected_answer": "JavaScript running because of an XSS vulnerability can access localStorage. More secure architectures may use secure, HttpOnly cookies where appropriate."
    },

    {
        "question": "What is an XSS vulnerability in a React application?",
        "expected_answer": "XSS occurs when untrusted content is interpreted as executable code in the user's browser. React escapes normal text output, but unsafe APIs or injected HTML can reintroduce risk."
    },

    {
        "question": "Why is dangerouslySetInnerHTML dangerous?",
        "expected_answer": "It inserts HTML directly into the DOM and can create XSS vulnerabilities if the HTML contains untrusted or insufficiently sanitized content."
    },


    ]

}