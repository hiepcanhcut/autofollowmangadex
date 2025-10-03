import requests
import json

#Nhập thông tin của bạn ở đây
CLIENT_ID = os.getenv("MANGADEX_CLIENT_ID") or input("Client ID: ")
CLIENT_SECRET = os.getenv("MANGADEX_CLIENT_SECRET") or input("Client Secret: ")
USERNAME = os.getenv("MANGADEX_USERNAME") or input("Username: ")
PASSWORD = os.getenv("MANGADEX_PASSWORD") or input("Password: ")

# File chứa danh sách truyện TruyenDex (mỗi dòng 1 tên truyện hoặc link)
TRUYEN_FILE = "data.txt"

#Step 1: Lấy access token từ MangaDex ====
def get_token():
    url = "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token"
    data = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": USERNAME,
        "password": PASSWORD
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()["access_token"]

#Step 2: Tìm manga trên MangaDex ====
def search_manga(title, token):
    url = "https://api.mangadex.org/manga"
    params = {"title": title, "limit": 5}  # lấy 5 kết quả để phòng khi sai tên
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, params=params)
    data = r.json()

    if r.status_code == 200 and "data" in data and len(data["data"]) > 0:
        # Lấy ra kết quả khớp nhất
        for manga in data["data"]:
            titles = [manga["attributes"]["title"].get("en", "").lower()]
            # gộp altTitles để so sánh
            for alt in manga["attributes"].get("altTitles", []):
                for v in alt.values():
                    titles.append(v.lower())

            # nếu tên mình đưa vào khớp với bất kỳ tên/alt nào → chọn
            if title.lower() in titles:
                return manga["id"]

        # nếu không tìm thấy khớp tuyệt đối thì lấy kết quả đầu tiên
        return data["data"][0]["id"]

    else:
        print(f"[DEBUG] search fail for '{title}': {data}")
        return None

#Step 3: Follow manga trực tiếp ====
def follow_manga(manga_id, token, status="plan_to_read"):
    url = f"https://api.mangadex.org/manga/{manga_id}/status"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = {"status": status}
    r = requests.post(url, headers=headers, json=data)
    print(f"[DEBUG] Set status for {manga_id}: {r.status_code}, {r.text}")
    return r.status_code in (200, 204)

def main():
    token = get_token()

    with open(TRUYEN_FILE, "r", encoding="utf-8") as f:
        titles = [line.strip() for line in f if line.strip()]

    for title in titles:
        manga_id = search_manga(title, token)
        if manga_id:
            ok = follow_manga(manga_id, token, status="reading")
            print(f"[OK] Followed {title}" if ok else f"[FAIL] {title}")
        else:
            print(f"[NOT FOUND] {title}")

if __name__ == "__main__":

    main()


