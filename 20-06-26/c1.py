'''d2={True:1,False:0,1:True,0:"False"}
print(d2)
print(0 and 0)'''
std=["A","B","C","D"]
sta=["P","A","P","P"]
marks=[80,86,87,76]
report=[]
for name,present,score in zip(std,sta,marks):
    if present != "P":
        if score < 85:
            cat="Bad"
        else:
            cat="Good"
    else:
        if score<85:
            cat="Avg"
        else:
            cat="Excl"
    report.append((name,cat))
print(report)
for idx,(name,cat) in enumerate(report,start=1):
    print(f"{idx:02d}: {name} -> {cat}")