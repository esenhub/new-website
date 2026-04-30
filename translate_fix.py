import sys, re
sys.stdout.reconfigure(encoding='utf-8')

file_path = r'c:\Users\Yigit Esen\Desktop\Claude\new-website\Sosyal Medya Uzmanlığı.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

em = '—'  # real em dash — as in the HTML file
lq = '“'  # left double quote "
rq = '”'  # right double quote "
apos = '’'  # right single quote / apostrophe '
ellipsis = '…'  # …

fixes = [
    # Summary bullet lines (file uses em dash —)
    (f'Synthesise AI {em} 12 months unlimited access',
     f'Synthesise AI {em} 12 ay sınırsız erişim'),
    (f'Dijital \xdcr\xfcn Form\xfcl\xfc 2.0 {em} Eksiksiz eğitim', None),  # skip - already done by name
    (f'Digital Product Formula {em} Complete training',
     f'Dijital \xdcr\xfcn Form\xfcl\xfc {em} Eksiksiz eğitim'),
    (f'Perfect Product Insurance {em} 60-day safety net',
     f'M\xfckemmel \xdcr\xfcn Sigortası {em} 60 g\xfcnl\xfck g\xfcvenlik ağı'),
    (f'Ghostwriter OS {em} 12 months unlimited access',
     f'Ghostwriter OS {em} 12 ay sınırsız erişim'),
    (f'AskIman AI {em} My 24/7 AI clone',
     f'AskIman AI {em} 7/24 Yapay Zeka klonum'),
    (f'Monetise Mania {em} 90-day competition',
     f'Monetise Mania {em} 90 g\xfcnl\xfck yarışma'),
    (f'Dedicated Support {em} Weekly Q&amp;A + success team',
     f'\xd6zel Destek {em} Haftalık Soru-Cevap + başarı ekibi'),

    # Guarantee header with curly quotes
    (f'Our {lq}Work-With-You-Until-You-Win{rq} Guarantee',
     f'{lq}Kazanana Kadar Seninle \xc7alışırız{rq} Garantimiz'),

    # Urgency - curly quotes
    (f'There is no {lq}come back next month{rq} or second chance waiting for you.',
     f'{lq}Gelecek ay geri gel{rq} ya da seni bekleyen ikinci bir şans yok.'),

    # CTA - curly apostrophe
    (f'We{apos}re here to answer any questions and guide you to success every step of the way. Schedule a call and get personalized support whenever you need it.',
     'T\xfcm sorularınızı yanıtlamak ve başarıya giden her adımda size rehberlik etmek i\xc7in buradayız. G\xf6r\xfcşme planlayın ve ihtiya\xe7 duyduğunuzda kişisel olarak destek alın.'),

    # UpLevel - curly apostrophe
    (f'Usually, the only way to get access to my team like this would be to enroll into our UpLevel program, which clients pay $7,800 for, but you{apos}re getting this as part of Monetise.',
     'Normalde, ekibime bu şekilde erişmenin tek yolu, m\xfcşterilerin $7.800 \xf6dediği UpLevel programımıza kaydolmaktır; ancak bunu Monetise{apos}in bir par\xe7ası olarak alıyorsun.'.replace('{apos}', apos)),

    # Taking care - uses ellipsis not dash
    (f'taking care of 2 kids</strong> at the same time{ellipsis}',
     f'aynı anda 2 \xe7ocuğuna bakarak{ellipsis}'),

    # Armando with <strong> tag inside
    (f'Or Armando, a 19-years-old who came from immigrant parents, <strong class="framer-text">made $111k and bought himself a McLaren:</strong>',
     f'Ya da g\xf6\xe7men ailelerden gelen 19 yaşındaki Armando, <strong class="framer-text">111 bin dolar kazanıp kendine bir McLaren aldı:</strong>'),

    # Testimonial with curly apostrophe
    (f'Iman it{apos}s been part of the big change that I took as a person, in so grateful for what he{apos}s done. This program 10/10 too.',
     f'Iman, bir insan olarak aldığım b\xfcy\xfck değişimin par\xe7ası oldu, yaptıkları i\xe7in \xe7ok minnettarım. Bu program da 10/10.'),

    # Second time - has inline spans, translate surrounding text
    ('The second time, we refined it and opened it up again. <span class="framer-text"',
     'İkinci seferde sistemi geliştirip yeniden a\xe7tık. <span class="framer-text"'),
    ('they had already surpassed the first challenge at $9.8M. By the 90th day:',
     '60 g\xfcn i\xe7inde ilk meydan okumayı $9,8M ile ge\xe7tiler. 90. g\xfcnde:'),

    # "making care" segment already handled but let's also handle the part with "taking care"
    ('">taking care of 2 kids</strong>',
     '">aynı anda 2 çocuğuna bakarak</strong>'),
]

count = 0
for old, new in fixes:
    if new is None:
        continue
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f'  FIXED: {old[:70]}')
    else:
        print(f'  NOT FOUND: {old[:70]}')

print(f'\nFixes applied: {count}')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('File saved.')
