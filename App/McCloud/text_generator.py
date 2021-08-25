from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random
import time


def create(text) -> str:
    try:
        output = ''
        trigrams_list = []
        trigrams_dict = {}
        trigrams_counter_dict = {}
        end_chars = set('!?.\n;')
        repeat = False
        iterator = 0

        start = time.time()

        tk = WhitespaceTokenizer()
        tokens = tk.tokenize(text)

        for i in range(0, len(tokens) - 2):
            trigrams_list.append([tokens[i], tokens[i + 1], tokens[i + 2]])

        for i in range(0, len(trigrams_list)):
            trigrams_dict.setdefault(trigrams_list[i][0] + ' ' + trigrams_list[i][1], []).append(trigrams_list[i][2])


        for key in trigrams_dict:
            trigrams_counter_dict[key] = Counter(trigrams_dict[key])

        random_head = random.choice(list(trigrams_counter_dict.keys()))

        while iterator < 10:

            while not random_head[0].isupper() or any((c in end_chars) for c in random_head):
                random_head = random.choice(list(trigrams_counter_dict.keys()))

            sentence = random_head
            i = 1
            while True:
                tail = random.choices(*zip(*trigrams_counter_dict[random_head].items()))[0]

                if time.time() - start > 5:
                    return 'timeout'

                if any((c in end_chars) for c in tail):
                    if i > 4:
                        sentence += " {}".format(tail)
                        break

                    else:
                        count_loop = 0

                        while any((c in end_chars) for c in tail):
                            if count_loop > len(trigrams_counter_dict[random_head]):
                                repeat = True
                                break

                            tail = random.choices(*zip(*trigrams_counter_dict[random_head].items()))[0]
                            count_loop += 1

                if repeat:
                    break

                sentence += " {}".format(tail)
                space_index = random_head.find(" ")
                random_head = random_head[space_index + 1:] + " " + tail
                i += 1

            if repeat:
                random_head = random.choice(list(trigrams_counter_dict.keys()))
                repeat = False

            else:
                output += (sentence + '\n')
                iterator += 1

        end = time.time()
        print(end-start)
        return output
    except:
        return 'bad input'
