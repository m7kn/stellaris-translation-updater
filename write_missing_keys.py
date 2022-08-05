"""
Write to file missing keys in the Stellaris translation file
"""

import sys
import utils


def main():
    """Main method"""
    args = sys.argv
    if len(args) < 4:
        print(f"""
Using:
python {args[0]} [filename_english] [filename_translated] [filename_missing_keys]
""")
        sys.exit()

    filename_english = args[1]
    filename_translated = args[2]
    filename_missing = args[3]

    print("Loading...")
    with open(filename_english, "r", encoding="utf-8") as f:
        lines_english: list[str] = f.readlines()

    with open(filename_translated, "r", encoding="utf-8") as f:
        lines_translated: list[str] = f.readlines()

    print("Preparing...")
    (datalines_eng, datalines_tr) = utils.create_datalines(lines_english, lines_translated)

    print("Processing...")
    missing_data = utils.find_missing_keys(datalines_eng, datalines_tr)
    print(f"Writing file {filename_missing}...")
    with open(filename_missing, "w", encoding="utf-8") as f:
        for item in missing_data:
            f.write(item["orig_txt"])
    
    print("Done!")

if __name__ == "__main__":
    main()
