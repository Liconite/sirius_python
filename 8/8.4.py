def BMI(w, h):
    index = w / (h **2)
    if index < 18.5:
        return "Недостаточный вес"
    if 18.5 <= index <= 25:
        return "ИМТ в норме"
    if index > 25:
        return "Избыточный вес"


weight, height = int(input()), int(input())
print(BMI(weight, height))
