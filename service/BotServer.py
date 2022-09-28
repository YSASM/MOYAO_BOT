from mirai import Mirai, WebSocketAdapter
def bot_config():
    bot = Mirai(
    qq=2819207569, 
    adapter=WebSocketAdapter(
        verify_key='12345678', host='localhost', port=8008
        )
    )
    return bot