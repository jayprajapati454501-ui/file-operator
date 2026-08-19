# 📔 Personal Journal Manager

A simple command-line **Personal Journal Manager** built with Python. The project allows users to create, view, search, and delete journal entries stored in a text file.

## 📌 Project Description

The **Personal Journal Manager** uses a `JournalManager` class to manage journal entries. Each new entry is saved with a timestamp in `journal.txt`.

The application provides a menu with five options:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

## ✨ Features

* 📝 Add new journal entries
* 🕐 Automatically add date and time
* 📖 View all saved entries
* 🔍 Search entries using a keyword or date
* 🗑️ Delete all journal entries
* ⚠️ Handles missing files
* 🔐 Handles permission errors
* 💾 Stores entries permanently in a text file
* 📋 Menu-driven command-line interface

## 🛠️ Technologies Used

* **Python 3**
* `os` module
* `datetime` module
* File handling
* Object-Oriented Programming
* Classes and methods
* Exception handling
* String processing

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── File operator.py
├── journal.txt
└── README.md
```

> `journal.txt` is created automatically when the first journal entry is added.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed:

```bash
python --version
```

### 2. Run the Program

Open a terminal in the project folder and run:

```bash
python "File operator.py"
```

## 💻 Main Class

The project uses a `JournalManager` class:

```python
class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename
```

The class is responsible for managing the journal file and its entries.

## 📝 Add a New Entry

The `add_entry()` method creates a timestamp and saves the journal entry using append mode.

Example format:

```text
[2026-08-19 15:30:00]
Today I learned Python file handling.
```

The program uses the format `[YYYY-MM-DD HH:MM:SS]` for timestamps.

## 📖 View All Entries

The `view_all_entries()` method reads and displays all saved journal entries.

If the journal file does not exist, the program displays an appropriate message instead of crashing.

## 🔍 Search Entries

The `search_entry()` method allows the user to search for a keyword or date.

The search is **case-insensitive**, meaning searches such as `Python`, `python`, and `PYTHON` can match the same entry.

## 🗑️ Delete All Entries

The `delete_all_entries()` method asks the user for confirmation before deleting the journal file.

```text
Are you sure you want to delete all entries? (yes/no):
```

Only a `yes` response performs the deletion.

## 📋 Application Menu

When the program starts, it displays:

```text
=== Welcome to Personal Journal Manager! ===

--> Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

## 🎯 Learning Objectives

This project helps beginners learn:

* Object-Oriented Programming
* Python classes and objects
* Functions and methods
* File handling
* Reading and writing text files
* Append mode
* Exception handling
* `try-except`
* Date and time handling
* String searching
* Conditional statements
* `while` loops
* User input
* Menu-driven programs

## 🧠 Python Concepts

### File Handling

The project uses:

```python
open(filename, 'a')
open(filename, 'r')
```

to write and read journal entries.

### Exception Handling

The program handles errors such as:

* `PermissionError`
* Unexpected exceptions

This helps prevent the application from terminating unexpectedly.

### Object-Oriented Programming

The application organizes journal functionality inside the `JournalManager` class.

Methods include:

```text
add_entry()
view_all_entries()
search_entry()
delete_all_entries()
```

## 🚀 Future Improvements

Possible improvements include:

* Edit existing journal entries
* Add entry IDs
* Search by date range
* Export journal entries to PDF
* Encrypt private journal entries
* Add a graphical user interface
* Add password protection
* Sort entries by date
* Add categories or tags
* Add a backup feature

## 👨‍💻 Author

**Your Name**

## 📄 License

This project is created for **educational and learning purposes**.


