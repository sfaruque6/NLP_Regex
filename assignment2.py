import re

def count_joe_biden_variations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            #include instances of either directly the twitter name, the surname, or any instances of the first name that involves other related words
            pattern = re.compile(r'@joebiden|(?<!@)joe(?!biden).*?(Donald|Trump|\bpresident\w*|\bdebate\w*)|Biden', re.IGNORECASE)
            # Loop through each line
            matches = pattern.findall(content)

            # Print the count
            count = len(matches)
            print(f'The variations of "Joe Biden appear {count} times in the text.')


    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def count_donald_trump_variations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            pattern = re.compile(r'@realdonaldtrump|(?<!@)donald(?!trump).*?(joe|biden|\bpresident\w*|\bdebate\w*)|trump', re.IGNORECASE)

            matches = pattern.findall(content)

            count = len(matches)
            print(f'The variations of "Donald Trump" appear {count} times in the text.')

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def print_chris_wallace_variations(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            pattern = re.compile(r'(@ChrisWallace101|Wallace|Chris.*?(?=(Joe|Donald|Trump|Biden)))', re.IGNORECASE)

            matches = pattern.findall(content)

            count = len(matches)
            print(f'The variations of "Chris Wallace" appear {count} times in the text.')

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'Presidential_Debate.txt'
count_joe_biden_variations(file_path)
count_donald_trump_variations(file_path)
print_chris_wallace_variations(file_path)