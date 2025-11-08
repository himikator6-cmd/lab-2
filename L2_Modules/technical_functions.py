import math
import json
import re


def tokeinized_text_extractor(filename):
    results = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            data = json.loads(line)
            results.append(data)                
    return results


def сosine_similarity(Vector1, Vector2):
    if ((len(Vector1)) != len(Vector2)):
        return 0
    else:
        Sum_ab = 0
        Sum_a = 0
        Sum_b = 0
        Cos = 0
        for i in range(len(Vector1)):
            Sum_ab = Sum_ab + Vector1[i] * Vector2[i]
            Sum_a = Sum_a + Vector1[i] * Vector1[i]
            Sum_b = Sum_b + Vector2[i] * Vector2[i]
        if ((Sum_a == 0) or (Sum_b == 0)):
            return 0
        else:
            Cos = Sum_ab / (math.sqrt(Sum_a) * math.sqrt(Sum_b))
        return Cos
