import requests
import re
import json
import subprocess
import zipfile
import os

def extract_id_from_url(url):
    """ 从给定的URL中提取以 'id' 开始的应用ID """
    match = re.search(r'/id(\d+)', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("No valid ID found in the URL.")

def lookup_app_by_id(app_id):
    """ 使用iTunes API查找应用并返回bundle ID """
    response = requests.get(f"https://itunes.apple.com/lookup?id={app_id}")
    response_data = response.json()
    if response_data["resultCount"] > 0:
        return response_data["results"][0]["bundleId"]
    else:
        raise ValueError("No results found for the provided ID.")

def download_app(bundle_id):
    """ 使用ipatool下载应用 """
    ipa_filename = f"{bundle_id}.ipa"
    try:
        subprocess.run(["ipatool", "download", "-b", bundle_id, "-o", ipa_filename], check=True)
        print("App download initiated successfully.")
        return ipa_filename
    except subprocess.CalledProcessError as e:
        print(f"Failed to download the app: {e}")
        return None

def unzip_ipa(ipa_filename):
    """ 解压IPA文件并找到.app目录 """
    if not ipa_filename or not os.path.exists(ipa_filename):
        print("No IPA file found to unzip.")
        return None

    extract_folder = "extracted_ipa"
    with zipfile.ZipFile(ipa_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    
    # 寻找 .app 文件夹
    for root, dirs, files in os.walk(extract_folder):
        for dir in dirs:
            if dir.endswith(".app"):
                app_path = os.path.join(root, dir)
                print(f"Found .app folder: {app_path}")
                return app_path
    return None

def rename_app_folder(app_path):
    """ 移除.app扩展名并重命名文件夹 """
    if app_path and app_path.endswith(".app"):
        new_path = app_path[:-4]  # 移除".app"
        os.rename(app_path, new_path)
        print(f"Renamed {app_path} to {new_path}")
        return new_path
    return app_path

def main():
    url = "https://apps.apple.com/cn/app/索玛立方体/id6450415992"
    app_id = extract_id_from_url(url)
    print(f"Extracted App ID: {app_id}")
    
    bundle_id = lookup_app_by_id(app_id)
    print(f"Bundle ID: {bundle_id}")

    # 执行下载
    ipa_filename = download_app(bundle_id)
    
    # 解压IPA文件
    app_path = unzip_ipa(ipa_filename)
    
    # 重命名.app文件夹
    if app_path:
        new_app_path = rename_app_folder(app_path)
        # 在这里你可以对新的文件夹进行进一步的处理

if __name__ == "__main__":
    main()
