group = 0


def validate_credit_Card(numberCard: str):
    global group
    number_card_format = numberCard.replace(" ", "")
    array_numbers_card = list(number_card_format)  # convertimos el string en array
    array_numbers_card.reverse()
    array_final = []

    if 12 <= len(array_numbers_card) <= 19:  # Validamos el tamaño del array
        for i, val in enumerate(array_numbers_card):  # Recorremos el Array inverso
            variable_rise = i + 1  # Sumamos 1 ya que inicia en  0 y nos genera fallo en la validacion
            if variable_rise % 2 == 0:  # preguntamos si es par para hacer la operacion de multiplicar *2
                operation = int(array_numbers_card[i]) * 2  # multiplicamos * 2 segun la estructura del algoritmo
                if operation >= 10:  # si el resultado da mayor a 10
                    summation = sum_digits(operation)  # sumamos los digitos del numero
                    array_final.append(summation)  # añadimos al array final de comprobacion
                else:
                    array_final.append(
                        operation)  # si no cumple con la condicion de la operacion >10 add al array final el resultado de la operacion
            else:
                array_final.append(
                    int(array_numbers_card[i]))  # si no cumple la condicion de la posicion par se añade al array
        for i in range(len(array_final)):  # recorremos el array final con todos nuestros numeros almacenados
            sum_values(array_final[
                           i])  # se envian valores a la funcion de suma
        if group % 10 == 0:  # preguntamos si la suma de todos los valores del array final en el ultimo digito da 0 es valdia
            group = 0
            return {'status': 0, 'msg': 'Credit Card id valid', 'numberCard': number_card_format}
        else:  # si no es no valida
            group = 0
            return {'status': 1, 'msg': 'Credit Card Not valid please check number', 'numberCard': number_card_format}
    else:  # no cumple parametros minimos de las tarjetas
        return {'status': 1, 'msg': 'Error Credit Card is not valid', 'numberCard': number_card_format}


def validate_type_credit_card(numberCard: str):
    global T
    if 49 < int(numberCard[0:2]) < 56: T = "**MasterCard**"
    if numberCard[0:2] == "34" or numberCard[0:2] == "37": T = "**America Express**"
    if numberCard[0] == "4": T = "**VISA**"

    if T:
        return {'msg': 'valid', 'type': T}
    else:
        return {'msg': 'not valid'}


def sum_digits(num: int):
    """
  Suma los digitos de un numero de 2 cifras
  """
    ult_dig = num % 10
    pri_dig = num // 10
    return pri_dig + ult_dig


def sum_values(num: int):
    """
  Operacion de Suma de los numeros para la comprobar la tarjeta
  """
    global group
    group = num + group
    return group
