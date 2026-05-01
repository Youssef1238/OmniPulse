import webview


def route(path):
    window.load_url(path)

def load_data():
    return [{"id":1, "target": "Osama Bin Laden"}, {"id":2, "target": "Mikel Arteta"}]

def log(content):
    print(content)
    


window = webview.create_window('OmniPulse', url='ui/index.html')
window.expose(load_data)
window.expose(log)
window.expose(route)

def start():
    webview.start()