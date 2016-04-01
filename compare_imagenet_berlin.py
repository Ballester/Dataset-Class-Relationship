from berlin_classes import *
from imagenet_synsets_ids import *
from nltk.corpus import wordnet as wn


berlin.sort()
# imagenet.sort()
offsets_dict = {s.offset(): s for s in wn.all_synsets()}
for i in range(0, len(imagenet)):
    imagenet[i] = offsets_dict[imagenet[i]]

print 'Berlin - Imagenet'
print '-----------------'
for i in range(0, len(berlin)):
    berlin_synsets = wn.synsets(berlin[i])
    #for each possible meaning in berlin[i]
    for j in berlin_synsets:
        if str(j).find('.n.') != -1:
            for k in range(0, len(imagenet)):
                l = imagenet[k]    
                if str(l).find('.n.') != -1:
                    similarity = j.lch_similarity(l)
                    if similarity > 2.0:
                        # print similarity, ' - ', berlin[i], l
                        print berlin[i], ' - ', l
