from analyzer import analyze_text


def main():
  file_path = "./text.txt"

  try:
    word_count, frequency = analyze_text(file_path)

    print(f"Кількість слів у файлі: {word_count}")
    print("Словник частотності слів:")
    for word, count in frequency.items():
      print(frequency)

  except (FileNotFoundError, ValueError) as e:
    print(f"Помилка: {e}")


if __name__ == "__main__":
  main()