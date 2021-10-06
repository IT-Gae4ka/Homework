# Task 4.8
# Implement a Pagination class helpful to arrange text on pages and list content on given page. The class should take in a text and a positive integer which indicate how many symbols will be allowed per each page (take spaces into account as well). You need to be able to get the amount of whole symbols in text, get a number of pages that came out and method that accepts the page number and return quantity of symbols on this page. If the provided number of the page is missing print the warning message "Invalid index. Page is missing". If you're familliar with using of Excpetions in Python display the error message in this way. Pages indexing starts with 0.

# Example:

# >>> pages = Pagination('Your beautiful text', 5)
# >>> pages.page_count
# 4
# >>> pages.item_count
# 19

# >>> pages.count_items_on_page(0)
# 5
# >>> pages.count_items_on_page(3)
# 4
# >>> pages.count_items_on_page(4)
# Exception: Invalid index. Page is missing.
# Optional: implement searching/filtering pages by symblos/words and displaying pages with all the symbols on it. If you're querying by symbol that appears on many pages or if you are querying by the word that is splitted in two return an array of all the occurences.

# Example:

# >>> pages.find_page('Your')
# [0]
# >>> pages.find_page('e')
# [1, 3]
# >>> pages.find_page('beautiful')
# [1, 2]
# >>> pages.find_page('great')
# Exception: 'great' is missing on the pages
# >>> pages.display_page(0)
# 'Your '

class Pagination:
    def __init__(self, text, symbols_on_page):
        self.text = text
        self.symbols_on_page = symbols_on_page
        self.pages = []

    def divide_by_pages(self):
        for index in range(0, len(self.text), self.symbols_on_page):
            page_content = self.text[index:index+self.symbols_on_page]
            self.pages.append(page_content)

    @property
    def page_count(self):
        self.divide_by_pages()
        pages_count = len(self.pages)
        print(pages_count)

    @property
    def item_count(self):
        print(len(self.text))

    def count_items_on_page(self, page_number):
        if page_number <= len(self.pages)-1:
            symbols_on_page = len(self.pages[page_number])
            print(symbols_on_page)
        else:
            raise IndexError("Invalid index. Page is missing")

    def display_page(self, page_number):
        if page_number <= len(self.pages)-1:
            print(self.pages[page_number])
        else:
            raise IndexError("Invalid index. Page is missing")

    def find_page(self, word):
        pages_with_content = []
        if word not in self.text:
            raise Exception(f"{word}' is missing on the pages")

        else:
            for index in range(0, len(self.pages)):
                print(self.pages)
                if word in self.pages[index]:
                    pages_with_content.append(index)
            print(pages_with_content)


p = Pagination('Your beautiful text', 5)

p.page_count
p.item_count
p.count_items_on_page(0)
p.display_page(3)
#p.display_page(4)
p.find_page("Your")
p.find_page("e")
p.find_page("beautiful")
#p.find_page("great")

