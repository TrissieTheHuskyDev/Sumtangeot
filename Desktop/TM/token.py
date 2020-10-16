from bs4 import BeautifulSoup
from konlpy.tag import Hannanum, Kkma, Komoran, Okt
import time
import re

# html 태그 제거 전처리 확인 코드
pattern = '<[^>]*>'
test = BeautifulSoup(test, 'html.parser').get_text()
print(re.sub(pattern=pattern, repl='', string=test))

# 태그별 속도 확인
sentence = test
sentences = [sentence] * 1000

morphs_processors = [('Hannanum', Hannanum()), ('Kkma', Kkma()),
                     ('Komoran', Komoran()), ('Okt', Okt())]
for name, morphs_processor in morphs_processors:
    strat_time = time.time()
    morphs = [morphs_processor.morphs(sentence) for sentence in sentences]
    elapsed_time = time.time() - strat_time
    print('morphs_processor name = %20s, %.5f secs' % (name, elapsed_time))

# 태거별 pos 분리 확인
komoran = Komoran()
hannanum = Hannanum()
okt = Okt()
kkma = Kkma()
# pos 분리가 많아지면 눈으로 확인 불가하므로 top10만 확인
%time print(kkma.pos(test)[:10])
%time print(komoran.pos(test)[:10])
%time print(hannanum.pos(test)[:10])
%time print(okt.pos(test)[:10])
