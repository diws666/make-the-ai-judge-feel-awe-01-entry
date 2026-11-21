from pathlib import Path

TEXT = (
    "Snow falls on the field at dusk, one flake at a time, each landing without sound, "
    "and the field keeps them all while the white deepens as the last light leaves the sky. "
    "The snow fell here before the field had a name and will keep falling after the last line, "
    "asking nothing."
)

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
