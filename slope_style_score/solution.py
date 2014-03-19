from __future__ import division

def slope_style_score(scores):
    scores.sort()
    score = 0.0
    for i in range(1,len(scores)-1):
        score = score + scores[i]
    score = score/(len(scores) - 2)
    return float(format(score,'.2f'))