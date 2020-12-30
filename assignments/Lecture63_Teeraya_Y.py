customerList = ["Kittikorn", "Mon", "May", "Miew"]

# ต้องการข้อมูลของลูกค้าคนแรก
print(customerList[0])

# ต้องการลูกค้า 2 คนแรก
print(customerList[0:2])
# ต้องการลูกค้า 2 คนแรก เหมือนกัน
print(customerList[:2])

# ต้องการลูกค้า ทั้งหมด
print(customerList)

customerList.append('Ney')
print(customerList)