from django.db import models
from contas.models import User

class TipoAtividade(models.Model):
    descricao = models.CharField("Descrição", max_length=50)

    class Meta:
        verbose_name = "Tipo de Atividade"
        verbose_name_plural = "Tipos de Atividades"

    def __str__(self):
        return self.descricao

class AtividadeComplementar(models.Model):
    aluno = models.ForeignKey(User, related_name='atividades_criadas', 
                                        on_delete=models.CASCADE, verbose_name='Alunos')
    atividade = models.ForeignKey(TipoAtividade, related_name='atividades', 
                                        on_delete=models.CASCADE, verbose_name='Atividade')
    descricao = models.CharField("Descrição", max_length=200)
    carga_horaria = models.CharField("Carga Horária", max_length=30)
    instituicao = models.CharField("Instituição", max_length=100)
    ano_conclusao = models.IntegerField("Ano de Conclusão")
    arquivo = models.FileField("Arquivo")
    observacao = models.TextField("Observação", max_length=500)

    class Meta:
        verbose_name = "Atividade Complementar"
        verbose_name_plural = "Atividades Complementares"

    def __str__(self):
        return self.descricao
