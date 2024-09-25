# Logger System

A customizable logging system that supports logging to multiple sinks such as file, console, and more. This project leverages modern design patterns to ensure extensibility, scalability, and maintainability.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Design Patterns](#design-patterns)
  - [Singleton Pattern](#singleton-pattern)
  - [Strategy Pattern](#strategy-pattern)
  - [Factory Pattern](#factory-pattern)
  - [Open-Closed Principle](#open-closed-principle)
- [Features](#features)
- [Usage](#usage)

---

## Getting Started

### Prerequisites

- Python 
- `pip` 
- Virtual environment support (recommended)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Himanshusingh038/logger-assignment.git
    cd logger-system
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

   To use the logger system in your project, follow this example:

   ```python
   from src.log.logger import Logger
   from src.log.enum import LogLevel
   from src.log.logger_config import LoggerConfig
   from src.log.sinks.file_sink import FileSink
   from src.log.sinks.console_sink import ConsoleSink

   # Define your sinks
   file_sink = FileSink(level=LogLevel.DEBUG, file_path='app.log', max_size_kb=100)
   console_sink = ConsoleSink(level=LogLevel.INFO)

   # Set up the logger configuration
   config = LoggerConfig(
       log_level=LogLevel.DEBUG,
       sinks=[file_sink, console_sink]
   )

   # Initialize the Logger
   logger = Logger(config=config)

   # Log some messages
   logger.log("This is a debug message", level=LogLevel.DEBUG, namespace="MyApp")
   logger.log("This is an info message", level=LogLevel.INFO, namespace="MyApp")

5. **Run tests:**
    ```bash
    python -m unittest discover tests/

    ```


Here’s the complete code for the README.md file:

markdown
Copy code
# Logger System

A customizable logging system that supports logging to multiple sinks such as file, console, and more. This project leverages modern design patterns to ensure extensibility, scalability, and maintainability.

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Design Patterns](#design-patterns)
  - [Singleton Pattern](#singleton-pattern)
  - [Strategy Pattern](#strategy-pattern)
  - [Factory Pattern](#factory-pattern)
  - [Open-Closed Principle](#open-closed-principle)
- [Features](#features)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)

---

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.7+
- `pip` package manager
- Virtual environment support (recommended)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/logger-system.git
    cd logger-system
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

   To use the logger system in your project, follow this example:

   ```python
   from src.log.logger import Logger
   from src.log.enum import LogLevel
   from src.log.logger_config import LoggerConfig
   from src.log.sinks.file_sink import FileSink
   from src.log.sinks.console_sink import ConsoleSink

   # Define your sinks
   file_sink = FileSink(level=LogLevel.DEBUG, file_path='app.log', max_size_kb=100)
   console_sink = ConsoleSink(level=LogLevel.INFO)

   # Set up the logger configuration
   config = LoggerConfig(
       log_level=LogLevel.DEBUG,
       sinks=[file_sink, console_sink]
   )

   # Initialize the Logger
   logger = Logger(config=config)

   # Log some messages
   logger.log("This is a debug message", level=LogLevel.DEBUG, namespace="MyApp")
   logger.log("This is an info message", level=LogLevel.INFO, namespace="MyApp")

5. **Run tests**:
```bash
python -m unittest discover tests/
```
# Project Structure
```bash
logger-system/
├── src/
│   ├── log/
│   │   ├── logger.py           # Core logger implementation
│   │   ├── logger_config.py    # Logger configuration class
│   │   ├── sinks/              # Log sinks (file, console, etc.)
│   │   └── enum/               # Enumerations for log levels, thread models, etc.
│   └── ...
├── tests/                      # Unit tests for the project
│   └── test_logger.py          # Logger unit tests
├── README.md                   # Project readme file
└── requirements.txt            # Python dependencies
```
## Design Patterns
This logging system is built using several important Object-Oriented Design Patterns to make the system scalable, flexible, and maintainable.

### Singleton Pattern
The Logger class uses the Singleton Pattern to ensure that only one instance of the logger exists throughout the application. This is crucial in a logging system because we want a unified log sink and avoid race conditions or duplicated instances writing to the same file concurrently.

```python
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance
```
### Strategy Pattern
The Strategy Pattern is used to separate how messages are logged. The system supports multiple logging strategies (or sinks), such as FileSink, ConsoleSink, and even future sinks like DatabaseSink. This pattern allows for easy extension of the logger by simply adding new sinks, without modifying the logger’s core logic.


```python
class FileSink:
    def write(self, message: Message):
        # Write the message to a file
        pass

class ConsoleSink:
    def write(self, message: Message):
        # Write the message to the console
        pass
```
The logger is decoupled from the specific logging mechanism, making it flexible and extensible.

### Factory Pattern
The logger configuration uses the Factory Pattern to dynamically create and configure sinks. This allows the logger to remain flexible, letting users specify different sinks and configurations at runtime without hardcoding log destinations.

#### Open-Closed Principle
The Open-Closed Principle states that software entities should be open for extension but closed for modification. The logger is designed so that new logging sinks can be easily added (e.g., email or network logging) without modifying the existing codebase.

Adding new sinks is as simple as creating a new class that implements the sink interface:

```python
class DatabaseSink:
    def write(self, message: Message):
        # Write the message to a database
        pass
```
### Features
- Supports multiple log levels: DEBUG, INFO, WARN, ERROR, FATAL
- Log rotation with configurable backup
- Asynchronous logging (multi-threading support)
- Extendable with custom sinks (e.g., file, console, database)
### Usage
You can configure and customize the logger by specifying the log level, log sinks, and other parameters through the LoggerConfig object. Here’s a quick overview of the log sinks:

**FileSink**: Writes logs to a file and supports log rotation based on size.
**ConsoleSink**: Outputs logs to the console (stdout).

**DatabaseSink**: logs into sqllite DB
