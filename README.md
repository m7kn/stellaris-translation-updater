# Find & update stellaris translation mod files

## Preparation:

- copy files or git clone
- in the project folder:
  ```
  $ pip -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```

## Usage:

- update translations:
  ```
  $ python update_translations.py [game_translation_folder] [mod_translation_folder]
  ```
  game_translation_folder: 
  - Linux GOG version: `~/GOG\ Games/Stellaris/game/localisation/english/`
  - Linux Steam version: `~/.local/share/Steam/steamapps/common/Stellaris/localisation/`
  - Windows Steam version: `C:\Program Files (x86)\Steam\SteamApps\common\Stellaris`
  
  mod_translation_folder:
  - Linux Steam version: `~/.local/share/Steam/steamapps/workshop/content/[mod_folder]/localisation/english/`
  - Linux possible other folders: 
    `~/.local/share/Paradox Interactive/Stellaris/mod/[mod_folder]/localisation/english/`
  - Windows possible folders: 
    `%USERPROFILE%\Documents\Paradox Interactive\Stellaris\mod\[mod_folder]\localisation\english\`
    `C:\Program Files (x86)\Steam\SteamApps\common\Stellaris\mod\[mod_folder]\localisation\english\`

- find missing key in a single file:
  ```
  $ python find_missing_keys [filename_english] [filename_translated]
  ```

- write missing keys to a file:
  ```
  $ python write_missing_keys [filename_english] [filename_translated] [filename_missing_keys]
  ```