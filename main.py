from pathlib import Path

TEXT = (
    "The night train crosses the plain with wheels keeping their even slow "
    "beat on rails laid before anyone was born. Dark fields slide past the "
    "window, night grows deeper. The plain outlasts the rails, asking "
    "nothing; the wheels keep even pace after the last line."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
