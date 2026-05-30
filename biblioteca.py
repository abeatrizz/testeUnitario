class Livro:
    def __init__(self, id_livro: int, titulo: str):
        self.id = id_livro
        self.titulo = titulo
        self.disponivel = True  # Controle de disponibilidade


class Biblioteca:
    def __init__(self):
        self.livros = {}

    def adicionar_livro(self, livro: Livro):
        self.livros[livro.id] = livro

    def emprestar_livro(self, id_livro: int) -> bool:
        # Livro indisponível não pode ser emprestado.
        if id_livro not in self.livros:
            raise ValueError("Livro não encontrado no acervo.")
        
        livro = self.livros[id_livro]
        
        if not livro.disponivel:
            return False  # Livro já está emprestado
            
        livro.disponivel = False
        return True

    def devolver_livro(self, id_livro: int) -> bool:
        # Devolução altera o status do livro para disponível.
        if id_livro not in self.livros:
            raise ValueError("Livro não encontrado no acervo.")
            
        livro = self.livros[id_livro]
        
        if livro.disponivel:
            return False  # Livro já estava na biblioteca
            
        livro.disponivel = True
        return True