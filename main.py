import eel


eel.init(".")

@eel.expose
def bmi_calc(height, weight):
    if height != "":
        if weight != "":
            bmi = int(weight)/((int(height)/100)**2)
            if bmi < 18.5:
                return 'Your BMI is ' + format(bmi, '.1f') + ' (Underweight)'
            elif bmi > 18.5 and bmi < 24.9:
                return 'Your BMI is ' + format(bmi, '.1f') + ' (Normal)'
            elif bmi > 24.5 and bmi < 29.9:
                return 'Your BMI is ' + format(bmi, '.1f') + ' (Overweight)'
            elif bmi > 29.9 and bmi < 200:
                return 'Your BMI is ' + format(bmi, '.1f') + ' (Obesity)'
            else:
                return 'YOU BROKE THE SYSTEM!!!'
        else:
            return 'Weight is EMPTY!!'
    else:
        return 'Height is EMPTY!!'

eel.start('index.html', size=(800, 600))