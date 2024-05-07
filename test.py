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
#


# Imports
import os
import pset1
import unittest

# Diretório
TEST_DIRECTORY = os.path.dirname(__file__)


# Classe para os testes de imagem:
class TestImagem(unittest.TestCase):
    def test_carregar(self):
        resultado = pset1.Imagem.carregar('test_images/centered_pixel.png')
        esperado = pset1.Imagem(11, 11,
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(resultado, esperado)

# Classe para os testes de inversão:
class TestInvertida(unittest.TestCase):
    def test_invertida_1(self):
        im = pset1.Imagem.carregar('test_images/centered_pixel.png')
        resultado = im.invertida()
        esperado = pset1.Imagem(11, 11,
                                [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                                 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255])
        self.assertEqual(resultado,  esperado)
        resultado.mostrar()
        esperado.mostrar()
        
    def test_invertida_2(self):
    # Escreva aqui o seu caso de teste
     im = pset1.Imagem.carregar('test_images/bluegill.png')
     resultado = im.invertida()
     resultado.salvar("bluegill_Invertido.png", modo="PNG")


    def test_imagens_invertidas(self):
        for nome_arquivo in ('mushroom', 'twocats', 'chess'):
            with self.subTest(f=nome_arquivo):
                arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', '%s_invert.png' % nome_arquivo)
                resultado = pset1.Imagem.carregar(arquivo_entrada).invertida()
                esperado = pset1.Imagem.carregar(arquivo_saida)
                self.assertEqual(resultado,  esperado)


# Classe para os testes dos filtros:
    class TestFiltros(unittest.TestCase):
        
        def test_borrada(self):
            imagem_entrada = pset1.Imagem.carregar('test_images/mushroom.png')
            imagem_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,imagem_entrada.pixels)
            imagem_copia.borrada(3).salvar("mushroon_Invertido_borrado.png", modo="PNG")
            imagem_entrada.salvar("mushroon_Invertido.png", modo="PNG")
            
        def test_focada1(self):
            caminho_arquivo = 'test_images/mushroom.png'
            imagem_entrada = pset1.Imagem.carregar(caminho_arquivo)
            imagem_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,imagem_entrada.pixels)
            tamanho_kernel = 6
            imagem_focada = imagem_copia.focada_subt_explicita(caminho_arquivo,tamanho_kernel)
            imamgem_borrada = imagem_copia.borrada(tamanho_kernel)
            
            imamgem_borrada.salvar("mushroon_borrada.png", modo="PNG")
            imagem_focada.salvar("mushroon_focada6.png", modo="PNG")
            
        def test_focada_kernel_3x3(self):
            caminho_arquivo = 'test_images/mushroom.png'
            imagem_entrada = pset1.Imagem.carregar(caminho_arquivo)
            imagem_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,imagem_entrada.pixels)
            
            imagem_focada = imagem_copia.focada_kernel_3x3()
            imamgem_borrada = imagem_copia.borrada(3)
            
            imamgem_borrada.salvar("mushroon_borrada.png", modo="PNG")
            imagem_focada.salvar("mushroon_focada11.png", modo="PNG")
      
        def test_borda(self):
            caminho_arquivo = 'test_images/construct.png'
            imagem_entrada = pset1.Imagem.carregar(caminho_arquivo)
            imagem_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,imagem_entrada.pixels)
            
            imagem_com_bordas = imagem_copia.borda()
            imagem_com_bordas.salvar("construct_com_borda.png", modo="PNG")
        
        def test_borradas(self):
            for tamanho_kernel in (1, 3, 7):
                for nome_arquivo in ('mushroom', 'twocats', 'chess'):
                    with self.subTest(k=tamanho_kernel, f=nome_arquivo):
                        arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                        arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results',
                                                    '%s_blur_%02d.png' % (nome_arquivo, tamanho_kernel))
                        imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                        imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                            imagem_entrada.pixels)
                        resultado = imagem_entrada.borrada(tamanho_kernel)
                        esperado = pset1.Imagem.carregar(arquivo_saida)
                        self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                        "Cuidado para não modificar a imagem original!")
                        self.assertEqual(resultado,  esperado)

        def test_focada(self):
            for tamanho_kernel in (1, 3, 9):
                for nome_arquivo in ('mushroom', 'twocats', 'chess'):
                    with self.subTest(k=tamanho_kernel, f=nome_arquivo):
                        arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                        arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results',
                                                    '%s_sharp_%02d.png' % (nome_arquivo, tamanho_kernel))
                        imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                        imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                            imagem_entrada.pixels)
                        resultado = imagem_entrada.focada(tamanho_kernel)
                        esperado = pset1.Imagem.carregar(arquivo_saida)
                        self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                        "Cuidado para não modificar a imagem original!")
                        self.assertEqual(resultado,  esperado)

        def test_bordas(self):
            for nome_arquivo in ('mushroom', 'twocats', 'chess'):
                with self.subTest(f=nome_arquivo):
                    arquivo_entrada = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % nome_arquivo)
                    arquivo_saida = os.path.join(TEST_DIRECTORY, 'test_results', '%s_edges.png' % nome_arquivo)
                    imagem_entrada = pset1.Imagem.carregar(arquivo_entrada)
                    imagem_entrada_copia = pset1.Imagem(imagem_entrada.largura, imagem_entrada.altura,
                                                        imagem_entrada.pixels)
                    resultado = imagem_entrada.bordas()
                    esperado = pset1.Imagem.carregar(arquivo_saida)
                    self.assertEqual(imagem_entrada, imagem_entrada_copia,
                                    "Cuidado para não modificar a imagem original!")
                    self.assertEqual(resultado,  esperado)


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)

