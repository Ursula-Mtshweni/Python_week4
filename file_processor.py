import os
from datetime import datetime

KEYWORDS = ['python', 'file', 'error']  # Keywords to transform

def transform_line(line: str, line_num: int) -> str:
    words = line.strip().split()
    transformed_words = [
        word.upper() if word.lower() in KEYWORDS else word
        for word in words
    ]
    word_count = len(words)
    return f"{line_num:03}: {' '.join(transformed_words)} [Words: {word_count}]"

def add_header_footer(content: list, filename: str) -> list:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"--- File: {filename} | Processed at: {timestamp} ---\n"
    footer = f"\n--- End of File | Finished at: {timestamp} ---"
    return [header] + content + [footer]

def process_file(input_filename: str, output_filename: str):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        modified_lines = [
            transform_line(line, i + 1)
            for i, line in enumerate(lines)
        ]

        final_content = add_header_footer(modified_lines, input_filename)

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(final_content))

        print(f"✅ File '{input_filename}' processed successfully.")
        print(f"📄 Modified content saved in '{output_filename}'.\n")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: You do not have permission to access this file.")
    except UnicodeDecodeError:
        print("❌ Error: Cannot decode file. It might be a binary file.")
    except IsADirectoryError:
        print("❌ Error: The provided path is a directory, not a file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

def show_menu():
    print("\n🗂️ File Processor Menu")
    print("1. Process a file")
    print("2. Test FileNotFoundError")
    print("3. Test PermissionError (on Unix/Linux/Mac only)")
    print("4. Test UnicodeDecodeError")
    print("5. Test IsADirectoryError")
    print("0. Exit")

def run_menu():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            input_file = input("Enter the input filename: ").strip()
            output_file = input("Enter the output filename: ").strip()
            process_file(input_file, output_file)

        elif choice == '2':
            process_file("non_existent_file.txt", "output.txt")

        elif choice == '3':
            # On Unix systems, /root is usually inaccessible
            restricted_file = "/root/secret.txt" if os.name != 'nt' else "C:\\System Volume Information\\secret.txt"
            process_file(restricted_file, "output.txt")

        elif choice == '4':
            # Try reading a binary file like an image
            process_file("test_image.jpg", "output.txt")

        elif choice == '5':
            process_file(".", "output.txt")

        elif choice == '0':
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    run_menu()
