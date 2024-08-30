def leap_year() -> str:
    year: int = int(input("Ingrese un año: "))
    if year % 100 == 0:
        if year % 400 == 0:
            return f"El año {year} es bisiesto"
        else:
            return f"El año {year} no es bisiesto"
    else:
        if year % 4 == 0:
            return f"El año {year} es bisiesto"
        else: 
            return f"El año {year} no es bisiesto"
