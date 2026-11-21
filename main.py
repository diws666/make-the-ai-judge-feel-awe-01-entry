TEXT = "rain on the tin roof\none drop at a time\nthe yard puddles\nthe sky rests in it"

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
