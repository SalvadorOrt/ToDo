class Tarea():
    def __init__(self,descripcion = None):
        self.descr = descripcion
    def listarTarea(self):
        query = '''
                   SELECT ID,Descripción,
                    CASE 
                        WHEN Estado = 1 THEN 'Completado'
                        WHEN Estado = 0 THEN 'Pendiente'
                    
                    END AS Estado
                FROM Tareas;
                '''
        return query
    def insertarTarea(self):
        query = '''
                insert into Tareas(Descripción) values(?)
                '''
        datos = (self.descr,)
        return (query,datos)
    def obternerTarea_ID(self,id):
        query = '''
                select ID,Descripción
                from Tareas
                where ID = ?
                '''
        datos = (id,)
        return (query,datos)
    def actualizarTarea(self,id,descripcion):
        query = '''
                update Tareas set Descripción  = ? where  ID = ?
                '''
        datos = (descripcion,id)
        return (query,datos)
    def eliminarTarea(self,id):
        query = '''
                delete Tareas where ID = ?
                '''
        datos = (id,)
        return (query,datos)
    def completarTarea(self,id):
        query = '''
                update Tareas set Estado  = 1 where  ID = ?
                '''
        datos = (id,)
        return (query,datos)