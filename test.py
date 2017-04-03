# -*- coding: utf-8 -*-
s1=85
s2=100
r=(s2-s1)/s1*100
if r>0:
    print('小明成绩提升：%.1f%%' %r)
elif r<0:
    print('小明成绩下降：%.1f%%' %abs(r))
else:
    print('小明成绩没有变化。')
    pass
