import pytest
from biblioteca import Livro, Biblioteca

@pytest.fixture
def biblioteca_com_livro():
    """Fixture que prepara uma biblioteca com um livro cadastrado para os testes."""
    bib = Biblioteca()
    livro = Livro(id_livro=1, titulo="Dom Casmurro")
    bib.adicionar_livro(livro)
    return bib


def test_emprestimo_realizado_com_sucesso(biblioteca_com_livro):
    """Sugestão: empréstimo realizado (Muda status para indisponível)"""
    bib = biblioteca_com_livro
    
    # Executa o empréstimo
    resultado = bib.emprestar_livro(1)
    
    # Validações
    assert resultado is True
    assert bib.livros[1].disponivel is False


def test_emprestimo_livro_ja_emprestado(biblioteca_com_livro):
    """Sugestão: livro já emprestado (Não deve permitir novo empréstimo)"""
    bib = biblioteca_com_livro
    
    # Primeiro empréstimo (sucesso)
    bib.emprestar_livro(1)
    
    # Tentativa de segundo empréstimo (deve falhar)
    resultado_segundo_emprestimo = bib.emprestar_livro(1)
    
    assert resultado_segundo_emprestimo is False
    assert bib.livros[1].disponivel is False


def test_devolucao_correta(biblioteca_com_livro):
    """Sugestão: devolução correta (Altera status de volta para disponível)"""
    bib = biblioteca_com_livro
    
    # Empresta primeiro para mudar o status
    bib.emprestar_livro(1)
    
    # Executa a devolução
    resultado_devolucao = bib.devolver_livro(1)
    
    # Validações
    assert resultado_devolucao is True
    assert bib.livros[1].disponivel is True


def test_erro_ao_interagir_com_livro_inexistente():
    """Teste extra: Garante que o sistema trata IDs inválidos"""
    bib = Biblioteca()
    
    with pytest.raises(ValueError):
        bib.emprestar_livro(999)