from pandas_test.ex07 import df_t

stat_list = [76, 73, 95, 10, 25]
df_t['stat'] = stat_list

score_list = df_t['stat'] + df_t['math']
df_t['score'] = score_list
grade_list = []
for i in range(len(score_list)):
    if score_list[i] >= 150:
        grade_list.append('A')
    elif score_list[i] >= 100:
        grade_list.append('B')
    elif score_list[i] >= 70:
        grade_list.append('C')
    else:
        grade_list.append('D')
df_t['grade'] = grade_list

print(df_t)
