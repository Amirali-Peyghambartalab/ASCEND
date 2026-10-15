import asyncio
import os
import flet as ft

TEST_ON_PC = True
LOGO = "logo.png"
BG_FILE= "mountain.jpg"

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
                ft.Image(src = LOGO , width = 230 , height = 230),
                ft.Container(
                    offset=ft.Offset(0, -0.4),
                    content=ft.Text("ASCEND" , size = 40 , weight = ft.FontWeight . BOLD , color = "white"),

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