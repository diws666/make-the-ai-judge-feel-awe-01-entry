TEXT = "starlight left that star before your first clock tick\nit is still on its way\nand it keeps arriving\n"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
