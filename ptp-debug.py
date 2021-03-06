from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": "7000"}]

# Note: decode_responses must be set to True when used with python3
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

__import__('ptpdb').set_trace()
