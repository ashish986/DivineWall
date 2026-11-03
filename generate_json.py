import os, json

dest_cdn = r'D:\divine_wallpapers_cdn'
api_dir = os.path.join(dest_cdn, 'api')
os.makedirs(api_dir, exist_ok=True)
json_path = os.path.join(api_dir, 'wallpapers.json')

wallpapers = [
  {
    "id": "cosmic_01",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/01.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_01.jpg",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9900",
      "accent": "#00E5FF",
      "background": "#060A17"
    },
    "shlokHindi": "आपदामपहर्तारं दातारं सर्वसम्पदाम्। लोकाभिरामं श्रीरामं भूयो भूयो नमाम्यहम्॥",
    "shlokHinglish": "Ram Hanuman Bhakti: Divine blessing with glowing lotus diya and cosmic starlight.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_02",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/02.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_02.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#FF4081",
      "background": "#080414"
    },
    "shlokHindi": "हे कृष्ण करुणासिन्धो दीनबन्धो जगत्पते। गोपिकेश गोपिकाकान्त राधाकान्त नमोऽस्तु ते॥",
    "shlokHinglish": "Radha Krishna Full Moon: Playing flute with blooming water lotuses and mystical stardust.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_03",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/03.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_03.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#7C4DFF",
      "accent": "#00E5FF",
      "background": "#0B0410"
    },
    "shlokHindi": "कस्तूरीतिलकं ललाटपटले वक्षःस्थले कौस्तुभं नासाग्रे वरमौक्तिकं करतले वेणुं करे कङ्कणम्॥",
    "shlokHinglish": "Divine Amrit Raas: Glowing lotus diya, sacred flute and ethereal cosmic ribbons.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_04",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/04.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_04.jpg",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#E040FB",
      "background": "#04050E"
    },
    "shlokHindi": "कर्पूरगौरं करुणावतारं संसारसारम् भुजगेन्द्रहारम्। सदावसन्तं हृदयारविन्दे भवं भवानीसहितं नमामि॥",
    "shlokHinglish": "Shiv Shakti Cosmic Glow: Sacred Shivling, celestial Trishul and radiant neon aura.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_05",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/05.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_05.jpg",
    "tab": "classic",
    "category": "lakshmi",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF4081",
      "background": "#050616"
    },
    "shlokHindi": "शान्ताकारं भुजगशयनं पद्मनाभं सुरेशं विश्वाधारं गगनसदृशं मेघवर्णं शुभाङ्गम्। लक्ष्मीकान्तं कमलनयनं योगिभिर्ध्यानगम्यम्॥",
    "shlokHinglish": "Lakshmi Narayan Divine Blessings: Sheshnaag protection, golden wealth kalash and traditional splendor.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_06",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/06.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_06.jpg",
    "tab": "aesthetic",
    "category": "durga",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF1744",
      "background": "#050B14"
    },
    "shlokHindi": "अयि गिरिनन्दिनि नन्दितमेदिनि विश्वविनोदिनि नन्दसुते। गिरिवरविन्ध्यशिरोऽधिनिवासिनि विष्णुविलासिनि जिष्णुनुते॥",
    "shlokHinglish": "Aigiri Nandini Mahishasuramardini: Golden typography, divine lion and radiant Trishul.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_07",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/07.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_07.jpg",
    "tab": "aesthetic",
    "category": "durga",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFAB00",
      "accent": "#D50000",
      "background": "#060913"
    },
    "shlokHindi": "सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥",
    "shlokHinglish": "Jai Ambe Maa: Radiant golden calligraphy with Trishul and sacred lotus flame.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_08",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/08.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_08.jpg",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF1744",
      "background": "#060B18"
    },
    "shlokHindi": "वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥",
    "shlokHinglish": "Vakratunda Mahakaya Minimalist: Glowing gold calligraphy with red hibiscus flower.",
    "isFeatured": false,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_09",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/09.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_09.jpg",
    "tab": "classic",
    "category": "ganesh",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFA000",
      "accent": "#FF4081",
      "background": "#090E1A"
    },
    "shlokHindi": "गजाननं भूतगणादिसेवितं कपित्थजम्बूफलचारुभक्षणम्। उमासुतं शोकविनाशकारकं नमामि विघ्नेश्वरपादपङ्कजम्॥",
    "shlokHinglish": "Vakratunda Mahakaya Divine: Full golden Ganesha seated on sacred lotus with Mushak and modaks.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_10",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/10.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_10.jpg",
    "tab": "aesthetic",
    "category": "other",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#FFD700",
      "background": "#0A1024"
    },
    "shlokHindi": "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्॥",
    "shlokHinglish": "Maha Gayatri Mantra: Sacred solar aura over sunrise river ghat and lotus flame.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_11",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/11.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_11.jpg",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF6D00",
      "background": "#040B1A"
    },
    "shlokHindi": "रामो राजमणिः सदा विजयते रामं रमेशं भजे। रामेणाभिहता निशाचरचमू रामाय तस्मै नमः॥",
    "shlokHinglish": "Jai Shree Ram Golden Bow: Vibrant golden typography with Kodanda arrow.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_12",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/12.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_12.jpg",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF1744",
      "background": "#050C19"
    },
    "shlokHindi": "ॐ नमः शिवाय। हर हर महादेव शम्भो काशी विश्वनाथ गंगे॥",
    "shlokHinglish": "Har Har Mahadev Trishul: Sacred Tripund and golden Trishul Damru typography.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_13",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/13.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_13.jpg",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#FFD700",
      "background": "#040916"
    },
    "shlokHindi": "ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय मामृतात्॥",
    "shlokHinglish": "Har Har Mahadev Silhouette: Cosmic crescent moon, sacred Shivling and divine profile.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_14",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/14.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_14.jpg",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#FFD700",
      "background": "#050C1B"
    },
    "shlokHindi": "श्रीरामचन्द्र कृपालु भजु मन हरण भवभय दारुणम्। नवकञ्ज लोचन कञ्ज मुख कर कञ्ज पद कञ्जारुणम्॥",
    "shlokHinglish": "Sita Ram Archer Silhouette: Golden rim light, Kodanda bow and saffron flag.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_15",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/15.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_15.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF3D00",
      "background": "#050C1A"
    },
    "shlokHindi": "अतुलितबलधामं हेमशैलाभदेहं दनुजवनकृशानुं ज्ञानिनामग्रगण्यम्। सकलगुणनिधानं वानराणामधीशं रघुपतिप्रियभक्तं वातजातं नमामि॥",
    "shlokHinglish": "Jai Bajrangbali Golden Gada: Auspicious tilak and mighty divine mace typography.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_16",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/16.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_16.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF6D00",
      "accent": "#FFAB00",
      "background": "#000000"
    },
    "shlokHindi": "मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम्। वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये॥",
    "shlokHinglish": "Veer Hanuman Saffron Silhouette: Bold minimalist devotional portrait.",
    "isFeatured": false,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_17",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/17.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_17.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#2979FF",
      "background": "#050C1E"
    },
    "shlokHindi": "श्रीराधा वृन्दावनेश्वरी कृष्णप्रिया मनोरमा। श्रीकृष्णसङ्गिनि देवी सर्वकामप्रदायिनी॥",
    "shlokHinglish": "Radhe Krishna Golden Bansuri: Peacock feather and blue silk draped flute.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_18",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/18.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_18.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFD700",
      "background": "#03040C"
    },
    "shlokHindi": "फुल्लेन्दीवरकान्तिमेलनकलाकुञ्जे वसन्तं सदा, राधाप्रेमसुधारसेन मधुरं गोविन्दमानन्ददम्॥",
    "shlokHinglish": "Radha Krishna Neon Contour: Golden-blue glowing silhouettes with sacred bansuri.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_19",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/19.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_19.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#2979FF",
      "accent": "#FFD700",
      "background": "#030716"
    },
    "shlokHindi": "अधरं मधुरं वदनं मधुरं नयनं मधुरं हसितं मधुरम्। हृदयं मधुरं गमनं मधुरं मधुराधिपतेरखिलं मधुरम्॥",
    "shlokHinglish": "Midnight Moonlight Vrindavan: Blue celestial silhouettes under glowing full moon.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_20",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/20.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_20.jpg",
    "tab": "classic",
    "category": "hanuman",
    "theme": "temple",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#FFD700",
      "background": "#0E0703"
    },
    "shlokHindi": "महाबीर बिक्रम बजरंगी। कुमति निवार सुमति के संगी॥",
    "shlokHinglish": "Fierce Golden Warrior: Cinematic traditional portrait of Bajrangbali with glowing mace.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_21",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/21.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_21.jpg",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF3D00",
      "background": "#050B1B"
    },
    "shlokHindi": "मङ्गल भवन अमङ्गल हारी। द्रवहु सुदसरथ अजिर बिहारी॥",
    "shlokHinglish": "Ayodhya Sunrise Kodanda: Lord Ram silhouette over glowing Ram Mandir.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_22",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/22.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_22.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF6D00",
      "accent": "#FFD700",
      "background": "#0B0502"
    },
    "shlokHindi": "लाल देह लाली लसे, अरु धरि लाल लंगूर। वज्र देह दानव दलन, जय जय जय कपिसूर॥",
    "shlokHinglish": "Fiery Devotion Profile: Glowing golden mane and fiery gaze of Mahaveer.",
    "isFeatured": false,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_23",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/23.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_23.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "रामदूत अतुलित बलधामा। अंजनिपुत्र पवनसुत नामा॥",
    "shlokHinglish": "Chest Glowing Ram: Mighty Hanuman with divine halo and golden Gada.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_24",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/24.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_24.jpg",
    "tab": "classic",
    "category": "ram",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFAB00",
      "accent": "#FF3D00",
      "background": "#0F0B18"
    },
    "shlokHindi": "रामाय रामभद्राय रामचन्द्राय वेधसे। रघुनाथाय नाथाय सीतायाः पतये नमः॥",
    "shlokHinglish": "Maryada Purushottam Ram: Grand royal portrait with Kodanda bow in Ayodhya.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_25",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/25.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_25.jpg",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF6D00",
      "background": "#040816"
    },
    "shlokHindi": "धर्मो रक्षति रक्षितः। रामो विग्रहवान् धर्मः साधुः सत्यपराक्रमः॥",
    "shlokHinglish": "Moonlit Ayodhya Hill: Lord Ram silhouette under full moon with sacred temple.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_26",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/26.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_26.jpg",
    "tab": "aesthetic",
    "category": "durga",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#FF1744",
      "background": "#020713"
    },
    "shlokHindi": "या देवी सर्वभूतेषु शक्तिरूपेण संस्थिता। नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥",
    "shlokHinglish": "Moonlit Celestial Durga: Majestic lion rider silhouette against giant full moon.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_27",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/27.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_27.jpg",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#00E5FF",
      "background": "#030612"
    },
    "shlokHindi": "एकदन्ताय विद्महे वक्रतुण्डाय धीमहि। तन्नो दन्तिः प्रचोदयात्॥",
    "shlokHinglish": "Neon Contour Ganesha: Dual-tone golden-cyan line art with blessing hand.",
    "isFeatured": false,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_28",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/28.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_28.jpg",
    "tab": "classic",
    "category": "durga",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#D50000",
      "background": "#0C0712"
    },
    "shlokHindi": "दुर्गे स्मृता हरसि भीतिमशेषजन्तोः स्वस्थैः स्मृता मतिमतीव शुभां ददासि॥",
    "shlokHinglish": "Mahishasuramardini Supreme: Hyper-realistic celestial warrior goddess with royal lion.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_29",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/29.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_29.jpg",
    "tab": "classic",
    "category": "ganesh",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFC107",
      "accent": "#FF4081",
      "background": "#060A18"
    },
    "shlokHindi": "प्रणम्य शिरसा देवं गौरीपुत्रं विनायकम्। भक्तावासं स्मरेन्नित्यमायुःकामार्थसिद्धये॥",
    "shlokHinglish": "Bal Ganesha Lotus Throne: Traditional sacred diya, mushak companion and hibiscus blossoms.",
    "isFeatured": false,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_30",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/30.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_30.jpg",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF1744",
      "background": "#040816"
    },
    "shlokHindi": "जय गणेश जय गणेश जय गणेश देवा। माता जाकी पार्वती पिता महादेवा॥",
    "shlokHinglish": "Golden Diya Vinayaka: Flowing golden calligraphy with glowing oil lamp.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_31",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/31.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_31.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#2979FF",
      "background": "#030716"
    },
    "shlokHindi": "संकट कटै मिटै सब पीरा। जो सुमिरै हनुमत बलबीरा॥",
    "shlokHinglish": "Celestial Contemplation: Dual-tone sapphire and gold devotion profile.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_32",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/32.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_32.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF3D00",
      "background": "#040816"
    },
    "shlokHindi": "भूत पिशाच निकट नहिं आवै। महाबीर जब नाम सुनावै॥",
    "shlokHinglish": "Jai Shree Hanuman Saffron Flag: Radiant typography with golden mace and dhwaja.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_33",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/33.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_33.jpg",
    "tab": "classic",
    "category": "hanuman",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#00E5FF",
      "background": "#060714"
    },
    "shlokHindi": "नासे रोग हरै सब पीरा। जपत निरन्तर हनुमत बीरा॥",
    "shlokHinglish": "King of Devotion: Majestic crowned warrior with golden mace and ruby jewels.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_34",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/34.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_34.jpg",
    "tab": "classic",
    "category": "saraswati",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FFFFFF",
      "background": "#050918"
    },
    "shlokHindi": "या कुन्देन्दुतुषारहारधवला या शुभ्रवस्त्रावृता। या वीणावरदण्डमण्डितकरा या श्वेतपद्मासना॥",
    "shlokHinglish": "Goddess Saraswati Swan & Veena: Radiant wisdom on pristine white lotus.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_35",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/35.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_35.jpg",
    "tab": "classic",
    "category": "lakshmi",
    "theme": "temple",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF4081",
      "background": "#07040D"
    },
    "shlokHindi": "ॐ श्रीं ह्रीं श्रीं कमले कमलालये प्रसीद प्रसीद श्रीं ह्रीं श्रीं ॐ महालक्ष्म्यै नमः॥",
    "shlokHinglish": "Maha Lakshmi Golden Shower: Sacred pink lotus with boundless prosperity.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_36",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/36.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_36.jpg",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#D50000",
      "background": "#030716"
    },
    "shlokHindi": "पवनतनय संकट हरन मंगल मूरति रूप। राम लखन सीता सहित हृदय बसहु सुर भूप॥",
    "shlokHinglish": "Sacred Gada on Rock: Crown, rudraksha and Jai Shree Ram crimson flag.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_37",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/37.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_37.jpg",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFD700",
      "background": "#030614"
    },
    "shlokHindi": "नमामीशमीशान निर्वाणरूपं विभुं व्यापकं ब्रह्मवेदस्वरूपम्। निजं निर्गुणं निर्विकल्पं निरीहं चिदाकाशमाकाशवासं भजेऽहम्॥",
    "shlokHinglish": "Trishul & Shivling Radiance: Crescent moon, Damru and sacred bilva blossoms.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_38",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/38.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_38.jpg",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFD700",
      "background": "#030614"
    },
    "shlokHindi": "ध्यायेन्नित्यं महेशं रजतगिरिनिभं चारुचन्द्रावतंसं रत्नाकल्पोज्ज्वलाङ्गं परशुमृगवराभीतिहस्तं प्रसन्नम्॥",
    "shlokHinglish": "Dhyan Mahadev Cosmic Locks: Glowing Om necklace, crescent moon and Vasuki serpent.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_39",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/39.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_39.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#2979FF",
      "background": "#030615"
    },
    "shlokHindi": "बर्हापीडं नटवरवपुः कर्णयोः कर्णिकारं बिभ्रद्वासः कनककपिशं वैजयन्तीं च मालाम्॥",
    "shlokHinglish": "Krishna Flute Starlight: Sapphire aura with glowing peacock feather and yellow scarf.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_40",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/40.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_40.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#FFD700",
      "background": "#030616"
    },
    "shlokHindi": "वंशी विभूषितकरात् नवनीरदाभात् पीताम्बरात् अरुणबिम्बफलाधरोष्ठात्। पूर्णेन्दुसुन्दरमुखात् अरविन्दनेत्रात् कृष्णात् परं किमपि तत्त्वमहं न जाने॥",
    "shlokHinglish": "Moonlit Bansuri Krishna: Profile under giant radiant moon with ethereal clouds.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "cosmic_41",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/41.jpg",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/cosmic/thumb_41.jpg",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#00E5FF",
      "background": "#030718"
    },
    "shlokHindi": "मूकं करोति वाचालं पङ्गुं लङ्घयते गिरिम्। यत्कृपा तमहं वन्दे परमानन्दमाधवम्॥",
    "shlokHinglish": "Sacred Bansuri on Silk: White jasmine flowers, peacock feather and Krishna silhouette.",
    "isFeatured": true,
    "createdAt": "2026-11-04T00:00:00Z"
  },
  {
    "id": "sw1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/saraswati/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/saraswati/thumb_01.png",
    "tab": "classic",
    "category": "saraswati",
    "theme": "divine_glow",
    "themeColors": {
      "primary": "#4FC3F7",
      "accent": "#FFFFFF",
      "background": "#F0F8FF"
    },
    "shlokHindi": "या कुन्देन्दुतुषारहारधवला या शुभ्रवस्त्रावृता । या वीणावरदण्डमण्डितकरा या श्वेतपद्मासना ॥ सा मां पातु सरस्वती भगवती निःशेषजाड्यापहा ॥",
    "shlokHinglish": "Devi Saraswati: Goddess of divine wisdom, arts, and sacred music adorned in white lotus serenity.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "sw2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/saraswati/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/saraswati/thumb_02.png",
    "tab": "aesthetic",
    "category": "saraswati",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#BA68C8",
      "accent": "#FFFFFF",
      "background": "#0B0813"
    },
    "shlokHindi": "सरस्वति नमस्तुभ्यं वरदे कामरूपिणि । विद्यारम्भं करिष्यामि सिद्धिर्भवतु मे सदा ॥",
    "shlokHinglish": "Cosmic Veena Saraswati: Radiant purple cosmic aura illuminating divine intellect and creative inspiration.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "lk1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/lakshmi/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/lakshmi/thumb_01.png",
    "tab": "classic",
    "category": "lakshmi",
    "theme": "golden_hour",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#FF80AB",
      "background": "#2B1B0E"
    },
    "shlokHindi": "नमस्तेऽस्तु महामाये श्रीपीठे सुरपूजिते । शङ्खचक्रगदाहस्ते महालक्ष्मि नमोऽस्तु ते ॥",
    "shlokHinglish": "Mahalakshmi: Divine mother of auspicious wealth, spiritual abundance, and fortune on sacred pink lotus.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "h6",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman/06.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman/thumb_06.png",
    "tab": "classic",
    "category": "hanuman",
    "theme": "divine_glow",
    "themeColors": {
      "primary": "#FF9900",
      "accent": "#FFD700",
      "background": "#FDF8F0"
    },
    "shlokHindi": "अतुलितबलधामं हेमशैलाभदेहं दनुजवनकृशानुं ज्ञानिनामग्रगण्यम् । सकलगुणनिधानं वानराणामधीशं रघुपतिप्रियभक्तं वातजातं नमामि ॥",
    "shlokHinglish": "Dhyan Hanuman: Bajrangbali in deep serene devotion and prayer adorned in sacred marigold garland.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "s6",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/06.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/thumb_06.png",
    "tab": "classic",
    "category": "shiv",
    "theme": "minimalist",
    "themeColors": {
      "primary": "#64B5F6",
      "accent": "#FFFFFF",
      "background": "#EDF2F7"
    },
    "shlokHindi": "कर्पूरगौरं करुणावतारं संसारसारम् भुजगेन्द्रहारम् । सदावसन्तं हृदयारविन्दे भवं भवानीसहितं नमामि ॥",
    "shlokHinglish": "Kailash Dhyan Shiva: Mahadev meditating atop snow-crowned Himalayas on sacred tiger skin with divine Trishul.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "s7",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/07.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/thumb_07.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#7C4DFF",
      "background": "#070C15"
    },
    "shlokHindi": "ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् । उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात् ॥",
    "shlokHinglish": "Cosmic Dhyan Shiva: Serene Lord Shiva in deep celestial meditation with radiant crescent moon and cosmic mist.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "sn11",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv_neon/11.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv_neon/thumb_11.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#B388FF",
      "accent": "#7C4DFF",
      "background": "#000000"
    },
    "shlokHindi": "जटाटवीगलज्जलप्रवाहपावितस्थले गलेऽवलम्ब्य लम्बितां भुजङ्गतुङ्गमालिकाम् । डमड्डमड्डमड्डमन्निनादवडड्डमर्वयं चकार चण्डताण्डवं तनोतु नः शिवः शिवम् ॥",
    "shlokHinglish": "Trishul Tandav Shiva: Powerful neon violet luminescence with divine serpent, sacred moon, and Trishul.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "s8",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/08.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiv/thumb_08.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#7C4DFF",
      "accent": "#00E5FF",
      "background": "#05030A"
    },
    "shlokHindi": "ॐ नमः शिवाय । नागेन्द्रहाराय त्रिलोचनाय भस्माङ्गरागाय महेश्वराय । नित्याय शुद्धाय दिगम्बराय तस्मै नकाराय नमः शिवाय ॥",
    "shlokHinglish": "Adiyogi Shiva: The first yogi standing monumental amidst cosmic nebulae with glowing crescent moon aura.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:55:00Z"
  },
  {
    "id": "r8",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/08.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_08.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "neon",
    "themeColors": {
      "primary": "#FFD700",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "श्री रामचन्द्र कृपालु भजु मन हरण भवभय दारुणम् । नवकंज लोचन, कंज मुख, कर कंज, पद कंजारुणम् ॥",
    "shlokHinglish": "Golden Radiant Kodanda: Shri Ram standing adorned in celestial golden ornaments and divine bow.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:48:00Z"
  },
  {
    "id": "r7",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/07.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_07.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FF007F",
      "background": "#000000"
    },
    "shlokHindi": "रामाय रामभद्राय रामचन्द्राय वेधसे । रघुनाथाय नाथाय सीतायाः पतये नमः ॥",
    "shlokHinglish": "Neon Archer Avatar: Shri Ram with radiant arrows and glowing tilak radiating cosmic tranquility.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:47:00Z"
  },
  {
    "id": "r6",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/06.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_06.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FF4081",
      "background": "#000000"
    },
    "shlokHindi": "लोकाभिरामं रणरंगधीरं राजीवनेत्रं रघुवंशनाथम् । कारुण्यरूपं करुणाकरं तं श्रीरामचन्द्रं शरणं प्रपद्ये ॥",
    "shlokHinglish": "Maryada Purushottam: Supreme warrior of righteousness in celestial neon aura on cosmic stars.",
    "isFeatured": true,
    "createdAt": "2026-10-31T17:46:00Z"
  },
  {
    "id": "hn14",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/14.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_14.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF9900",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "संकट कटै मिटै सब पीरा । जो सुमिरै हनुमत बलबीरा ॥ जै जै जै हनुमान गोसाईं । कृपा करहु गुरुदेव की नाईं ॥",
    "shlokHinglish": "Warrior March Hanuman: Marching fearlessly with fiery radiant Gada illuminating the cosmos.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:45:00Z"
  },
  {
    "id": "hn13",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/13.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_13.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF007F",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "महावीर विक्रम बजरंगी । कुमति निवार सुमति के संगी ॥ कंचन बरन बिराज सुबेसा । कानन कुंडल कुंचित केसा ॥",
    "shlokHinglish": "Gada Veer Hanuman: Muscular neon cyan silhouette with glowing magenta Gada resting on shoulder.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:45:00Z"
  },
  {
    "id": "hn12",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/12.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_12.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FF007F",
      "background": "#000000"
    },
    "shlokHindi": "अतुलितबलधामं हेमशैलाभदेहं दनुजवनकृशानुं ज्ञानिनामग्रगण्यम् । सकलगुणनिधानं वानराणामधीशं रघुपतिप्रियभक्तं वातजातं नमामि ॥",
    "shlokHinglish": "Abhaya Mudra Blessing: Neon cyan & magenta Bajrangbali radiating divine protection and cosmic strength.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:45:00Z"
  },
  {
    "id": "hn11",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/11.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_11.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF5500",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम् । वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये ॥",
    "shlokHinglish": "Fiery Halo Dhyan: Bajrangbali in deep serene meditation with radiant solar halo and golden tilak.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:45:00Z"
  },
  {
    "id": "k8",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/08.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_08.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#FFD700",
      "background": "#000511"
    },
    "shlokHindi": "करारविन्देन पदारविन्दं मुखारविन्दे विनिवेशयन्तम्। वटस्य पत्रस्य पुटे शयानं बालं मुकुन्दं मनसा स्मरामि॥",
    "shlokHinglish": "Bal Krishna Kanha Portrait: Divine eyes, peacock feather crown, golden tilak & celestial glow.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:30:00Z"
  },
  {
    "id": "k7",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/07.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_07.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "अधरं मधुरं वदनं मधुरं नयनं मधुरं हसितं मधुरम्। हृदयं मधुरं गमनं मधुरं मधुराधिपतेरखिलं मधुरम्॥",
    "shlokHinglish": "Bansuri Aura Silhouette: Krishna playing flute amidst cosmic blue nebula & golden starlight.",
    "isFeatured": true,
    "createdAt": "2026-10-31T16:30:00Z"
  },
  {
    "id": "k1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_01.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन। मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥",
    "shlokHinglish": "Golden Flute Silhouette: Side profile with glowing Mor Pankh, sapphire rim light & radiant bansuri.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "k2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_02.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#76FF03",
      "background": "#000000"
    },
    "shlokHindi": "कस्तूरीतिलकं ललाटपटले वक्षःस्थले कौस्तुभं नासाग्रे वरमौक्तिकं करतले वेणुं करे कङ्कणम्॥",
    "shlokHinglish": "Divine Smile Close-up: Radiant eyes, glowing Vaishnav tilak & turquoise peacock feather on pure black.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "k3",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/03.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_03.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#2979FF",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत। अभ्युत्थानमधर्मस्य तदात्मानं सृजाम्यहम्॥",
    "shlokHinglish": "Yamuna Ghat Full Moon: Playing flute on ancient ghat steps, giant glowing moon & floating diyas.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "k4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_04.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#FFC400",
      "background": "#000000"
    },
    "shlokHindi": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज। अहं त्वां सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः॥",
    "shlokHinglish": "Kadamba Tree Night: Full body leaning serenely under giant mystical tree glowing with starlight.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "k5",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/05.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/krishna/thumb_05.png",
    "tab": "aesthetic",
    "category": "krishna",
    "theme": "neon",
    "themeColors": {
      "primary": "#651FFF",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "मन्मना भव मद्भक्तो मद्याजी मां नमस्कुरु। मामेवैष्यसि सत्यं ते प्रतिजाने प्रियोऽसि मे॥",
    "shlokHinglish": "Maha Raas Cosmic Vortex: Meditating in galaxy core, glowing spiral nebulae & divine aura ring.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "s1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/thumb_01.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#2979FF",
      "background": "#000000"
    },
    "shlokHindi": "ॐ नमः शिवाय। कर्पूरगौरं करुणावतारं संसारसारम्॥",
    "shlokHinglish": "Dark Rim-Light Trishul & Damru: Cyan-white neon contour on pure pitch black AMOLED.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "s2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/thumb_02.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#00B0FF",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम्। उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय मामृतात्॥",
    "shlokHinglish": "Third Eye Awakening: Fiery golden-amber third eye flame with crescent moon on jata.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "s3",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/03.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/thumb_03.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#00E5FF",
      "accent": "#76FF03",
      "background": "#000000"
    },
    "shlokHindi": "जटाटवीगलज्जलप्रवाहपावितस्थले गलेऽवलम्ब्य लम्बितां भुजङ्गतुङ्गमालिकाम्॥",
    "shlokHinglish": "Serpent Vasuki & Crescent Moon: Coiled neon green glowing cobra on Mahadev neck.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "s4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/thumb_04.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#651FFF",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "कैलासशिखरस्थाय भालचन्द्राय शम्भवे। नमो नीलकण्ठाय महादेवाय ते नमः॥",
    "shlokHinglish": "Kailash Peak Dhyan: Meditating in padmasana on mountain peak under swirling galaxy aurora.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "s5",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/05.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/shiva/thumb_05.png",
    "tab": "aesthetic",
    "category": "shiv",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "डमरूध्वनिसंयुक्तां ताण्डवनृत्यप्रियां सदा। नमामि शङ्करं देवं सर्वकामफलप्रदम्॥",
    "shlokHinglish": "Cosmic Nataraja Tandava: Fiery ring of neon flames, dynamic cosmic dance of creation.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "g1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/thumb_01.png",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9900",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "एकदन्ताय विद्महे वक्रतुण्डाय धीमहि तन्नो दन्तिः प्रचोदयात्॥",
    "shlokHinglish": "Cosmic Night Rim-Light: Golden-saffron outline emerging from pitch black darkness & stars.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "g2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/thumb_02.png",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "shadow",
    "themeColors": {
      "primary": "#FFA000",
      "accent": "#FFE082",
      "background": "#000000"
    },
    "shlokHindi": "गजाननं भूतगणादिसेवितं कपित्थजम्बूफलचारुभक्षणम्। उमासुतं शोकविनाशकारकं नमामि विघ्नेश्वरपादपङ्कजम्॥",
    "shlokHinglish": "Shadow of the God: Majestic celestial silhouette glowing above temple with tiny mushak.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "g3",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/03.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/thumb_03.png",
    "tab": "aesthetic",
    "category": "ganesh",
    "theme": "lotus",
    "themeColors": {
      "primary": "#FF5722",
      "accent": "#E040FB",
      "background": "#000000"
    },
    "shlokHindi": "श्री गणेशाय नमः। सर्वविघ्नहर्ता मंगलकर्ता॥",
    "shlokHinglish": "Lotus Galaxy: Orange, gold & magenta neon line-art on giant cosmic glowing lotus.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "g4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/thumb_04.png",
    "tab": "classic",
    "category": "ganesh",
    "theme": "festival",
    "themeColors": {
      "primary": "#FF6F00",
      "accent": "#FFD54F",
      "background": "#FFFDF5"
    },
    "shlokHindi": "वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥",
    "shlokHinglish": "Festival Grandeur: Ganesh Chaturthi royal throne, silk dhoti, modaks & golden halo.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "g5",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/05.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ganesh/thumb_05.png",
    "tab": "classic",
    "category": "ganesh",
    "theme": "cute",
    "themeColors": {
      "primary": "#FF4081",
      "accent": "#FFD700",
      "background": "#FFF5F8"
    },
    "shlokHindi": "गणपति बप्पा मोरया, मंगल मूर्ति मोरया 🐘",
    "shlokHinglish": "Cute & Calm Bal Ganesh: Sweet smile holding modak, glowing lotus & pastel cosmic clouds.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "r1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_01.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "cosmic",
    "themeColors": {
      "primary": "#FF9900",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "रामो राजमणिः सदा विजयते रामं रमेशं भजे।",
    "shlokHinglish": "Dark Rim-Light Kodanda: Golden-saffron outline emerging from darkness holding the sacred bow.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "r2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_02.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "shadow",
    "themeColors": {
      "primary": "#FFA000",
      "accent": "#FFE082",
      "background": "#000000"
    },
    "shlokHindi": "मर्यादा पुरुषोत्तम प्रभु श्री राम॥",
    "shlokHinglish": "Shadow of Ayodhya: Noble stance with bow on shoulder and glowing temple spire silhouette.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "r3",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/03.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_03.png",
    "tab": "aesthetic",
    "category": "ram",
    "theme": "kodanda",
    "themeColors": {
      "primary": "#FF6F00",
      "accent": "#FFD54F",
      "background": "#000000"
    },
    "shlokHindi": "धीरोदात्तो गुणोत्तरः। स कोऽस्मिन् साम्प्रतं लोके गुणवान् कश्च वीर्यवान्॥",
    "shlokHinglish": "Neon Kodanda Radiance: Fiery saffron-orange and electric gold line-art with glowing halo ring.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "r4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_04.png",
    "tab": "classic",
    "category": "ram",
    "theme": "saryu",
    "themeColors": {
      "primary": "#E65100",
      "accent": "#FFD700",
      "background": "#FFFDF5"
    },
    "shlokHindi": "रामो राजमणिः सदा विजयते रामं रमेशं भजे रामेणाभिहता निशाचरचमू रामाय तस्मै नमः।",
    "shlokHinglish": "Ayodhya Saryu Ghat: Divine blue-complexioned Lord Ram with Kodanda bow at sunset.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "r5",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/05.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/ram/thumb_05.png",
    "tab": "classic",
    "category": "ram",
    "theme": "darbar",
    "themeColors": {
      "primary": "#D84315",
      "accent": "#FFD54F",
      "background": "#FFF8E1"
    },
    "shlokHindi": "मंगल भवन अमंगल हारी। द्रवहु सुदसरथ अजिर बिहारी॥",
    "shlokHinglish": "Ayodhya Ram Darbar: Majestic royal court with Sita ji, Lakshman ji, and Hanuman ji.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "d1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/thumb_01.png",
    "tab": "aesthetic",
    "category": "durga",
    "theme": "shakti",
    "themeColors": {
      "primary": "#FF1744",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "सर्वमङ्गलमाङ्गल्ये शिवे सर्वार्थसाधिके। शरण्ये त्र्यम्बके गौरि नारायणि नमोऽस्तु ते॥",
    "shlokHinglish": "Dark Rim-Light Divine Face: Red-gold rim light, golden mukut, bindi & trishul on pitch black AMOLED.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "d2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/thumb_02.png",
    "tab": "aesthetic",
    "category": "durga",
    "theme": "shakti",
    "themeColors": {
      "primary": "#D50000",
      "accent": "#FFAB00",
      "background": "#000000"
    },
    "shlokHindi": "या देवी सर्वभूतेषु शक्तिरूपेण संस्थिता। नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥",
    "shlokHinglish": "Dark Rim-Light Simhavahini: Maa Durga seated calmly on noble lion with golden-red outlines.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "d4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/durga/thumb_04.png",
    "tab": "classic",
    "category": "durga",
    "theme": "classic",
    "themeColors": {
      "primary": "#C2185B",
      "accent": "#FFD700",
      "background": "#FFF5F8"
    },
    "shlokHindi": "जयन्ती मङ्गला काली भद्रकाली कपालिनी। दुर्गा क्षमा शिवा धात्री स्वाहा स्वधा नमोऽस्तु ते॥",
    "shlokHinglish": "Classic Royal Mahishasuramardini: Magnificent traditional painting with 8 arms, lion & golden aura.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn1",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/01.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_01.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF6D00",
      "accent": "#FFD600",
      "background": "#000000"
    },
    "shlokHindi": "अतुलितबलधामं हेमशैलाभदेहं दनुजवनकृशानुं ज्ञानिनामग्रगण्यम्॥",
    "shlokHinglish": "Neon Silhouette with Gada: Fiery saffron contour holding golden mace on pitch black.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn2",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/02.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_02.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF9100",
      "accent": "#FFEA00",
      "background": "#000000"
    },
    "shlokHindi": "मनोजवं मारुततुल्यवेगं जितेन्द्रियं बुद्धिमतां वरिष्ठम्॥",
    "shlokHinglish": "Pranam Mudra Golden Aura: Devotional folded hands posture with glowing lotus background.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn3",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/03.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_03.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF3D00",
      "accent": "#FFD600",
      "background": "#000000"
    },
    "shlokHindi": "वातात्मजं वानरयूथमुख्यं श्रीरामदूतं शरणं प्रपद्ये॥",
    "shlokHinglish": "Cosmic Colossal Shadow: Giant glowing guardian watching serenely over starry cosmos.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn4",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/04.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_04.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF6D00",
      "accent": "#00E5FF",
      "background": "#000000"
    },
    "shlokHindi": "लाय सजीवन लखन जियाये। श्रीरघुबीर हरषि उर लाये॥",
    "shlokHinglish": "Pawanputra Sanjeevani Udan: Carrying glowing mountain across the night sky.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn5",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/05.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_05.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF9E80",
      "accent": "#FFD700",
      "background": "#000000"
    },
    "shlokHindi": "महाबीर बिक्रम बजरंगी। कुमति निवार सुमति के संगी॥",
    "shlokHinglish": "Veera Hanuman Sunset: Mighty stance holding sacred golden gada on shoulder.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn6",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/06.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_06.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF5722",
      "accent": "#FFD600",
      "background": "#000000"
    },
    "shlokHindi": "रामदूत अतुलित बलधामा। अंजनिपुत्र पवनसुत नामा॥",
    "shlokHinglish": "AMOLED Glowing Tilak Contour: Minimal dark silhouette with radiant white-red tilak.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn7",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/07.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_07.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF6D00",
      "accent": "#FFAB00",
      "background": "#000000"
    },
    "shlokHindi": "जय जय जय हनुमान गोसाईं। कृपा करहु गुरुदेव की नाईं॥",
    "shlokHinglish": "Dark Warrior Neon Gada: Fiery eyes, glowing tilak and protective aura.",
    "isFeatured": true,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn8",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/08.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_08.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FFA000",
      "accent": "#FFD54F",
      "background": "#000000"
    },
    "shlokHindi": "हाथ बज्र औ ध्वजा बिराजै। कांधे मूँज जनेऊ साजै॥",
    "shlokHinglish": "AMOLED Sacred Golden Gada: Minimal black background with divine floating embers.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn9",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/09.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_09.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FFAB00",
      "accent": "#FF6D00",
      "background": "#000000"
    },
    "shlokHindi": "कंचन बरन बिराज सुबेसा। कानन कुंडल कुंचित केसा॥",
    "shlokHinglish": "Bhakti Pranam Lotus Aura: Pure devotion with folded hands in temple light.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  },
  {
    "id": "hn10",
    "imageUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/10.png",
    "thumbnailUrl": "https://raw.githubusercontent.com/ashish986/DivineWall/main/wallpapers/hanuman_neon/thumb_10.png",
    "tab": "aesthetic",
    "category": "hanuman",
    "theme": "neon",
    "themeColors": {
      "primary": "#FF6F00",
      "accent": "#FFD54F",
      "background": "#000000"
    },
    "shlokHindi": "संकट कटै मिटै सब पीरा। जो सुमिरै हनुमत बलबीरा॥",
    "shlokHinglish": "Celestial Guardian Dusk: Watching peacefully over creation from high mountain ridge.",
    "isFeatured": false,
    "createdAt": "2026-10-31T12:00:00Z"
  }
]

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(wallpapers, f, indent=2, ensure_ascii=False)

print(f'Successfully created {json_path} with {len(wallpapers)} wallpapers!')
