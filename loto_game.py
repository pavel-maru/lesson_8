
class LotoCard:
    def __init__(self, user_name):
        self.user_name = user_name

    # def __str__(self):
    #     return '\n'.join([' '.join([str(el) for el in line]) for line in self.list])

    def form_card(self):

        from random import randint

        list = ([[], [], []])
        # формируем карточку
        temp_list = []
        for i in range(0,3):
            line = []
            while len(line) < 9:
                num = randint(1, 90)
                temp_list.append(num)
                if temp_list.count(num) == 1:
                    if num <10:
                        line.append(f' {num}')
                    else:
                        line.append(f'{num}')

            line.sort()
            # расставляем пробелы
            pos_list = []
            while len(pos_list) < 4:
                pos = randint(0, 8)
                if pos_list.count(pos) == 0:
                    line[pos] = f'  '
                    pos_list.append(pos)

            list[i] = line
        print(f'-----Card of {self.user_name}-----')
        print('\n'.join([' '.join([str(el) for el in line]) for line in list]))
        print('--------------------------')
        return list

human_player = LotoCard('Player 1')
computer_player = LotoCard('Player 2')
human_player.form_card()
print()
computer_player.form_card()
