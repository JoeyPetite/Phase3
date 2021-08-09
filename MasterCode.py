from multiprocessing import Process

def one(): import Camera
def two(): import Phase3Final

Process.daemon=True

Process(target=one).start()
Process(target=two).start()
