from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota
from modelos.turma import Turma


def main():
    turmas = []
    disciplinas = []
    professores = []
    alunos = []
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Gerenciar Turmas")
        print("2. Gerenciar Disciplinas")
        print("3. Gerenciar Professores")
        print("4. Gerenciar Alunos")
        print("5. Gerenciar Notas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            print("Saindo do sistema...")
            break
            
        elif opcao == "1":
            gerenciar_turmas(turmas, disciplinas, alunos)
            
        elif opcao == "2":
            gerenciar_disciplinas(disciplinas)
            
        elif opcao == "3":
            gerenciar_professores(professores, disciplinas)
            
        elif opcao == "4":
            gerenciar_alunos(alunos, turmas, disciplinas)
            
        elif opcao == "5":
            gerenciar_notas(alunos, professores, disciplinas)
            
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_turmas(turmas, disciplinas, alunos):
    while True:
        print("\n--- GERENCIAR TURMAS ---")
        print("1. Criar turma")
        print("2. Listar turmas")
        print("3. Adicionar aluno à turma")
        print("4. Adicionar disciplina à turma")
        print("5. Remover aluno da turma")
        print("6. Exibir detalhes da turma")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            nome = input("Digite o nome da turma: ")
            periodo = input("Digite o período da turma: ")
            turma1 = Turma(nome, periodo)
            print(f"Turma {turma1.nome} criada com sucesso!")
            
        elif opcao == "2":
            Turma.listar_turmas()
                
        elif opcao == "3":
            if not turmas or not alunos:
                print("É necessário ter turmas e alunos cadastrados primeiro.")
                continue
                
            listar_turmas(turmas)
            turma_idx = int(input("Número da turma: ")) - 1
            
            listar_alunos(alunos)
            aluno_idx = int(input("Número do aluno: ")) - 1
            
            turmas[turma_idx].adicionar_aluno(alunos[aluno_idx])
            print(f"Aluno {alunos[aluno_idx].nome} adicionado à turma {turmas[turma_idx].nome}")
            
        elif opcao == "4":
            if not turmas or not disciplinas:
                print("É necessário ter turmas e disciplinas cadastradas primeiro.")
                continue
                
            listar_turmas(turmas)
            turma_idx = int(input("Número da turma: ")) - 1
            
            listar_disciplinas(disciplinas)
            disciplina_idx = int(input("Número da disciplina: ")) - 1
            
            turmas[turma_idx].adicionar_disciplina(disciplinas[disciplina_idx])
            print(f"Disciplina {disciplinas[disciplina_idx].nome} adicionada à turma {turmas[turma_idx].nome}")
            
        elif opcao == "5":
            if not turmas:
                print("Não há turmas cadastradas.")
                continue
                
            listar_turmas(turmas)
            turma_idx = int(input("Número da turma: ")) - 1
            
            if not turmas[turma_idx].alunos:
                print("Esta turma não tem alunos.")
                continue
                
            for i, aluno in enumerate(turmas[turma_idx].alunos, 1):
                print(f"{i}. {aluno.nome}")
                
            aluno_idx = int(input("Número do aluno a remover: ")) - 1
            turmas[turma_idx].remover_aluno(turmas[turma_idx].alunos[aluno_idx])
            
        elif opcao == "6":
            if not turmas:
                print("Não há turmas cadastradas.")
                continue
                
            listar_turmas(turmas)
            turma_idx = int(input("Número da turma: ")) - 1
            turmas[turma_idx].exibir()
            
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_disciplinas(disciplinas):
    while True:
        print("\n--- GERENCIAR DISCIPLINAS ---")
        print("1. Criar disciplina")
        print("2. Listar disciplinas")
        print("3. Listar notas de uma disciplina")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            nome = input("Nome da disciplina: ")
            id_disciplina = input("ID da disciplina: ")
            disciplina = Disciplina(nome, id_disciplina)
            disciplinas.append(disciplina)
            print(f"Disciplina {nome} criada com sucesso!")
            
        elif opcao == "2":
            listar_disciplinas(disciplinas)
            
        elif opcao == "3":
            if not disciplinas:
                print("Não há disciplinas cadastradas.")
                continue
                
            listar_disciplinas(disciplinas)
            disciplina_idx = int(input("Número da disciplina: ")) - 1
            disciplinas[disciplina_idx].listar_notas()
            
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_professores(professores, disciplinas):
    while True:
        print("\n--- GERENCIAR PROFESSORES ---")
        print("1. Cadastrar professor")
        print("2. Listar professores")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            if not disciplinas:
                print("É necessário cadastrar disciplinas primeiro.")
                continue
                
            cpf = input("CPF do professor (apenas números): ")
            nome = input("Nome do professor: ")
            
            listar_disciplinas(disciplinas)
            disciplina_idx = int(input("Número da disciplina que o professor leciona: ")) - 1
            
            professor = Professor(cpf, nome, disciplinas[disciplina_idx])
            professores.append(professor)
            print(f"Professor {nome} cadastrado com sucesso!")
            
        elif opcao == "2":
            for i, professor in enumerate(professores, 1):
                print(f"{i}. {professor.nome} - CPF: {professor.cpf} - Disciplina: {professor.disciplina.nome}")
                
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_alunos(alunos, turmas, disciplinas):
    while True:
        print("\n--- GERENCIAR ALUNOS ---")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Matricular aluno em disciplina")
        print("4. Consultar notas do aluno")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            cpf = input("CPF do aluno (apenas números): ")
            nome = input("Nome do aluno: ")
            aluno = Aluno(cpf, nome)
            alunos.append(aluno)
            print(f"Aluno {nome} cadastrado com sucesso!")
            
        elif opcao == "2":
            listar_alunos(alunos)
            
        elif opcao == "3":
            if not alunos or not disciplinas:
                print("É necessário ter alunos e disciplinas cadastrados primeiro.")
                continue
                
            listar_alunos(alunos)
            aluno_idx = int(input("Número do aluno: ")) - 1
            
            listar_disciplinas(disciplinas)
            disciplina_idx = int(input("Número da disciplina: ")) - 1
            
            try:
                alunos[aluno_idx].matricular(disciplinas[disciplina_idx])
                print(f"Aluno {alunos[aluno_idx].nome} matriculado em {disciplinas[disciplina_idx].nome}")
            except Aluno_duplicado_error as e:
                print(f"Erro: {e}")
                
        elif opcao == "4":
            if not alunos:
                print("Não há alunos cadastrados.")
                continue
                
            listar_alunos(alunos)
            aluno_idx = int(input("Número do aluno: ")) - 1
            
            try:
                alunos[aluno_idx].consultar_notas()
            except ValueError as e:
                print(f"Erro: {e}")
                
        else:
            print("Opção inválida. Tente novamente.")

def gerenciar_notas(alunos, professores, disciplinas):
    while True:
        print("\n--- GERENCIAR NOTAS ---")
        print("1. Adicionar nota (professor)")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            break
            
        elif opcao == "1":
            if not professores or not alunos or not disciplinas:
                print("É necessário ter professores, alunos e disciplinas cadastrados primeiro.")
                continue
                
            listar_professores(professores)
            professor_idx = int(input("Número do professor: ")) - 1
            
            listar_alunos(alunos)
            aluno_idx = int(input("Número do aluno: ")) - 1
            
            av1 = float(input("Nota AV1: "))
            av2 = float(input("Nota AV2: "))
            
            try:
                professores[professor_idx].adicionar_nota2(alunos[aluno_idx], disciplinas[professor_idx].disciplina, av1, av2)
                print("Notas adicionadas com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
            except TypeError as e:
                print(f"Erro: {e}")
                
        else:
            print("Opção inválida. Tente novamente.")

def listar_turmas(turmas):
    for i, turma in enumerate(turmas, 1):
        print(f"{i}. {turma.nome} - {turma.periodo}")

def listar_disciplinas(disciplinas):
    for i, disciplina in enumerate(disciplinas, 1):
        print(f"{i}. {disciplina.nome} - ID: {disciplina.id}")

def listar_alunos(alunos):
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno.nome} - CPF: {aluno.cpf}")

def listar_professores(professores):
    for i, professor in enumerate(professores, 1):
        print(f"{i}. {professor.nome} - Disciplina: {professor.disciplina.nome}")

if __name__ == "__main__":
    main()

# Criar aluno 
'''
aluno1 = Aluno("12345678900", "Lucas Silva")
aluno2 = Aluno("12345678901", "Mariana Costa")
aluno3 = Aluno("12345678902", "João Pereira")
aluno4 = Aluno("12345678903", "Ana Souza")
aluno5 = Aluno("12345678904", "Pedro Oliveira")
aluno6 = Aluno("12345678905", "Julia Rocha")
aluno7 = Aluno("12345678906", "Carlos Lima")
aluno8 = Aluno("12345678907", "Beatriz Mendes")
aluno9 = Aluno("12345678908", "Rafael Martins")
aluno10 = Aluno("12345678909", "Fernanda Almeida")


#Criar Disciplina
disciplina1 = Disciplina("Matemática", 101)
disciplina2 = Disciplina("Portugues", 102)
disciplina3 = Disciplina("Geografia", 103)
disciplina4 = Disciplina("Historia", 104)
disciplina5 = Disciplina("Matemática", 105)


#Criar Professor
professor1 = Professor('123456789', 'Julio', disciplina1)
professor2 = Professor('123456788', 'Antonio', disciplina2)
professor3 = Professor('123456787', 'Carlos', disciplina3)
professor4 = Professor('123456786', 'Gabriela', disciplina4)
professor5 = Professor('123456785', 'Marcos', disciplina5)



#Criando a turma e adicionando os alunos e disciplina dela
turma1 = Turma('1 serie', 'Matutino')

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10]
for aluno in lista_alunos:
    turma1.adicionar_aluno(aluno)

lista_disciplinas = [disciplina1, disciplina2, disciplina3, disciplina4, disciplina5]
for disciplina in lista_disciplinas:
    turma1.adicionar_disciplina(disciplina)

turma1.exibir()



# Criar e registrar nota
nota1 = Nota(aluno1, disciplina1, 8.0, 7.0)
nota2 = Nota(aluno1, disciplina2, 7.0, 6.0)
nota3 = Nota(aluno1, disciplina3, 7.0, 6.0)
nota4 = Nota(aluno1, disciplina4, 7.0, 6.0)
nota5 = Nota(aluno1, disciplina5, 7.0, 6.0)

professor1.adicionar_nota1(aluno1, disciplina1, 10, 10)
professor2.adicionar_nota1(aluno1, disciplina2, 7.0, 6.0)
professor3.adicionar_nota1(aluno1, disciplina3, 7.0, 6.0)
professor4.adicionar_nota1(aluno1, disciplina4, 7.0, 6.0)
professor5.adicionar_nota1(aluno1, disciplina5, 7.0, 6.0)

# Consultar as notas do aluno
aluno1.consultar_notas()'''