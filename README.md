# Relatório de Criação e Execução dos Testes

1. Objetivo
O objetivo desta atividade foi criar e executar testes automatizados utilizando o framework Pytest para validar o 
funcionamento do sistema de biblioteca.

2. Criação dos Testes
Foi criado o arquivo `test_biblio.py` contendo testes para verificar os principais comportamentos do sistema:

* Empréstimo realizado com sucesso.
* Tentativa de empréstimo de um livro já emprestado.
* Devolução correta de um livro.
* Tratamento de erro ao tentar interagir com um livro inexistente.

Cada teste foi desenvolvido seguindo o padrão AAA (Arrange, Act, Assert):

* Arrange: preparação dos dados necessários para o teste.
* Act: execução da ação a ser testada.
* Assert: verificação do resultado esperado.

3. Instalação e Configuração do Pytest

Inicialmente ocorreu o erro:
ModuleNotFoundError: No module named 'pytest'
Esse problema foi resolvido instalando o Pytest no ambiente virtual do projeto.
Foi utilizada a seguinte verificação:
python -m pytest --version
Resultado obtido:
pytest 9.0.3

4. Execução dos Testes
Os testes foram executados através do comando:
python -m pytest -v
O parâmetro `-v` (verbose) exibe informações detalhadas sobre cada teste executado.

5. Resultado Obtido
Todos os testes foram executados com sucesso.
Resultado apresentado pelo Pytest:

test_biblio.py::test_emprestimo_realizado_com_sucesso PASSED
test_biblio.py::test_emprestimo_livro_ja_emprestado PASSED
test_biblio.py::test_devolucao_correta PASSED
test_biblio.py::test_erro_ao_interagir_com_livro_inexistente PASSED

Resumo:

4 passed in 0.05s

6. Evidências

Como evidência da execução correta dos testes, foi anexado um print da saída do terminal mostrando:
Como: "evidencia_pytest"

7. Conclusão

Os testes automatizados foram criados e executados com sucesso. Todos os cenários planejados 
foram validados e o sistema apresentou o comportamento esperado em todas as situações testadas.
