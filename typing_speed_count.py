from time import*
import random as r


def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if paratest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1
    return error


def speep_time(time_s, time_e, userinput):
    time_delay = time_e-time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test = ["The pronunciation of GIF has been disputed since the 1990s. ",
        "an acronym for the Graphics Interchange Format, is popularly pronounced in English as a one-syllable word. ",
        "The most common pronunciations in English are /dʒf/ (listen) (with a soft g as in gin) and // (listen) (with a hard g as in gift).",
        " differing in the phoneme represented by the letter G. Many public figures and institutions have taken sides in the debate; Steve Wilhite",
        " the file format's creator, gave a speech at the 2013 Webby Awards (slide pictured) arguing that only the soft g pronunciation is correct.",
        " Polls show that the hard g pronunciation is more common, although the frequency of each pronunciation varies by region; in addition, some speakers enunciate each letter in GIF, making it /dʒi a ɛf/ (listen). ",
        "English dictionaries generally accept both main alternatives as valid, and linguistic analyses show no clear advantage for either main pronunciation based on the pronunciation frequencies of similar English words."]

test1 = r.choice(test)
print("''''''''typing speed''''")
print(test1)
print()
print()
time_1 = time()
testinput = input("enter : ")
time_2 = time()


print('speed : ', speep_time(time_1, time_2, testinput),"W/sec")
print('Error : ', mistake(test1, testinput))
