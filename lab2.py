from googletrans import Translator, LANGUAGES
import re

translator = Translator()

def CodeLang(lang):
    lang = lang.lower().strip()
    if lang in LANGUAGES:
        return lang
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return None

def LangDetect(text):
    try:
        det = translator.detect(text)
        lang_code = det.lang
        lang_name = LANGUAGES.get(lang_code, "unknown")
        return lang_code, lang_name
    except Exception as e:
        return None, f"Помилка: {e}"

def TransLate(text, lang):
    try:
        lang_code = CodeLang(lang)
        if not lang_code:
            return "Помилка: мову не знайдено"

        # 1. Розбиваємо вхідний текст на окремі речення.
        # Шукаємо кінець речення (.!?) за яким йдуть пробіли, і ділимо текст.
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        
        translated_sentences = []
        
        # 2. Перекладаємо кожне речення ОКРЕМО
        for sentence in sentences:
            if sentence.strip(): # Якщо речення не порожнє
                res = translator.translate(sentence, dest=lang_code)
                translated_sentences.append(res.text.strip())

        # 3. Склеюємо перекладені речення акуратно через один пробіл
        final_translation = ' '.join(translated_sentences)

        return final_translation

    except Exception as e:
        return f"Помилка перекладу: {e}"

if __name__ == "__main__":
    txt = "Доброго дня. Як справи? Сподіваюсь, все добре."
    target_lang = "en"

    code, name = LangDetect(txt)
    
    # Вивід результатів
    print("-" * 50)
    print(f"Вхідний текст:    {txt}")
    print(f"Виявлена мова:    {name} ({code})")
    print(f"Результат ({target_lang}):  {TransLate(txt, target_lang)}")
    print("-" * 50)

    # Інтерактивний режим
    print("\nСпробуйте свій варіант:")
    user_text = input("Введіть текст: ")
    user_lang = input("Введіть мову: ")

    result = TransLate(user_text, user_lang)
    print(f"\nРезультат: {result}")