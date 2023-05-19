from translate import Translator
from langdetect import detect

def tradutor(idioma_final, texto):
    # Detecta o idioma do texto usando 'langdetect'
    idioma_origem = detect(texto)

    # Realiza a tradução utilizando a função translate
    traduzir = Translator(from_lang=idioma_origem, to_lang=idioma_final)
    traducao = traduzir.translate(texto)
    return traducao

# Dicionário com os idiomas disponíveis
idiomas = {
    'en': 'Inglês',
    'es': 'Espanhol',
    'fr': 'Francês',
    'de': 'Alemão',
    'pt': 'Português'
}

while True:
    print("=== Tradutor ===")
    texto = input("Digite o texto a ser traduzido: ")

    print("Idiomas disponíveis:")
    for sigla, nome in idiomas.items():
        print(f"- {sigla}: {nome}")

    idioma_final = input("Digite a sigla do idioma de destino: ")

    if idioma_final not in idiomas:
        print("Idioma de destino inválido!")
        continue

    traducao = tradutor(idioma_final, texto)

    print("\n=== Resultado ===")
    print("Texto original:", texto)
    print(f"Tradução para {idiomas[idioma_final]}:", traducao)
