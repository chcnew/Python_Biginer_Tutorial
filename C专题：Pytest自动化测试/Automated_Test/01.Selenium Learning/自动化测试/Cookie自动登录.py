#coding: utf-8


from selenium import webdriver
import time

driver=webdriver.Firefox()
#网优大数据平台-OLD
driver.get('http://211.139.11.136:18070/mtnx/home/login')
driver.maximize_window()
time.sleep(2)

#跳过验证码登录 Fiddler上传获取Cookie
driver.add_cookie({'name':'PageVersion','value':'202004300936'})
driver.add_cookie({'name':'PageStyleConfig','value':'%7B%22%23comment%22%3A%5B%5D%2C%22login-title-name%22%3A%22%E8%B4%B5%E5%B7%9E%E7%BD%91%E4%BC%98%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0%22%2C%22index-title-name%22%3A%22%E8%B4%B5%E5%B7%9E%E7%BD%91%E4%BC%98%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0%22%2C%22login-advantage-ifno%22%3A%7B%22title%22%3A%22%E8%B4%B5%E5%B7%9E%E7%BD%91%E4%BC%98%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0(%E7%BD%91%E4%BC%98%E5%B9%B3%E5%8F%B0)_%E5%85%A8%E6%96%B0%E4%B8%8A%E7%BA%BF%22%2C%22item%22%3A%5B%22%E9%9D%A2%E5%90%91%E5%AE%9E%E9%99%85%E4%BC%98%E5%8C%96%E5%B7%A5%E4%BD%9C%E7%81%B5%E6%B4%BB%E5%AE%9A%E5%88%B6%E7%9A%84%E7%BD%91%E4%BC%98%E5%85%A8%E6%81%AF%E5%B7%A5%E4%BD%9C%E6%94%AF%E6%92%91%E5%B9%B3%E5%8F%B0%22%2C%22%E8%9E%8D%E5%90%88%E5%90%84%E7%A7%8D%E4%BC%98%E5%8C%96%E6%95%B0%E6%8D%AE%EF%BC%8C%E6%8F%90%E4%BE%9B%E6%9F%A5%E8%AF%A2%E3%80%81%E5%88%86%E6%9E%90%E3%80%81%E8%AE%BE%E8%AE%A1%E3%80%81%E7%AE%A1%E6%8E%A7%E3%80%81%22%2C%22%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E3%80%81%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%81%E8%87%AA%E5%8A%A8%E5%8C%96%E7%9A%84%E5%85%A8%E6%96%B9%E4%BD%8D%E4%BF%A1%E6%81%AF%E5%8C%96%E6%94%AF%E6%92%91%E3%80%82%22%2C%22%22%2C%22%22%2C%22%22%5D%7D%2C%22login-admin-info%22%3A%7B%22item%22%3A%5B%22%E5%BB%BA%E8%AE%BE%E9%83%A8%E9%97%A8%EF%BC%9A%E8%B4%B5%E5%B7%9E%E7%A7%BB%E5%8A%A8%E7%BD%91%E7%BB%9C%E4%BC%98%E5%8C%96%E4%B8%AD%E5%BF%83%22%2C%22%E7%B3%BB%E7%BB%9F%E5%90%8D%E7%A7%B0%EF%BC%9A%E8%B4%B5%E5%B7%9E%E7%BD%91%E4%BC%98%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%B9%B3%E5%8F%B0(%E7%BD%91%E4%BC%98%E5%B9%B3%E5%8F%B0)%22%2C%22%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F%EF%BC%9A%E8%B4%B5%E5%B7%9E%E7%A7%BB%E5%8A%A8%E9%9B%86%E4%B8%AD%E4%BC%98%E5%8C%96%E5%B9%B3%E5%8F%B0%20%20QQ%3A189543026%22%2C%22%E5%BB%BA%E8%AE%BE%E5%8E%82%E5%AE%B6%EF%BC%9A%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%90%8D%E9%80%9A%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%5D%7D%2C%22login-update-info%22%3A%7B%22item%22%3A%5B%22%E5%BD%93%E5%89%8D%E7%89%88%E6%9C%AC%EF%BC%9AV1.2.3%20%22%2C%22%E6%9C%80%E5%90%8E%E6%9B%B4%E6%96%B0%E6%97%B6%E9%97%B4%EF%BC%9A2019%E5%B9%B412%E6%9C%8816%E6%97%A522%E7%82%B912%E5%88%86%22%2C%22%E6%96%B0%E5%A2%9E%E5%BA%94%E7%94%A8%EF%BC%9A%E7%B3%BB%E7%BB%9F%E6%A1%86%E6%9E%B6%22%2C%22%E6%9C%80%E6%96%B0%E9%87%8D%E7%82%B9%E5%BA%94%E7%94%A8%EF%BC%9A%E7%AB%8B%E4%BD%93%E8%A6%86%E7%9B%96%E8%AF%84%E4%BC%B0%22%5D%7D%2C%22index-top-bg%22%3A%7B%22%40show%22%3A%22false%22%2C%22%40selected%22%3A%22newYear%22%2C%22item%22%3A%7B%22%40name%22%3A%22newYear%22%2C%22%40path%22%3A%22static%2Fcommon%2Fimg%2FAppFrame%2FStyleCloud%2Ftop-bg%2Fyuandan.png%22%7D%7D%2C%22theme%22%3A%7B%22%40name%22%3A%22word-blue%22%7D%7D'})
driver.add_cookie({'name':'ASP.NET_SessionId','value':'z31tm0iptlpye2dizha4si0m'})

time.sleep(2)
driver.refresh() #刷新
time.sleep(1)
driver.find_element_by_class_name('app-popbtn-ok').click()
driver.find_element_by_link_text('外包优化管理').click()
driver.find_element_by_link_text('日常优化任务流程').click()
driver.switch_to.frame(0)
driver.find_element_by_id("mtnoh").click()

time.sleep(5)
driver.quit()
