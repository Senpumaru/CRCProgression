import os
import numpy as np
import pickle
import numpy as np
from sklearn.metrics import accuracy_score, roc_curve, confusion_matrix, classification_report, auc

# Software
while True:
    data_array = np.array([])
    yes_choices = ["YES", "Y"]
    no_choices = ["NO", "N"]

    print("\n ### \n"
          "\n ### \n"
          "Система оценки прогрессирования пациента в течении 1 года: \n"
          "\n ### \n"
          "WARNING: ВСЕ ДАННЫЕ ДОЛЖНЫ БЫТЬ ГОТОВЫ ПЕРЕД НАЧАЛОМ. \n"
          "\n ### \n"
          "Укажите параметры: ")

    a = input("Мутация в регионе KRAS: (Y/N)").upper()
    if a in yes_choices:

        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    a = input("Мутация в регионе BRAF V600E: (Y/N)").upper()
    if a in yes_choices:

        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    a = input("Локализация левостороняя или правосторонняя: (LEFT/RIGHT)").upper()
    if a == "LEFT":
        data_array = np.concatenate((data_array, np.array([0])))
    elif a == "RIGHT":
        data_array = np.concatenate((data_array, np.array([1])))
    else:
        print("Укажите LEFT/RIGHT.")

    a = input("Выберите pT: (T1/T2/T3/T4)").upper()
    if a in ["T1", "T2"]:
        data_array = np.append(data_array, np.array([1, 0]))
    elif a == "T3":
        data_array = np.append(data_array, np.array([1, 0]))
    elif a == "T4":
        data_array = np.append(data_array, np.array([0, 1]))
    else:
        print("Укажите T1/T2/T3/T4.")

    a = input("Выберите pN: (N0/N1/N2)").upper()
    if a == "N0":
        data_array = np.append(data_array, np.array([1, 0, 0]))
    elif a == "N1":
        data_array = np.append(data_array, np.array([0, 1, 0]))
    elif a == "N2":
        data_array = np.append(data_array, np.array([0, 0, 1]))
    else:
        print("Укажите N0/N1/N2.")

    a = input("Грейд высокий или низкий: (HIGH/LOW)").upper()
    if a == "HIGH":
        data_array = np.concatenate((data_array, np.array([0])))
    elif a == "LOW":
        data_array = np.concatenate((data_array, np.array([1])))
    else:
        print("Укажите HIGH/LOW.")

    a = input("Венозная инвазия: (Y/N)").upper()
    if a in yes_choices:

        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    a = input("Лимфоидная инвазия: (Y/N)").upper()
    if a in yes_choices:

        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    a = input("Периневральная инвазия: (Y/N)").upper()
    if a in yes_choices:

        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    a = input("S: (Y/N)").upper()
    if a in yes_choices:
        data_array = np.concatenate((data_array, np.array([1])))
    elif a in no_choices:
        data_array = np.concatenate((data_array, np.array([0])))
    else:
        print("Укажите Y/N.")

    # Load the model from disk
    filename = "Model.sav"
    loaded_model = pickle.load(open(os.path.join(os.getcwd(), filename), 'rb'))
    predictions = loaded_model.predict(data_array.reshape(1, -1))
    predictions_prob = loaded_model.predict_proba(data_array.reshape(1, -1))
    print(
        "\n ### \n"
        "Статус:", predictions,
        "Вероятность:", predictions_prob[0],
        "Конец анлиза.")

    while True:
        answer = input("Хотите провести новый анализ? (Y/N): ")
        if answer in ("Y", "N"):
            break
        print("Неверный ввод.")
    if answer == "Y":
        continue
    else:
        print("Пишитие о багах на сайте https://github.com/Senpumaru/CRCProgression.")
        break
