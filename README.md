# New Yorker-style Diaeresis Updater for Publii Sites

## Overview

This Python script scans a Publii-generated SQLite database and automatically updates words to include the **diaeresis** (¨), following the editorial style of **The New Yorker**. Examples include changing **cooperation** to **coöperation** or **reenter** to **reënter**.

The diaeresis clarifies that two adjacent vowels should be pronounced separately. While most modern style guides no longer use it, The New Yorker continues this tradition, providing clarity and elegance to written text.

This script makes it easy for Publii users and editors to consistently implement this stylistic choice across their websites and can be adapted for other text search and replace uses in the database used by your Publii site.

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
