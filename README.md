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

5. **Run tests:**
    ```bash
    python -m unittest discover tests/

    ```