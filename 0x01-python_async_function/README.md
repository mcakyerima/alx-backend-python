## Asynchronous Python Tasks 🚀

This project encompasses tasks aimed at familiarizing oneself with asynchronous code in Python 3.

### Tasks Overview

#### 0. Understanding Async Basics
- **File**: `0-basic_async_syntax.py`
- **Description**: This file includes an asynchronous coroutine named `wait_random`. It accepts an integer argument (`max_delay`, default: 10) and waits for a random delay between 0 and `max_delay` seconds. The result is eventually returned. The `random` module is utilized for generating random delays.

#### 1. Concurrent Coroutines Execution
- **File**: `1-concurrent_coroutines.py`
- **Description**: This script incorporates multiple coroutines execution simultaneously. Key requirements include:
  - Importing `wait_random` from the previous Python file.
  - Defining an async routine called `wait_n` that accepts two integer arguments: `n` and `max_delay`.
  - Spawning `wait_random` `n` times with the specified `max_delay`.
  - Returning the list of delays (float values) in ascending order without utilizing `sort()` due to concurrency.

#### 2. Runtime Measurement
- **File**: `2-measure_runtime.py`
- **Description**: This script focuses on measuring runtime. Key tasks include:
  - Importing `wait_n` from the previous file.
  - Creating a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n` as a float.
  - Employing the `time` module to measure an approximate elapsed time.

#### 3. Task Management
- **File**: `3-tasks.py`
- **Description**: This script is dedicated to task management. Key highlights are:
  - Importing `wait_random` from `0-basic_async_syntax`.
  - Writing a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

#### 4. Task Alteration
- **File**: `4-tasks.py`
- **Description**: This script involves task alteration by modifying the code from `wait_n` into a new function named `task_wait_n`. The code closely resembles `wait_n`, except that `task_wait_random` is invoked.
