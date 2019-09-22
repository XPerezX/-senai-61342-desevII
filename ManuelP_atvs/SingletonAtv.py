class call:

    @staticmethod
    def class_name(name):
        if name == "professor":
            return professor()



class professor():

    __instance = None


    __caderneta = {

    }


    def set_alunos(self, id, nome, nota):

        self.__caderneta[id] = [nome,nota]



    def get_alunos(self):
        return self.__caderneta


    def get_alunos(self):
        return self.__caderneta



    @staticmethod
    def instance():
        if not professor.__instance:
            professor.__instance = professor()
        return professor.__instance

aluno1 = call.class_name("professor").instance()
aluno1.set_alunos(1,"carlos",2)
print(aluno1.get_alunos())

aluno2 = professor.instance()
aluno2.set_alunos(2,"joseph",10)
print(aluno2.get_alunos())










