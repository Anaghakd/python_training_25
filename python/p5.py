'''
Accept avg_score from the student of his exam and print his result as follows:
0 to 49 is fail
50 to 74 is second class
75 to 90 is first class 
91 to 100 is ditinction
Also check for invalid avg_score
'''

avg_score = int(input('Enter the avg_score(0 to 100 only):'))
if avg_score >= 0 and avg_score <= 49:
    print("Result is Fail")
elif avg_score >= 50 and avg_score <= 74:
    print('Result is Second class')
elif avg_score >= 75 and avg_score <= 90:
    print('Result is Fist class')
elif avg_score >=91 and avg_score <= 100:
    print('Result is Dsitinction')
else:
    print('Invalid avg_score')