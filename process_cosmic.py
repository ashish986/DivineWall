import os, glob, json
from PIL import Image

upload_dir = r'C:\Users\ashis\.gemini\antigravity\brain\5a73a213-bfd9-421d-9432-224bb7fb911f\.user_uploaded'
cdn_dir = r'D:\divine_wallpapers_cdn'
cosmic_dir = os.path.join(cdn_dir, 'wallpapers', 'cosmic')
api_dir = os.path.join(cdn_dir, 'api')
json_path = os.path.join(api_dir, 'wallpapers.json')
gen_script_path = os.path.join(cdn_dir, 'generate_json.py')

os.makedirs(cosmic_dir, exist_ok=True)
os.makedirs(api_dir, exist_ok=True)

files = sorted(glob.glob(os.path.join(upload_dir, '*.jpg')), key=os.path.getmtime)
print(f"Total uploaded files found: {len(files)}")

# 41 Wallpapers classification:
# Dark Cosmic / Symbolic -> tab: 'aesthetic', theme: 'cosmic'
# Realistic / Traditional -> tab: 'classic', theme: 'temple'
# category: subcategory of God / Goddess
all_metadata = [
    # 01
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ram",
        "primary": "#FF9900", "accent": "#00E5FF", "bg": "#060A17",
        "shlokHindi": "आपदामपहर्तारं दातारं सर्वसम्पदाम्। लोकाभिरामं श्रीरामं भूयो भूयो नमाम्यहम्॥",
        "shlokHinglish": "Ram Hanuman Bhakti: Divine blessing with glowing lotus diya and cosmic starlight.",
        "featured": True
    },
    # 02
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#00B0FF", "accent": "#FF4081", "bg": "#080414",
        "shlokHindi": "हे कृष्ण करुणासिन्धो दीनबन्धो जगत्पते। गोपिकेश गोपिकाकान्त राधाकान्त नमोऽस्तु ते॥",
        "shlokHinglish": "Radha Krishna Full Moon: Playing flute with blooming water lotuses and mystical stardust.",
        "featured": True
    },
    # 03
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#7C4DFF", "accent": "#00E5FF", "bg": "#0B0410",
        "shlokHindi": "कस्तूरीतिलकं ललाटपटले वक्षःस्थले कौस्तुभं नासाग्रे वरमौक्तिकं करतले वेणुं करे कङ्कणम्॥",
        "shlokHinglish": "Divine Amrit Raas: Glowing lotus diya, sacred flute and ethereal cosmic ribbons.",
        "featured": True
    },
    # 04
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "shiv",
        "primary": "#00E5FF", "accent": "#E040FB", "bg": "#04050E",
        "shlokHindi": "कर्पूरगौरं करुणावतारं संसारसारम् भुजगेन्द्रहारम्। सदावसन्तं हृदयारविन्दे भवं भवानीसहितं नमामि॥",
        "shlokHinglish": "Shiv Shakti Cosmic Glow: Sacred Shivling, celestial Trishul and radiant neon aura.",
        "featured": True
    },
    # 05 (Full deity painting -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "lakshmi",
        "primary": "#FFD700", "accent": "#FF4081", "bg": "#050616",
        "shlokHindi": "शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम्। लक्ष्मीकान्तं कमलनयनं योगिभिर्ध्यानगम्यम्॥",
        "shlokHinglish": "Lakshmi Narayan Divine Blessings: Sheshnaag protection, golden wealth kalash and traditional splendor.",
        "featured": True
    },
    # 06 (Dark Symbolic Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "durga",
        "primary": "#FFD700", "accent": "#FF1744", "bg": "#050B14",
        "shlokHindi": "अयि गिरिनन्दिनि नन्दितमेदिनि विश्वविनोदिनि नन्दसुते। गिरिवरविन्ध्यशिरोऽधिनिवासिनि विष्णुविलासिनि जिष्णुनुते॥",
        "shlokHinglish": "Aigiri Nandini Mahishasuramardini: Golden typography, divine lion and radiant Trishul.",
        "featured": True
    },
    # 07 (Dark Symbolic Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "durga",
        "primary": "#FFAB00", "accent": "#D50000", "bg": "#060913",
        "shlokHindi": "सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥",
        "shlokHinglish": "Jai Ambe Maa: Radiant golden calligraphy with Trishul and sacred lotus flame.",
        "featured": True
    },
    # 08 (Minimalist Symbolic Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ganesh",
        "primary": "#FFD700", "accent": "#FF1744", "bg": "#060B18",
        "shlokHindi": "वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥",
        "shlokHinglish": "Vakratunda Mahakaya Minimalist: Glowing gold calligraphy with red hibiscus flower.",
        "featured": False
    },
    # 09 (Full 3D Lotus Deity -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "ganesh",
        "primary": "#FFA000", "accent": "#FF4081", "bg": "#090E1A",
        "shlokHindi": "गजाननं भूतगणादिसेवितं कपित्थजम्बूफलचारुभक्षणम्। उमासुतं शोकविनाशकारकं नमामि विघ्नेश्वरपादपङ्कजम्॥",
        "shlokHinglish": "Vakratunda Mahakaya Divine: Full golden Ganesha seated on sacred lotus with Mushak and modaks.",
        "featured": True
    },
    # 10 (Symbolic Mantra Aura -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "other",
        "primary": "#FF9100", "accent": "#FFD700", "bg": "#0A1024",
        "shlokHindi": "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्॥",
        "shlokHinglish": "Maha Gayatri Mantra: Sacred solar aura over sunrise river ghat and lotus flame.",
        "featured": True
    },
    # 11 (Symbolic Bow Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ram",
        "primary": "#FFD700", "accent": "#FF6D00", "bg": "#040B1A",
        "shlokHindi": "रामो राजमणिः सदा विजयते रामं रमेशं भजे। रामेणाभिहता निशाचरचमू रामाय तस्मै नमः॥",
        "shlokHinglish": "Jai Shree Ram Golden Bow: Vibrant golden typography with Kodanda arrow.",
        "featured": True
    },
    # 12 (Symbolic Trishul Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "shiv",
        "primary": "#FFD700", "accent": "#FF1744", "bg": "#050C19",
        "shlokHindi": "ॐ नमः शिवाय। हर हर महादेव शम्भो काशी विश्वनाथ गंगे॥",
        "shlokHinglish": "Har Har Mahadev Trishul: Sacred Tripund and golden Trishul Damru typography.",
        "featured": True
    },
    # 13 (Dark Silhouette & Shivling -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "shiv",
        "primary": "#00B0FF", "accent": "#FFD700", "bg": "#040916",
        "shlokHindi": "ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय मामृतात्॥",
        "shlokHinglish": "Har Har Mahadev Silhouette: Cosmic crescent moon, sacred Shivling and divine profile.",
        "featured": True
    },
    # 14 (Dark Archer Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ram",
        "primary": "#FF9100", "accent": "#FFD700", "bg": "#050C1B",
        "shlokHindi": "श्रीरामचन्द्र कृपालु भजु मन हरण भवभय दारुणम्। नवकञ्ज लोचन कञ्ज मुख कर कञ्ज पद कञ्जारुणम्॥",
        "shlokHinglish": "Sita Ram Archer Silhouette: Golden rim light, Kodanda bow and saffron flag.",
        "featured": True
    },
    # 15 (Symbolic Gada Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FFD700", "accent": "#FF3D00", "bg": "#050C1A",
        "shlokHindi": "अतुलितबलधामं हेमशैलाभदेहं दनुजवनकृशानुं ज्ञानिनामग्रगण्यम्। सकलगुणनिधानं वानराणामधीशं रघुपतिप्रियभक्तं वातजातं नमामि॥",
        "shlokHinglish": "Jai Bajrangbali Golden Gada: Auspicious tilak and mighty divine mace typography.",
        "featured": True
    },
    # 16 (Bold Saffron Graphic Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FF6D00", "accent": "#FFAB00", "bg": "#000000",
        "shlokHindi": "मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम्। वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये॥",
        "shlokHinglish": "Veer Hanuman Saffron Silhouette: Bold minimalist devotional portrait.",
        "featured": False
    },
    # 17 (Symbolic Flute Typography -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#FFD700", "accent": "#2979FF", "bg": "#050C1E",
        "shlokHindi": "श्रीराधा वृन्दावनेश्वरी कृष्णप्रिया मनोरमा। श्रीकृष्णसङ्गिनि देवी सर्वकामप्रदायिनी॥",
        "shlokHinglish": "Radhe Krishna Golden Bansuri: Peacock feather and blue silk draped flute.",
        "featured": True
    },
    # 18 (Neon Contour Outline -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#00E5FF", "accent": "#FFD700", "bg": "#03040C",
        "shlokHindi": "फुल्लेन्दीवरकान्तिमेलनकलाकुञ्जे वसन्तं सदा, राधाप्रेमसुधारसेन मधुरं गोविन्दमानन्ददम्॥",
        "shlokHinglish": "Radha Krishna Neon Contour: Golden-blue glowing silhouettes with sacred bansuri.",
        "featured": True
    },
    # 19 (Dark Moonlight Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#2979FF", "accent": "#FFD700", "bg": "#030716",
        "shlokHindi": "अधरं मधुरं वदनं मधुरं नयनं मधुरं हसितं मधुरम्। हृदयं मधुरं गमनं मधुरं मधुराधिपतेरखिलं मधुरम्॥",
        "shlokHinglish": "Midnight Moonlight Vrindavan: Blue celestial silhouettes under glowing full moon.",
        "featured": True
    },
    # 20 (Fierce Realistic Warrior Portrait -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "hanuman",
        "primary": "#FF9100", "accent": "#FFD700", "bg": "#0E0703",
        "shlokHindi": "महाबीर बिक्रम बजरंगी। कुमति निवार सुमति के संगी॥",
        "shlokHinglish": "Fierce Golden Warrior: Cinematic traditional portrait of Bajrangbali with glowing mace.",
        "featured": True
    },
    # 21 (Dark Ayodhya Sunrise Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ram",
        "primary": "#FFD700", "accent": "#FF3D00", "bg": "#050B1B",
        "shlokHindi": "मङ्गल भवन अमङ्गल हारी। द्रवहु सुदसरथ अजिर बिहारी॥",
        "shlokHinglish": "Ayodhya Sunrise Kodanda: Lord Ram silhouette over glowing Ram Mandir.",
        "featured": True
    },
    # 22 (Fiery Mane Profile -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FF6D00", "accent": "#FFD700", "bg": "#0B0502",
        "shlokHindi": "लाल देह लाली लसे, अरु धरि लाल लंगूर। वज्र देह दानव दलन, जय जय जय कपिसूर॥",
        "shlokHinglish": "Fiery Devotion Profile: Glowing golden mane and fiery gaze of Mahaveer.",
        "featured": False
    },
    # 23 (Chest Glowing Ram Symbol -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FF9100", "accent": "#FFD700", "bg": "#000000",
        "shlokHindi": "रामदूत अतुलित बलधामा। अंजनिपुत्र पवनसुत नामा॥",
        "shlokHinglish": "Chest Glowing Ram: Mighty Hanuman with divine halo and golden Gada.",
        "featured": True
    },
    # 24 (Realistic Daylight Royal Prince Ram -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "ram",
        "primary": "#FFAB00", "accent": "#FF3D00", "bg": "#0F0B18",
        "shlokHindi": "रामाय रामभद्राय रामचन्द्राय वेधसे। रघुनाथाय नाथाय सीतायाः पतये नमः॥",
        "shlokHinglish": "Maryada Purushottam Ram: Grand royal portrait with Kodanda bow in Ayodhya.",
        "featured": True
    },
    # 25 (Dark Moonlight Hill Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ram",
        "primary": "#FFD700", "accent": "#FF6D00", "bg": "#040816",
        "shlokHindi": "धर्मो रक्षति रक्षितः। रामो विग्रहवान् धर्मः साधुः सत्यपराक्रमः॥",
        "shlokHinglish": "Moonlit Ayodhya Hill: Lord Ram silhouette under full moon with sacred temple.",
        "featured": True
    },
    # 26 (Moonlit Lion Rider Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "durga",
        "primary": "#00B0FF", "accent": "#FF1744", "bg": "#020713",
        "shlokHindi": "या देवी सर्वभूतेषु शक्तिरूपेण संस्थिता। नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥",
        "shlokHinglish": "Moonlit Celestial Durga: Majestic lion rider silhouette against giant full moon.",
        "featured": True
    },
    # 27 (Neon Contour Dual-Tone -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ganesh",
        "primary": "#FFD700", "accent": "#00E5FF", "bg": "#030612",
        "shlokHindi": "एकदन्ताय विद्महे वक्रतुण्डाय धीमहि। तन्नो दन्तिः प्रचोदयात्॥",
        "shlokHinglish": "Neon Contour Ganesha: Dual-tone golden-cyan line art with blessing hand.",
        "featured": False
    },
    # 28 (Realistic Warrior Queen Durga Portrait -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "durga",
        "primary": "#FFD700", "accent": "#D50000", "bg": "#0C0712",
        "shlokHindi": "दुर्गे स्मृता हरसि भीतिमशेषजन्तोः स्वस्थैः स्मृता मतिमतीव शुभां ददासि॥",
        "shlokHinglish": "Mahishasuramardini Supreme: Hyper-realistic celestial warrior goddess with royal lion.",
        "featured": True
    },
    # 29 (Bal Ganesha Seated Lotus -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "ganesh",
        "primary": "#FFC107", "accent": "#FF4081", "bg": "#060A18",
        "shlokHindi": "प्रणम्य शिरसा देवं गौरीपुत्रं विनायकम्। भक्तावासं स्मरेन्नित्यमायुःकामार्थसिद्धये॥",
        "shlokHinglish": "Bal Ganesha Lotus Throne: Traditional sacred diya, mushak companion and hibiscus blossoms.",
        "featured": False
    },
    # 30 (Symbolic Golden Calligraphy -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "ganesh",
        "primary": "#FFD700", "accent": "#FF1744", "bg": "#040816",
        "shlokHindi": "जय गणेश जय गणेश जय गणेश देवा। माता जाकी पार्वती पिता महादेवा॥",
        "shlokHinglish": "Golden Diya Vinayaka: Flowing golden calligraphy with glowing oil lamp.",
        "featured": True
    },
    # 31 (Dark Sapphire Rim-Light -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FFD700", "accent": "#2979FF", "bg": "#030716",
        "shlokHindi": "संकट कटै मिटै सब पीरा। जो सुमिरै हनुमत बलबीरा॥",
        "shlokHinglish": "Celestial Contemplation: Dual-tone sapphire and gold devotion profile.",
        "featured": True
    },
    # 32 (Symbolic Typography & Flag -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FFD700", "accent": "#FF3D00", "bg": "#040816",
        "shlokHindi": "भूत पिशाच निकट नहिं आवै। महाबीर जब नाम सुनावै॥",
        "shlokHinglish": "Jai Shree Hanuman Saffron Flag: Radiant typography with golden mace and dhwaja.",
        "featured": True
    },
    # 33 (Realistic Crowned King Hanuman Portrait -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "hanuman",
        "primary": "#FFD700", "accent": "#00E5FF", "bg": "#060714",
        "shlokHindi": "नासे रोग हरै सब पीरा। जपत निरन्तर हनुमत बीरा॥",
        "shlokHinglish": "King of Devotion: Majestic crowned warrior with golden mace and ruby jewels.",
        "featured": True
    },
    # 34 (Traditional Devi Saraswati Portrait -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "saraswati",
        "primary": "#FFD700", "accent": "#FFFFFF", "bg": "#050918",
        "shlokHindi": "या कुन्देन्दुतुषारहारधवला या शुभ्रवस्त्रावृता। या वीणावरदण्डमण्डितकरा या श्वेतपद्मासना॥",
        "shlokHinglish": "Goddess Saraswati Swan & Veena: Radiant wisdom on pristine white lotus.",
        "featured": True
    },
    # 35 (Traditional Devi Lakshmi Portrait -> Classic)
    {
        "tab": "classic", "theme": "temple", "category": "lakshmi",
        "primary": "#FFD700", "accent": "#FF4081", "bg": "#07040D",
        "shlokHindi": "ॐ श्रीं ह्रीं श्रीं कमले कमलालये प्रसीद प्रसीद श्रीं ह्रीं श्रीं ॐ महालक्ष्म्यै नमः॥",
        "shlokHinglish": "Maha Lakshmi Golden Shower: Sacred pink lotus with boundless prosperity.",
        "featured": True
    },
    # 36 (Symbolic Gada & Flag on Rock -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "hanuman",
        "primary": "#FFD700", "accent": "#D50000", "bg": "#030716",
        "shlokHindi": "पवनतनय संकट हरन मंगल मूरति रूप। राम लखन सीता सहित हृदय बसहु सुर भूप॥",
        "shlokHinglish": "Sacred Gada on Rock: Crown, rudraksha and Jai Shree Ram crimson flag.",
        "featured": True
    },
    # 37 (Symbolic Trishul & Shivling Radiance -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "shiv",
        "primary": "#00E5FF", "accent": "#FFD700", "bg": "#030614",
        "shlokHindi": "नमामीशमीशान निर्वाणरूपं विभुं व्यापकं ब्रह्मवेदस्वरूपम्। निजं निर्गुणं निर्विकल्पं निरीहं चिदाकाशमाकाशवासं भजेऽहम्॥",
        "shlokHinglish": "Trishul & Shivling Radiance: Crescent moon, Damru and sacred bilva blossoms.",
        "featured": True
    },
    # 38 (Dhyan Mahadev Cosmic Locks -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "shiv",
        "primary": "#00E5FF", "accent": "#FFD700", "bg": "#030614",
        "shlokHindi": "ध्यायेन्नित्यं महेशं रजतगिरिनिभं चारुचन्द्रावतंसं रत्नाकल्पोज्ज्वलाङ्गं परशुमृगवराभीतिहस्तं प्रसन्नम्॥",
        "shlokHinglish": "Dhyan Mahadev Cosmic Locks: Glowing Om necklace, crescent moon and Vasuki serpent.",
        "featured": True
    },
    # 39 (Sapphire Starlight Flute -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#FFD700", "accent": "#2979FF", "bg": "#030615",
        "shlokHindi": "बर्हापीडं नटवरवपुः कर्णयोः कर्णिकारं बिभ्रद्वासः कनककपिशं वैजयन्तीं च मालाम्॥",
        "shlokHinglish": "Krishna Flute Starlight: Sapphire aura with glowing peacock feather and yellow scarf.",
        "featured": True
    },
    # 40 (Moonlit Bansuri Silhouette -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#00B0FF", "accent": "#FFD700", "bg": "#030616",
        "shlokHindi": "वंशी विभूषितकरात् नवनीरदाभात् पीताम्बरात् अरुणबिम्बफलाधरोष्ठात्। पूर्णेन्दुसुन्दरमुखात् अरविन्दनेत्रात् कृष्णात् परं किमपि तत्त्वमहं न जाने॥",
        "shlokHinglish": "Moonlit Bansuri Krishna: Profile under giant radiant moon with ethereal clouds.",
        "featured": True
    },
    # 41 (Symbolic Bansuri on Silk -> Cosmic)
    {
        "tab": "aesthetic", "theme": "cosmic", "category": "krishna",
        "primary": "#FFD700", "accent": "#00E5FF", "bg": "#030718",
        "shlokHindi": "मूकं करोति वाचालं पङ्गुं लङ्घयते गिरिम्। यत्कृपा तमहं वन्दे परमानन्दमाधवम्॥",
        "shlokHinglish": "Sacred Bansuri on Silk: White jasmine flowers, peacock feather and Krishna silhouette.",
        "featured": True
    }
]

cdn_base = 'https://raw.githubusercontent.com/ashish986/DivineWall/main'

new_wallpapers = []

for idx, fpath in enumerate(files, 1):
    meta = all_metadata[idx - 1]
    num_str = f"{idx:02d}"
    dest_full = os.path.join(cosmic_dir, f"{num_str}.jpg")
    dest_thumb = os.path.join(cosmic_dir, f"thumb_{num_str}.jpg")

    # 1. Save full image optimized
    with Image.open(fpath) as img:
        img_rgb = img.convert('RGB')
        img_rgb.save(dest_full, 'JPEG', quality=95, optimize=True)

        # 2. Save thumbnail
        thumb_img = img_rgb.copy()
        thumb_width = 380
        aspect = thumb_img.height / thumb_img.width
        thumb_height = int(thumb_width * aspect)
        thumb_img = thumb_img.resize((thumb_width, thumb_height), Image.Resampling.LANCZOS)
        thumb_img.save(dest_thumb, 'JPEG', quality=85, optimize=True)

    # 3. Create entry
    entry = {
        'id': f'cosmic_{num_str}',
        'imageUrl': f'{cdn_base}/wallpapers/cosmic/{num_str}.jpg',
        'thumbnailUrl': f'{cdn_base}/wallpapers/cosmic/thumb_{num_str}.jpg',
        'tab': meta['tab'],
        'category': meta['category'],
        'theme': meta['theme'],
        'themeColors': {
            'primary': meta['primary'],
            'accent': meta['accent'],
            'background': meta['bg']
        },
        'shlokHindi': meta['shlokHindi'],
        'shlokHinglish': meta['shlokHinglish'],
        'isFeatured': meta['featured'],
        'createdAt': '2026-11-04T00:00:00Z'
    }
    new_wallpapers.append(entry)
    print(f"Processed [{idx:02d}/41]: id={entry['id']}, tab={entry['tab']}, cat={entry['category']}")

# Now load existing wallpapers from wallpapers.json
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        existing_list = json.load(f)
else:
    existing_list = []

# Filter out old cosmic_ entries
filtered_existing = [w for w in existing_list if not str(w.get('id', '')).startswith('cosmic_')]

final_wallpapers = new_wallpapers + filtered_existing

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(final_wallpapers, f, indent=2, ensure_ascii=False)

print(f"\nSuccessfully generated {json_path}!")
cosmic_count = sum(1 for w in new_wallpapers if w['tab'] == 'aesthetic')
classic_count = sum(1 for w in new_wallpapers if w['tab'] == 'classic')
print(f"-> Cosmic (Aesthetic/Symbolic) Wallpapers: {cosmic_count}")
print(f"-> Classic (Devotional/Traditional) Wallpapers: {classic_count}")
print(f"-> Total wallpapers in JSON: {len(final_wallpapers)}")
