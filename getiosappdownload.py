import requests
import re
import json
import subprocess

def extract_id_from_url(url):
    """ 从给定的URL中提取以 'id' 开始的应用ID """
    match = re.search(r'/id(\d+)', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("No valid ID found in the URL.")

def lookup_app_by_id(app_id):
    """ 使用iTunes API查找应用并返回bundle ID """
    response = requests.get(f"https://itunes.apple.com/us/lookup?id={app_id}")
    response_data = response.json()
    if response_data["resultCount"] > 0:
        return response_data["results"][0]["bundleId"]
    else:
        raise ValueError("No results found for the provided ID.")

def download_app(bundle_id):
    """ 使用ipatool下载应用 """
    try:
        subprocess.run(["ipatool", "download", "-b", bundle_id], check=True)
        print("App download initiated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download the app: {e}")

def main():
    url = "https://apps.apple.com/us/app/photoroom-%E7%BC%96%E8%BE%91%E7%85%A7%E7%89%87%E5%92%8C%E8%83%8C%E6%99%AF/id1455009060?l=zh-Hans-CN&ppid=d2ffc899-92a4-47c6-bbf4-cfadbea6ddb2"
    app_id = extract_id_from_url(url)
    print(f"Extracted App ID: {app_id}")
    
    bundle_id = lookup_app_by_id(app_id)
    print(f"Bundle ID: {bundle_id}")

    # 执行下载
    download_app(bundle_id)

if __name__ == "__main__":
    main()
