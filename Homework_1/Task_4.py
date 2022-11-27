# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

quarter_number = int(input('Please write the number of the quarter: '));
if quarter_number == 1:
    print('x coordinates > 0, y coordinates > 0');
elif quarter_number == 2:
    print('x coordinates < 0, y coordinates > 0');
elif quarter_number == 3:
    print('x coordinates < 0, y coordinates < 0');
elif quarter_number == 4:
    print('x coordinates > 0, y coordinates < 0');
else:
    print("it's not he number of the quarter");
