import os

ENTRY = (
    "The moon rises over the sleeping roofs of the quiet town, and the same slow light "
    "falls as it fell a hundred years ago and will fall long after tonight. "
    "The streets are dark and still, nothing moving except the moon's slow arc. "
    "The light keeps travelling after this line ends."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
