# import re
# import requests
#
# c_code = (
#     'ACWI',
#     'PTNQ',
#     'AFTY',
#     'ASHR',
#     'BNDX',
#     'AAAU',
#     'IEZ',
#     'AGG',
#     'IVE',
#     'DIA')
#
# # Setting headers
# s_header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
#
# # Getting cookies
# s_origin_url = ''.join(
#     ['https://finance.yahoo.com/quote/ACWI/history?p=ACWI&.tsrc=fin-srch'])
# s_origin_content = requests.get(s_origin_url, headers=s_header)
#
# c_cookies = requests.utils.dict_from_cookiejar(s_origin_content.cookies)
# c_session = requests.session()
# requests.utils.add_dict_to_cookiejar(c_session.cookies, c_cookies)
#
# # Getting crumb
# s_origin_text = s_origin_content.text
# s_crumb = re.findall('\"CrumbStore":{"crumb":"(.*?)\"}', s_origin_text)
# s_crumb = s_crumb[0]
#
# for s_code in c_code:
#     s_url = ''.join(
#         [
#             'https://query1.finance.yahoo.com/v7/finance/download/',
#             s_code,
#             '?period1=0&period2=9999999999&interval=1d&events=history&crumb=',
#             s_crumb,
#             '&download=',
#             s_code,
#             '.csv'])
#
#     s_content = c_session.get(s_url)
#
#     if s_content.status_code == 200:
#         s_file = ''.join([s_code, '.csv'])
#         with open(s_file, 'wb') as data:
#             data.write(s_content.content)
#             print(s_code, 's Data downloaded')
#
#     else:
#         print(s_code, 's Data failed')