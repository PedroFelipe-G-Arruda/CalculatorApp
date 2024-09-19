import flet as ft
# import shared_preferences
import math

def main(page: ft.Page):
    page.views.clear()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.HIDDEN
    
    def arredondar(numero):
        numero *= 10**5
        numero = math.ceil(numero)
        print(numero)
        return numero / 10**5
    
    def calcular(e):
        if not page.client_storage.get("preco"):
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha o valor de preço.")
            )
            page.open(alerta)
        elif not valor_altura.value or not valor_comprimento.value or not valor_largura.value:
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha os valores.")
            )
            page.open(alerta)
        else:
            valor_total = float(valor_altura.value) * float(valor_comprimento.value) * float(valor_largura.value) * page.client_storage.get("preco")
            preco_calculado.value = f'R${valor_total:.2f}'
            preco_calculado.update()

    def calcular_area(e):
        if not page.client_storage.get("preco"):
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha o valor de preço.")
            )
            page.open(alerta)
        elif not valor_cm_quadadro.value or not valor_largura_cm_quadrado.value:
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha os valores.")
            )
            page.open(alerta)
        else:
            valor_total_area = float(valor_cm_quadadro.value) * float(valor_largura_cm_quadrado.value) * page.client_storage.get("preco")
            preco_calculado_area.value = f'R${valor_total_area:.2f}'
            preco_calculado_area
            preco_calculado_area.update()
            layout_home.scroll_to(key="A")

    def acoes(e):
        if e.control == valor_altura:
            valor_comprimento.focus()
        elif e.control == valor_comprimento:
            valor_largura.focus()
        elif e.control == valor_cm_quadadro:
            valor_largura_cm_quadrado.focus()
         

    def limpa_texto(e):
        e.control.value=""
        e.control.update()


    def salvar(e):
        page.client_storage.set("preco",float(valor_venda.value))

    def acoes_conf(e):
        if e.control == base_altura_preco:
            base_comprimento_preco.focus()
        elif e.control == base_comprimento_preco:
            base_largura_preco.focus()
        elif e.control == base_largura_preco:
            valor_bloco.focus()

    def calculo_preco_custo(e):
        if not base_altura_preco.value or not base_comprimento_preco.value or not base_largura_preco.value:
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha os valores.")
            )
            page.open(alerta)
        else:
            valor_custo.value=arredondar(float(valor_bloco.value)/(float(base_altura_preco.value)*float(base_comprimento_preco.value)*float(base_largura_preco.value)))
            page.update()

    def calculo_preco_venda(e):
        if not valor_custo.value or not fator_ganho.value :
            alerta = ft.AlertDialog(
                title = ft.Text("Preeancha os valores de custo e fator ganho.")
            )
            page.open(alerta)
        else:
            valor_venda.value=arredondar(float(valor_custo.value)*(float(fator_ganho.value) /100))
            page.update()
    

    ##SETTING
    # valor_venda = 0.00049
    base_altura_preco = ft.TextField(label="Altura em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes_conf)
    base_comprimento_preco = ft.TextField(label="Comprimento em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes_conf)
    base_largura_preco = ft.TextField(label="Largura em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes_conf)
    valor_bloco = ft.TextField(label="Valor do bloco",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=calculo_preco_custo)
    valor_custo = ft.TextField(label="Valor de custo",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto)
    fator_ganho = ft.TextField(label="Fator de ganho (%)",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto)

    valor_venda = ft.TextField(value=page.client_storage.get("preco"),label="Valor de venda",keyboard_type=ft.KeyboardType.NUMBER)
    
    botao_calcular_valor_venda = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Calcular valor Venda",size=20, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
        on_click=calculo_preco_venda,
        height=45)
   
    ##HOME
    valor_altura = ft.TextField(label="Altura em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes)
    valor_comprimento = ft.TextField(label="Comprimento em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes)
    valor_largura = ft.TextField(label="Largura em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=calcular)

    valor_cm_quadadro = ft.TextField(label="Área em cm²",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=acoes)
    valor_largura_cm_quadrado = ft.TextField(label="Largura em cm",keyboard_type=ft.KeyboardType.NUMBER, on_focus=limpa_texto, on_submit=calcular_area)

    #normal
    botao_calcular = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Calcular",size=20, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
        on_click=calcular,
        height=45)
    preco_calculado = ft.Text("",weight=ft.FontWeight.BOLD,size=30)

    #area quadrada
    botao_calcular_area = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Calcular",size=20, color=ft.colors.BLACK),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
        on_click=calcular_area,
        height=45)
    preco_calculado_area = ft.Text("",weight=ft.FontWeight.BOLD,size=30)

    

    def route_change(route):
        print(page.views)
        # page.views.clear()
        if not page.views:
            page.views.append(
                ft.View(
                    "/",
                    scroll = ft.ScrollMode.HIDDEN,
                    controls=[
                        appbar_home,
                        layout_home
                    ],
                )
            )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    controls=[
                        appbar_setting,
                        layout_settings,
                    ]
                )
            )
        page.update()

    #HOME
    appbar_home = ft.AppBar(
        title=ft.Text("Calculadora EPS"),
        center_title= True,
        actions=[
            ft.IconButton(ft.icons.SETTINGS, on_click=lambda _: page.go("/settings"))
        ]
    )

    layout_home = ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        controls=[
            ft.ResponsiveRow(
                [
                    ft.Container(
                        valor_altura,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        valor_comprimento,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        valor_largura,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        botao_calcular,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        preco_calculado,
                        alignment=ft.alignment.center,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Divider(),
                    ft.Container(
                        ft.Text("Calculo placa", size=20),
                        alignment=ft.alignment.center,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        valor_cm_quadadro,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        valor_largura_cm_quadrado,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        botao_calcular_area,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                    ft.Container(
                        preco_calculado_area,
                        alignment=ft.alignment.center,
                        padding= 5,
                        key="A",
                        col={"sm":12, "md":3, "xl":3}
                    )
                ]    
            )
        ]
    )
    
    #CONFIGURAÇÃO
    appbar_setting = ft.AppBar(
        title=ft.Text("Configuração"),
        center_title= True,
        actions=[
            ft.IconButton(ft.icons.SAVE, on_click=salvar)
        ]
    )

    layout_settings = ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        
        controls=[
            ft.ResponsiveRow(
                [
                    ft.Container(
                        base_altura_preco,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Container(
                        base_comprimento_preco,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Container(
                        base_largura_preco,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Container(
                        valor_bloco,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Divider(),

                    ft.Container(
                        fator_ganho,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Container(
                        valor_custo,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Divider(),

                    ft.Container(
                        valor_venda,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),

                    ft.Container(
                        botao_calcular_valor_venda,
                        padding= 5,
                        col={"sm":12, "md":3, "xl":3}
                    ),
                ]
            )
        ]
    )
    
    def view_pop(view):
        print("voltou")
        page.views.pop()
        page.go(page.views[-1].route)


    print(page.views)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # page.add(layout)


ft.app(target=main)