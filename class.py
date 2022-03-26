import os
import shutil

root = os.path.dirname(os.path.abspath(__file__))
print(root)
lines = [l.strip() for l in open(root+'/read.txt', 'r').readlines()]

idxs = [i for i, l in enumerate(lines) if l.startswith('-')]+[200]

demo_path = os.path.join(root, '../demo')
file_list = os.listdir(demo_path)

for i, idx in enumerate(idxs[:-1]):
    name = lines[idx][1:].strip()
    path = os.path.join(root, name)
    if not os.path.exists(path):
        os.makedirs(path)

    cur_lines = [l for l in lines[idx+1:idxs[i+1]] if l.startswith('Leetcode')] 
    nums = [l.split('Leetcode')[1].strip().replace('.', '').split(' ')[0].strip() for l in cur_lines]
    print(name, ':', nums)

    for num in nums:
        for file in file_list:
            if len(num)<=3 and num==file[:3].lstrip('0'):
                org_file = os.path.join(demo_path, file)
                shutil.copy(org_file, path)



