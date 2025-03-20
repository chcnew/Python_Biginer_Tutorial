"""
 * @Description: Python3.8
 * @Author: chc
 * @CreateDate: 
 * @Environment: Anaconda3
"""
import requests
from bs4 import BeautifulSoup

res = requests.get(
    url="https://movie.douban.com/subject/30359376/reviews/",
)
headers = {
    'User-Agent ': "Mozilla/5.0 (Macintosh; Intel Mac 0S x 10_14_0) ApplewebKit/537.36 "
                   "(KHTML,like Gecko) Chrome/99.0.4844.51 Safari/537.36", }
bs_object = BeautifulSoup(res.text, "html.parser")
comment_object_list = bs_object.find_all("p", attrs={"data-page": "0"})
for comment_object in comment_object_list:
    text = comment_object.text
    print(text)
