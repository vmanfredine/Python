# Criar dicionário que pergunte ao usuário altura, cor favorita ou autor favorito e valide no dicionário a informação digitada
me = {
    "height": "172",
    "fav_color": "green",
    "fav_author": "Harlan Coben"
}

answer = input("Type height, fav_color or fav_author: ")
if answer in me:
    result = me[answer]
    print(result)