# Requests 使用笔记

### https请求
再访问https请求的时候会报错，是因为没有指定证书的原因
```
    # 错误信息
    certificate verify failed: unable to get local issuer certificate
    # 解决方法：
    1. 指定一个证书
    verify='/path/to/certfile'
    2. 忽略认证
    verify=False
```

### request SSL证书

