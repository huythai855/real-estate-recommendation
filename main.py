import json
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

with open('mock-data.json', 'r') as f:
    data = json.load(f)

with open('customer.json', 'r') as f:
    customer = json.load(f)


def to_vector(entry):
    loai_hinh_map = {'nhà mặt đất': 1, 'chung cư': 0}
    loai_hinh = loai_hinh_map.get(entry['loại hình'], 0)
    gia = float(entry['giá'])
    dien_tich = float(entry['diện tích'])
    mat_tien = float(entry['mặt tiền']) if entry['mặt tiền'] else 0
    so_phong_khach = float(entry['số phòng khách'])
    so_phong_ngu = float(entry['số phòng ngủ'])
    so_phong_tam = float(entry['số phòng tắm']) if entry['số phòng tắm'] else 0

    return np.array([loai_hinh, gia, dien_tich, mat_tien, so_phong_khach, so_phong_ngu, so_phong_tam])


data_vectors = np.array([to_vector(entry) for entry in data])
customer_vector = to_vector(customer)

scaler = StandardScaler()
data_vectors = scaler.fit_transform(data_vectors)
customer_vector = scaler.transform([customer_vector])

knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(data_vectors)
distances, indices = knn.kneighbors(customer_vector)


recommendations = [data[i] for i in indices[0]]


for i, rec in enumerate(recommendations, start=1):
    print(f"Căn nhà {i}:")
    print(f"  Loại hình: {rec['loại hình']}")
    print(f"  Giá: {rec['giá']}")
    print(f"  Diện tích: {rec['diện tích']} m²")
    print(f"  Mặt tiền: {rec['mặt tiền']} m")
    print(f"  Số phòng khách: {rec['số phòng khách']}")
    print(f"  Số phòng ngủ: {rec['số phòng ngủ']}")
    print(f"  Số phòng tắm: {rec['số phòng tắm']}")
    print(f"  Khu vực: {rec['khu vực']['phường']}, {rec['khu vực']['quận']}, {rec['khu vực']['thành phố']}")
    print("\n")
