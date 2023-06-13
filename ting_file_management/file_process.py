from ting_file_management.file_management import txt_importer

processed = set()


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return

    lines = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)

    processed.add(path_file)

    print(data)


def remove(instance):
    if instance.is_empty():
        print("Não há elementos")
        return

    info_to_remove = instance.dequeue()

    path_file = info_to_remove["nome_do_arquivo"]

    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
