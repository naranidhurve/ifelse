
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
l=[]
n=[]
m=[]
l_count=0
n_count=0
m_count=0
while i<len(kitna_paisa_hai):
        if kitna_paisa_hai[i]<100000:
                l.append(kitna_paisa_hai[i])
                l_count=l_count+1
        elif kitna_paisa_hai[i]<10000000:
                n.append(kitna_paisa_hai[i])
                n_count=n_count+1
        else:
                m.append(kitna_paisa_hai[i]) 
                m_count=m_count+1
        i=i+1
print(l,"dilwale",l_count)
print(n,"lakhpati",n_count)
print(m,"crorepati",m_count)





    
        