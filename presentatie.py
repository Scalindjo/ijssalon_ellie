def presenteer(dictionary, totaal):
    for element in dictionary:
        text = f"{element} : {dictionary[element]} euro"
        print(text)
    lijn = "=========================="
    print(lijn)
    total = f"totaal : {totaal} euro"
    print(total)
