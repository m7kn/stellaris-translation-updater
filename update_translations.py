"""
Updating Stellaris translation mod files with missing keys from the game
"""

import sys
import os
import shutil
import utils


def get_yml_files(folder_name):
    filenames = []
    for dir_entry in os.scandir(folder_name):
        if dir_entry.is_file and dir_entry.name.endswith(".yml"):
            filenames.append(dir_entry.name)

    return filenames


def main():
    """Main method"""
    args = sys.argv
    if len(args) < 3:
        print(f"""
Using:
python {args[0]} [game_translation_folder] [mod_translation_folder]
""")
        sys.exit()

    folder_english = args[1]
    folder_translated = args[2]

    print("Scanning folders...")
    filenames_english = get_yml_files(folder_english)
    filenames_translated = get_yml_files(folder_translated)

    counter = 1
    for fname_eng in filenames_english:
        path_eng = os.path.join(folder_english, fname_eng)
        path_tr = os.path.join(folder_translated, fname_eng)
        if fname_eng in filenames_translated:
            print(f"[{counter}] Find missing translation keys in {fname_eng}...")
            with open(path_eng, "r", encoding="utf-8") as f:
                lines_english: list[str] = f.readlines()
            with open(path_tr, "r", encoding="utf-8") as f:
                lines_translated: list[str] = f.readlines()
            (datalines_eng, datalines_tr) = utils.create_datalines(lines_english, lines_translated)
            missing_data = utils.find_missing_keys(datalines_eng, datalines_tr)

            if (len(missing_data) > 0):
                print(f"[{counter}] Writing missing keys...")
                with open(path_tr, "a", encoding="utf-8") as f:
                    for item in missing_data:
                        f.write(item["orig_txt"])
            else:
                print(f"[{counter}] Translations are identical in {fname_eng}")
        else:
            print(f"[{counter}] Copy missing file: {fname_eng}")
            shutil.copyfile(path_eng, path_tr)
        counter = counter + 1
        print()
                
    print("All done!")


if __name__ == "__main__":
    main()
