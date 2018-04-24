import rediser

r = rediser.redis_pool

r.set('foo', 'Bar')
print(r.get('foo'))
