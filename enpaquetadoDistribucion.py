import flet as ft

def main(page: ft.Page):
    page.title = "Mi Primera App Empaquetada"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    texto = ft.Text("¡Hola! Esta aplicación corre de forma independiente.", size=20)
    
    page.add(
        ft.Row(
            [texto],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)
