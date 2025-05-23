from modelos.aluno import Aluno
from modelos.professor import Professor
from modelos.disciplina import Disciplina
from modelos.nota import Nota
from modelos.turma import Turma


alunos = []
professores = []
disciplinas = []
turmas = []
notas = []

def menu():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Aluno")
        print("2. Professor")
        print("3. Disciplina")
        print("4. Turma")
        print("5. Notas")
        print("0. Sair")
        op = input("Escolha: ")

        if op == '1':
            menu_aluno()
        elif op == '2':
            menu_professor()
        elif op == '3':
            menu_disciplina()
        elif op == '4':
            menu_turma()
        elif op == '5':
            menu_nota()
        elif op == '0':
            break
        else:
            print("Opção inválida")


# ---------------- ALUNO ---------------- #
def menu_aluno():
    while True:
        print("\n--- Menu Aluno ---")
        print("1. Cadastrar (e adicionar na turma)")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            aluno = Aluno(cpf, nome)

            if not turmas:
                print("Nenhuma turma cadastrada. Crie uma primeiro.")
            else:
                print("Escolha a turma para o aluno:")
                for i, t in enumerate(turmas):
                    print(f"{i} - {t.nome} | Período: {t.periodo}")
                idx = int(input("Turma: "))
                turma = turmas[idx]
                turma.adicionar_aluno(aluno)

            alunos.append(aluno)
            print(f"Aluno {aluno.nome} cadastrado e adicionado na turma {turma.nome}.")

        elif op == '2':
            for i, aluno in enumerate(alunos):
                print(f"{i} - {aluno.nome} | CPF: {aluno.cpf}")

        elif op == '3':
            idx = int(input("Escolha índice do aluno: "))
            aluno = alunos[idx]
            aluno.nome = input(f"Novo nome ({aluno.nome}): ") or aluno.nome
            print("Aluno editado.")

        elif op == '4':
            idx = int(input("Escolha índice do aluno: "))
            excluido = alunos.pop(idx)
            print(f"Aluno {excluido.nome} excluído.")

        elif op == '0':
            break


# ---------------- PROFESSOR ---------------- #
def menu_professor():
    while True:
        print("\n--- Menu Professor ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")

            if not disciplinas:
                print("Cadastre uma disciplina primeiro.")
                continue

            for i, disc in enumerate(disciplinas):
                print(f"{i} - {disc.nome}")
            idx = int(input("Escolha disciplina: "))
            professor = Professor(cpf, nome, disciplinas[idx])
            professores.append(professor)
            print("Professor cadastrado.")

        elif op == '2':
            for i, prof in enumerate(professores):
                print(f"{i} - {prof.nome} | CPF: {prof.cpf} | Disciplina: {prof.disciplina.nome}")

        elif op == '3':
            idx = int(input("Escolha índice do professor: "))
            prof = professores[idx]
            prof.nome = input(f"Novo nome ({prof.nome}): ") or prof.nome
            print("Professor editado.")

        elif op == '4':
            idx = int(input("Escolha índice do professor: "))
            excluido = professores.pop(idx)
            print(f"Professor {excluido.nome} excluído.")

        elif op == '0':
            break


# ---------------- DISCIPLINA ---------------- #
def menu_disciplina():
    while True:
        print("\n--- Menu Disciplina ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == '1':
            nome = input("Nome da disciplina: ")
            id = len(disciplinas) + 1
            disciplina = Disciplina(nome, id)
            disciplinas.append(disciplina)
            print("Disciplina cadastrada.")

        elif op == '2':
            for i, disc in enumerate(disciplinas):
                print(f"{i} - {disc.nome} | ID: {disc.id}")

        elif op == '3':
            idx = int(input("Escolha índice da disciplina: "))
            disc = disciplinas[idx]
            disc.nome = input(f"Novo nome ({disc.nome}): ") or disc.nome
            print("Disciplina editada.")

        elif op == '4':
            idx = int(input("Escolha índice da disciplina: "))
            excluido = disciplinas.pop(idx)
            print(f"Disciplina {excluido.nome} excluída.")

        elif op == '0':
            break


# ---------------- TURMA ---------------- #
def menu_turma():
    while True:
        print("\n--- Menu Turma ---")
        print("1. Cadastrar (e adicionar disciplinas)")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == '1':
            nome = input("Nome da turma: ")
            periodo = input("Período: ")
            turma = Turma(nome, len(turmas)+1, periodo)

            if not disciplinas:
                print("Nenhuma disciplina cadastrada. Cadastre uma primeiro.")
            else:
                print("Selecione as disciplinas da turma (separe por vírgula):")
                for i, disc in enumerate(disciplinas):
                    print(f"{i} - {disc.nome}")
                indices = input("Escolhas (ex: 0,1,2): ").split(',')
                for idx in indices:
                    try:
                        turma.adicionar_disciplina(disciplinas[int(idx.strip())])
                    except:
                        print(f"Índice inválido: {idx}")

            turmas.append(turma)
            print(f"Turma {turma.nome} cadastrada com sucesso.")

        elif op == '2':
            for i, turma in enumerate(turmas):
                print(f"{i} - {turma.nome} | Período: {turma.periodo}")
                turma.exibir()

        elif op == '3':
            idx = int(input("Escolha índice da turma: "))
            turma = turmas[idx]
            turma.nome = input(f"Novo nome ({turma.nome}): ") or turma.nome
            turma.periodo = input(f"Novo período ({turma.periodo}): ") or turma.periodo
            print("Turma editada.")

        elif op == '4':
            idx = int(input("Escolha índice da turma: "))
            excluido = turmas.pop(idx)
            print(f"Turma {excluido.nome} excluída.")

        elif op == '0':
            break


# ---------------- NOTA ---------------- #
def menu_nota():
    while True:
        print("\n--- Menu Notas ---")
        print("1. Lançar Nota")
        print("2. Consultar Notas de Aluno")
        print("3. Consultar Notas de Disciplina")
        print("0. Voltar")
        op = input("Escolha: ")

        if op == '1':
            if not professores or not alunos:
                print("Cadastre professor e aluno primeiro.")
                continue

            for i, prof in enumerate(professores):
                print(f"{i} - {prof.nome} | Disciplina: {prof.disciplina.nome}")
            idx_prof = int(input("Escolha professor: "))
            professor = professores[idx_prof]

            for i, aluno in enumerate(alunos):
                print(f"{i} - {aluno.nome}")
            idx_aluno = int(input("Escolha aluno: "))
            aluno = alunos[idx_aluno]

            av1 = float(input("Nota AV1: "))
            av2 = float(input("Nota AV2: "))
            professor.adicionar_nota2(aluno, professor.disciplina, av1, av2)
            print("Nota lançada.")

        elif op == '2':
            for i, aluno in enumerate(alunos):
                print(f"{i} - {aluno.nome}")
            idx = int(input("Escolha aluno: "))
            aluno = alunos[idx]
            try:
                aluno.consultar_notas()
            except ValueError as e:
                print(e)

        elif op == '3':
            for i, disc in enumerate(disciplinas):
                print(f"{i} - {disc.nome}")
            idx = int(input("Escolha disciplina: "))
            disciplina = disciplinas[idx]
            disciplina.listar_notas()

        elif op == '0':
            break


if __name__ == "__main__":
    menu()

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