# Implementation from https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
# from flask import *

# text_str = '''
# Those Who Are Resilient Stay In The Game Longer
# “On the mountains of truth you can never climb in vain: either you will reach a point higher up today, or you will be training your powers so that you will be able to climb higher tomorrow.” — Friedrich Nietzsche
# Challenges and setbacks are not meant to defeat you, but promote you. However, I realise after many years of defeats, it can crush your spirit and it is easier to give up than risk further setbacks and disappointments. Have you experienced this before? To be honest, I don’t have the answers. I can’t tell you what the right course of action is; only you will know. However, it’s important not to be discouraged by failure when pursuing a goal or a dream, since failure itself means different things to different people. To a person with a Fixed Mindset failure is a blow to their self-esteem, yet to a person with a Growth Mindset, it’s an opportunity to improve and find new ways to overcome their obstacles. Same failure, yet different responses. Who is right and who is wrong? Neither. Each person has a different mindset that decides their outcome. Those who are resilient stay in the game longer and draw on their inner means to succeed.
# I’ve coached mummy and mom clients who gave up after many years toiling away at their respective goal or dream. It was at that point their biggest breakthrough came. Perhaps all those years of perseverance finally paid off. It was the 19th Century’s minister Henry Ward Beecher who once said: “One’s best success comes after their greatest disappointments.” No one knows what the future holds, so your only guide is whether you can endure repeated defeats and disappointments and still pursue your dream. Consider the advice from the American academic and psychologist Angela Duckworth who writes in Grit: The Power of Passion and Perseverance: “Many of us, it seems, quit what we start far too early and far too often. Even more than the effort a gritty person puts in on a single day, what matters is that they wake up the next day, and the next, ready to get on that treadmill and keep going.”
# I know one thing for certain: don’t settle for less than what you’re capable of, but strive for something bigger. Some of you reading this might identify with this message because it resonates with you on a deeper level. For others, at the end of their tether the message might be nothing more than a trivial pep talk. What I wish to convey irrespective of where you are in your journey is: NEVER settle for less. If you settle for less, you will receive less than you deserve and convince yourself you are justified to receive it.
# “Two people on a precipice over Yosemite Valley” by Nathan Shipps on Unsplash
# Develop A Powerful Vision Of What You Want
# “Your problem is to bridge the gap which exists between where you are now and the goal you intend to reach.” — Earl Nightingale
# I recall a passage my father often used growing up in 1990s: “Don’t tell me your problems unless you’ve spent weeks trying to solve them yourself.” That advice has echoed in my mind for decades and became my motivator. Don’t leave it to other people or outside circumstances to motivate you because you will be let down every time. It must come from within you. Gnaw away at your problems until you solve them or find a solution. Problems are not stop signs, they are advising you that more work is required to overcome them. Most times, problems help you gain a skill or develop the resources to succeed later. So embrace your challenges and develop the grit to push past them instead of retreat in resignation. Where are you settling in your life right now? Could you be you playing for bigger stakes than you are? Are you willing to play bigger even if it means repeated failures and setbacks? You should ask yourself these questions to decide whether you’re willing to put yourself on the line or settle for less. And that’s fine if you’re content to receive less, as long as you’re not regretful later.
# If you have not achieved the success you deserve and are considering giving up, will you regret it in a few years or decades from now? Only you can answer that, but you should carve out time to discover your motivation for pursuing your goals. It’s a fact, if you don’t know what you want you’ll get what life hands you and it may not be in your best interest, affirms author Larry Weidel: “Winners know that if you don’t figure out what you want, you’ll get whatever life hands you.” The key is to develop a powerful vision of what you want and hold that image in your mind. Nurture it daily and give it life by taking purposeful action towards it.
# Vision + desire + dedication + patience + daily action leads to astonishing success. Are you willing to commit to this way of life or jump ship at the first sign of failure? I’m amused when I read questions written by millennials on Quora who ask how they can become rich and famous or the next Elon Musk. Success is a fickle and long game with highs and lows. Similarly, there are no assurances even if you’re an overnight sensation, to sustain it for long, particularly if you don’t have the mental and emotional means to endure it. This means you must rely on the one true constant in your favour: your personal development. The more you grow, the more you gain in terms of financial resources, status, success — simple. If you leave it to outside conditions to dictate your circumstances, you are rolling the dice on your future.
# So become intentional on what you want out of life. Commit to it. Nurture your dreams. Focus on your development and if you want to give up, know what’s involved before you take the plunge. Because I assure you, someone out there right now is working harder than you, reading more books, sleeping less and sacrificing all they have to realise their dreams and it may contest with yours. Don’t leave your dreams to chance.
# '''

import nltk
nltk.download

import requests
from bs4 import BeautifulSoup

# /////////////////////////////////////////////////////////////////////////////////////



def test_function():
    print("Hello World")


def trade_spider(url):
    # url = "https://indianexpress.com/article/world/coronavirus-india-china-south-korea-world-outbreak-live-updates-6300155/?#liveblogstart"
    # urls = "https://www.thehindu.com/news/national/parliament-updates-live-house-reassembles-after-a-break/article30988017.ece?homepage=true"
    # url = "https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_89%3ARedmi&dc&fst=as%3Aoff&qid=1583409680&rnid=3837712031&ref=lp_1389401031_nr_p_89_0"
    # url = "https://en.wikipedia.org/wiki/Mahatma_Gandhi"

    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text)

    # print(soup)
    val=""
    # for link in soup.find_all('p', {'itemprop', 'articleBody'}):
    for link in soup.find_all('p'):
        # href = "https://en.wikipedia.org/" + link.get('href')
        title =link.string
        # print(title)
        val=val+convert_string(title)
    # print("sgedgdg",val)
    return val


    # print("dfhgfhfghgfhf", source_code)

    # print(title[0])


def trade_spiders(urls):
    # url = "https://indianexpress.com/article/world/coronavirus-india-china-south-korea-world-outbreak-live-updates-6300155/?#liveblogstart"
    # urls = "https://timesofindia.indiatimes.com/india/coronavirus-in-india-live-updates-28529-people-being-monitored-harsh-vardhan-tells-parliament/liveblog/74484303.cms"
    # url = "https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_89%3ARedmi&dc&fst=as%3Aoff&qid=1583409680&rnid=3837712031&ref=lp_1389401031_nr_p_89_0"
    # url = "https://en.wikipedia.org/wiki/Mahatma_Gandhi"

    source_code = requests.get(urls)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text)

    # print(soup)
    val=""
    # for link in soup.find_all('p', {'itemprop', 'articleBody'}):
    for link in soup.find_all('p'):
        # href = "https://en.wikipedia.org/" + link.get('href')
        title =link.string
        # print(title)
        val=val+convert_string(title)

    return val


def convert_string(value):
    new_value = str(value)
    return new_value



# /////////////////////////////////////////////////////////////////////////////////////








def _create_frequency_table(text_string) -> dict:
    """
    we create a dictionary for the word frequency table.
    For this, we should only use the words that are not part of the stopWords array.
    Removing stop words and making frequency table
    Stemmer - an algorithm to bring words to its root word.
    :rtype: dict
    """
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable


def _score_sentences(sentences, freqTable) -> dict:
    """
    score a sentence by its words
    Basic algorithm: adding the frequency of every non-stop word in a sentence divided by total no of words in a sentence.
    :rtype: dict
    """

    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        word_count_in_sentence_except_stop_words = 0
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                word_count_in_sentence_except_stop_words += 1
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        if sentence[:10] in sentenceValue:
            sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] / word_count_in_sentence_except_stop_words

        '''
        Notice that a potential issue with our score algorithm is that long sentences will have an advantage over short sentences. 
        To solve this, we're dividing every sentence score by the number of words in the sentence.
        
        Note that here sentence[:10] is the first 10 character of any sentence, this is to save memory while saving keys of
        the dictionary.
        '''

    return sentenceValue


def _find_average_score(sentenceValue) -> int:
    """
    Find the average score from the sentence value dictionary
    :rtype: int
    """
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = (sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] >= (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary


def run_summarization(text):
    # 1 Create the word frequency table
    freq_table = _create_frequency_table(text)

    '''
    We already have a sentence tokenizer, so we just need 
    to run the sent_tokenize() method to create the array of sentences.
    '''

    # 2 Tokenize the sentences
    sentences = sent_tokenize(text)

    # 3 Important Algorithm: score the sentences
    sentence_scores = _score_sentences(sentences, freq_table)

    # 4 Find the threshold
    threshold = _find_average_score(sentence_scores)

    # 5 Important Algorithm: Generate the summary
    summary = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

    return summary


# if __name__ == '__main__':
#     fu = request.form['furl']
#     su = request.form['surl']
#
#     val = trade_spider(fu)
#     # print("checked",val)
#     vals = trade_spiders(su)
#     # print("checkedval", vals)
#
#     valmain = val + vals
#
#     result = run_summarization(valmain)
#     print(result)

# val = """Petrol and diesel prices on Thursday were hiked by 25 paise per litre each, the second straight day of increase in rates that took the prices to new highs.Petrol now costs ₹84.70 per litre in Delhi and diesel is priced at ₹74.88, according to a price notification from oil marketing companies. This is the second straight day of a price increase. Rates were hiked by 25 paise each on Wednesday after a five-day hiatus. In Mumbai, the price of petrol was increased to ₹91.32 a litre from ₹91.07 previously, while diesel rates went up from ₹81.34 to ₹81.60 per litre. Petrol price is at a record high in Delhi and is just a shy away from the highest ever rate of ₹91.34 in Mumbai. Diesel price in Mumbai is at an all-time high. State-owned fuel retailers — Indian Oil Corporation Ltd (IOC), Bharat Petroleum Corporation Ltd (BPCL) and Hindustan Petroleum Corporation Ltd (HPCL) — had on January 6, resumed daily price revision after nearly a month-long hiatus. Rates were hiked on two consecutive days - totalling 49 paise for petrol and 51 paise for diesel — before they hit a pause button again. The price increase cycle resumed on Wednesday, after international oil prices rose to their highest level since February 2020, before the coronavirus outbreak in China began spreading across the world, forcing lockdowns that shaved off demand. Rates, however, eased a bit on Thursday with Brent down 11 cents to USD 55.95 per barrel while NYMEX light sweet crude was down 10 cents at USD 52.81. The highest ever rate of diesel in Delhi was touched on October 4, 2018, when it touched ₹75.45 a litre mark. On that day petrol was priced at ₹ 84. In Mumbai, the highest level for petrol was also on the same day when it scaled to ₹91.34. The government had responded to the situation in October 2018, by cutting excise duty on petrol and diesel by ₹1.50 per litre in a bid to ease inflationary pressure and boost consumer confidence. Alongside, state-owned fuel retailers cut prices by another ₹1 a litre, which they recouped later. Though petrol and diesel rates are to be revised on a daily basis in line with benchmark international price and foreign exchange, government-controlled fuel retailers have been moderating rates since the pandemic broke out. This after they adjusted a ₹13 per litre hike in excise duty on petrol and ₹15 a litre on diesel, against a decrease in the retail selling price that was warranted by crude oil prices falling to an average of USD 19 per barrel in April. Excise duty totals ₹32.98 per litre in petrol and ₹31.83 in diesel. VAT in Delhi totals to ₹19.32 a litre on petrol and ₹10.85 on diesel. With international oil prices rebounding from the lows of April, retail rates in India too were revised. Since May 2020, petrol price has risen by ₹15.04 per litre and diesel by ₹12.59 a litre, price notifications of oil companies showed."""
# print("checked",val)
# vals = """Petrol price on Friday was hiked by 57 paise per litre and diesel by 59 paise a litre as oil companies adjusted retail rates - the sixth straight day of increase in rates since oil firms ended an 82-day hiatus of rate revision.In six hikes, petrol price has gone up by Rs 3.31 per litre and diesel by Rs 3.42. Petrol price in Delhi was hiked to Rs 74.57 per litre from Rs 74, while diesel rates were increased to Rs 72.81 a litre from Rs 72.22, according to a price notification of state oil marketing companies. Rates have been increased across the country and vary in each state depending on the incidence of local sales tax or value added tax. This is the sixth consecutive daily increase in rates since oil companies on Sunday restarted revising prices in line with costs, after ending an 82-day hiatus. In six hikes, petrol price has gone up by Rs 3.31 per litre and diesel by Rs 3.42. Petrol and diesel prices on Thursday were hiked by 60 paise per litre each - the fifth straight daily increase in rates since oil PSUs ended an 82-day hiatus in rate revision. Petrol price on Wednesday was hiked by 40 paise per litre and diesel by 45 paise, the fourth straight daily increase in rates after oil PSUs ended an 82-day hiatus in rate revision. Petrol price on Tuesday was hiked by 54 paise per litre and diesel by 58 paise a litre - the third straight daily increase in rates after oil PSUs ended an 82-day hiatus in rate revision Prices were raised by 60 paise per litre each on both petrol and diesel on Sunday as well as on Monday. In all, petrol price has gone up by Rs 1.74 per litre and diesel by Rs 1.78 a litre in three days."""
# print("checkedval", vals)
# valmain=val+vals
# result=run_summarization(valmain)
# print("dg",result)
