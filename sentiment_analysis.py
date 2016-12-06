"""VADER"""
"""Citation for VADER: 
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014."""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv

"""ACCESSS DATA"""
"""
mon = open('mon.txt', 'r')
tue = open('tue.txt', 'r')
wed = open('wed.txt', 'r')
thu = open('thu.txt', 'r')
fri = open('fri.txt', 'r')
sat = open('sat.txt', 'r')
sun = open('sun.txt', 'r')

mon_tweets


mon.close()
tue.close()
wed.close()
thu.close()
fri.close()
sat.close()
sun.close()
"""
mon_tweets = ['I havent been on here for 2 months! Wow!  Hello to everyone! Gonna get on FB now. :D', "is so glad the a/c is done. now i'm back on my reg routine. yea! i'm also LOVIN this sunshine! it's about damn time!!!", '@blondielalonde I kinda figured everyone was a fun tie to the whole night. :)', "I liked a @YouTube video https://t.co/rb9pulGMbM Miss Mulatto - No More Talking 'The Rap Game'", 'I liked a @YouTube video from @littlecarlyyt https://t.co/2g7aGkV6ID Minecraft-Little Carly Adventures-DRESS SHOPPING FOR THE NEXT', 'The stone face Clinton-Trump fama, the "pit" reminds me of American Gladiator....which would be more dignified than what I expect to see', "I'm at Denver International Airport - @denairport in Denver, CO https://t.co/p7DOU508sX", "I'm at Petersen Automotive Museum - @petersen_museum in Los Angeles, CA https://t.co/x8d2000lfe", "I'm at Miracle Mile Food Trucks in Los Angeles, CA https://t.co/pwyMDnEVVK", "I'm at Hollywood Walk of Fame in Hollywood, CA https://t.co/1IFemmDfGU", "I'm at Pancho's Restaurant - @panchos_mb in Manhattan Beach, CA https://t.co/hZceu0Hutj", 'Excellent insight via @Blavity https://t.co/OKIMdFuQ0m #relocation #employment #worklifebalance', 'At it again - @nymgamer cranking out quality food for thought! #AR #VR #BlackMirror https://t.co/rtyzaL36Zm', "Minnesota's race gap in voter participation echos some key health gaps. Agreed - it's concerning. #HealthEquity… https://t.co/xbwkOzqWzY", 'I added @sanebox to my inbox to beat email overload. Try it for free: http://t.co/KH5v60cik7', 'Ticket to DC Margarita March https://t.co/j6smMCtD1A via @LivingSocial', "RT @Brook_star: I'd just like to say that @sbarksdale2 is such a ride or die joint. Lol, she goes (cont) http://t.co/a41YSoJZaB", '#glamlife is over...back to my #reallife. He made me do dishes in full hair &amp; makeup!!!… http://t.co/IwvVS8CkYF', 'Mr @kanyewest for president #2020 🇺🇸', "Welp. Guess I was wrong. 💁🏼 I'm okay with this cavs win.", "Double overtime. I'm calling it right now. 🏀 #NBAFinals2015", 'My vegan journey begins tomorrow #nervous ❌🚫🐔🐓🐮🐷🐣', '@KStater91 Carson Palmer just threw his third TD pass.', "@KStater91 I'm confident I might still grab the last playoff spot even if I lose to you, so it's OK. :)", '@lovethewayUNLAY he was like "you\'re right nga, people will retweet/like if it\'s relatable" ☹️😅', 'Most definately #TeamCap #ScarletWitch  😍', 'Finally makes it to Las Vegas... @britneyspears  isnt performing 😭', 'City Select 2014 Giveaway http://t.co/qoAXF5MLKB', '@RattKilla lmao! I am sure u dp', "hi my name is Regina &amp; I'm a creep 🙃 https://t.co/uGd0GbO9U9", 'I just entered to win a 9-month supply of prenatal vitamins. You can too! http://t.co/yMEjrY8P http://t.co/tHeTgIXQ', 'Learn about SEO in 2016 https://t.co/z600NDAaN4 #hoboseo', 'New Today - Rich Cards expands to more verticals https://t.co/K0WMAfOJz5', 'Are H1 Tags Important For SEO? https://t.co/nNaSgpbVUb #hoboseo', "OMG AREN'T YOU FUN https://t.co/U757vmPhAq", 'Tips on how to listen to the (thousands and thousands and thousands) of dead ones? https://t.co/pDabjFubBf', '@ArizonaDOT thank you so much!', 'Hey @ArizonaDOT - help! No one is answering phones and I need to report our move to Ohio. (Can I get part of my registration fee back??)', 'Sometimes we smile in our sleep :) #babygram #babygarcia https://t.co/3hFKCD8vN8', 'First meal on the new stove! #countryliving https://t.co/QDbSWyBaro', "@His_Dreamgirl @DF_4_RCM Tattoo talk?! I'm ready for another! See you in Seattle on Saturday :)))", '@gemstwin @His_Dreamgirl @wzDMBfan Hi Amber! how are you?', '@His_Dreamgirl @wzDMBfan the Gorge? How about Indy!!! cartwheels at the Conrad!? Is it June 20th yet? ;)', 'Nnnooooooo Riiiiccckkkkkkk #TheWalkingDead', "@WyzeChef we can only hope... who's worse Tara or Carl?", 'So disrespectful #TheWalkingDead', 'Look at her #TheWalkingDead', 'After day 2 of the Sydney test was rained out, Cricket Australia have issued a Gayle warning, while the Hurricanes were not so threatening.', 'Finally some cricket being played after rain delays all morning. Loving the front row seats. @… https://t.co/sjUQ0cCxAI', 'At the cricket with dad #sydneytest #zincup @commbank @ Sydney Cricket Ground (SCG) https://t.co/PHY7urbUub', "Hotline Bling groove progress. Still working on it but happy with how it's sounding.… https://t.co/kfCNxxfXBQ", '@ChrisRGMcPhail I remember you doing this too ❤️ thought of you when I learned the sad news! X', '@nickybyrneoffic great show with the lads 2day on 2fm... was tuned in for whole show... made my day xx', 'presale tickets for westlife 2morrow... whooo hope i get them', 'loving the songs iv heard so far cant wait tll next week for album.. ye were fab on childline, children in need n the lotto welcome back xx', 'Never felt so betrayed in my life', 'Video: My new favorite commercial. Well done Deutsch LA! http://tumblr.com/xda1zs4v90', 'My first GIF. yay! http://tumblr.com/xda1rsxuhk', 'Wow "...$4.325 billion in cash..." how do you carry that?\nJohnson &amp; Johnson to buy AMO for $4.33 billion in cash https://t.co/6x69MELGgU', '@__debo Happy birthday!!!! 🎉🎈🎂🎁 hope you have a lovely Aussie birthday!!!! x', '*Blocks @Amazon on every device for the rest of the day to save bank account*', 'Made my holiday baking grocery list. First item is: butter (x6). #LETSDOIT #DIABETES', "'Ricas Tapas!' ONLY @ Saffron Restaurant &amp; Bar. Don't miss out on trying Sensational Flavours with our very own... https://t.co/QoR3Kquocm", 'Raspberry Ketone is all the new craze!! http://t.co/ku7CWjNH', 'Health Benefits of Raspberry Ketone http://t.co/JqhRix6L', "have you signed jordin sparks' bday card yet? http://www.groupcard.com/c/EJE9Vz_JtKU", "have you signed jordin's bday card yet? http://www.groupcard.com/c/EJE9Vz_JtKU", 'Are you going to celebrate your birthday with your family and friends? :) Vikings extends their Birthday promo... http://t.co/b6C4EfcdiV', "Mochi is a delicious Japanese delicacy usually eaten during New Year. What's your favorite mochi flavor?... http://t.co/uIFAnjAxPu", "There are only 2 days before the year 2015 starts, how's your preparation for the upcoming Media Noche going? :)... http://t.co/XjUsi8KqwY", 'I  know you guys love Lechong Kawali :) http://t.co/2B1aXalmGe', "Egg Muffins for breakfast, anyone? :) \n\nHere's a step-by-step recipe that you can do in less than an hour. http://t.co/FYwu5Lxyez", 'Voluntarily drinking water.', 'Back to homelessness again', 'alive, alive ho', 'Where is this thing called sleep', '@atavistian lol, sounds real familiar on staying awake', 'Attempting to stat awake', 'Sleep would be a blessing', 'Uh oh. I just heard some high schooler  referring to "The Rock" as Dwayne Johnson.  Didn\'t see that one coming with age..', "@sarahsams93 @MattBellassai I've never seen a more accurate tweet in my life", 'I wonder if @ArizonaDOT feels like a broken record yet? Bless you for your patience and thanks for the updates on the I17 crash.', 'Drive safely out there and watch your speed limits through school zones now that school is back… https://t.co/ssjbXbIBRc', '@AngryBlackLady the Bernie jacket. Dude. 😒😒😒😒😒', "What's with white guys getting older and dyeing their hair orange? I'm seeing it a lot on sportscasters and tv dudes.", 'What I love most about @Theresacaputo is that she is such a bright spirit who radiates positivity! Love #LongIslandMedium!', "Raider Red's favorite tailgate dish is BEVO! It's what's for dinner! #CapitalOneRaiderRed", '@KoolestKidOut I am so sick right now. 12:06 and there was nothing left for me 😢😢😢 plz tell me you will be releasing more...', 'Congratulations to the newlyweds!!!!! Stay away from pregnant people! They are contagious!!!… https://t.co/cVR9kkUs35']

"""TOKENIZE"""
mon_tokenized = [tokenize.sent_tokenize(tweet) for tweet in mon_tweets]
monday = []
for tweet in mon_tokenized:
    monday.append(tweet[0])

"""SENTIMENT ANALYSIS"""
"""
sid = SentimentIntensityAnalyzer()
for tweet in monday:
    print (tweet)
    ss = sid.polarity_scores(tweet)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print ()
"""
"""SENTIMENT ANALYSIS AND WRITE TO CSV"""
sid = SentimentIntensityAnalyzer()
with open('mon.csv', 'w') as csvfile:
    fieldnames = ['compound', 'neg', 'neu', 'pos', 'tweet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for tweet in monday:
        print (tweet)
        ss = sid.polarity_scores(tweet)
        ss['tweet'] = tweet
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        writer.writerow(ss)
        print ()



