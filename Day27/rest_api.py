import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Cybersecurity Learning",
    "body": "Day 27: REST API with POST, PUT, DELETE",
    "userId": 1
}

response_post = requests.post(BASE_URL, json=new_post)
print("✅ POST - Tạo dữ liệu mới:")
print(response_post.json())

update_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post has been updated",
    "userId": 1
}

response_put = requests.put(BASE_URL + "/1", json=update_post)
print("\n✅ PUT - Cập nhật dữ liệu:")
print(response_put.json())

response_delete = requests.delete(BASE_URL + "/1")
print("\n✅ DELETE - Xóa dữ liệu:")
print("Status code:", response_delete.status_code)
