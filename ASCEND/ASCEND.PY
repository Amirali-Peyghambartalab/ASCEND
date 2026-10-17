import asyncio
import os
import flet as ft

TEST_ON_PC = True
LOGO = "logo.png"
WORDMARK = "wordmark.png"
BG_FILE= "mountain.jpg"
SHOW_SPLASH = False
CARD = "121823"

def fa(n):
    return str(n).translate(str.maketrans("0123456789" , "۰۱۲۳۴۵۶۷۸۹"))

TASKS = [
    {"TITLE" : "مطالعه زبان انگلیسی" , "MIN" : 30, "CAT" : "یادگیری" , "DONE" : True},
    {"TITLE" : "تمرین ورزشی" , "MIN" : 60, "CAT" : "سلامتی" , "DONE" : True},
    {"TITLE" : "کار روی پروژه " , "MIN" : 90, "CAT" : "کار" , "DONE" : True},
    {"TITLE" : "مطالعه کتاب" , "MIN" : 45, "CAT" : "رشد فردی" , "DONE" : False},

]

def build_home(page : ft. Page):
    count_text = ft.Text("" , size=14 , color="white")
    ring = ft.ProgressRing(value=0 , width=64, height=64, stroke_width=5,
                           color="#dfe7f3" , bgcolor="#232c3b")

    def set_progress():
        done = sum(1 for t in TASKS if t ["done"])
        count_text.value = f"{fa(done)}/{fa(len(TASKS))}"
    

async def main(Page: ft.Page) :
    Page.title = "ASCEND"
    Page.rtl = True
    Page.bgcolor = "#05070b"
    Page.padding = 0 

    if TEST_ON_PC :
        Page.window.width = 390
        Page.window.height = 844

    here = os.path.dirname(os.path.abspath(__file__))
    has_bg = os.path.exists(os.path.join(here , "assets" , BG_FILE))
    print("LOGO :" , os.path.exists(os.path.join(here , "assets" , LOGO)), "| MOUNTAIN :" , has_bg)

    bar = ft.ProgressBar(width = 180 , value = 0 , color = "#cfd8e6" , bgcolor = "#232c3b")

    front = ft.Column(
        left=0, top=0, right=0, bottom=0,
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
                ft.Image(src = LOGO, width = 210 , height = 210),
                ft.Container(
                    offset=ft.Offset(0, -0.4),
                    content=ft.Image(src=WORDMARK, width=250 , height=33),
                    ),
                   

                
                ft.Text("Better Plans" , size = 14 , color = "grey"),
                ft.Text("Higher Results", size=14, color="grey"),
                ft.Container(height=180),
            
            ],
        )
        
    bottom = ft . Column(
        left=0, right=0, bottom=50,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Loading ...", size = 12 , color = "grey"),
            bar,

            
        ],
    )

    Layers = [
        ft.Container(
            left=0, top=0, right=0, bottom=0,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0,-1),
                end=ft.Alignment(0, 1),
                colors=["#1b2433" , "#05070b"],
            )
        )
    ]

    if has_bg:
        Layers.append(ft.Image(src=BG_FILE, left=0, top=0, right=0, bottom=0, fit="cover")) 
        Layers.append(ft.Container(left=0, top=0, right=0, bottom=0, bgcolor="#9905070b"))
    Layers.append(front)
    Layers.append(bottom)

    Page.add(ft.Stack(expand=True, controls=Layers))
    Page.update()
    

    for i in range(21):
        bar.value = i / 20
        Page.update()
        await asyncio.sleep(0.1)

    Page.clean()
    Page.bgcolor = "#0a0e16"
    Page.padding = 20
    Page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text("GOOD MORNING", size = 28, weight=ft.FontWeight.BOLD , color = "white"),
                ft.Text("Every small step brings you closer." , size = 14, color = "grey"),
                ft.Container(
                    content=ft.Text("3/4 : today's tasks" , size = 18 , color = "white") ,
                    bgcolor="#121823",
                    border_radius=18,
                    padding=16,

                ),
            ],
        )
    )
    Page.update()

ft.run(main , assets_dir="assets")