class Programador:
    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Estagio(Programador):
    def mostrar_tarefas(self):
        print('Tenta fazer alguma coisa estagiaria!')

    def busca_tickets_do_dia(self, dia=None):
        print(f'Mostrando tickets - {dia}' if dia else 'Mostrando os tickets de hoje')


class DevJunior(Programador):
    def mostrar_tarefas(self):
        print('Fez muita coisa hoje DevJunior!')

    def busca_tickets_resolvidos(self):
        print('Mostrando tickets resolvidos')

class DevPleno(Programador):
    def mostrar_tarefas(self):
        print('Ja resolveu muito b.o!')

    def mandar_tickets_para_devs(self):
        print('Enviando tickets para a equipe')


class Junior(Estagio):
    pass

class Senior(DevJunior, DevPleno):
    pass


aline = Junior()
aline.mostrar_tarefas()
aline.busca_tickets_do_dia()
aline.registra_horas(12)

glaucia = Senior()
glaucia.busca_tickets_resolvidos()
glaucia.registra_horas(16)
glaucia.mandar_tickets_para_devs()
glaucia.mostrar_tarefas()


