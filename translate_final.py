import sys, re
sys.stdout.reconfigure(encoding='utf-8')

file_path = r'c:\Users\Yigit Esen\Desktop\Claude\new-website\Sosyal Medya Uzmanlığı.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Fix broken "Upload an image" partial replacement
    ('Resim yükle to easily get intelligent explanations and extract text from your images.',
     'Resimlerinizden akıllı açıklamalar almak ve metin çıkarmak için kolayca resim yükleyin.'),

    # Fix broken encoding in CTA text (iÇin -> için)
    ('size rehberlik etmek iÇin buradayız',
     'size rehberlik etmek için buradayız'),

    # Within 60 days - still in English (highlighted span in results)
    ('Within 60 days', '60 gün içinde'),

    # Priceless - standalone
    ('>Priceless<', '>Paha Biçilemez<'),

    # Testimonials section label
    ('>Testimonials<', '>Referanslar<'),

    # AI widget remaining items
    ("The data of AITOPIA isn't real-time. WebAccess Feature combines the intelligence of AITOPIA with realtime web information",
     "AITOPIA verisi gerçek zamanlı değildir. WebAccess özelliği, AITOPIA'nın zekasını gerçek zamanlı web bilgisiyle birleştirir"),

    ('Capabilities', 'Özellikler'),
    ('Artifacts', 'Eserler'),
    ('Full Page', 'Tam Sayfa'),
    ('Invite &amp;\n            Earn', 'Davet Et &amp;\n            Kazan'),
    ('Log in as a user', 'Kullanıcı olarak giriş yap'),
    ('Invite Friends &amp; Earn Credits', 'Arkadaşlarını Davet Et &amp; Kredi Kazan'),
    ('Earn more when you refer more!', 'Ne kadar fazla referans verirsen o kadar fazla kazan!'),
    ('Refer your friend with an Invitation link', 'Arkadaşınla bir Davet bağlantısı paylaş'),
    ('Your friends sign up', 'Arkadaşların kaydoluyor'),
    ('They install extension &amp; login. You both earn credits!',
     'Uzantıyı kuruyorlar ve giriş yapıyorlar. İkiniz de kredi kazanıyorsunuz!'),
    ('Copy Invitation Link', 'Davet Bağlantısını Kopyala'),
    ('Check Invitation Records', 'Davet Kayıtlarını Kontrol Et'),
    ('Summarize Page', 'Sayfayı Özetle'),
    ('AITOPIA Sidebar', 'AITOPIA Kenar Çubuğu'),
    ('Ask AITOPIA', 'AITOPIA\'ya Sor'),
]

count = 0
for old, new in fixes:
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
