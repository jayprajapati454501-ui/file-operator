import os
from datetime import datetime

class JournalManager:
    """Encapsulates all operations and exception handling for managing journal.txt."""
    
    def __init__(self, filename="journal.txt"):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Demonstrates exclusive creation mode ('x') safely."""
        try:
            # Create file exclusively if it does not already exist
            with open(self.filename, 'x') as f:
                pass
        except FileExistsError:
            pass  # File already exists, no setup needed
        except PermissionError:
            print(f"[Error] Permission denied while initializing '{self.filename}'.")
        except Exception as e:
            print(f"[Error] Unexpected setup failure: {e}")

    def add_entry(self):
        """Appends a new journal entry using append mode ('a')."""
        content = input("\nEnter your journal entry:\n> ").strip()
        if not content:
            print("[Warning] Empty entry ignored.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"[{timestamp}]\n{content}\n{'-' * 40}\n"

        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(formatted_entry)
            print("[Success] Entry added successfully.")
        except PermissionError:
            print(f"[Error] Permission denied: Cannot write to '{self.filename}'.")
        except Exception as e:
            print(f"[Error] Failed to add entry: {e}")

    def view_entries(self):
        """Reads and displays all entries using read mode ('r')."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = f.read()
                if not data.strip():
                    print("\n[Info] Journal is currently empty.")
                else:
                    print("\n--- JOURNAL ENTRIES ---")
                    print(data)
        except FileNotFoundError:
            print(f"[Error] '{self.filename}' does not exist.")
        except PermissionError:
            print(f"[Error] Permission denied: Cannot read '{self.filename}'.")
        except Exception as e:
            print(f"[Error] Failed to read entries: {e}")

    def search_entries(self):
        """Searches for keywords or dates using read mode ('r')."""
        query = input("\nEnter keyword or date to search: ").strip()
        if not query:
            print("[Warning] Search query cannot be empty.")
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                entries = f.read().split("-" * 40)

            matches = [e.strip() for e in entries if query.lower() in e.lower() and e.strip()]

            if matches:
                print(f"\n--- FOUND {len(matches)} MATCH(ES) ---")
                for entry in matches:
                    print(entry)
                    print("-" * 40)
            else:
                print(f"[Info] No entries found matching '{query}'.")
        except FileNotFoundError:
            print(f"[Error] '{self.filename}' does not exist.")
        except PermissionError:
            print(f"[Error] Permission denied: Cannot access '{self.filename}'.")
        except Exception as e:
            print(f"[Error] Search failed: {e}")

    def delete_entries(self):
        """Clears/removes entries by deleting the file or truncating via write mode ('w')."""
        confirm = input("\nAre you sure you want to delete ALL entries? (y/n): ").strip().lower()
        if confirm != 'y':
            print("[Cancelled] Action aborted.")
            return

        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
                print(f"[Success] Journal file '{self.filename}' deleted successfully.")
            else:
                print(f"[Info] '{self.filename}' does not exist.")
        except PermissionError:
            # Fallback to write mode ('w') if file removal is blocked by file locks
            try:
                with open(self.filename, 'w') as f:
                    pass
                print(f"[Success] Journal contents cleared via write mode ('w').")
            except PermissionError:
                print(f"[Error] Permission denied: Cannot delete or overwrite '{self.filename}'.")
        except Exception as e:
            print(f"[Error] Deletion failed: {e}")


def main():
    journal = JournalManager("journal.txt")

    while True:
        print("\n==============================")
        print("    FILE OPERATOR JOURNAL     ")
        print("==============================")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nSelect an option (1-5): ").strip()

        if choice == '1':
            journal.add_entry()
        elif choice == '2':
            journal.view_entries()
        elif choice == '3':
            journal.search_entries()
        elif choice == '4':
            journal.delete_entries()
        elif choice == '5':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("[Error] Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
