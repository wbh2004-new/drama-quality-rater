def clean(comments):
    result = []
    seen = set()
    for c in comments:
        if not isinstance(c, str):      # 空1：类型过滤，筛掉非字符串
            continue
        text = c.strip()                  # 空2：去首尾空白
        if not text:                     # 空3：空字符串/纯空格判断（想：什么算"空"？）
            continue
        if text.isdigit():
            continue
        if text in seen:                 # 空4：见过没？
            continue
        seen.add(text)
        result.append(text)
    return result


raw_comments = [
    "  这部剧太好看了  ",
    "好看",
    "",
    "   ",
    "好看",
    "节奏拖沓，弃了",
    "好看",      # 又一次重复
    None,        # 爬取失败产生的空值
    "123",       # 数字当评论混进来了（类型不对）
]

print(clean(raw_comments))