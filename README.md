# Diaeresis and Smart Quotes Updater for Publii

This Python script scans your [Publii](https://getpublii.com/) site's SQLite database and updates text inside posts to:

- Correctly apply **diaereses** (¨) to appropriate words (e.g., `cooperate` ➔ `coöperate`)
- Optionally replace **straight quotes** with **smart (curly) quotes** (e.g., `"example"` ➔ `“example”`)
- Fix common casual word usages (e.g., `webpage` ➔ `Web page`, `gonna` ➔ `going to`)

It ensures a more precise, formal, and polished English writing style across your site.

---

## Why use it?

English words that combine vowels across syllables (like "cooperate" or "reelect") traditionally used the diaeresis to clarify pronunciation. Restoring this usage improves readability and reflects a more careful, literate style.

Similarly, replacing straight quotation marks with smart (curly) quotes enhances typographic quality and aligns your site with professional publishing standards.

This script allows you to make these corrections **automatically** across your Publii site.

---

## How it works

- Connects directly to your site's `db.sqlite` file.
- Scans the `posts` table, updating the `title` and `text` fields.
- Only words listed in the internal dictionary are replaced — no uncontrolled edits.
- Optionally replaces straight quotes with properly matched opening/closing smart quotes.
- Supports **dry-run mode** to preview changes without modifying your database.
- Automatically creates a backup (`db.sqlite.bak`) unless disabled.

---

## Example

Before:

> Cooperation and "coordination" are key to reevaluating our plans.

After:

> Coöperation and “coördination” are key to reëvaluating our plans.

---

## ⚠️ Important Warning

**Please read carefully before using this tool.**

- Always make your own manual backup of your Publii site's `db.sqlite` file before running the script — even though the script will automatically create a `.bak` copy.
- If used improperly or on the wrong file, the script could unintentionally modify your database.
- Always run a `--dry-run` first to preview the changes.
- Only proceed with full updates once you have verified the changes are safe and appropriate for your site.

**Use at your own risk.**

---

## Installation and usage

### 1. Requirements

- Python 3.8 or newer (comes with SQLite support).

### 2. Setup

First, make sure to back up your Publii site as changes made are not reversible.

Clone this repository or download the script:

```bash
git clone https://github.com/your-username/publii-diaeresis-updater.git
cd publii-diaeresis-updater
```

### 3. Configure

Open `diaeresis-updater.py` and modify this line to point to your database:

```python
sqlite_file = "/path-to-your-Publii-folder/sites/site-name/input/db.sqlite"
```

### 4. Run the script

Preview changes without modifying anything:

```bash
python3 diaeresis-updater.py --dry-run
```

Apply changes to your database:

```bash
python3 diaeresis-updater.py
```

Skip the backup (not recommended)

```bash
python3 diaeresis-updater.py --no-backup
```

Adjusting settings (optional)

Inside the script:

```python
apply_smart_quotes = True  # Set to False to disable smart quotes replacement
```

Example output:

```
📋 Words that would be changed (dry run):
- [posts][row 21][text]: website ➔ Web site
- [posts][row 33][text]: webpage ➔ Web page, smart quotes applied
- [posts][row 68][text]: website ➔ Web site
- [posts][row 108][text]: Cooperation ➔ Coöperation, Reemphasize ➔ Reëmphasize, smart quotes applied
```

### 5. Sync your website

With the changes made in the database, press the "Sync your website" button on Publii to push all changes to your live website.

---

## Important to know

- This script **always makes a backup** of your Publii database before running unless `--no-backup` is specified.
- This script directly modifies your database upon execution.
- It only replaces words explicitly defined in its built-in dictionary.

---

## Contributing

Contributions, bug reports, and suggestions are very welcome!

- Submit an issue to suggest new words or report problems.
- Open a pull request to contribute improvements or features.


---

## Acknowledgments

Inspired by The New Yorker's dedication to meticulous editorial style and clarity.

Thanks to Publii's developers and the open-source community for accessible, elegant web publishing.
