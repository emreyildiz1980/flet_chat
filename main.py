import flet as ft





def create_message_row(page, message, who):
    empty_container = ft.Container(width=page.window_width / 2, )
    container = get_message_container(page, message, ft.colors.GREY_400)
    row = ft.Row()
    if who == "ME":
        container.bgcolor = ft.colors.CYAN
        row.controls.append(empty_container)
        row.controls.append(container)
    else:
        row.controls.append(container)
        row.controls.append(empty_container)

    return row


def get_message_container(page, message, color):
    return ft.Container(
        bgcolor=color,
        border_radius=8,
        width=page.window_width / 3,
        padding=8,
        content=ft.Text(
            color=ft.colors.WHITE,
            size=15,
            value=message
        )
    )


def main(page: ft.Page):
    def send_message(e):
        lv.controls.append(create_message_row(page, input1.value, "ME"))
        input1.value = ""
        page.update()

    page.title = "Flet Chat Application"
    page.bgcolor = ft.colors.WHITE

    page.window_width = 800
    page.window_height = 800
    page.window_resizable = False

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    lv.controls.append(create_message_row(page, "Message1", "ME"))
    lv.controls.append(create_message_row(page, "Message2", "ME"))
    lv.controls.append(create_message_row(page, "Message3", "FRIEND"))
    lv.controls.append(create_message_row(page, "Message4", "ME"))
    lv.controls.append(create_message_row(page, "Message5", "FRIEND"))
    lv.controls.append(create_message_row(page, "Message6 Message6 Message6 Message6 Message6 Message6 Message6", "FRIEND"))

    input1 = ft.TextField(text_align=ft.TextAlign.LEFT, value="", color=ft.colors.BLACK)

    page.add(
        ft.Column(
            [
                ft.Row(
                    height=page.window_height - 120,
                    controls=[
                        lv,
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            input1,
                            expand=True
                        ),
                        ft.IconButton(
                            ft.icons.SEND,
                            on_click=send_message,
                            bgcolor=ft.colors.CYAN
                        )
                    ],
                )
            ],
        )
    )


ft.app(target=main)
