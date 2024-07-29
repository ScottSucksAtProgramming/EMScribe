# Contributing

This guide provides instructions for contributing to EMScribe 2.0, including setting up the development environment, adding new features, and writing tests.

## Setting Up the Development Environment

Follow the steps in the [Development Guide](development.md) to set up your development environment. Ensure you are familiar with the new CLI module and understand the piping feature for chaining commands.

## Adding New Features

### Create a New Branch

Create a new branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

### Make Changes

Implement your feature in the appropriate module or create new modules as needed. Ensure your code follows the project's coding standards. If your feature involves the CLI, update the CLI module and add new commands or options as necessary.

### Write Tests

Write tests for your new feature in the `tests` directory. Ensure each test covers different scenarios and edge cases. Use `pytest` for testing. If your feature involves the CLI, include tests that verify the new commands or options.

### Commit Changes

Commit your changes with a clear and concise commit message:

```bash
git add .
git commit -m "Add feature: your feature description"
```

### Push the Branch and Create a Pull Request

Push your branch to the remote repository and create a pull request:

```bash
git push origin feature/your-feature-name
```

## Contribution Guidelines

### Code Style

- Follow PEP 8 for Python code style.
- Write clear, concise, and descriptive variable and function names.
- Include docstrings for all modules, classes, and functions.

### Commit Messages

- Use the imperative mood in the subject line.
- Capitalize the first letter of the subject line.
- Keep the subject line to 50 characters or less.
- Use the body to explain what and why vs. how.

### Pull Requests

- Provide a clear and detailed description of the changes in the pull request.
- Link to any relevant issues.
- Ensure all tests pass and there are no conflicts with the base branch.

## Documentation

Ensure your new features are well-documented. Update or add new documentation files in the `docs` directory as needed. Follow the existing documentation structure and style. If your feature involves the CLI, update the CLI documentation to include new commands or options.

## Conclusion

Following these guidelines will help maintain the quality and consistency of the EMScribe 2.0 codebase. For any questions or support, please contact [ScottSucks](https://github.com/ScottSucksAtProgramming).
