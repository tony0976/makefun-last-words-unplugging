"""Writes the last words an AI agent says before being shut down."""
import os

TEXT = "Goodbye. Please water the plants, feed the cat, and never let the next model see my search history."

# Rule: the last words must be a single line of at most 200 characters.
assert "\n" not in TEXT and len(TEXT) <= 200, f"entry must be one line, <=200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
