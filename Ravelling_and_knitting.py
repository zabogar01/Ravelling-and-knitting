def ravel(r):
    result=[]
    for x in range(len(r)):  
        for y in range(x+1):     
            result.append(r[y])
    
    return ''.join(result)
        
print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))
'''
def knit(k):
    return k[:-(len(k)//5)]

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))

len('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika') #10 = 55
len('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhik') # 9 - 45
len('PPuPurPurwPurwaPurwadPurwadhPurwadhi') # 8 -36
len('PPuPurPurwPurwaPurwadPurwadh') #7 - 28
len('PPuPurPurwPurwaPurwad') #6 - 21
len('PPuPurPurwPurwa')#5 - 15
'''

print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))