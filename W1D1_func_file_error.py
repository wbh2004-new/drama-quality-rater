def clean(text):
    text=text.strip()
    text=" ".join(text.split())
    return text

def avg(lst):
     if len(lst) == 0: 
         return 0
     sum=0
     for i in range(len(lst)):
          sum+=lst[i]
     return sum/len(lst)


with open("短剧评论.txt", 'w',encoding="utf-8") as f:
    f.write("123吱吱吱吱在\n大师傅\nv阿萨打\n算下周爱上自\n行车委屈委屈我\n")
with open("短剧评论.txt",encoding="utf-8") as f:
    for line in f:
        print(line, end="")   

with open("短剧评论.txt", encoding="utf-8") as f:
    with open("短剧评论带序号.txt", "w", encoding="utf-8") as out:
        for n, line in enumerate(f, start=1):
            line = line.strip()                
            out.write(f"{n}. {line}\n")     

def safe_div(a, b):
    try:
        result=a/b
    except ZeroDivisionError:
     return "不能除以 0"
    return result

try:
    with open("不存在的文件.txt", encoding="utf-8") as f:
        for line in f:
            print(line,end="")                    
except FileNotFoundError:           
    print("文件不存在，请检查文件名后重试")   