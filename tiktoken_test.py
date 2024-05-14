import csv
import tiktoken
import re

# 获取编码对象
encoding = tiktoken.get_encoding("o200k_base")

# 定义要迭代的 token ID 范围
# 假设编码支持最多200,000个 token，根据需要调整
token_range = range(200000)

# 打开两个CSV文件，一个用来写所有tokens，一个用来写包含汉字的tokens
with open('tokens.csv', 'w', newline='', encoding='utf-8') as csvfile_all, \
     open('zh-cn.csv', 'w', newline='', encoding='utf-8') as csvfile_cn:
    
    csvwriter_all = csv.writer(csvfile_all, escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    csvwriter_cn = csv.writer(csvfile_cn, escapechar='\\', quoting=csv.QUOTE_MINIMAL)
    
    # 写入表头
    csvwriter_all.writerow(['Token ID', 'Decoded String'])
    csvwriter_cn.writerow(['Token ID', 'Decoded String'])
    
    # 迭代 token ID 并写入CSV
    for token_id in token_range:
        try:
            # 解码单个 token bytes 并转换为字符串
            decoded_bytes = encoding.decode_single_token_bytes(token_id)
            decoded_string = decoded_bytes.decode('utf-8')
            
            # 写入所有tokens到tokens.csv
            csvwriter_all.writerow([token_id, decoded_string])
            
            # 检查是否包含汉字，并写入zh-cn.csv
            if re.search(r'[\u4e00-\u9fff]', decoded_string):
                csvwriter_cn.writerow([token_id, decoded_string])
        
        except Exception as e:
            print(f"跳过 token_id {token_id}，错误: {e}")
            continue