# Diaeresis Updater for Publii Sites

## Overview

This Python script scans a Publii-generated SQLite database and automatically updates words to include the **diaeresis** (¨), following the editorial style of **The New Yorker**. Examples include changing **cooperation** to **coöperation** or **reenter** to **reënter**.

The diaeresis serves a vital role in making English clearer and more readable. It indicates that two adjacent vowels should be pronounced separately, preventing ambiguity and ensuring that words are understood as intended. Without it, a word like cooperation can momentarily confuse the reader, suggesting an unintended pronunciation like “coo-peration.” Written as coöperation, the structure and rhythm of the word become immediately clear. Restoring the diaeresis strengthens the connection between how words are spelled and how they sound, preserving the precision and nuance that English once prioritized. It is a stylistic choice, and a small (but meaningful) way to respect the integrity of language and to enhance the reader’s experience.

This script makes it easy for Publii users and editors to consistently implement this stylistic choice across their websites. This may be adapted for other text search and replace uses in your Publii site database.

---

## Why use this?

Publii stores website content in a SQLite database. Manually updating each post or entry to match New Yorker-style diaereses would be tedious and error-prone.

This script helps by:

- Automatically identifying and correcting eligible words.
- Covering multiple word forms (like *cooperating* ➜ *coöperating*).
- Ensuring consistent use of diaereses across your website.
- Saving considerable time.

---

## Features

- Scans all tables and text fields in your SQLite database.
- Applies replacements from an extensive, scholarly diaeresis dictionary.
- Automatically handles capitalization.
- Only updates entries that require changes (safe and efficient).
- Prints informative messages about what’s updated.

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

```bash
python3 diaeresis-updater.py
```

Example output:

```
Scanning table: posts
Updated row 15 in table posts
Updated row 47 in table posts
Done.
```

### 5. Sync your website

With the changes made in the database, press the "Sync your website" button on Publii to push all changes to your live website.

---

## Important

- **Always make a backup** of your Publii database before running.
- This script directly modifies your database upon execution.
- It only replaces words explicitly defined in its built-in dictionary.

---

## Contributing

Contributions, bug reports, and suggestions are very welcome!

- Submit an issue to suggest new words or report problems.
- Open a pull request to contribute improvements or features.

---

## Example

Before:

> Cooperation and coordination are key to reevaluating our plans.

After:

> Coöperation and coördination are key to reëvaluating our plans.


---

## Acknowledgments

Inspired by The New Yorker's dedication to meticulous editorial style and clarity.

Thanks to Publii's developers and the open-source community for accessible, elegant web publishing.
