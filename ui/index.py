import webview


def load_data():
    return [{"id":1, "target": "Osama Bin Laden"}, {"id":2, "target": "Mikel Arteta"}]

def log(content):
    print(content)
    

def start():
    window = webview.create_window('OmniPulse', 'ui/index.html')
    window.expose(load_data)
    window.expose(log)
    webview.start()