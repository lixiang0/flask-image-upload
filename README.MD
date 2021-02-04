
# 基于Flask的图片上传和读取示例

<image src='1612423313.png' height=400/>


## web.py方法说明：

### 1.上传图片

图片保留在static文件夹下
```
@app.route("/upload", methods=['POST'])
def upload():
...
```

### 2.下载图片
```
@app.route("/show/<filename>", methods=['GET'])
def show(filename):
...
```

## js中方法说明：

### 1.设置预览
```
       var img
        function previewFile() {
            const preview = document.querySelector('img');
            const file = document.querySelector('input[type=file]').files[0];
            const reader = new FileReader();

            reader.addEventListener("load", function () {
                // get base64 image 
                preview.src = reader.result;
                img = reader.result
            }, false);

            if (file) {
                reader.readAsDataURL(file);
            }
        }
```

### 2.显示返回的图片
```
        function onClick() {
            $.post('/upload', { "base64": img }, function (result) {
                console.log(result)
                b64 = result.base64
                document.getElementById('id_result').src = 'data:image/jpeg;base64,' + b64.replace(/#/g, '/')
            }, "json");
        }
```


## 链接说明：

- http://<ip>:<port>/uplad 上传图片（post方式）
- http://<ip>:<port>/uplad/<filename>get方式获取base64图片）
- http://<ip>:<port>/static/<filename> 文件流方式获取图片