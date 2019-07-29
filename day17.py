import redis
client=redis.Redis(host='127.0.0.1',port=6379,password='wanlhwanhs1.A')
client.set('username','admin')
client.hset('student','name','hao')
client.hset('student','age',38)
