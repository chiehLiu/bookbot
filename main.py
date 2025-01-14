def main(): 
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = count_words(text)
  chars_dict = get_chars_dict(text)


  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  print("")
  sort_on_and_print(chars_dict)
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())

def get_chars_dict(text):
  chars = {}

  for c in text:
    lowerc = c.lower()
    if lowerc in chars:
      chars[lowerc] += 1
    else:
      chars[lowerc] = 1

  return chars

def sort_on_and_print(chars_dict):
  for c in chars_dict:
    if c.isalpha():
      print(f"The {c} character was found {chars_dict[c]} times")
main()
