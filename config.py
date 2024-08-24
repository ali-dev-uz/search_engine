from environs import Env

env = Env()
env.read_env()

API_KEY = env.str("API_KEY")
CX = env.str("CX")
GPT_API_KEY = env.str("GPT_API_KEY")





