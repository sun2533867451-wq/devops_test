department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

lin1 = 'Department1 name:%s    Manager:%s COURSE FEES:6.2%f The End !'%(department1,depart1_m,COURSE_FEES_SEC)
lin2 = 'Department2 name:{0:<10} Manager:{1:<10} COURSE FEES:{2:<10.2f} The End !'.format(department2,depart2_m,COURSE_FEES_Python)
lin3 = f'Department3 name:{department1:<10} Manager:{depart1_m:^10} COURSE FEES:{COURSE_FEES_SEC:>10} The End !'


length = len(lin1)
print('='*length)
print(lin1)
print(lin2)
print(lin3)
print('='*length)
length = len(lin1)
print('='*length)
print(lin1)
print(lin2)
print(lin3)
print('='*length)
