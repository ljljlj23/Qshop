from alipay import AliPay

# 公钥
alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoKgRki1TWBrFIEbZ486mrwE6qj0yQa2I5ybPIp618JHXq1XpRSUyoFjW7xEGgvEI2zSA6+qk927Cp2KZddRHMAGOowmjNswhdT1nIcK9MCtX0GRE5E4JOLUzD0Ir0SBihQyrdMxZxmwhDs4o2HJdyC5CkSYeGuMH4CxmcM7CBU5mgwHLXmvjWldT/QTsvos0eGELZRq7o/GYAo/S7N3Qb4z4FPwdTEzyqMYFH+2s+Hkpg3QApPGzti8lD/MfjaykU09wXzAIuYcQ8/VvAzPGRC6FTbFqaEd2R+UfRZ8mxBPlwSl5awpg0uGzTp28INAUnYlA1OvabazqDkG3KOo4GQIDAQAB
-----END PUBLIC KEY-----'''
# 私钥
alipay_private_key_string='''-----BEGIN PRIVATE KEY-----
MIIEogIBAAKCAQEAoKgRki1TWBrFIEbZ486mrwE6qj0yQa2I5ybPIp618JHXq1XpRSUyoFjW7xEGgvEI2zSA6+qk927Cp2KZddRHMAGOowmjNswhdT1nIcK9MCtX0GRE5E4JOLUzD0Ir0SBihQyrdMxZxmwhDs4o2HJdyC5CkSYeGuMH4CxmcM7CBU5mgwHLXmvjWldT/QTsvos0eGELZRq7o/GYAo/S7N3Qb4z4FPwdTEzyqMYFH+2s+Hkpg3QApPGzti8lD/MfjaykU09wXzAIuYcQ8/VvAzPGRC6FTbFqaEd2R+UfRZ8mxBPlwSl5awpg0uGzTp28INAUnYlA1OvabazqDkG3KOo4GQIDAQABAoIBABXkENDcQDkHHMkzHkl+RRQflMDRqeFtJfRpQ1wySBRJqxt7j1eOpAFZWaAlr79z3IMR+mcrB+N3QirQspxtmm2eKLNqgsTat8xj24OsJ19C6KpKn2CEiZkih5ySpanPQd1jRpGZrrnszexYhxRHMSQvuX5RtVRwjwgqxKKmaaWTO/ToS5KuRLR1TuYVK/phnkEtj+5lKMXSYhIPj9PQr1puEDWJDIrFFjgeyZqjwH+gHywve8GqiM+xYOgY7A9ACmTLFESEP0WmbZF1e8KzP+7JQZdEI/T19kxaBVXbcwLZ7+RO0eWzzRa877ZWo2TNIn+ZHzJL4FLhuMwCRUn+m6ECgYEA0WWW3Sk3nvC7EF2PC6KsAKK6ZeqGKRahbwxuL7zLvzi7wHNkhwNgWKsmaotrkOAO924AekLb4Hi1/xpf/6oTFOAEGXV8lQqORhYd+7zWXTsBdIlBhzbQmWJ86W3KeE9wfi5hsBbaOn7t9hnBmPA0Q4JdoOthOZAEUubBSXbB130CgYEAxGl+aRsQZKvU7ey+7BKYYDBcIvxpmF89eNDuf3xtBiyDgqL9S/vvJzqn+4y6qqXI49AdWjPOxgvuNXRnfP7yGHTqLxOnwvsBpPizlMDNmK4YIKJUnk1yLsLh4kCdyYJQa3cROfoQ/oWpIjGjnO2DAstfB/3dWEIbnQKa0pj9nc0CgYBm5eId6hxACZITN7aMhDK72Tt5y6aD2HAaDuSyprcEz89Lgij7Q8h7qhclsj94oPIZ2r93VRWRmB/vLTnRe/UGhBLfo+FFqDtD66huRVyd0dokNzKxTFlzlndFikM9nePszcQJcSFqL2emUP/WtOsp5Y02/5P2YnQNfQGspSQaTQKBgBl9/7QwmQ4X50kCIz2MpE5HuI2p6SKnqdjWdT4CrjvQ5zi7YtjL2BxlVowllcy0O8ClsEmW082MmtxBQXVNuapG8mYtzOZXob0Bsn0qEQUyA1uo9gad0qYTETJGZLRUv49TIt89f5spSexwOOYTRZ/FOY5V+raLzf2w6ttOlAw5AoGAKM3/EwyI6oK74v36Hhdxk+dWeMLVrhCKISj9XRKGXR7FfOQHpgBdOvr6r5AD0qtxDr1+GxRuom9VWH2Bkv1NXrP40e9cbRMg9c/eCiasEc7mWsExdVDboaRgla0npcGFRyk3EcFq+gltl8H6JLrI9xR2gBgnTPhQkhbp3Lt2JFk=
-----END PRIVATE KEY-----'''
# 实例化支付对象
alipay = AliPay(
    appid='2016101300673951',
    app_notify_url=None,
    app_private_key_string=alipay_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
)
# 实例化订单
order_string = alipay.api_alipay_trade_page_pay(
    subject = '牛羊生鲜',    # 交易主题
    out_trade_no = '10000000009',    # 订单号
    total_amount='400000',    # 交易总金额
    return_url=None,    # 请求支付之后及时回调的一个接口
    notify_url=None    # 通知地址
)
# 发送支付请求
# 请求地址：支付网关+实例化订单

result = 'https://openapi.alipaydev.com/gateway.do?'+order_string
print(result)