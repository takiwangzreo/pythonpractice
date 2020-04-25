import requests
import
data=requests.put('https://www.youtube.com/api/stats/ads?ver=2&ns=1&event=1&device=1&content_v=iHUnUHA5hek&el=detailpage&ei=qJWNXuHoPNiDs8IPpraFuAI&devicever=2.20200406.06.02&bti=9477942&break_type=1&conn=0&cpn=QjvDu2W2XLqgM56J&lact=1384&m_pos=0&mt=0&p_h=360&p_w=640&rwt=[RWT]&sdkv=h.3.0.0&slot_pos=0&vis=0&vol=53&wt=1586337194636')
print(data.json())