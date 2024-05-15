# getiOSApp


 这个脚本是ChatGPT帮我写的，过程如下
## 注意 下载之前 最好用电脑上登录的appleid，在手机上下载一下
### 1、提问
https://apps.apple.com/cn/app/索玛立方体/id6450415992


根据这个url 提取URL的path的最后一个，就是id1455009060，注意要求必须以id开头

然后 拼接到 https://itunes.apple.com/us/lookup?id={上面获取到的id}

请求https://itunes.apple.com/us/lookup?id={上面获取到的id}，获取返回的字符串，解析json，然后获取bundle id

然后再执行 ipatool download -b 获取到的bundle id

### 2、将这个过程 写一个 python 脚本吧 可以吗

### 3、print(f"ipatool download -b {bundle_id}") 可以直接执行吗？

### 4、download_app(bundle_id) 下载成功后 帮我zip解压ipa，增加 去除文件夹名字中的 .app 这一步操作

---

### lookreq.py 用于把Charles抓到的post请求上传的图片 提取出来

### renamejpg 将此函数加入 .zshrc 方法调用，目的是一些图片缓存目录是没有后缀的，方便查看
