# Refactor berserker project into TypeScript web interpreter

1. Initialize a Vite + TypeScript project and move existing Python source into a `static` directory for reference.
2. Implement a web-based pseudo terminal that mimics the Python interactive interpreter, rendering output inside a DOM text area and capturing keyboard input.
3. Provide dynamic loading of game logic from the `static` directory based on user selections during the name/class selection phase.
4. Add localStorage-based state management for persisting user session and game data between refreshes.
5. Integrate Google OIDC login flow for user authentication.
6. Remove ORM-style patterns; keep only native JavaScript/TypeScript constructs.
7. Ensure all JavaScript/TypeScript resides in the `static` directory and is loaded dynamically at runtime.
8. Provide build scripts via Vite and update project documentation.
