# <img src="https://github.com/Dryd33n/Dryd33n/blob/main/logos/uvic.png" height="25"> SENG265: Software Development Methods
Project files for UVic SENG 265 course in C and Python, including topics such as: 

Topics Covered in C
- **Core Programming Concepts**: Loops, conditionals, functions, and modularity.
- **Structs**: Organizing related data into custom data types.
- **String Manipulation**: Using functions like `strtok`, `strncpy`, and `strcmp`.
- **Memory Management**: Dynamic allocation with `malloc`, `calloc`, and `free`.
- **File I/O**: Reading/writing data with `fopen`, `fgets`, and `fclose`.
- **Debugging**: Identifying memory leaks and runtime errors.
- **Code Organization**: Separating code into files and using headers for modular design.

---

Topics Covered in Python
- **Object-Oriented Programming (OOP)**: Classes, inheritance, encapsulation, and equality methods (`__eq__`, `__repr__`).
- **Data Persistence**: File handling with JSON and `pickle`, custom serialization.
- **Testing**: Unit and integration testing using `unittest` and assertions.
- **GUI Development**: Building interfaces with PyQt6, event handling, and styling.
- **Data Validation**: Input validation with regular expressions and error handling.
- **Software Design**: Modular structure, type hinting, and reusable utilities.
- **Iterative Development**: Evolving systems through incremental improvements.

## [Assignment 1: Survey Processing in C](./a1) 147%
**Purpose**: Analyze survey responses from science and engineering students about computer science attitudes.

**Key Features**:
- Uses `structs` for organizing survey data.
- Implements standard I/O and string manipulation (`fgets`, `strtok`).
- Includes dynamic memory management and modular function design.
- Demonstrates core C concepts: loops, conditionals, and function documentation.

---

## [Assignment 2: Enhanced Survey Processing in C](./a2) 112%
**Purpose**: Extends Assignment 1 with dynamic filtering and scoring of survey data.

**Key Features**:
- Advanced memory management (`malloc`, `calloc`, `free`).
- File I/O for reading/writing survey data.
- Custom data structures for respondents and filters.
- Implements dynamic arrays, conditional filtering, and debug tools for memory and logic errors.

---

## [Assignment 3: Clinic Management System in Python](./a3) 100%
**Purpose**: A basic patient and note management system.

**Key Features**:
- Patient CRUD operations with attributes like PHN, name, and notes.
- Unit testing with `unittest` for system reliability.
- Object-oriented programming with classes for `Patient`, `Record`, and `Note`.
- Integration of Python features: type hinting, datetime handling, and list comprehensions.

---

## [Assignment 4: Persistent Clinic Management System in Python](./a4) 100%
**Purpose**: Enhances Assignment 3 by introducing data persistence.

**Key Features**:
- File handling with JSON (patients) and `pickle` (notes).
- Custom JSON serialization/deserialization for complex objects.
- Improved error handling with custom exceptions.
- Autosave functionality and robust data validation.
- Continued use of OOP, `pathlib` for file paths, and type hinting.

---

## [Assignment 5: GUI-based Clinic Management System in Python](./a5) 100%
**Purpose**: Evolves Assignment 4 into a GUI-based application using PyQt6.

**Key Features**:
- User-friendly interface for managing patients and notes.
- Login system with data validation and error handling.
- Custom dark theme with enhanced visual appeal.
- PyQt6 widgets for interactive components and dialogs.
- Regular expressions and custom utility functions for formatting/validation.
