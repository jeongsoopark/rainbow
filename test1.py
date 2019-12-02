import facebook


my_page_id = '120983479301427'
my_app_id = '796913680752917'
my_app_secret = '0b4492b78976d5096d6a10d562c10f0d'
my_access_token = 'EAALUyezboRUBAEeCgQrpXGjbya04M8gEa4xz4vxrKzh4NRjEoQ4UqZBUdZCxwgi3IFDELHvaI86LZBemvZAZAwHXQq85XhXITtZBUGOBmfy5YjPlhwLdnn5LCjXmHlF4PJbjH6BDtOclPcMKWEJZAA4aM4CZBRhDAWXI61PqLx6RH1x8mOqHrDXk'
my_adaccount = '120983479301427'

test_page_id = '102768471210944'

graph = facebook.GraphAPI(my_access_token)
graph.put_object(my_page_id, "feed", message="test message")
print(graph)

