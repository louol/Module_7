team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Использование %:
summary_line_team1 = "В команде %s, участников: %s" % (team1_name, team1_num)
summary_line_total = "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num)

# Использование format():
summary_line_score_2 = "Команда {} решила {} задач!".format(team2_name, score_2)
summary_line_time = "Команда {} решили задачи за {} с ".format(team2_name, team2_time)

# Использование f-строк:
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = f'Команда {team1_name} победила!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = f'Команда {team2_name} победила!'
else:
    challenge_result = 'Ничья!'

summary_line_scores = f"Команды решили {score_1} и {score_2} задач."
summary_line_result = f"Результат битвы:  {challenge_result}!"
summary_line_tasks = f"Сегодня было решено {tasks_total} задач, в среднем по  {time_avg} секунды на задачу!."

print(summary_line_team1)
print(summary_line_total)
print(summary_line_score_2)
print(summary_line_time)
print(summary_line_scores)
print(summary_line_result)
print(summary_line_tasks)

