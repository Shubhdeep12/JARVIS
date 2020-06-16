import wolframalpha
client = wolframalpha.Client('VPEQGT-RLXK7WX75U')
res = client.query('weather in patna now')
print(next(res.results).text)
