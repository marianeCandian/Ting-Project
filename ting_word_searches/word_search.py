def exists_word(word, instance):
    occurrences = []

    for item in instance._data:
        file_name = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        file_occurrences = []

        for i, line in enumerate(lines):
            if word.lower() in line.lower():
                file_occurrences.append({"linha": i + 1})

        if file_occurrences:
            file_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": file_occurrences,
            }
            occurrences.append(file_info)

    return occurrences


def search_by_word(word, instance):
    occurrences = []

    for item in instance._data:
        file_name = item["nome_do_arquivo"]
        lines = item["linhas_do_arquivo"]
        file_occurrences = []

        for i, line in enumerate(lines):
            if word.lower() in line.lower():
                line_content = line.strip()
                file_occurrences.append(
                    {"linha": i + 1, "conteudo": line_content}
                )

        if file_occurrences:
            file_info = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": file_occurrences,
            }
            occurrences.append(file_info)

    return occurrences
