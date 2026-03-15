import datetime

def garden_advice():
    month = datetime.datetime.now().month
# ///
    if month in [12, 1, 2]:
        print("Summer: Water plants frequently and protect from heat.")
    elif month in [3, 4, 5]:
        print("Autumn: Prepare soil and plant cool season vegetables.")
    elif month in [6, 7, 8]:
        print("Winter: Protect plants from frost.")
    elif month in [9, 10, 11]:
        print("Spring: Plant flowers and vegetables.")

garden_advice()
# ****
