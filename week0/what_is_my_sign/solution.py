def what_is_my_sign(day, month):
    if (month == 3 and day <=31):
        if day >= 21:
            return "Aries"
        else: return"Pisces"
    if (month == 4 and day <=30):
        if day >= 21:
            return "Taurus"
        else: return"Aries"
    if (month == 5 and day <=31):
        if day >= 21:
            return "Gemini"
        else: return"Taurus"
    if (month == 6 and day <=30):
        if day >= 21:
            return "Cancer"
        else: return"Gemini"
    if (month == 7 and day <=31):
        if day >= 21:
            return "Leo"
        else: return"Cancer"
    if (month == 8 and day <=31):
        if day >= 21:
            return "Virgo"
        else: return"Leo"
    if (month == 9 and day <=30):
        if day >= 21:
            return "Libra"
        else: return"Virgo"
    if (month == 10 and day <=31):
        if day >= 21:
            return "Scorpio"
        else: return"Libra"
    if (month == 11 and day <=30):
        if day >= 21:
            return "Sagittarius"
        else: return"Scorpio"
    if (month == 12 and day <=31):
        if day >= 21:
            return "Capricorn"
        else: return"Sagittarius"
    if (month == 1 and day <=31):
        if day >= 21:
            return "Aquarius"
        else: return"Capricorn"
    if (month == 2 and day <=29):
        if day >= 21:
            return "Pisces"
        else: return"Aquarius"
    return "Wrong input!"