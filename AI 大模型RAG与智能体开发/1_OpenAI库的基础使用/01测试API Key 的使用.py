from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key="{密钥}",
    #！！！保护安全，在环境变量设置后，api_key可有可无。
    base_url="{ai接口的地址}"
    #平台地址
)

messages = [{"role": "user", "content": "你是谁"}]
              #给定角色               #内容
completion = client.chat.completions.create(     #模型加载和调试
    model = "{模型}",  # 您可以按需更换为其它深度思考模型
    messages = messages,
    extra_body = {"enable_thinking": True},
    stream = True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)