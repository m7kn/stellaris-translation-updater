"""
Find missing keys in the Stellaris translation file
"""

import sys
import utils


def main():
    """Main method"""
    args = sys.argv
    if len(args) < 3:
        print(f"""
Using:
python {args[0]} [filename_english] [filename_translated]
""")
        sys.exit()

    filename_english = args[1]
    filename_translated = args[2]

    print("Loading...")
    with open(filename_english, "r", encoding="utf8") as f:
        lines_english: list[str] = f.readlines()

    with open(filename_translated, "r", encoding="utf-8") as f:
        lines_translated: list[str] = f.readlines()

    print("Preparing...")
    (datalines_eng, datalines_tr) = utils.create_datalines(lines_english, lines_translated)

    print("Processing...")
    missing_data = utils.find_missing_keys(datalines_eng, datalines_tr)
    print("Missing keys in the translated file:")
    print(utils.get_keys(missing_data))


if __name__ == "__main__":
    main()
