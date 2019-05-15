from collections import defaultdict,Counter

class WordUnscrambler(object):
 
  def __init__(self):
    self.word_list=[]
    with open("data.csv","r") as f:
      for line in f.readlines():
        self.word_list.append(map(self._to_int,line.strip().split(",")))

  def _to_int(self,i):
    try:
      return int(i)
    except:
      return i

  def unscramble(self, letters):
    retval=defaultdict(list)
    count = Counter(letters.lower())
    freq=[0]*26
    for key,value in count.items():
      freq[ord(key)-97]=value
    for word_data in self.word_list:
      is_eligable=reduce(lambda x,y: x&y, [i>=j for i,j in zip(freq,word_data[1:-1])])
      if is_eligable:
        retval[word_data[-1]].append(word_data[0])
    return retval


if __name__=="__main__":
  wu=WordUnscrambler()
  print wu.unscramble("defba")
