import sqlite3
import re
import os

# Define your replacement roots. Note that capitalization of words is preserved.
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
}

# Automatically create replacements including capitalized versions
replacements = {}
for k, v in roots.items():
    replacements[k] = v
    replacements[k.capitalize()] = v.capitalize()

def fix_text(text):
    if text is None:
        return text
    if not isinstance(text, str):
        text = str(text)
    for word, new_word in replacements.items():
        text = re.sub(r'\b{}\b'.format(re.escape(word)), new_word, text)
    return text

def process_sqlite_file(sqlite_path):
    if not os.path.exists(sqlite_path):
        print(f"File not found: {sqlite_path}")
        return

    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    # Find all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for (table_name,) in tables:
        print(f"Scanning table: {table_name}")

        # Get all columns for each table
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()

        text_columns = [col[1] for col in columns if col[2].lower() in ('text', 'varchar', 'char', '')]

        if not text_columns:
            continue

        select_query = f"SELECT rowid, {', '.join(text_columns)} FROM '{table_name}';"
        cursor.execute(select_query)
        rows = cursor.fetchall()

        for row in rows:
            rowid = row[0]
            updated_fields = {}
            for idx, col_name in enumerate(text_columns, start=1):
                original_text = row[idx]
                fixed_text = fix_text(original_text)
                if fixed_text != original_text:
                    updated_fields[col_name] = fixed_text

            if updated_fields:
                set_clause = ', '.join([f"{col} = ?" for col in updated_fields.keys()])
                update_query = f"UPDATE '{table_name}' SET {set_clause} WHERE rowid = ?"
                values = list(updated_fields.values()) + [rowid]
                cursor.execute(update_query, values)
                print(f"Updated row {rowid} in table {table_name}")

    conn.commit()
    conn.close()
    print("Done.")

if __name__ == "__main__":
    sqlite_file = "/path-to-your-Publii-folder/sites/site-name/input/db.sqlite"  # <-- Change this to your SQLite file path
    process_sqlite_file(sqlite_file)
