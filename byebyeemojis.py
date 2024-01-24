import os
import re

def remove_emojis_from_filename(filename):
    # Regular expression to match a wide range of emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"  
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002500-\U00002BEF"  # various symbols
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642" 
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)

    return emoji_pattern.sub(r'', filename)

def process_directory(path, recursive=False):
    for root, dirs, files in os.walk(path):
        for file in files:
            # Remove emojis from file name
            new_filename = remove_emojis_from_filename(file)
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(root, new_filename)

            # Rename file if the name has changed
            if new_filename != file:
                os.rename(old_file_path, new_file_path)
                print(f'Renamed "{old_file_path}" to "{new_file_path}"')

        if not recursive:
            break

def main():
    choice = input("Do you want to remove emojis from filenames in all subfolders as well? (yes/no): ").strip().lower()
    recursive = choice == 'yes'

    current_directory = os.getcwd()
    process_directory(current_directory, recursive)

if __name__ == "__main__":
    main()
