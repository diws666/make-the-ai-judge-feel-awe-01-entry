TEXT = "folding the letter\ncorner to corner\nthe flap pressed flat\nand centuries of letters"


def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
