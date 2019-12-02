import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class Eventos:
    def on_entdni_focus_out_event(self, widget, Data = None):
        #De momento nada
    def on_vPrincipal_destroy(self, widget, Data = None):
        Gtk.main_quit()

class Dni:
    def __init__(self):  #iniciamos libreria
        self.b = Gtk.Builder()
        self.b.add_from_file('ventana.glade')
        #vamos cargando los widgets a utilizar en los eventos
        self.ventana = self.b.get_object('vPrincipal')
        self.b.connect_signals(Eventos())
        #Conectamos y mostramos
        self.ventana.show()

    if __name__ == '__main__':
        dni = Dni()
        Gtk.main()