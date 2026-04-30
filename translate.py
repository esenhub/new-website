import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = r'c:\Users\Yigit Esen\Desktop\Claude\new-website\Sosyal Medya Uzmanlığı.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Translation map: longer/more specific strings first
replacements = [
    # ========== HERO ==========
    ("Either you 10x your investment with this offer, or we'll keep working with you until you do.",
     "Bu teklifle yatırımını 10 katına çıkarırsın ya da biz bunu sağlayana kadar seninle çalışmaya devam ederiz."),

    ("GET ACCESS NOW", "ŞİMDİ ERİŞ"),
    ("The Complete", "Eksiksiz"),
    ("AI Business System", "Yapay Zeka İş Sistemi"),

    # ========== PAIN POINTS ==========
    ("No Experience", "Deneyim Gerekmez"),
    ("No Showing Your Face", "Yüzünü Gösterme Zorunluluğu Yok"),
    ("No Audience", "Kitleye Gerek Yok"),
    ("No Quitting Your 9-5", "9'dan 5'e İşinden Ayrılmak Zorunda Değilsin"),
    ("No Content Creation", "İçerik Üretme Zorunluluğu Yok"),
    ("No Ad Spend", "Reklam Harcaması Gerekmez"),

    # ========== RESULTS SECTION ==========
    ("The first time I made this system available, people who implemented it generated",
     "Bu sistemi ilk sunduğumda, uygulayan kişiler"),
    ("$8.9 million", "$8,9 milyon"),
    ("in tracked sales in less than 90 days.",
     "takip edilen satışa ulaştı ve bu 90 günden kısa sürdü."),
    ("The second time, we refined it and opened it up again. Within 60 days they had already surpassed the first challenge at $9.8M. By the 90th day: $15 million.",
     "İkinci seferde sistemi geliştirip yeniden açtık. 60 gün içinde ilk meydan okumayı $9,8M ile geçtiler. 90. günde: $15 milyon."),
    ("And now, for the 3rd and final time, we expect even",
     "Ve şimdi, 3. ve son kez, daha da"),
    ("bigger results.", "büyük sonuçlar bekliyoruz."),
    ("It Works", "İşe Yarıyor"),
    ("No Matter Where You Are", "Nerede Olursan Ol"),
    ("The first 2 times I ran this Live Challenge, I saw people with completely different realities succeeding with this.",
     "Bu Canlı Meydan Okumayı ilk 2 kez yürüttüğümde, tamamen farklı koşullardaki insanların bununla başardığını gördüm."),
    ("Like Zada, who", "Zada gibi, o"),
    ("made $120K", "120 bin dolar kazandı"),
    ("while taking care of 2 kids at the same time—",
     "aynı anda 2 çocuğuna bakarak—"),
    ("Or Armando, a 19-years-old who came from immigrant parents, made $111k and bought himself a McLaren:",
     "Ya da göçmen ailelerden gelen 19 yaşındaki Armando, 111 bin dolar kazanıp kendine bir McLaren aldı:"),

    # ========== OFFERS ==========
    ("OFFER 1", "TEKLİF 1"),
    ("OFFER 2", "TEKLİF 2"),
    ("OFFER 3", "TEKLİF 3"),
    ("OFFER 4", "TEKLİF 4"),

    # Synthesise AI
    ("Value: $2,999", "Değer: $2.999"),
    ("The specialised AI that effortlessly builds an entire digital product FOR you, trained on $3 billion in real sales data from Whop.\n\nI used it myself to build one product in under 60 minutes. It made $370,000 in 30 days.",
     "Whop'tan gelen 3 milyar dolarlık gerçek satış verisiyle eğitilmiş, sizin için eksiksiz bir dijital ürünü zahmetsizce oluşturan özelleşmiş yapay zeka.\n\nBen kendim 60 dakikadan kısa sürede bir ürün oluşturmak için kullandım. 30 günde $370.000 kazandırdı."),
    ("Knows what's already selling, where the gaps are, and what buyers want right now",
     "Neyin sattığını, boşlukların nerede olduğunu ve alıcıların şu an ne istediğini bilir"),
    ("Builds the research, product, structure, and assets, completely hands-free",
     "Araştırma, ürün, yapı ve varlıkları tamamen eller serbest şekilde oluşturur"),
    ("Unlimited credits for 12 months, create as many products as you want, fail as many times as you want, at zero extra cost",
     "12 ay boyunca sınırsız kredi, istediğin kadar ürün yarat, istediğin kadar başarısız ol, sıfır ekstra maliyet"),

    # Digital Product Formula 2.0
    ("Digital Product Formula 2.0", "Dijital Ürün Formülü 2.0"),
    ("Value: $1,495", "Değer: $1.495"),
    ("The exact step-by-step blueprint used by every person on the leaderboard during the last two challenges.\n\nWatch over my shoulder as I build from absolute zero, every click, every strategy, every decision mapped out so you just copy what I do.",
     "Son iki meydan okumada liderlik tablosundaki her kişinin kullandığı adım adım plan.\n\nSıfırdan oluştururken omzumun üzerinden izle, her tıklama, her strateji, her karar haritalanmış; sadece benim yaptığımı kopyala."),
    ("Complete training from zero to launched business, no guessing, no improvising",
     "Sıfırdan kurulmuş işletmeye kadar eksiksiz eğitim, tahmin yok, doğaçlama yok"),
    ("Follow along in real time with your own product as I build mine",
     "Benimkini kurarken kendi ürününle gerçek zamanlı takip et"),
    ('Every move is mapped so you never wonder "what\'s the next step?"',
     "Her adım haritalanmıştır, bir daha \"sıradaki adım ne?\" diye merak etmezsin"),

    # AskIman AI
    ("AskIman AI (24/7 Access)", "AskIman AI (7/24 Erişim)"),
    ("Value: Priceless", "Değer: Paha Biçilemez"),
    ("My entire 10-year journey, every video, every paid program, thousands of hours of private consulting calls, fed into an AI you can message like a menthor who never sleeps.\n\nThe equivalent of having a multi-millionaire business owner in your pocket around the clock.",
     "10 yıllık tüm yolculuğum, her video, her ücretli program, binlerce saatlik özel danışmanlık görüşmesi — hiç uyumayan bir mentor gibi mesaj atabileceğin bir yapay zekaya aktarıldı.\n\nSaat başı cebinde bir multi-milyoner iş sahibine sahip olmanın eşdeğeri."),
    ("Available 24/7 from your phone or laptop, answers in seconds",
     "Telefonundan veya dizüstü bilgisayarından 7/24 erişilebilir, saniyeler içinde yanıt verir"),
    ("Trained on everything I know after generating $100M+ in this industry",
     "Bu sektörde $100M+ ürettikten sonra bildiğim her şeyle eğitildi"),
    ("Same strategies my private clients pay $25,000+ to access, in your back pocket",
     "Özel müşterilerimin erişmek için $25.000+ ödediği stratejilerin aynısı, cebinde"),

    # Perfect Product Insurance
    ("Perfect Product Insurance Policy", "Mükemmel Ürün Sigorta Poliçesi"),
    ("Value: $7,800", "Değer: $7.800"),
    ("If you don't make your first sale within 60 days, my team, the same team behind a $100M+ company, personally steps in.\n\nThey review your product, diagnose what's broken, and hand you a customised action plan.",
     "60 gün içinde ilk satışını yapmazsan, $100M+ şirketin arkasındaki ekibim devreye girer.\n\nÜrününü incelerler, neyin bozuk olduğunu teşhis ederler ve sana özel bir eylem planı sunarlar."),
    ("60-day safety net, we work with you until you make your first sale",
     "60 günlük güvenlik ağı, ilk satışını yapana kadar seninle çalışırız"),
    ("Same team that's generated $100M+ working directly on YOUR product",
     "$100M+ üretenin aynı ekibi doğrudan SENİN ürünün üzerinde çalışıyor"),
    ("You don't need to trust yourself to get it right, you just need to trust that our team will catch you",
     "Her şeyi doğru yapmana güvenmek zorunda değilsin, sadece ekibimizin seni kurtaracağına güven"),
    ("Usually, the only way to get access to my team like this would be to enroll into our UpLevel program, which clients pay $7,800 for, but you're getting this as part of Monetise.",
     "Normalde, ekibime bu şekilde erişmenin tek yolu, müşterilerin $7.800 ödediği UpLevel programımıza kaydolmaktır; ancak bunu Monetise'in bir parçası olarak alıyorsun."),

    # ========== BONUS ==========
    # Monetise Mania
    ("The competition that generated the $8.9M and $15M results previously. Everyone starts from scratch. Anyone can win.\n\nTop 20 finishers will get an in-person invitation to one of our offices",
     "Daha önce $8,9M ve $15M sonuçlar yaratan yarışma. Herkes sıfırdan başlar. Herkes kazanabilir.\n\nİlk 20 kişi ofislerimizden birine yüz yüze davet alacak"),
    ("90-day competition, everyone starts at zero, no special treatment",
     "90 günlük yarışma, herkes sıfırdan başlar, özel muamele yok"),
    ("Top performers win exclusive prizes worth tens of thousands",
     "En iyi performans gösterenler onlarca bin değerinde özel ödüller kazanır"),
    ('Built-in accountability that turns "I\'ll do it tomorrow" into "I\'m doing it now"',
     '"Yarın yapacağım"ı "Şimdi yapıyorum"a dönüştüren yerleşik hesap verebilirlik'),

    # Dedicated Support
    ("Dedicated Support", "Özel Destek"),
    ("You're Never Alone", "Hiçbir Zaman Yalnız Değilsin"),
    ("No being left alone to figure things out like you're just a number in a system. Inside Monetise, you have a team whose only job is making sure you succeed.",
     "Sisteme girdiğin bir numara gibi tek başına bırakılmazsın. Monetise içinde, tek görevi başarmanı sağlamak olan bir ekibin var."),
    ('Multiple weekly Q&amp;A calls, product creation, topic selection, AI software, or "what should I do next?"',
     'Haftada birden fazla Soru-Cevap görüşmesi, ürün oluşturma, konu seçimi, yapay zeka yazılımı veya "sıradaki ne yapmalıyım?"'),
    ("Success team actively answering questions in the community throughout your entire journey",
     "Tüm yolculuğun boyunca toplulukta aktif olarak soruları yanıtlayan başarı ekibi"),
    ("Live welcome call with Rebecca from our success team the moment you sign up, onboarding you personally",
     "Kaydolduğun anda başarı ekibimizden Rebecca ile canlı hoş geldiniz görüşmesi, seni kişisel olarak karşılıyor"),

    # Ghostwriter OS
    ("The specialised AI that writes product pages that actually convert, trained on pages that have generated hundreds of millions in digital product sales.\n\nTell it what your product is. It writes the page in under a minute.",
     "Gerçekten dönüşüm sağlayan ürün sayfaları yazan özelleşmiş yapay zeka, dijital ürün satışlarında yüz milyonlar üreten sayfalarda eğitilmiş.\n\nÜrününün ne olduğunu söyle. Sayfayı bir dakikadan kısa sürede yazar."),
    ("Applies the same persuasion techniques the best copywriters charge five figures to produce manually",
     "En iyi metin yazarlarının manuel olarak üretmek için beş haneli ücret talep ettiği ikna tekniklerinin aynısını uygular"),
    ("Iman paid over $407,850 in licensing fees in the last 6 months just to let you keep access this tool to this tool inside Monetise",
     "Iman, bu araca Monetise içinde erişiminizi sürdürebilmeniz için son 6 ayda lisans ücretlerinde $407.850'den fazla ödedi"),
    ("12 months of unlimited credits at no extra cost so you can write as many pages as you want (this is how you scale your income",
     "Ekstra maliyet olmadan 12 aylık sınırsız kredi, istediğin kadar sayfa yaz (gelirinizi böyle ölçeklendirirsiniz"),

    # ========== SUMMARY ==========
    ("Everything You Get Inside Monetise:", "Monetise İçinde Aldığınız Her Şey:"),
    ("Synthesise AI � 12 months unlimited access", "Synthesise AI — 12 ay sınırsız erişim"),
    ("Digital Product Formula � Complete training", "Dijital Ürün Formülü — Eksiksiz eğitim"),
    ("Perfect Product Insurance � 60-day safety net", "Mükemmel Ürün Sigortası — 60 günlük güvenlik ağı"),
    ("Ghostwriter OS � 12 months unlimited access", "Ghostwriter OS — 12 ay sınırsız erişim"),
    ("AskIman AI � My 24/7 AI clone", "AskIman AI — 7/24 Yapay Zeka klonum"),
    ("Monetise Mania � 90-day competition", "Monetise Mania — 90 günlük yarışma"),
    ("Dedicated Support � Weekly Q&amp;A + success team", "Özel Destek — Haftalık Soru-Cevap + başarı ekibi"),
    ("Financing available at checkout", "Ödeme sırasında finansman mevcut"),

    # ========== GUARANTEE ==========
    ("\U0001f512 Work-With-You-Until-You-Win Guarantee: 10x your investment or we keep working with you until you do.",
     "\U0001f512 Kazanana Kadar Seninle Çalışırız Garantisi: Yatırımını 10 katına çıkar ya da biz bunu sağlayana kadar seninle çalışmaya devam ederiz."),
    ("Our �Work-With-You-Until-You-Win� Guarantee",
     '"Kazanana Kadar Seninle Çalışırız" Garantimiz'),
    ("Apart from the regular 7-Day No-Questions-Asked Money-Back Guarantee, we have an even better guarantee in place:",
     "Normal 7 günlük sorgusuz sualsiz para iade garantisinin yanı sıra, çok daha iyi bir garantimiz var:"),
    ("When you join Monetise,", "Monetise'e katıldığında,"),
    ("you either 10x your investment, or we keep working with you until you do, up until 3 years.",
     "ya yatırımını 10 katına çıkarırsın, ya da bunu sağlayana kadar 3 yıla kadar seninle çalışmaya devam ederiz."),
    ("We'll never charge you another dollar for updates. We'll keep consulting you, keep giving you access to new programs.",
     "Güncellemeler için seni bir dolar daha ücretlendirmeyeceğiz. Danışmanlık yapmaya, yeni programlara erişim vermeye devam edeceğiz."),

    # ========== SOCIAL PROOF ==========
    ("Don't Take My Word For It", "Bana Güvenmek Zorunda Değilsin"),
    ("Over the last 12 months, we've made multiple updates inside Monetise. And we'll keep doing it.",
     "Son 12 ay içinde Monetise içinde birden fazla güncelleme yaptık. Ve yapmaya devam edeceğiz."),
    ("Take a look at our clients' feedback every time we announce a new update:",
     "Her yeni güncelleme duyurusunda müşterilerimizin geri bildirimlerine bakın:"),
    ("We really take care of our clients.", "Müşterilerimize gerçekten iyi bakıyoruz."),
    ("It won't be different with you. We'll keep working together until you win.",
     "Senin için farklı olmayacak. Kazanana kadar birlikte çalışmaya devam edeceğiz."),

    # ========== WHY SECTION ==========
    ("Why I'm Even Doing This (Call Me Selfish)", "Bunu Neden Yapıyorum (Bencil Deyin Bana)"),
    ("As a co-owner of Whop (the platform where you’ll host your digital products), I get a tiny percentage of every sale made.",
     "Whop'un (dijital ürünlerini barındıracağın platformun) ortak sahibi olarak, yapılan her satıştan küçük bir yüzde alıyorum."),
    ("As a co-owner of Whop (the platform where you'll host your digital products), I get a tiny percentage of every sale made.",
     "Whop'un (dijital ürünlerini barındıracağın platformun) ortak sahibi olarak, yapılan her satıştan küçük bir yüzde alıyorum."),
    ("In other words: When you make money, I make money. Literally.",
     "Başka bir deyişle: Sen para kazandığında, ben para kazanıyorum. Gerçekten."),
    ("So yes, call me selfish. I need you to profit so that I can build Whop into a $100 billion company. And the only way to accelerate that is by making sure the system I'm handing you actually works.",
     "Evet, bencil deyin bana. Whop'u $100 milyarlık bir şirkete dönüştürmek için senin kâr etmen gerekiyor. Ve bunu hızlandırmanın tek yolu, sana verdiğim sistemin gerçekten işe yaradığından emin olmaktır."),
    ("Lifetime Users Earnings", "Ömür Boyu Kullanıcı Kazançları"),

    # ========== URGENCY ==========
    ("But You Need To Act", "Ama Harekete Geçmen Gerekiyor"),
    ("We only open this a few times a year, and when it closes, it is gone.",
     "Bunu yılda yalnızca birkaç kez açıyoruz ve kapandığında gidiyor."),
    ('There is no �come back next month� or second chance waiting for you.',
     '"Gelecek ay geri gel" ya da seni bekleyen ikinci bir şans yok.'),
    ("Spots won't be open for long", "Kontenjanlar uzun süre açık kalmayacak"),
    ("No guaranteed reopen date", "Garantili yeniden açılış tarihi yok"),
    ("You either get in now or you miss it", "Ya şimdi girersin ya da kaçırırsın"),
    ("If you are serious about building income with AI doing the heavy lifting, this is it.",
     "Yapay zekanın ağır işleri yapmasıyla gelir elde etme konusunda ciddiysen, bu tam sana göre."),
    ("The smartest move you can make is to act today, not later.",
     "Yapabileceğin en akıllıca hamle, bugün harekete geçmektir, sonra değil."),

    # ========== CTA ==========
    ("Book A Call", "Görüşme Ayarla"),
    ("Our Team Is Ready To Help You", "Ekibimiz Size Yardım Etmeye Hazır"),
    ("We're here to answer any questions and guide you to success every step of the way. Schedule a call and get personalized support whenever you need it.",
     "Tüm sorularınızı yanıtlamak ve başarıya giden her adımda size rehberlik etmek için buradayız. Görüşme planlayın ve ihtiyaç duyduğunuzda kişiselleştirilmiş destek alın."),
    ("Send Whatsapp Message", "WhatsApp Mesajı Gönder"),
    ("Just send us a WhatsApp message to +44 7907 501962",
     "+44 7907 501962 numarasına WhatsApp mesajı gönderin"),
    ("Still have questions?", "Hâlâ sorunuz mu var?"),
    ("We're ready to help you through WhatsApp.", "WhatsApp üzerinden yardım etmeye hazırız."),

    # ========== FAQ ==========
    ("Frequently Asked Questions", "Sıkça Sorulan Sorular"),
    ("Is this just another course?", "Bu sadece başka bir kurs mu?"),
    ("Do I need to show my face or create content?", "Yüzümü göstermem veya içerik oluşturmam gerekiyor mu?"),
    ("What if I'm not technical?", "Teknik biri değilsem ne olur?"),
    ("Do I need money for ads?", "Reklamlar için paraya ihtiyacım var mı?"),
    ("What if I don't have much time?", "Çok fazla zamanım yoksa ne olur?"),
    ("How is this different from other AI programs?", "Bu diğer yapay zeka programlarından nasıl farklı?"),
    ("What if I've failed before?", "Daha önce başarısız olduysam ne olur?"),
    ("What if I can't afford it?", "Karşılayamazsam ne olur?"),

    # ========== TESTIMONIALS ==========
    ("What Our Clients Are Saying", "Müşterilerimiz Ne Diyor"),
    ("Load More", "Daha Fazla Yükle"),
    ("A trailblazer in this industry! Thank you Iman for your knowledge and the sharing to change peoples lives.",
     "Bu sektörde bir öncü! Bilgini ve insanların hayatlarını değiştirmek için paylaştıklarını paylaşman için teşekkürler Iman."),
    ("The features and programs are first class but the quality of mentors and members is life changing to be apart of.",
     "Özellikler ve programlar birinci sınıf, ancak mentör ve üyelerin kalitesi bir parçası olmak için hayat değiştirici."),
    ("I appreciate how much coaching and assistance there is in this program. You really can’t fail unless you stop trying.",
     "Bu programdaki koçluk ve yardım miktarını takdir ediyorum. Denemeyi bırakmadıkça gerçekten başarısız olamazsın."),
    ("I appreciate how much coaching and assistance there is in this program. You really can't fail unless you stop trying.",
     "Bu programdaki koçluk ve yardım miktarını takdir ediyorum. Denemeyi bırakmadıkça gerçekten başarısız olamazsın."),
    ("What I am seeing develop here is awesome! I have been in a lot of masterminds and this is the platform/program to put things I've learned into monetizable actions. Looking forward to the journey!",
     "Burada gelişen şeyi görmek harika! Pek çok mastermind grubunda bulundum ve bu, öğrendiklerimi para kazandıran eylemlere dönüştürmek için gereken platform/program. Yolculuğu dört gözle bekliyorum!"),
    ("Iman really does over-deliver! I feel as if I'm sat at the foot of the Xmas tree with so many, many presents to open and engage with!",
     "Iman gerçekten fazlasıyla veriyor! Sanki Noel ağacının dibinde oturuyormuşum gibi hissediyorum, açacak ve ilgilenecek çok, çok fazla hediye var!"),
    ("Probably the most value I've ever received in one place.",
     "Muhtemelen tek bir yerden aldığım en değerli şey."),
    ("I really really like what Iman and his team have created! So helpful information and help all the way!",
     "Iman ve ekibinin yarattığı şeyi gerçekten çok beğeniyorum! Baştan sona çok faydalı bilgi ve yardım!"),
    ("They possess abundant resources and excel in their work. Absolutely no complaints. The coaching and guidance I have received on my journey have been top-notch. This community! This team! This family! They are truly remarkable, and I have no doubt that I will continue to thrive here.",
     "Bol kaynaklara sahipler ve işlerinde mükemmeller. Kesinlikle şikayet yok. Yolculuğumda aldığım koçluk ve rehberlik birinci sınıftı. Bu topluluk! Bu ekip! Bu aile! Gerçekten olağanüstüler, burada gelişmeye devam edeceğimden hiç şüphem yok."),
    ("Love this. Grateful I took this steps to finally put everything together. Congrats to everyone starting too! You're a game changer!",
     "Bunu seviyorum. Sonunda her şeyi bir araya getirmek için bu adımı attığım için minnettarım. Başlayan herkesi de tebrik ederim! Sen bir oyun değiştiricisisin!"),
    ("I'm a part of Monetise for just a few days... It really is an awesome platform with great community! Looking forward to monetise some creators!",
     "Sadece birkaç gündür Monetise'in parçasıyım... Gerçekten harika bir toplulukla muhteşem bir platform! Bazı içerik üreticilerini para kazandırmayı dört gözle bekliyorum!"),
    ("Learned so much here about how to teach and bring my knowledge together and make it presentable to the masses. The coaches of all backgrounds really make this course/community TOP TIER.",
     "Burada bilgimi nasıl öğreteceğim, bir araya getireceğim ve kitlelere nasıl sunabileceğim hakkında çok şey öğrendim. Farklı geçmişlerden koçlar gerçekten bu kursu/topluluğu ZİRVEYE taşıyor."),
    ("This is one of the best investment I've ever done in my business! Iman's programs are incredibly smart, clear and easy to follow step by step. Every time I learn a new strategy or tool, I'm blown away by its efficiency. It literally gives us a shortcut to success, from scratch! Iman doesn't hesitate",
     "Bu, işimde yaptığım en iyi yatırımlardan biri! Iman'ın programları inanılmaz derecede akıllı, net ve adım adım takip etmesi kolay. Her yeni strateji veya araç öğrendiğimde, verimliliği beni şaşırtıyor. Sıfırdan başarıya gerçekten kısayol sağlıyor! Iman tereddüt etmiyor"),
    ("Great product, top support - best money spend this year!",
     "Harika ürün, mükemmel destek — bu yılki en iyi para harcaması!"),
    ("Only a few days in but there is so much information and guidance that it helps keep me positive on this new business venture and life changing opportunity.",
     "Sadece birkaç gün içinde ama bu yeni iş girişiminde ve hayat değiştiren fırsatta beni olumlu tutmaya yardımcı olan çok fazla bilgi ve rehberlik var."),
    ("I believe that people don’t realize yet what a crazy advantage they have with this program... that’s why I made the jump. It’s promising!",
     "İnsanların bu programla sahip oldukları çılgın avantajı henüz fark etmediklerine inanıyorum... bu yüzden atladım. Umut verici!"),
    ("I believe that people don't realize yet what a crazy advantage they have with this program... that's why I made the jump. It's promising!",
     "İnsanların bu programla sahip oldukları çılgın avantajı henüz fark etmediklerine inanıyorum... bu yüzden atladım. Umut verici!"),
    ("Awesome!!!! I'm learning so much as someone starting their first digital product business!",
     "Müthiş!!!! İlk dijital ürün işini kuran biri olarak çok şey öğreniyorum!"),
    ("To be honest I am speechless!! What a platform with amazing A.I. tools!!",
     "Dürüst olmak gerekirse sözlerim tükendi!! Ne bir platform, inanılmaz yapay zeka araçlarıyla!!"),
    ("The work that you have taken the burden off of those of us willing to see the gifts you are truly gifting us, taking on a bigger responsibility to help those that have started to try to help themselves, is phenomenal!",
     "Gerçekten bize hediye ettiğin armağanları görmek isteyenlerden yükü alan çalışman, kendilerine yardım etmeye çalışmaya başlayanları yardım etmek için daha büyük bir sorumluluk üstlenmen, olağanüstü!"),
    ("Great people and sense of community, it might not be the most adorable option but it pays off when you put time and whole into it.",
     "Harika insanlar ve topluluk hissi, en cazip seçenek olmayabilir ama zaman ve tüm enerjini koyduğunda meyvesini veriyor."),
    ("They put the costumer first, I love that. If you want to succeed you have the resources right here. They only way you fail is if you give up.",
     "Müşteriyi her şeyin önüne koyuyorlar, bunu seviyorum. Başarmak istiyorsan kaynaklar tam burada. Başarısız olmanın tek yolu vazgeçmektir."),
    ("Iman has done it again. Helping others succeed with proven methods and frameworks! Highly recommend for anyone looking to gain financial independence.",
     "Iman bunu yine yaptı. Kanıtlanmış yöntemler ve çerçevelerle başkalarının başarmasına yardımcı oluyor! Finansal bağımsızlık kazanmak isteyen herkese şiddetle tavsiye ederim."),
    ("Amazing training videos, next-level tools, and the best support money can buy! I wish I could give 10 stars.",
     "Harika eğitim videoları, bir üst seviye araçlar ve parayla satın alınabilecek en iyi destek! Keşke 10 yıldız verebilseydim."),
    ("Could anything out there in the market be more beast-mode than this?!!",
     "Piyasada bundan daha güçlü bir şey olabilir mi?!!"),
    ("Best decition in my life to get Iman’s program.",
     "Iman'ın programını almak hayatımın en iyi kararı."),
    ("Best decition in my life to get Iman's program.",
     "Iman'ın programını almak hayatımın en iyi kararı."),
    ("It just helped me through so many things and I’m still learning!! I can’t wait to finish up these courses and fully complete and start selling all of my combined and upscaling products!",
     "Pek çok konuda bana yardımcı oldu ve hâlâ öğreniyorum!! Bu kursları bitirip tüm birleşik ve ölçeklenen ürünlerimi satmaya başlamak için sabırsızlanıyorum!"),
    ("It just helped me through so many things and I'm still learning!! I can't wait to finish up these courses and fully complete and start selling all of my combined and upscaling products!",
     "Pek çok konuda bana yardımcı oldu ve hâlâ öğreniyorum!! Bu kursları bitirip tüm birleşik ve ölçeklenen ürünlerimi satmaya başlamak için sabırsızlanıyorum!"),
    ("Iman it's been part of the big change that I took as a person, in so grateful for what he's done. This program 10/10 too.",
     "Iman, bir insan olarak aldığım büyük değişimin parçası oldu, yaptıkları için çok minnettarım. Bu program da 10/10."),
    ("An abundance of valuable information and top notch support! Thank you!",
     "Bol miktarda değerli bilgi ve birinci sınıf destek! Teşekkürler!"),
    ("Amazing platform, insane opportunity, definitely suggested if you are interested in digital products.",
     "Harika platform, çılgın fırsat, dijital ürünlerle ilgileniyorsan kesinlikle önerilen."),
    ("You cannot fail, unless you do not follow the Blueprint! Every possible (potential) roadblock, for a digital product creator, has been overcome and/or addressed in this complete system. You get everything...just put the pieces together and make money while helping others.",
     "Taslağı takip etmezsen başarısız olamazsın! Bir dijital ürün yaratıcısı için olası her (potansiyel) engel, bu eksiksiz sistemde aşılmış ve/veya ele alınmıştır. Her şeyi alıyorsun... sadece parçaları bir araya getir ve başkalarına yardım ederken para kazan."),
    ("It is incredible the value that is in here, you have every tool everything that is necessary for you to succeed with digital products.",
     "Buradaki değer inanılmaz, dijital ürünlerle başarılı olman için gereken her araç ve her şey burada."),
    ("Great platform and support! If Whop could create a feature where you could invite a team member to join your account then that would be awesome!",
     "Harika platform ve destek! Whop hesabına bir ekip üyesi davet edebileceğin bir özellik oluşturabilseydi harika olurdu!"),
    ("Getting started and appreciate the huge volume of tools and information here. Thoroughly put together offering huge value if and when you get to work.",
     "Başlıyorum ve buradaki devasa araç ve bilgi hacmini takdir ediyorum. Çalışmaya başladığında büyük değer sunan kapsamlı bir yapı."),
    ("Monetise is a GAMECHANGER. I was smart enough to invest in Monetise PRO and I have absolutely ZERO REGRETS. I 150% recommend because Iman and his team go above and beyond to help.",
     "Monetise bir OYUN DEĞİŞTİRİCİ. Monetise PRO'ya yatırım yapacak kadar akıllıydım ve kesinlikle HİÇBİR PİŞMANLIĞIM YOK. %150 tavsiye ediyorum çünkü Iman ve ekibi yardım etmek için her şeyi yapıyor."),

    # ========== FOOTER ==========
    ("Privacy Policy", "Gizlilik Politikası"),
    ("Terms &amp; Conditions", "Kullanım Koşulları"),
    ("This site is not a part of the Facebook website or Facebook Inc. Additionally, This site is NOT endorsed by Facebook in any way. FACEBOOK is a trademark of FACEBOOK, Inc.",
     "Bu site, Facebook web sitesinin veya Facebook Inc.'in bir parçası değildir. Ayrıca bu site, Facebook tarafından hiçbir şekilde onaylanmamıştır. FACEBOOK, FACEBOOK, Inc.'in ticari markasıdır."),

    # ========== AI CHAT WIDGET ==========
    ("New Conversation", "Yeni Konuşma"),
    ("Close modal", "Kapat"),
    ("Upgrade Now", "Şimdi Yükselt"),
    ("Explain Artificial Intelligence so\n                        that I can explain it to my six-year-old child.",
     "Yapay Zekayı altı yaşındaki çocuğuma açıklayabileceğim şekilde anlat."),
    ("Please give me the best 10 travel\n                        ideas around the world",
     "Dünya genelinde en iyi 10 seyahat fikrini ver"),
    ('Translate "I love you" French', '"Seni seviyorum"u Fransızcaya çevir'),
    ("\U0001f4ad Translate, summarize, fix grammar and more…",
     "\U0001f4ad Çevir, özetle, dilbilgisini düzelt ve daha fazlası…"),
    ("Hello, how can I help you today?", "Merhaba, bugün size nasıl yardımcı olabilirim?"),
    ("Read Message", "Mesajı Oku"),
    ("Your usage limit has been reached. Please upgrade your plan to continue using.",
     "Kullanım limitinize ulaştınız. Kullanmaya devam etmek için planınızı yükseltin."),
    ("Stop generating", "Üretimi durdur"),
    ("Free Plan", "Ücretsiz Plan"),
    ("Fast Text", "Hızlı Metin"),
    ("Advanced Text", "Gelişmiş Metin"),
    ("Take a screenshot", "Ekran görüntüsü al"),
    ("Upload an image", "Resim yükle"),
    ("Upload File", "Dosya Yükle"),
    ("Read Page", "Sayfayı Oku"),
    ("Upload an image to easily get intelligent explanations and extract text from your images.",
     "Resimlerinizden akıllı açıklamalar almak ve metin çıkarmak için kolayca resim yükleyin."),
    ("Supported image types are JPEG and PNG", "Desteklenen resim türleri JPEG ve PNG'dir"),
    ("Drag your Image here or click to upload", "Resminizi buraya sürükleyin veya yüklemek için tıklayın"),
    ("Upload a PDF, Word, Excel, or PowerPoint file to easily get intelligent summaries and answers for your documents.",
     "Belgeleriniz için akıllı özetler ve yanıtlar almak için PDF, Word, Excel veya PowerPoint dosyası yükleyin."),
    ("Supported file types are PDF, Word, Excel, and PowerPoint",
     "Desteklenen dosya türleri PDF, Word, Excel ve PowerPoint'tir"),
    ("Drag your file here or click to upload", "Dosyanızı buraya sürükleyin veya yüklemek için tıklayın"),
    ("Fetches live information beyond the model training data.",
     "Model eğitim verilerinin ötesinde canlı bilgileri getirir."),
    ("Fetches and reads full content from specific URLs (docs, articles, Reddit).",
     "Belirli URL'lerden (belgeler, makaleler, Reddit) tam içeriği getirir ve okur."),
    ("Uses OpenAI Images to create visuals from text prompts.",
     "Metin istemlerinden görseller oluşturmak için OpenAI Images kullanır."),
    ("Runs lightweight analysis over uploaded data files.",
     "Yüklenen veri dosyaları üzerinde hafif analiz çalıştırır."),
    ("Adds deeper reasoning before the final reply.",
     "Son yanıttan önce daha derin muhakeme ekler."),
    ("Allow the model to create rich artifacts (code/HTML/etc).",
     "Modelin zengin eserler (kod/HTML/vb.) oluşturmasına izin ver."),
    ("Show progress tracking for complex multi-step tasks.",
     "Karmaşık çok adımlı görevler için ilerleme takibini göster."),
    ("Web Search", "Web Arama"),
    ("Not supported.", "Desteklenmiyor."),
    ("Web Crawl", "Web Tarama"),
    ("Image Generation", "Görsel Üretme"),
    ("Data Analysis", "Veri Analizi"),
    ("Think Mode", "Düşünme Modu"),
    ("Task Progress", "Görev İlerlemesi"),
    ("Group Chat", "Grup Sohbeti"),
    ("Web Access", "Web Erişimi"),
    ("Voice Input", "Ses Girişi"),
    ("Make a Review &amp; Earn Credit", "Yorum Yap ve Kredi Kazan"),
]

count = 0
not_found = []
for eng, tur in replacements:
    if eng in content:
        content = content.replace(eng, tur)
        count += 1
        print(f'  OK: {eng[:70]}')
    else:
        not_found.append(eng[:70])
        print(f'  NOT FOUND: {eng[:70]}')

print(f'\nTotal replacements made: {count} out of {len(replacements)}')
print(f'\nNot found ({len(not_found)}):')
for x in not_found:
    print(f'  - {x}')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('\nFile saved successfully.')
