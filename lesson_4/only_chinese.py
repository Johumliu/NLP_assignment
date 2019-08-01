import re
import jieba

f_in = open('wiki_simple.txt', 'r')
f_out = open('wiki_only_simple_and_cut.txt', 'w')
line = f_in.readline()

while line:
    if line == '\n':
        line = f_in.readline()
        continue
    pattern = re.compile('[\u4E00-\u9FA5]')
    result = pattern.findall(line)
    line = ''.join(result)
    line = jieba.cut(line)
    new_line = ' '.join(line)
    f_out.writelines(new_line)
    f_out.write('\n')
    line = f_in.readline()
    
f_in.close()
f_out.close()