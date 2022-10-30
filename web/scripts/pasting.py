from web.scripts.telegraph_helper import telegraph, telegraph_name


def telegraph_paste(text):
    tele_cont = []
    path = []
    if len(text.encode("utf-8")) > 39000:
        tele_cont.append(text)
    if text != "":
        tele_cont.append(text)
    if len(tele_cont) == 0:
        return "", None
    for content in tele_cont:
        path.append(
            telegraph.create_page(title=telegraph_name, content=content)["path"]
        )
    if len(path) > 1:
        telegraph.edit_telegraph(path, tele_cont)
    tlg_url = f"https://graph.org/{path[0]}"
    return tlg_url
