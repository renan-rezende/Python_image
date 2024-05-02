# IDENTIFICAÇÃO DO ESTUDANTE:
# Preencha seus dados e leia a declaração de honestidade abaixo. NÃO APAGUE
# nenhuma linha deste comentário de seu código!
#
#    Nome completo:
#    Matrícula:
#    Turma:
#    Email:
#
# DECLARAÇÃO DE HONESTIDADE ACADÊMICA:
# Eu afirmo que o código abaixo foi de minha autoria. Também afirmo que não
# pratiquei nenhuma forma de "cola" ou "plágio" na elaboração do programa,
# e que não violei nenhuma das normas de integridade acadêmica da disciplina.
# Estou ciente de que todo código enviado será verificado automaticamente
# contra plágio e que caso eu tenha praticado qualquer atividade proibida
# conforme as normas da disciplina, estou sujeito à penalidades conforme
# definidas pelo professor da disciplina e/ou instituição.


# Imports permitidos (não utilize nenhum outro import!):
import sys
import math
import base64
import tkinter
from io import BytesIO
from PIL import Image as PILImage


# Classe Imagem:
class Imagem:
    def __init__(self, largura, altura, pixels):
        self.largura = largura
        self.altura = altura
        self.pixels = pixels
    #Kernels de exmplo do arquivo pset1.pdf
    kernel_translação_a_direita = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
    kernel_media = [
    [0.0, 0.2, 0.0],
    [0.2, 0.2, 0.2],
    [0.0, 0.2, 0.0]
]
   



    def get_pixel(self, x, y):
    # Se x ou y estiverem fora dos limites, retorna 0
     if x < 0 or x >= self.largura or y < 0 or y >= self.altura: 
        return 0
     return self.pixels[y * self.largura + x]

    def set_pixel(self, x, y, c):
     self.pixels[y * self.largura + x] = c


    def aplicar_por_pixel(self, func):
     resultado = Imagem.nova(self.largura, self.altura)
     for x in range(resultado.largura):
         for y in range(resultado.altura):
             cor = self.get_pixel(x, y)
             nova_cor = func(cor)
             resultado.set_pixel(x, y, nova_cor)
     return resultado


    def invertida(self):
        return self.aplicar_por_pixel(lambda c: 255 - c)

    def borrada(self,tamanho_kernel):
        
     #Kernel 3x3
     """ kernel_borrar = [
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1]
     ]"""

         
     # Cria uma imagem nova para armazenar o resultado do filtro
     resultado = Imagem.nova(self.largura, self.altura)
    
     # Percorre todos os pixels da imagem de entrada
     for y in range(self.altura):
         for x in range(self.largura):
             soma = 0
             # Percorre a vizinhança do pixel atual definida pelo tamanho do kernel
             for j in range(tamanho_kernel):
                 for i in range(tamanho_kernel):
                     # Obtém o valor do pixel na vizinhança
                     pixel_vizinho = self.get_pixel(x+i + (-1), y+j + (-1))
                     valor_pixel = pixel_vizinho * 1
                     
                     soma += valor_pixel
            
             # Calcula a média dos valores dos pixels na vizinhança
             media = soma // (tamanho_kernel * tamanho_kernel)
            
             # Define o valor médio como o novo valor do pixel na imagem de saída
             resultado.set_pixel(x, y, round(media))
    
     return resultado
    
    def focada_kernel_3x3(self):
     kernel_nitidez = [
     [-1, -1, -1],
     [-1, 17, -1],
     [-1, -1, -1]
]

     # Cria uma imagem nova para armazenar o resultado do filtro
     imagem_focada = Imagem.nova(self.largura, self.altura)
     
     # Percorre todos os pixels da imagem de entrada
     for y in range(self.altura):
         for x in range(self.largura):
             soma = 0
             # Percorre a vizinhança do pixel atual definida pelo tamanho do kernel
             for j in range(3):
                 for i in range(3):
                     # Obtém o valor do pixel na vizinhança
                     pixel_vizinho = self.get_pixel(x+i + (-1), y+j + (-1))
                     valor_pixel = pixel_vizinho * kernel_nitidez[j][i]
                     
                     soma += valor_pixel
            
             # Calcula a média dos valores dos pixels na vizinhança
             media = soma // 9
            
             # Define o valor médio como o novo valor do pixel na imagem de saída
             imagem_focada.set_pixel(x, y, round(media))
    
     return imagem_focada
        
        
    def focada_subt_explicita(self, caminho_arquivo):
        
        imagem_borrada = Imagem.carregar(caminho_arquivo).borrada(3)
        imagem_focada = Imagem.nova(self.largura, self.altura)
        
        for y in range(self.altura):
          for x in range(self.largura):
              # "Seta" o pixel da imagem focada (coordenadas x,y) como a operação feita dentro do round() 
              imagem_focada.set_pixel(x,y,round(2*self.get_pixel(x,y) - imagem_borrada.get_pixel(x,y)))
              
        return imagem_focada
    
    def bordas(self):
        raise NotImplementedError

    # Abaixo deste ponto estão utilitários para carregar, salvar e mostrar
    # as imagens, bem como para a realização de testes. Você deve ler as funções
    # abaixo para entendê-las e verificar como funcionam, mas você não deve
    # alterar nada abaixo deste comentário.
    #
    # ATENÇÃO: NÃO ALTERE NADA A PARTIR DESTE PONTO!!! Você pode, no final
    # deste arquivo, acrescentar códigos dentro da condicional
    #
    #                 if __name__ == '__main__'
    #
    # para executar testes e experiências enquanto você estiver executando o
    # arquivo diretamente, mas que não serão executados quando este arquivo
    # for importado pela suíte de teste e avaliação.
    def __eq__(self, other):
        return all(getattr(self, i) == getattr(other, i)
                   for i in ('altura', 'largura', 'pixels'))

    def __repr__(self):
        return "Imagem(%s, %s, %s)" % (self.largura, self.altura, self.pixels)

    @classmethod
    def carregar(cls, nome_arquivo):
        """
        Carrega uma imagem do arquivo fornecido e retorna uma instância dessa
        classe representando essa imagem. Também realiza a conversão para tons
        de cinza.

        Invocado como, por exemplo:
           i = Imagem.carregar('test_images/cat.png')
        """
        with open(nome_arquivo, 'rb') as guia_para_imagem:
            img = PILImage.open(guia_para_imagem)
            img_data = img.getdata()
            if img.mode.startswith('RGB'):
                pixels = [round(.299 * p[0] + .587 * p[1] + .114 * p[2]) for p in img_data]
            elif img.mode == 'LA':
                pixels = [p[0] for p in img_data]
            elif img.mode == 'L':
                pixels = list(img_data)
            else:
                raise ValueError('Modo de imagem não suportado: %r' % img.mode)
            l, a = img.size
            return cls(l, a, pixels)

    @classmethod
    def nova(cls, largura, altura):
        """
        Cria imagens em branco (tudo 0) com a altura e largura fornecidas.

        Invocado como, por exemplo:
            i = Imagem.nova(640, 480)
        """
        return cls(largura, altura, [0 for i in range(largura * altura)])

    def salvar(self, nome_arquivo, modo='PNG'):
        """
        Salva a imagem fornecida no disco ou em um objeto semelhante a um arquivo.
        Se o nome_arquivo for fornecido como uma string, o tipo de arquivo será
        inferido a partir do nome fornecido. Se nome_arquivo for fornecido como
        um objeto semelhante a um arquivo, o tipo de arquivo será determinado
        pelo parâmetro 'modo'.
        """
        saida = PILImage.new(mode='L', size=(self.largura, self.altura))
        saida.putdata(self.pixels)
        if isinstance(nome_arquivo, str):
            saida.save(nome_arquivo)
        else:
            saida.save(nome_arquivo, modo)
        saida.close()

    def gif_data(self):
        """
        Retorna uma string codificada em base 64, contendo a imagem
        fornecida, como uma imagem GIF.

        Função utilitária para tornar show_image um pouco mais limpo.
        """
        buffer = BytesIO()
        self.salvar(buffer, modo='GIF')
        return base64.b64encode(buffer.getvalue())

    def mostrar(self):
        """
        Mostra uma imagem em uma nova janela Tk.
        """
        global WINDOWS_OPENED
        if tk_root is None:
            # Se Tk não foi inicializado corretamente, não faz mais nada.
            return
        WINDOWS_OPENED = True
        toplevel = tkinter.Toplevel()
        # O highlightthickness=0 é um hack para evitar que o redimensionamento da janela
        # dispare outro evento de redimensionamento (causando um loop infinito de
        # redimensionamento). Para maiores informações, ver:
        # https://stackoverflow.com/questions/22838255/tkinter-canvas-resizing-automatically
        tela = tkinter.Canvas(toplevel, height=self.altura,
                              width=self.largura, highlightthickness=0)
        tela.pack()
        tela.img = tkinter.PhotoImage(data=self.gif_data())
        tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        def ao_redimensionar(event):
            # Lida com o redimensionamento da imagem quando a tela é redimensionada.
            # O procedimento é:
            #  * converter para uma imagem PIL
            #  * redimensionar aquela imagem
            #  * obter os dados GIF codificados em base 64 (base64-encoded GIF data)
            #    a partir da imagem redimensionada
            #  * colocar isso em um label tkinter
            #  * mostrar a imagem na tela
            nova_imagem = PILImage.new(mode='L', size=(self.largura, self.altura))
            nova_imagem.putdata(self.pixels)
            nova_imagem = nova_imagem.resize((event.width, event.height), PILImage.NEAREST)
            buffer = BytesIO()
            nova_imagem.save(buffer, 'GIF')
            tela.img = tkinter.PhotoImage(data=base64.b64encode(buffer.getvalue()))
            tela.configure(height=event.height, width=event.width)
            tela.create_image(0, 0, image=tela.img, anchor=tkinter.NW)

        # Por fim, faz o bind da função para que ela seja chamada quando a tela
        # for redimensionada:
        tela.bind('<Configure>', ao_redimensionar)
        toplevel.bind('<Configure>', lambda e: tela.configure(height=e.height, width=e.width))

        # Quando a tela é fechada, o programa deve parar
        toplevel.protocol('WM_DELETE_WINDOW', tk_root.destroy)


# Não altere o comentário abaixo:
# noinspection PyBroadException
try:
    tk_root = tkinter.Tk()
    tk_root.withdraw()
    tcl = tkinter.Tcl()


    def refaz_apos():
        tcl.after(500, refaz_apos)


    tcl.after(500, refaz_apos)
except:
    tk_root = None

WINDOWS_OPENED = False

if __name__ == '__main__':
    # O código neste bloco só será executado quando você executar
    # explicitamente seu script e não quando os testes estiverem
    # sendo executados. Este é um bom lugar para gerar imagens, etc.
    pass

    # O código a seguir fará com que as janelas de Imagem.mostrar
    # sejam exibidas corretamente, quer estejamos executando
    # interativamente ou não:
    if WINDOWS_OPENED and not sys.flags.interactive:
        tk_root.mainloop()
