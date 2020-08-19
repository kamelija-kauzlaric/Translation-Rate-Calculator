# Count the number of characters, words and translator pages in a file and calculate the translation rate with and without counting empty spaces.

from prettytable import PrettyTable

print("WELCOME TO THE TRANSLATOR RATE CALCULATOR")

file_name = input("- Source file name with extension: ")
characters_per_page = int(input("- Number of characters per translator page: "))
rate_per_page = int(input("- Your rate per translator page: "))
currency = input("- Currency: ")
print('\n'*0)

# Count the number of characters and translator pages and the translation rate with spaces included.
with open(file_name, "r", encoding="utf8") as source_text_file:
    source_text_with_spaces = source_text_file.read()

character_count_with_spaces = len(source_text_with_spaces)
translator_page_count_with_spaces = round(character_count_with_spaces / characters_per_page, 2)
translator_rate_with_spaces = round(translator_page_count_with_spaces * rate_per_page, 2)

# Count the number of characters and translator pages and the translation rate without spaces.
with open(file_name, "r", encoding="utf8") as source_text_file:
    source_text_without_spaces = source_text_file.read().replace(" ", "")

character_count_without_spaces = len(source_text_without_spaces)
translator_page_count_without_spaces = round(character_count_without_spaces / characters_per_page, 2)
translator_rate_without_spaces = round(translator_page_count_without_spaces * rate_per_page, 2)

# Count the number of words and translator pages and the translation rate.
word_count = len(source_text_with_spaces.split())

# Display everything in a table.
table = PrettyTable(["Translation Info", "With spaces", "Without spaces"])
table.add_row(["Characters", character_count_with_spaces, character_count_without_spaces])
table.add_row(["Words", word_count, word_count])
table.add_row(["Translator pages", translator_page_count_with_spaces, translator_page_count_without_spaces])
table.add_row(["Translator rate in " + currency, translator_rate_with_spaces, translator_rate_without_spaces])
print(table)
