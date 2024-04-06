def main():

  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  print(f"{num_words} words found in the document")
  chars_dict = char_count(text)
  print(chars_dict)


def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def char_count(text):
  chars = {}
  for i in text:
    lowered_i = i.lower()
    if lowered_i in chars:
      chars[lowered_i] += 1
    else:
      chars[lowered_i] = 1
  return chars



main()

"""
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
  print(file_contents)
if __name__ == "__main__":
    main()

I guess we don't need this anymore...?

"""
