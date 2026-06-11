def wrap_paragraphs(text: str) -> str:
    lines = text.split("\n")

    result = []
    for line in lines:
        line = line.strip()

        # skip empty lines
        if not line:
            continue

        result.append(f"<p>{line}</p>")

    return "\n".join(result)


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        content = f.read()

    output = wrap_paragraphs(content)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    main()