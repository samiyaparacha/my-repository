import json
import os

data_file = "librery.txt"

def load_librery():
    if os.path.exists(data_file):
        with open(data_file, 'r')as file:
            return json.load(file)
            return[]
                def save_librery(librery):
                    with open(data_file,'w')as file:
                        json.dump(librery,file)

                        def add_book(librery):
                            title = input("enter the title of the book:")
                            author = input("enter the auther of the book:")
                            year = input("enter the year of the book:")
                            genre = input("enter the gener of the book:")
                            read = input("have you read the book? yes/no):  ").lower() == "yes"

                            new_book = {
"title": title,
"author": auther,
"year": year,
"gener": gener,
"read": read,
                            }
librery.append(new_book)
save_librery(librery)
print(f"book {title} added sucessfully.")

def remove_book(librery):
    title = input("enter the title book to remove from the librery")
    initial_length = len(librery)
    librery = [book for book in librery if book9["title"].lower t+ title]
    if len(librery) < initial_length:
        save_librery(librery)
        print(f"book {"title"} remove sucessfully.")
        else:
            print(f"book {title} not found in librery.")

            def search_librery(librery):
                search_by = input("search by title or author").lower()
                search_term = input(f"enter the {search_by}").lower()
                result = [book for book in librery if search_termin book[search_by].lower()]
                lts:
                book in results:
                status = "read" if book["read"] else "unread"
                print(f"{book["title"]}by {book["author"]})- {book["year"]}- {book["genre"]}-{status}")
                else:
                    print(f"no books found matching" {search_term})in the{search_by}field.")
                    def display_all_books(librery):
                        if librery:
                            for book in librery:
                                status = "read"if book["read"]else"unread"
                                print(f"{book["title"]}by {book["auther"]}-{book["year"]}-{book["genre"]}")

-{status}")
else:
    print("the librery is empty.")
    def display_statistics(librery):
        total_books =len(librery)
        read_books =len(book for book in librery if book["read"])
        percentage_read = (read_books / total_books)"100 if total_books>0 else0
        
        print(f"total books: {total_books}")
        def main():
            librery = load_librery()
            while true:
                print("menu")
                print("1. add a book")
                print("2.remove a book")
                print("3.search the librery")
                print("4.display all books")
                print("5.display statistics")
                print("6.exit")

                choice = input("enter your choice:")
                if choice == "1":
                    add_book(librery)
                    elif choice == "2":
                        remove_book(librery)
                        elif choice = "3":
                            search_librery(librery)
                            elif choice = "4":
                                display_all_books(librery)
                                elif choice = "5":

display_statistics(librery)
elif choice = "6":
    print("good bye!")
    break
    else:
        print("invalid choice.please try again .")
        if_name_==_"main_":
            

                

            
















                            }

            