from django.db import models



class produto(models.Model):
    tipo=models.CharField(max_length=100,verbose_name="Tipo do produto")
    nome=models.CharField(max_length=100,verbose_name="Nome do produto")
    preco=models.PositiveIntegerField(verbose_name="Preço do produto")
    promocao=models.CharField(max_length=100,verbose_name="Esta em promoção?")

    def __str__(self):
        return "({}){}".format(self.tipo,self.nome)



class Compra_campo(models.Model):
    compra=models.ForeignKey(produto, on_delete=models.CASCADE)
    def __str__(self):
         return f" Compra de ({self.compra.tipo}){self.compra.nome}"

    