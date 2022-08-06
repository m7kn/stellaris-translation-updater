# Update Stellaris translation mod files
Tools for find, write and update missing translation text keys

**Tested**: Stellaris 3.4.5 Cepheus

## Requirements:
- `python` 3.5 or higher
- `pip`
  install: 
  - Linux: https://packaging.python.org/en/latest/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers
  - Windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

## Preparation:

- copy files or `git clone`
- in the project folder:
  ```bash
  $ pip -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```

## Usage:

- **update translations:**
  ```bash
  $ python update_translations.py [game_translation_folder] [mod_translation_folder]
  ```
  ***`game_translation_folder:`*** 
  - Linux GOG version: `~/GOG\ Games/Stellaris/game/localisation/english/`
  - Linux Steam version: `~/.local/share/Steam/steamapps/common/Stellaris/localisation/english/`
  - Windows Steam version: `C:\Program Files (x86)\Steam\SteamApps\common\Stellaris\localisation\english\`
  
  ***`mod_translation_folder` (`english` folder is with the hungarian mod, maybe different for other translations mods):***
  - Linux Steam version: `~/.local/share/Steam/steamapps/workshop/content/[mod_folder]/localisation/english/`
  - Linux other mod path variations: 
    `~/.local/share/Paradox Interactive/Stellaris/mod/[mod_folder]/localisation/english/`
  - Windows mod path variations: 
    `%USERPROFILE%\Documents\Paradox Interactive\Stellaris\mod\[mod_folder]\localisation\english\`
    `C:\Program Files (x86)\Steam\SteamApps\common\Stellaris\mod\[mod_folder]\localisation\english\`


- **find missing keys in a single file:**
  ```bash
  $ python find_missing_keys.py [filename_english] [filename_translated]
  ```

- **find & write missing keys from a single file to a "missing keys file":**
  ```bash
  $ python write_missing_keys.py [filename_english] [filename_translated] [filename_missing_keys]
  ```

- **save all missing translations (missing key or english text) in the `missing_translations` folder:**
  ```bash
  $ python save_missing_translations.py [game_translation_folder] [mod_translation_folder]
  ```
  If the folder exists, first remove it.
  