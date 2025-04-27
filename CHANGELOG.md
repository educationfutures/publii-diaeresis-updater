# Changelog

All notable changes to this project will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2025-04-27

### Added
- Initial release of the **Diaeresis and Smart Quotes Updater for Publii**.
- Automatic detection and correction of English words needing a diaeresis (e.g., `cooperate` ➔ `coöperate`).
- Optional replacement of straight quotation marks with properly matched smart (curly) quotes.
- Correction of common informal word usages (e.g., `webpage` ➔ `Web page`, `gonna` ➔ `going to`).
- Support for `--dry-run` mode to preview changes without modifying the database.
- Automatic creation of `.bak` backup files (unless disabled via `--no-backup`).
- Detailed change report listing only the specific words corrected in each post.
- Safe targeting of the `posts` table and `title`/`text` columns only.
