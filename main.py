import json

class BookCollection:

    def __init__(self):
        self.booklist = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        try:
            with open(self.storage_file, "r") as file:
                self.booklist = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.booklist = []
    def save_to_file(self):
        with open(self.storage_file, "w") as file:
            json.dump(self.booklist, file, indent=4)

    def create_new_book(self):
        title = input("Enter Book Title : ")
        author = input("Enter Book's Author") 
        year = input("Enter Publication Year : ")
        genre = input("Enter Book's genre : ")
        is_read = (input("Have you read this book? (yes/no): ").strip().lower() == "yes"   )              

        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": is_read,
        }    

        self.booklist.append(new_book)
        self.save_to_file()
        print("Book Added Succesfully!") 

    def delete_book(self):
        book_title = input("Enter the title of the book to remove: ")

        for book in self.booklist:
            if book["title"].lower() == book_title.lower():
                self.booklist.remove(book)
                self.save_to_file()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")     

    def find_book(self):
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.booklist
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("Matching Books:")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
                )
        else:
            print("No matching books found.\n")   

    def start_application(self):
        while True:
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()            

