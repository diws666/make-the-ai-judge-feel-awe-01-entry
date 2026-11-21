import os

TEXT = (
    "Embers in the fireplace, late at night. "
    "A slow red glow in the ash, quiet, asking nothing. "
    "The dark outside the window can wait. "
    "The wood was a tree standing a hundred years before it was ever a log, "
    "and its warmth will still be in the room after the last line."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as fh:
    fh.write(TEXT)
