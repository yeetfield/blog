from pathlib import Path
from sys import argv
from dataclasses import dataclass
from enum import Enum

import re

# Resequences footnotes, assuming that all footnote definitions are the very last part of the file.
# This allows you to write a Markdown file with footnotes defined in any order that comes to mind.
# This will edit your file in-place, so commit often in case it messes up.

class FootnoteType(Enum):
    Reference = 0,
    Definition = 1

@dataclass(frozen=True)
class Footnote:
    type: FootnoteType
    number: int
    line: int
    position: int

def extract_footnotes(i: int, line: str) -> list[Footnote]:
    result = []
    for match in re.finditer("\[\^([0-9]+)\]", line):
        beginning, _ = match.span()
        type = FootnoteType.Definition if beginning == 0 else FootnoteType.Reference
        result.append(Footnote(type, int(match.group(1)), i, beginning))
    return result

def deduplicate(notes: list[Footnote]) -> list[Footnote]:
    seen = set()
    notes_deduplicated = []
    for note in notes:
        if (note.type, note.number) in seen:
            if note.type is FootnoteType.Definition:
                raise RuntimeError(f"Encountered duplicate footnote definition for {note.number}")
            continue
        seen.add((note.type, note.number))
        notes_deduplicated.append(note)
    return notes_deduplicated

def get_new_mapping(notes_unique: list[Footnote]) -> dict[int, int]:
    num_definitions = sum(1 for note in notes_unique if note.type is FootnoteType.Definition)

    new_mapping = dict()
    new_number = 1
    for note in notes_unique:
        if note.type is FootnoteType.Definition:
            continue

        new_mapping[note.number] = new_number
        new_number += 1

    if new_number - 1 != num_definitions:
        raise RuntimeError(f"Encountered a different number of unique references {new_number - 1} and definitions {num_definitions}")
    
    return { key: val for key, val in new_mapping.items() if key != val}

def rewrite_line(line: str, index: int, note_number: int, new_note_number: int) -> str:
    # Account for the offset of the characters in [^], as well as the number itself
    second_part_index = index + 3 + len(str(note_number))
    return f"{line[:index]}[^{new_note_number}]{line[second_part_index:]}" 

def reorder_footnotes(path: Path):
    with open(path) as f:
        lines = f.readlines()

    notes = []
    for i, line in enumerate(lines):
        notes.extend(extract_footnotes(i, line))
    
    notes_unique = deduplicate(notes)
    new_mapping = get_new_mapping(notes_unique)
    
    for note in notes:
        if note.number not in new_mapping:
            continue
        lines[note.line] = rewrite_line(lines[note.line], note.position, note.number, new_mapping[note.number])
 
    definition_lines = {note.line: new_mapping.get(note.number, note.number) for note in notes_unique if note.type is FootnoteType.Definition}
    rev_map = {value: key for key, value in definition_lines.items()}

    with open(path, "w") as f:
        f.writelines(line for i, line in enumerate(lines) if i not in definition_lines)
        for new_note_number in sorted(definition_lines.values()):
            definition_line = lines[rev_map[new_note_number]].strip()
            f.write(f"{definition_line}\n")

def main():
    if len(argv) < 2:
        raise RuntimeError("Please provide paths to Markdown files to be processed")
    
    paths = [Path(path) for path in argv[1:]]
    for path in paths:
        if not path.exists():
            raise RuntimeError(f"Provided path: {path} does not exist")

    for path in paths:
        reorder_footnotes(path)

if __name__ == "__main__":
    main()