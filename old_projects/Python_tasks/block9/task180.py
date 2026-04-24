def check_words_in_sentences(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = set(sentence2.split())

    results = {}
    for word in words1:
        results[word] = word in words2

    return results


sentence1 = "Какой интересный вопрос о автоматизации."
sentence2 = "Автоматизация интересна и полезна."

results = check_words_in_sentences(sentence1, sentence2)

for word, exists in results.items():
    print(f"Слово '{word}' {'входит' if exists else 'не входит'}\
        во второе предложение.")
