"""
Save all missing translations (missing key or english text)
Create a translation_needed folder

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
    if len(args) < 4:
        print(f"""
Using:
python {args[0]} [game_translation_folder] [mod_translation_folder] [lang]
""")
        sys.exit()

    folder_english = args[1]
    folder_translated = args[2]
    lang = args[3]

    print("Scanning folders...")
    filenames_english = get_yml_files(folder_english)
    filenames_translated = get_yml_files(folder_translated)

    if (len(filenames_english) == 0):
      print("Not found translation files!")
      sys.exit()

    dirname = f"missing_translations/{lang}"
    try:
        os.mkdir("missing_translations")
    except FileExistsError:
        pass
        
    try:
        os.mkdir(dirname)
    except FileExistsError:
        shutil.rmtree(dirname)
        os.mkdir(dirname)

    counter = 1
    writing_files_count = 0
    for fname_eng in filenames_english:
        path_eng = os.path.join(folder_english, fname_eng)
        path_tr = os.path.join(folder_translated, fname_eng)
        if fname_eng in filenames_translated:
            print(f"[{counter}] Find missing translation texts in {fname_eng}...")
            with open(path_eng, "r", encoding="utf-8") as f:
                lines_english: list[str] = f.readlines()
            with open(path_tr, "r", encoding="utf-8") as f:
                lines_translated: list[str] = f.readlines()
            (datalines_eng, datalines_tr) = utils.create_datalines(lines_english, lines_translated)
            missing_keys = utils.find_missing_keys(datalines_eng, datalines_tr)
            not_translated = utils.missing_translations(datalines_eng, datalines_tr)
            missing_data = missing_keys + not_translated

            if (len(missing_data) > 0):
                print(f"[{counter}] Writing missing translations...")
                with open(os.path.join(dirname, fname_eng), "w", encoding="utf-8") as f:
                    for item in missing_data:
                        f.write(item["orig_txt"])
                writing_files_count = writing_files_count + 1
            else:
                print(f"[{counter}] Translations are identical in {fname_eng}")
        else:
            print(f"[{counter}] Copy missing file: {fname_eng}")
            shutil.copyfile(path_eng, os.path.join(dirname, fname_eng))
            writing_files_count = writing_files_count + 1
        counter = counter + 1
        print()

    if writing_files_count > 0:                
      print(f"Created {writing_files_count} missing translations files in the {dirname}/ folder.")
      print("Happy translation!")
    else:
      print("All translation files are identical!")


if __name__ == "__main__":
    main()
