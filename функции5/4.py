ingredients = [0, 0, 0]

recipes = {
    "Эспрессо":         [1, 0, 0],
    "Капучино":         [1, 3, 0],
    "Маккиато":         [2, 1, 0],
    "Кофе по-венски":   [1, 0, 2],
    "Латте Маккиато":   [1, 2, 1],
    "Кон Панна":        [1, 0, 1],
}

def choose_coffee(*preferences):
    global ingredients
    for drink in preferences:
        if drink in recipes:
            need = recipes[drink]
            if all(ingredients[i] >= need[i] for i in range(3)):
                for i in range(3):
                    ingredients[i] -= need[i]
                return drink
    return "К сожалению, не можем предложить Вам напиток"
