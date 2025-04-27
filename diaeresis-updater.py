import sqlite3
import re
import os
import shutil
import sys

# SETTINGS
sqlite_file = "/path-to-your-Publii-folder/sites/site-name/input/db.sqlite"  # <-- Adjust to your path
dry_run = "--dry-run" in sys.argv
create_backup = "--no-backup" not in sys.argv
apply_smart_quotes = True  # Set False if you ever want to disable smart quotes

print(f"Dry run mode: {dry_run}")
print(f"Create backup: {create_backup}")

# Define your replacement roots
roots = {
    "coequal": "coëqual",
    "coequally": "coëqually",
    "cooperate": "coöperate",
    "cooperated": "coöperated",
    "cooperates": "coöperates",
    "cooperating": "coöperating",
    "cooperation": "coöperation",
    "cooperative": "coöperative",
    "coordinate": "coördinate",
    "coordinated": "coördinated",
    "coordinates": "coördinates",
    "coordinating": "coördinating",
    "coordination": "coördination",
    "coordinator": "coördinator",
    "preeminence": "preëminence",
    "preeminent": "preëminent",
    "preemploy": "preëmploy",
    "preemployed": "preëmployed",
    "preemployment": "preëmployment",
    "preempt": "preëmpt",
    "preempted": "preëmpted",
    "preempting": "preëmpting",
    "preemption": "preëmption",
    "preemptive": "preëmptive",
    "preexist": "preëxist",
    "preexisted": "preëxisted",
    "preexistence": "preëxistence",
    "preexisting": "preëxisting",
    "reelect": "reëlect",
    "reelected": "reëlected",
    "reelecting": "reëlecting",
    "reelection": "reëlection",
    "reemerge": "reëmerge",
    "reemerged": "reëmerged",
    "reemerging": "reëmerging",
    "reemphasize": "reëmphasize",
    "reemphasized": "reëmphasized",
    "reemphasizing": "reëmphasizing",
    "reenact": "reënact",
    "reenacted": "reënacted",
    "reenacting": "reënacting",
    "reenactment": "reënactment",
    "reencounter": "reëncounter",
    "reencountered": "reëncountered",
    "reencountering": "reëncountering",
    "reenergize": "reënergize",
    "reenergized": "reënergized",
    "reenergizing": "reënergizing",
    "reengage": "reëngage",
    "reengaged": "reëngaged",
    "reengagement": "reëngagement",
    "reengaging": "reëngaging",
    "reenlist": "reënlist",
    "reenlisted": "reënlisted",
    "reenlisting": "reënlisting",
    "reenlistment": "reënlistment",
    "reenter": "reënter",
    "reentered": "reëntered",
    "reentering": "reëntering",
    "reentry": "reëntry",
    "reestablish": "reëstablish",
    "reestablished": "reëstablished",
    "reestablishing": "reëstablishing",
    "reestablishment": "reëstablishment",
    "reevaluate": "reëvaluate",
    "reevaluated": "reëvaluated",
    "reevaluating": "reëvaluating",
    "reevaluation": "reëvaluation",
    "reexamination": "reëxamination",
    "reexamine": "reëxamine",
    "reexamined": "reëxamined",
    "reexamines": "reëxamines",
    "reexamining": "reëxamining",
    # Plus common fixes
    "webpage": "Web page",
    "website": "Web site",
    "gonna": "going to",
    "wanna": "want to",
    "kinda": "kind of",
    "...": "…",
}

# Create capitalization variants automatically
replacements = {}
for k, v in roots.items():
    replacements[k] = v
    replacements[k.capitalize()] = v.capitalize()

# Smart quotes fixer
def fix_smart_quotes(text):
    if text is None:
        return text, False
    if not isinstance(text, str):
        text = str(text)

    original_text = text

    # Handle double quotes
    result = []
    double_quote_open = True
    for char in text:
        if char == '"':
            if double_quote_open:
                result.append('“')
            else:
                result.append('”')
            double_quote_open = not double_quote_open
        else:
            result.append(char)
    text = ''.join(result)

    # Handle apostrophes and single quotes
    text = re.sub(r"(\w)'(\w)", r"\1’\2", text)

    result = []
    single_quote_open = True
    for char in text:
        if char == "'":
            if single_quote_open:
                result.append('‘')
            else:
                result.append('’')
            single_quote_open = not single_quote_open
        else:
            result.append(char)

    text = ''.join(result)

    changed = (text != original_text)
    return text, changed

# Main text fixer
def fix_text(text):
    if text is None:
        return text, False
    if not isinstance(text, str):
        text = str(text)

    changed = False

    for word, new_word in replacements.items():
        pattern = r'(?<!\w){}(?!\w)'.format(re.escape(word))
        new_text = re.sub(pattern, new_word, text, flags=re.IGNORECASE)
        if new_text != text:
            changed = True
            text = new_text

    if apply_smart_quotes:
        text, smart_quotes_changed = fix_smart_quotes(text)
        if smart_quotes_changed:
            changed = True

    return text, changed

# Process the database
def process_sqlite_file(sqlite_path):
    if not os.path.exists(sqlite_path):
        print(f"❌ File not found: {sqlite_path}")
        return

    if create_backup:
        backup_path = sqlite_path + ".bak"
        shutil.copy2(sqlite_file, backup_path)
        print(f"🛡 Backup created: {backup_path}")

    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    changes = []

    # Scan only the posts table
    table_name = "posts"
    print(f"🔎 Scanning table: {table_name}")

    cursor.execute(f"PRAGMA table_info('{table_name}');")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]

    target_cols = [col for col in ["title", "text"] if col in column_names]

    if not target_cols:
        print("⚠️ No target columns found.")
        return

    select_query = f"SELECT rowid, {', '.join(target_cols)} FROM '{table_name}';"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    for row in rows:
        rowid = row[0]
        updated_fields = {}
        for idx, col_name in enumerate(target_cols, start=1):
            original_text = row[idx]
            fixed_text, text_changed = fix_text(original_text)
            if text_changed and fixed_text != original_text:
                updated_fields[col_name] = fixed_text
                changes.append({
                    "table": table_name,
                    "rowid": rowid,
                    "column": col_name,
                    "original": original_text,
                    "updated": fixed_text,
                })

        if updated_fields and not dry_run:
            set_clause = ', '.join([f"{col} = ?" for col in updated_fields.keys()])
            update_query = f"UPDATE '{table_name}' SET {set_clause} WHERE rowid = ?"
            values = list(updated_fields.values()) + [rowid]
            cursor.execute(update_query, values)

    if not dry_run:
        conn.commit()

    conn.close()
    print("✅ Done.\n")

    # Reporting
    if changes:
        print("📋 Words changed:" if not dry_run else "📋 Words that would be changed (dry run):")
        for change in changes:
            changed_words = []
            original_text = change["original"]
            updated_text = change["updated"]

            for word, new_word in replacements.items():
                if word in original_text and new_word in updated_text:
                    changed_words.append(f"{word} ➔ {new_word}")

            if any(q in updated_text for q in ['“', '”', '‘', '’']) and not any(q in original_text for q in ['“', '”', '‘', '’']):
                changed_words.append("smart quotes applied")

            if changed_words:
                print(f"- [{change['table']}][row {change['rowid']}][{change['column']}]: {', '.join(changed_words)}")
    else:
        print("No changes detected.")

# Run the script
if __name__ == "__main__":
    process_sqlite_file(sqlite_file)
