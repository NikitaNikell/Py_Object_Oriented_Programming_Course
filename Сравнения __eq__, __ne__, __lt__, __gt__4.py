class Morph:

    def __init__(self, *args):
        self.forms = [i.lower() for i in args]

    def add_word(self, word):
        if word not in self.forms:
            self.forms.append(word.lower())

    def get_words(self):
        return tuple(self.forms)

    def __eq__(self, other):
        return other.lower() in self.forms


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами','формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам','эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = input()
count = 0


for sp in dict_words:
    for slo in text.strip('.').split():
        if slo == sp:
            count += 1

print(count)