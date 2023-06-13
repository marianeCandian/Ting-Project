from ting_file_management import txt_importer


def process(path_file, instance):
    file_name = path_file.split("/")[-1]

    if any(item["nome_do_arquvo"] == file_nema for item in instance._data):
        return None

    lines = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(dict)

    print(dict)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
