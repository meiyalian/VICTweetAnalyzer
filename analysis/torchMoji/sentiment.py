import re
import emoji
import numpy as np
import emoji, json
from torchmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH
from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis
import couchdb  # importing couchdb
from datetime import datetime


EMOJIS = ":joy: :unamused: :weary: :sob: :heart_eyes: :pensive: :ok_hand: :blush: :heart: :smirk: :grin: :notes: :flushed: :100: :sleeping: :relieved: :relaxed: :raised_hands: :two_hearts: :expressionless: :sweat_smile: :pray: :confused: :kissing_heart: :heartbeat: :neutral_face: :information_desk_person: :disappointed: :see_no_evil: :tired_face: :v: :sunglasses: :rage: :thumbsup: :cry: :sleepy: :yum: :triumph: :hand: :mask: :clap: :eyes: :gun: :persevere: :smiling_imp: :sweat: :broken_heart: :yellow_heart: :musical_note: :speak_no_evil: :wink: :skull: :confounded: :smile: :stuck_out_tongue_winking_eye: :angry: :no_good: :muscle: :facepunch: :purple_heart: :sparkling_heart: :blue_heart: :grimacing: :sparkles:".split(
    ' ')
model = torchmoji_emojis(PRETRAINED_PATH)
with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)
st = SentenceTokenizer(vocabulary, 30)

# reference :https://github.com/huggingface/torchMoji/blob/master/examples/text_emojize.py
def deepmojify(sentence, top_n=5):
    def top_elements(array, k):
        ind = np.argpartition(array, -k)[-k:]
        return ind[np.argsort(array[ind])][::-1]

    tokenized, _, _ = st.tokenize_sentences([sentence])
    prob = model(tokenized)[0]
    emoji_ids = top_elements(prob, top_n)
    emojis = map(lambda x: EMOJIS[x], emoji_ids)
    return emoji.emojize(f"{sentence} {' '.join(emojis)}", use_aliases=True)


def get_emoji(sentence):
    if sentence == "":
        return sentence
    else:
        return deepmojify(sentence).split()[-5:]

#reference: https://stackoverflow.com/a/52571541
def give_emoji_free_text(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

def get_unicode(s):
    string_unicode = str(s)
    string_encode = string_unicode.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode


def process_tweets(text):
    txt = re.sub('@[\w]+','',text)
    txt = txt.lower()
    rem_txt = re.sub(r"http\S+", "", txt)
    rem_txt_e = give_emoji_free_text(get_unicode(rem_txt))
    return rem_txt_e

# reference: CCC Assignment one
def get_word_and_score(text):
    last_space_pos = 0
    for i in range(len(text)):
        try:
            int(text[i:].split()[0])
            last_space_pos = i
            break
        except:
            continue
    return text[:last_space_pos], int(text[last_space_pos + 1:])

# reference: CCC Assignment one
def get_words_from_index(text):
    text_splited = text.split()
    afinn_words = {}
    afinn_phrase = {}
    words = []
    for word in text_splited:
        exact_word = get_exact_word(word)
        if words_index.get(exact_word) is not None:
            for afinn_word in words_index[exact_word]:
                if len(afinn_word.split()) > 1:
                    afinn_phrase[afinn_word] = None
                else:
                    afinn_words[afinn_word] = None
    for word in afinn_phrase.keys():
        words.append(word)
    for word in afinn_words.keys():
        words.append(word)
    return words


# reference: CCC Assignment one
def get_exact_word(text):
    start = -1
    end = -1
    
    for i in range(len(text)):
        punctuation_index = '?.!,\'"'.find(text[i])
        if punctuation_index == -1 and start == -1:
            start = i
            continue
        if punctuation_index != -1 and start != -1:
            end = i
            break
    if end != -1:
        return text[start:end]
    else:
        return text[start:]

# reference: CCC Assignment one
def get_score(content):
    total_score = 0
    for word in get_words_from_index(content):
        regex = "[' ']" + word + '[?.!,\'" ]|' + '^' + word + \
                '[?.!,\'" ]|' + "[' ']" + word + '$|' + '^' + word + '$'
        matches = re.findall(regex, content)
        score = words_score[word]
        if len(matches) != 0:
            content = content.replace(word, '')
        # print('matched words: ', matches, ' score: ',score)
        # print('tweet content: ',text)
        total_score += len(matches) * score
    return total_score


def get_hashtags(text):
    list_hash = [i  for i in str(text).split() if i.startswith("#")]
    return list_hash



host = "172.26.132.110"
port = "5984"
username = password = "admin"


def connect_to_couch_db_server(host, port, username, password):
    return couchdb.Server('http://' + username + ':' + password + '@' + host + ':' + port)


def connect_to_database(database_name, server):
    try:
        return server[database_name]
    except:
        return server.create(database_name)


if __name__ == '__main__':

    words_score = {}
    words_index = {}

    file_words = open('AFINN.txt', 'r')
    try:
        while True:
            text_line = file_words.readline()
            if text_line:
                word, score = get_word_and_score(text_line)
                words_score[word] = score
                index = word.split()[0]
                if words_index.get(index) is None:
                    index_value = [word]
                    words_index[index] = index_value
                else:
                    words_index[index].append(word)
            else:
                break

    finally:
        file_words.close()

    dbserver = connect_to_couch_db_server(host, port, username, password)
    vic_tweets = connect_to_database("vic_tweets", dbserver)
    # analysis = connect_to_database("analysis", dbserver)
    analysis = connect_to_database("test_db",dbserver)
    # sentiment_tweets_db = connect_to_database("sentiment_tweets", dbserver)
   #since = 1
    count = 0
    firstTime = True
    analysis_count = 0
    since =""
    while True:
        try:
            if firstTime:
                changes = vic_tweets.changes(limit = 5000,  filter="vic_tweets/important" )
                firstTime = False
            else:
                changes = vic_tweets.changes(since=since, limit = 5000,  filter="vic_tweets/important" )
            
            since = changes["last_seq"]
            for changeset in changes["results"]:
                try:
                    doc = vic_tweets[changeset["id"]]
                except couchdb.http.ResourceNotFound:
                    continue
                else:
                    analysis_id = changeset["id"] + "_analysis"
                    analysis_count +=1
                    if analysis_count % 2000 == 0:
                        print("check {} tweets.".format(analysis_count))
                    if analysis_id not in analysis:
                        try:
                            txt = doc['text']
                            p_txt = process_tweets(txt)
                            time = doc['time']
                            datetime_t = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                            hour = datetime_t.hour
                            location = doc['location']
                            score = get_score(p_txt)
                            hash_tag = get_hashtags(p_txt)
                            emojis = get_emoji(p_txt)
                            sentiment = {
                                "tid": str(changeset["id"]),
                                "type": "analysis",
                                "score": score,
                                "hashtags": hash_tag,
                                "emoji": emojis,
                                "hour": hour,
                                "location": location,
                                "ts": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                            }
                            analysis[analysis_id] = sentiment
                            count += 1
                            if count % 100 == 0:
                                print("save {} tweets.".format(count))
                        except:
                            continue
                            
        except KeyboardInterrupt:
            print("End Session.")
            break






    # for item in vic_areas_tweets_db.view('_all_docs'):
    #     id = item['id']
    #     if id not in sentiment_tweets_db:
    #         try:
    #             doc = vic_areas_tweets_db[id]
    #             txt = doc['text']
    #             p_txt = process_tweets(txt)
    #             time = doc['time']
    #             #to do: categorized to hour value 0~24
    #             location = doc['location']
    #             score = get_score(p_txt)
    #             hash_tag = get_hashtags(p_txt)
    #             emojis = get_emoji(p_txt)
    #             sentiment = {
    #                 "score": score,
    #                 "hashtags": hash_tag,
    #                 "emoji": emojis,
    #                 "hour": time,
    #                 "location": location,
    #                 "ts": 
    #             }
    #             sentiment_tweets_db[id] = sentiment
    #             count += 1
    #             if count % 100 == 0:
    #                 print("save {} tweets.".format(count))
    #         except:
    #             continue
    # print("successful save {} tweets.".format(count))



