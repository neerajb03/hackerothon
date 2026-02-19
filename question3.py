import sys
import re
from collections import Counter

def func(file_path):
    with open(file_path,'r') as file:
        lines= file.readlines()

    words = [] 
    for line in lines:
        words += line.lower().split()
    total=len(words)
    if total==0:
        print('No words found')

    counts = Counter(words)
    threshold = max(1, total // 100)
    
    for line in lines:
        for w in line.lower().split():
            if counts[w] < threshold:
                print(line.strip())
                break
