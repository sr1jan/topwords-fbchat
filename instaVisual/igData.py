import json

with open('messages.json', 'r') as fp:
    data = json.load(fp)

mem = ['mrinal.xd', 'sr1jann', '_shubham1506_', '_ankur03_', 's.kard.e', 'ankit.anvekar', 'mohit.3333']
grp = []
for r in data:
    if set(mem).issubset(set(r['participants'])):
        grp.append(r['conversation'])

ms_list = []
sentences = []
for g in grp:
    for ms in g:
        try:
            date = ms['created_at'][:10]
            text = ms['text']
        except:
            continue

        ms_list.append(f"{date}\t{ms['sender']}\t\t{text}\n")
        sentences.append(f"{text}\n")

       #  print(f"{ms['sender']}\t{text}\n")

with open('sent.txt', '+w') as fp:
    for s in sentences[::-1]:
        fp.write(s)

# with open('grpMessages.txt', '+w') as fp:
#     for m in ms_list[::-1]:
#         fp.write(m)




