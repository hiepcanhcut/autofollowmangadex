# 📚 MangaDex Auto Follow Tool

> _Import manga từ file `.txt` sang MangaDex chỉ với 1 cú chạy script._

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  
![MangaDex API](https://img.shields.io/badge/MangaDex-API-orange)  
![Automation](https://img.shields.io/badge/Automation-Yes-brightgreen)

---

## 🚀 Giới thiệu

Đây là một tool nhỏ để **thêm manga vào library MangaDex** dựa trên danh sách có sẵn trong file `data.txt`.  
Không cần click từng truyện → chỉ cần liệt kê tên vào file `.txt` rồi chạy script.  

---

## ⚙️ Cách dùng

### 1. Clone repo & cài dependencies
```bash
git clone https://github.com/hiepcanhcut/autofollowmangadex.git
cd autofollowmangadex/src
pip install -r requirements.txt
````

### 2. Chuẩn bị `data.txt`

* File `data.txt` chứa danh sách tên manga (mỗi dòng một tên).
* Ví dụ:

  ```
  Aharen-san wa Hakarenai
  Onna Tomodachi wa Tanomeba Igaito Yarasete Kureru
  Kusunoki-san wa Koukou Debut ni Shippai Shite Iru
  ```

### 3. Cấu hình tài khoản

Script sẽ đọc thông tin đăng nhập từ **biến môi trường** hoặc hỏi bạn nhập khi chạy.
👉 Bạn **không cần (và không nên) hardcode** thông tin vào file Python.

Linux/macOS:

```bash
export MANGADEX_CLIENT_ID="your-client-id"
export MANGADEX_CLIENT_SECRET="your-client-secret"
export MANGADEX_USERNAME="your-username"
export MANGADEX_PASSWORD="your-password"
```

Windows PowerShell:

```powershell
setx MANGADEX_CLIENT_ID "your-client-id"
setx MANGADEX_CLIENT_SECRET "your-client-secret"
setx MANGADEX_USERNAME "your-username"
setx MANGADEX_PASSWORD "your-password"
```

### 4. Chạy script

```bash
python wolf.py
```

---

## 🛠 Tuỳ chỉnh

Bạn có thể chọn trạng thái khi add vào library:

* `"plan_to_read"`
* `"reading"`
* `"completed"`
* `"dropped"`
* `"on_hold"`

Ví dụ:

```python
ok = follow_manga(manga_id, token, status="reading")
```

---

## ⚡ Demo

![demo](https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif)

> *“Một lần chạy, cả trăm bộ truyện tự động vào library.”*

---

## ⚠️ Lưu ý quan trọng

* Repo này **chỉ đọc từ file txt**.
* Không commit thông tin nhạy cảm (client_id, secret, username, password) lên GitHub.
* Hãy dùng biến môi trường để bảo mật.

---

## 🐉 Lời kết

Tool này giúp bạn:

* Import hàng loạt manga vào library MangaDex nhanh gọn.
* Tránh thao tác thủ công mỏi tay.
* Giữ cho acc của bạn an toàn bằng cách **không public thông tin nhạy cảm**.

---
