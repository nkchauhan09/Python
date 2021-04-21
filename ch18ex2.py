with open("ch18ex2.html", "r") as rf:
    with open("ch18ex2.txt", "a") as wf:
        page = rf.read()
        link_exist = True
        while link_exist:
            pos = page.find("<a href=")
            if pos == -1:
                link_exist = False
            else:
                fq = page.find("\"",pos)
                sq = page.find("\"",fq+1)
                url = page[fq+1:sq]
                wf.write(f"{url}\n")
                page = page[sq:]