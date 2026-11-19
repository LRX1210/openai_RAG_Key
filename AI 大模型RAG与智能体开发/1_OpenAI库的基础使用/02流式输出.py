from openai import OpenAI
#1,  获取client对象，openai类对象
client = OpenAI(
    base_url="{ai接口的地址}",
)

# 2.  调用模型
e=[{"role":"system","content":"你是一个python编程专家,并且话不多"},
   {"role":"assistant","conten":"我是一个python编程专家，请问有什么可以帮到您的"},
   {"role":"user","content":"你是谁"}]
response=client.chat.completions.create(
    model="{模型}",
    messages=e,
    stream=True      #开启流式输出的功能
)

# 3. 处理结束
for chuck in response:  #流式输出，使回答流畅
    if not chuck.choices:
        continue
    shuc=chuck.choices[0].delta.content
    if not shuc:
        continue
    print(
        shuc,
        end=" ",  # 分隔
        flush=True  # 立刻刷新缓冲区
    )