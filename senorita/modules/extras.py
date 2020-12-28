import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from senorita import dispatcher
from senorita.modules.disable import DisableAbleCommandHandler

ABUSE_STRINGS = (
    "OO BOCHLIKE SUDHAR JAA",
    "JAKE PADHAI LIKHAI KR DIMAG MT KHARAB KR ",
    "GIRLS KI RESPECT KR BAE CHUTIYE",
    "SALA PAGAL H KYA🤐",
    "IDHR SUN BAE GANDU",
    "TERA BAAP AAYA ...PROFESSOR ",
    "गजब कि चुतियागीरी चल रही ",
    "कुते भाग जा",
    "बड़े हरामी हो बेटा",
    "खाता है इधर का गाता है  उधर का! भारत हमारी मां है इज्जत दे भरवे",
    "अबे ग*ड न फुलाओ, माँ चो* देंगे तुम्हारी",
    "अटैक में भी गन, डिफेंस में भी गन, हम बनाएंगे bihar को अमेरिका PROFESSOR😎",
    "ज़िंदगी हो तो ऐसी हो, ज़िंदा तो झ*ट के बाल भी हैं",
    "साले हॉर्न ग*ड में डाल देंगे अभी, पो पो पो पो ……… हेलीकॉप्टर बनके जाओगे Professor😎",
    "माता जी यहाँ हैं , बहन यहाँ है, माँ-बहन एक करने में आसानी होगी। Professor😎🔥”    ",
    "म्यूजिक बंद कर माद*चो*",
    "Babuji ne kaha gaon chhod do ... sab ne kaha Paro ko chhod do ... Paro ne kaha sharab chhod do ... aaj tumne keh diya grouop chhod do ... ek din aayega jab woh kahenge, duniya hi chhod do   😖",
    "Ab jyada nhi bolenge sidhe thok denge",
    "NIKAL LAUDI PAHLE FURSAT ME NIKAL PROFESSOR BAAP H TERA BULAU KYA.....😏"
)

SONG_STRINGS = (
    "🎶 Bann ha Tu meri Rani.. tenu Mahal gawa dunga💐 🎶.",
    "🎶 Mauka Milega To Ham Bta Denge,,Tumhe Kitna Pyaar Karte Hai Sanam... 🎶",
    "🎶 Yaara teri yaari ko Maine to khuda maana Yaad karegi duniya Tera mera afsana.... 🎶", 
    "🎶 Pal bhar ke liye koi hume pyaar karle, Jhoota hi sahi. ... 🎶", 
    "🎶 Telegram ki Rani Hu Mera professor Yaha Ka kottwal Apne baap Ka n samjho maal... 🎶", 
 )

@run_async
def abuse(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(ABUSE_STRINGS))
    else:
      message.reply_text(random.choice(ABUSE_STRINGS))

@run_async
def sing(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SONG_STRINGS))
    else:
      message.reply_text(random.choice(SONG_STRINGS))

__help__ = """
- /abuse : Abuse someone in Professor style.
- /sing : First lines of some random hindi  Songs.
"""

__mod_name__ = "Extras"

ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
