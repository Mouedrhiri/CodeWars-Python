#Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

#Rules for a smiling face:

#Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
#A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
#Every smiling face must have a smiling mouth that should be marked with either ) or D
#No additional characters are allowed except for those mentioned.

#Valid smiley face examples: :) :D ;-D :~)
#Invalid smiley faces: ;( :> :} :]

#Example
#countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
#countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
#countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;


def count_smileys(arr):
        res = 0
        for i in arr:   
            if check(i):
                res += 1
        return res#the number of valid smiley faces in array/list
def check(i):
    if i[0] != ':' and i[0] != ';':
      return False
    if len(i) == 3 and i[1] != '-' and i[1] != '~':
      return False
    if len(i) == 3 and i[2] != ')' and i[2] != 'D':
      return False
    if len(i) == 2 and i[1] != ')' and i[1] != 'D':
      return False
