import pandas as pan
data1=["Godfather","Taken","Shawshank Redemption","Shutter Island"]
data2=["Suits","OTH","Riverdale","Lucifer"]
Index=[1,2,3,4]
data3={"movie":data1,"shows":data2}
a=pan.DataFrame(data3,index=Index)
print(a)
