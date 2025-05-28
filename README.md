python manage.py makemigrations

python manage.py migrate

python manage.py shell

# shell içinde çalıştırmak için
from englishubdjango_app_api.models import Type, Level, Question, Option

# 1. Type verileri
vocab = Type.objects.create(name='Vocabulary')
reading = Type.objects.create(name='Reading')
grammar = Type.objects.create(name='Grammar')

# 2. Level verileri (her bir type için A1–C2)
levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
level_objs = []
for t in [vocab, reading, grammar]:
    for l in levels:
        level_objs.append(Level.objects.create(name=l, type=t))

# 3. Örnek Question ve Option verisi
# Örneğin, Vocabulary - A1 seviyesi için 1 soru ve 4 seçenek:
vocab_a1 = Level.objects.get(name='A1', type=vocab)
q1 = Question.objects.create(description='Choose the correct word for "apple".', level=vocab_a1)

Option.objects.create(description='Apple', question=q1)
Option.objects.create(description='Table', question=q1)
Option.objects.create(description='Run', question=q1)
Option.objects.create(description='Blue', question=q1)

# Grammar - B2 için 1 soru
grammar_b2 = Level.objects.get(name='B2', type=grammar)
q2 = Question.objects.create(description='Which sentence is grammatically correct?', level=grammar_b2)

Option.objects.create(description='He go to school.', question=q2)
Option.objects.create(description='He goes to school.', question=q2)
Option.objects.create(description='He going to school.', question=q2)
Option.objects.create(description='He gone to school.', question=q2)

# Reading - C1 için 1 soru
reading_c1 = Level.objects.get(name='C1', type=reading)
q3 = Question.objects.create(description='What is the main idea of the passage?', level=reading_c1)

Option.objects.create(description='To describe a scientific process.', question=q3)
Option.objects.create(description='To tell a personal story.', question=q3)
Option.objects.create(description='To explain a political issue.', question=q3)
Option.objects.create(description='To introduce a character.', question=q3)
