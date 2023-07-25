import os

api_id = int(os.environ.get("API_ID", "24465982"))
api_hash = os.environ.get("API_HASH", "2b3131b7d3f6a42bd4ae1ba3b58c11c4")
bot_token = os.environ.get("BOT_TOKEN", "6174363799:AAFZaR-eJ0NYdBInhKpIVXO8TK4QAjJMQqA")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://cicimail:<password>@cluster0.edaepoo.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001803534224"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001667852253"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1001884106616"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1001861428348"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1837660746"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "25"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "25"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "25"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "25"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "25"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "25"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "25"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#FwbGirl #FwbBoy #FwbAsk #FwbFind #FwbSpill #FwbStory #FwbTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/be7557797c055f7aaefda.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/41918a7d034b943307201.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://telegra.ph/file/a44172fea6755cc697a5c.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://telegra.ph/file/14ca710511333621be61d.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://telegra.ph/file/10232ac2404b3e822f99d.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://telegra.ph/file/90359cf42550732058d20.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://telegra.ph/file/432e8cb26179ade6eba70.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://telegra.ph/file/e0dc732430d9b1b0cbfa1.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph/file/197089300f64d33a3535e.jpg")
pic_ownergirl = os.environ.get("PIC_OWNERGIRL" , "https://telegra.ph/file/bdb7a2c65d9e1272af639.jpg")
pic_neko = os.environ.get("PIC_NEKO" , "https://telegra.ph/file/2d46007dd7d22645c4ec3.jpg")
pic_admingirl = os.environ.get("PIC_ADMINGIRL" , "https://telegra.ph/file/30c7b36f68d69840a762c.jpg")
pic_adminboy = os.environ.get("PIC_ADMINBOY" , "https://telegra.ph/file/192be803ec6722b3935ab.jpg")
# ============================================================#
pic_rekberboy = os.environ.get("PIC_REKBERBOY", "https://telegra.ph/file/78acf322385616cb5bab0.jpg")

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#FwbBoy / #FwbGirl untuk Mencari Pasangan,Teman , Partner dll
#FwbAsk untuk Bertanya
#FwbStory untuk Berbagi Cerita
#FwbSpill untuk Spill Masalah
#FwbFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#FwbBoy / #FwbGirl untuk Mencari Pasangan, Teman , Partner dll
#FwbAsk untuk Bertanya
#FwbStory untuk Berbagi Cerita
#FwbSpill untuk Spill Masalah
#FwbFind untuk Mencari Pasangan, Teman, Partner dll
""")
