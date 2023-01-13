import requests
# Change the value of experience that you want to test
url = 'http://172.27.35.69:5000/api'
feature = [[666,44,3,5555,2,1,1,66665,1,0,1]]
#final_data = feature.reshape(1,11,1)
labels ={
  0: "Not-Exited",   
  1: "Exited",
 }

r = requests.post(url,json={'feature': feature})
print(labels[r.json()])
