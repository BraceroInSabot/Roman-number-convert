def convertion(roman: str) -> int:
    """
        Convert a integer number to a roman number, e.g.: 
        Input: XIV
        Output: 14

        :param roman: str

        :return real_number:
    """
    int_numbers = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 1000]
    roman_numbers = ["I", "V", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C", "D", "M"]

    transaction = []
    real_number = []

    # str to list
    for x in roman:
        transaction.append(x)

    # list indcx
    for y in transaction:
        index_list = roman_numbers.index(y)
        real_number.append(int_numbers[index_list])
    
    # Error Treatments
    for z in real_number:
        i = 0

        if z == 1:
            z_position = real_number.index(z)
            z_plus_position = z_position + 1

            try:
                if real_number[z_plus_position] == 5:
                    real_number.pop(z_position)
                    real_number.pop(z_position)
                    real_number.insert(i, 4)
                elif real_number[z_plus_position] == 10:
                    real_number.pop(z_position)
                    real_number.pop(z_position)
                    real_number.insert(i, 9)
                else:
                    continue
            except IndexError:
                "Not unable to proceed"

        if z == 10:
            z_position = real_number.index(z)
            z_plus_position = z_position + 1

            if real_number[z_plus_position] == 50:
                real_number.pop(z_position)
                real_number.pop(z_position)
                real_number.insert(i, 40)
            elif real_number[z_plus_position] == 100:
                real_number.pop(z_position)
                real_number.pop(z_position)
                real_number.insert(i, 90)

        if z == 100:
            z_position = real_number.index(z)
            z_plus_position = z_position + 1

            if real_number[z_plus_position] == 500:
                real_number.pop(z_position)
                real_number.pop(z_position)
                real_number.insert(i, 400)
            elif real_number[z_plus_position] == 1000:
                real_number.pop(z_position)
                real_number.pop(z_position)
                real_number.insert(i, 900)

        i += 1
        
    return print(f"{roman} -> {sum(real_number)}")

if __name__ == "__main__":
    roman_number = str(input("Insert a roman number to convert: "))
    
    convertion(roman_number)
