# model-benchmarking
大模型api压测

## 参考
```https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/quick_start.html```

## task_cfg 参数说明
```
url：压测接口
query_template：接口 body 参数模版
api: 将测试集转为url post 请求参数
dataset: 测试集解析类型，支持自定义
dataset_path：本地测试集
```