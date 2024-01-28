import psutil

class Resfresh_Port():
    def __init__(self, name="HD-Player.exe"):
        self.name = name

    def ResfreshPort(self):
        bluestacks_processes = []
        for process in psutil.process_iter():
            if process.name() == self.name:
                bluestacks_processes.append(process)

        ports_in_use = set() 
        print(bluestacks_processes)
        for process in bluestacks_processes:
            for connection in process.connections():
                if connection.status == psutil.CONN_LISTEN and connection.laddr.port != 0 and connection.laddr.port !=2222:
                    ports_in_use.add(connection.laddr.port)

        if len(ports_in_use) == 0:
            return [0]
        else:
            return ports_in_use