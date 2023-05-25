url_recognition = "http://117.6.133.148:9000/recognition"
 
url_mode = 'http://117.6.133.148:9000/camid2mode/{}'
    
url_mac2mode = "http://117.6.133.148:9000/mac2mode/{}"

url_avt = "http://117.6.133.148:3000/img/avatar/{}.jpg"

url_status = "http://117.6.133.148:9000/status"

url_cam = "http://117.6.133.148:3000/v1/cameras/{}"

url_new_user = 'http://117.6.133.148:9000/faces'
# api
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

cameraId = None

organizationId = None

txt = "model/slim-320.prototxt"
    
caffe = 'model/slim-320.caffemodel'

api_key = '1777e1c6994c63ad16f9ae8012ee46f1'

url_log  = 'http://117.6.133.148:9000/log'

version =  '1.1'

mac = 'done get a mac'

token = ''

import os
path_project = os.getcwd().split('/')
path_project = '/'.join(path_project[:-1]) 
path_project = os.path.join(path_project, "data")

if os.path.exists(path_project) == False:
    os.mkdir(path_project)

start_no_internet = None

try:
    mac = open('/home/viebox/value.txt', 'r').read(); mac = mac.split('\n')[0]
except:
    
    # check where are value.txt?
    if os.path.isfile('/home/vieface/value.txt'):
        mac = open('/home/vieface/value.txt', 'r').read(); mac = mac.split('\n')[0]
    else:
        from getmac import get_mac_address as gma
        mac = gma()
        # print("[INFOR]: Không có file lưu trữ địa chỉ MAC")

 