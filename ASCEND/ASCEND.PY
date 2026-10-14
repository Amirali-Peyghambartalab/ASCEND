import flet as ft
def main(page : ft.Page) :
    page.title="ASCEND"
    page.rtl=True
    page.bgcolor="#0a0e16"
    page.padding=0
    page.window.width = 390
    page.window.height = 844

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                expand=True,
                padding=20,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        ft.Text("Good Morning" , size=28, weight=ft.FontWeight.BOLD,color="white"),
                        ft.Text("Every small step brings you closer to a bigger goal." , size=14,color="grey"),
                        ft.Container(
                            content=ft.Text("3/4 : Today's tasks" , size=18,color="white"),
                            bgcolor="#121823",
                            border_radius=18,
                            padding=16,
                        ),
                    ],
                ),
            ),
        )
    )
ft.run(main)