Considere os seguintes esquemas de relação:
- Professor (prof-numero, prof-nome, prof-rua, prof-cidade, prof-telefone)
- Aluno (alu-numero, alu-nome, alu-rua, alu-cidade)
- Disciplina (disc-codigo,disc-nome,disc-quant-aulas-semana)
- Matricula(alu-numero,disc-codigo, ano, semestre, nota, frequencia)
- ProfessorDisciplina (prof-numero, disc-codigo)

<b>Os nomes de todos os alunos que têm aula com o professor Marcos.</b>

    Πalu_nome(σ(Matricula.alu_numero=Aluno.alu_num(AlunoX(σ(Professor.prof_nome="Marcos"(MatriculaX(σ(ProfessorDisciplina.prof_numero = Professor.prof_numero(ProfessorDisciplinaXProfessor)))))))))

<b>Os números dos professores que dão aula da disciplina que tem código 48.</b>

    Πprof_numero(σ(Disciplina.cod_disc =48 (ProfessorXDisciplina)))

<b>Os nomes de todos os professores que ministram disciplina chamada “Bancos de Dados”.</b>

    Πprof_nome(σ(Disciplina.disc_nome ="Banco de Dados" (ProfessorXDisciplina)))

<b>O código da disciplina de “Matemática Básica”.</b>

    Πdisc_codigo(σ(Disciplina.disc_nome ="Matemática Básica" (Disciplina)))

<b>A rua do professor “Marcos Santos”</b>

    Πprof_rua(σ(Professor.prof_nome ="Marcos Santos" (Professor)))

<b>Os números dos professores que dão aula da disciplina que tem código MAT101.</b>

    Π(prof_numero)σ(disc_codigo="MAT101")(σ(ProfessorDisciplina.prof_numero =Professor.prof_numero)(ProfessorDisciplinaXprofessor))

<b>O nome e o número dos professores que dão aula da disciplina que tem código MAT101.</b>

    Π(prof_numero,prof_nome)σ(disc_codigo="MAT101")(σ(ProfessorDisciplina.prof_numero =Professor.prof_numero)(ProfessorDisciplinaXProfessor))

<b>Os nomes de todos os professores que ministram disciplina chamada “Física Aplicada”.</b>

    Π(prof_nome)(σ(disc_nome="Física Aplicada"))(σ(ProfessorDisciplina.disc_codigo =Disciplina.disc_codigo))(DisciplinaX(σ(ProfessorDisciplina.prof_numero =Professor.prof_numero)(ProfessorDisciplinaXProfessor)))

<b>Os nomes de todos os alunos que cursam a disciplina que tem código MAT101.</b>

    Π(alu_nome)(σ(disc_cod="MAT101"))((σ(Aluno.alu_num= Matricula.alu_num))(AlunoXMatricula))

<b>Os nomes de todos os alunos que cursam a disciplina que tem nome “Matemática Básica”.</b>

    Π(alu_nome)(σ(disc_nome="Matemática Básica"))(σ(Matricula.disc_cod=Disciplina.disc_cod ))(DisciplinaX(σ(Aluno.alu_num= Matricula.alu_num))(AlunoXMatricula))

<b>Os nomes de todos os alunos que têm aula com o professor “João Silva”.</b>

    Resultado ← (σ(ProfessorDisciplina.disc_codigo= Matricula.disc_codigo))(ProfessorDisciplina X Π(Aluno.alu_numero,nome_aluno,Matricula.disc_codigo)(σ(Aluno.alu_num= Matricula.alu_num))(AlunoXMatricula))

    Π(alu_nome)(σ(prof_nome="João Silva))(σ(ProfessorDisciplina.professor_numero=Professor.professor_numero))(ProfessorXResultado)

<b>Os nomes de todos os alunos que têm aula com o professor “Marcos Santos”.</b>

    Resultado ← (σ(ProfessorDisciplina.disc_codigo= Matricula.disc_codigo))(ProfessorDisciplina X Π(Aluno.alu_numero,nome_aluno,Matricula.disc_codigo)(σ(Aluno.alu_num= Matricula.alu_num))(AlunoXMatricula))

    Π(alu_nome)(σ(prof_nome="Marcos Santos"))(σ(ProfessorDisciplina.professor_numero=Professor.professor_numero))(ProfessorXResultado)

<h3>Operação Adicionais</h3>
<b>Os nomes de todos os alunos que tiraram nota maior que o aluno “Ana Silva” na disciplina FIS202.</b>

    ρ(nota-ana)(Π(nota)σ(alu-nome="Ana Silva" ∧ disc-codigo="FIS202" )(Aluno |x| Matricula))
    ρ(alunos)(σ(alu-nome !="Ana Silva" ∧disc-codigo="FIS202" )(Aluno |x| Matricula))
    Π(nome)σ(alunos.nota>nota-ana.nota)(nota-ana X alunos)

