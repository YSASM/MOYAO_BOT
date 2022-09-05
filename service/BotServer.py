from mirai import Mirai, WebSocketAdapter
def bot_config():
    bot = Mirai(
    qq=2260879310, 
    adapter=WebSocketAdapter(
        verify_key='12345678', host='localhost', port=8765
        )
    )
    return bot