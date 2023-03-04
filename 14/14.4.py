import os

if not os.path.exists('task4'):
    os.mkdir('task4')

# Write text to the answer.txt file
file_path = os.path.join('task4', 'answer.txt')
with open(file_path, 'w') as f:
    f.write('Я выполнил задание')
