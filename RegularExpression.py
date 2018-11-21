import re
regex = "[aiueoAIUEO][^bcdfghjklmnpqrstvwxyz]"
text = input()
spl_text = text.split()
pattern = re.compile(regex)
matchObj = pattern.findall(text)

list = []
for i in range(0, len(spl_text)):
    if pattern.findall(spl_text[i]):
        list.append(spl_text[i])
print(list)
# TEST iNPUT: au aoi love ie kaf Ioa Hfr