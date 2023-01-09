n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 0
    books[book] += 1

book_count = sorted(list(books.items()), key = lambda x: (-x[1], x[0]))

print(book_count[0][0])