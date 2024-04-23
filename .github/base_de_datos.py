import unittest
def busqueda_de_datos(*args, **kwargs):
    for llave, valor in kwargs.items():
        encontrado = True
        for x, y in valor.items():
            if y not in args:
                encontrado = False
        if encontrado:
            return llave
    return "La persona no está"

database = {
    "persona1": {
        "primer_nombre": "Martin",
        "segundo_nombre": "Ignacio",
        "primer_apellido": "Tarantoviez",    
    },
    "persona2": {
        "primer_nombre": "Gabriel",
        "segundo_nombre": "",
        "primer_apellido": "Tarantoviez",
    },
    "persona3": {
        "primer_nombre": "Agustin",
        "segundo_nombre": "Damian",
        "primer_apellido": "Blandini",
    },
    "persona4": {
        "primer_nombre": "Nehuen",
        "segundo_nombre": "",
        "primer_apellido": "Donozo",
    },
    "persona5": {
        "primer_nombre": "Franco",
        "segundo_nombre": "",
        "primer_apellido": "Quiroga",
    },
    "persona6": {
        "primer_nombre": "Tomas",
        "segundo_nombre": "",
        "primer_apellido": "Liza",
    },
    "persona7": {
        "primer_nombre": "Diego",
        "segundo_nombre": "",
        "primer_apellido": "Xuhuang",
    }
}


class TestKwargs(unittest.TestCase):
    def test_persona1(self):
        resultado = busqueda_de_datos("Martin", "Ignacio", "Tarantoviez", **database)
        self.assertEqual(resultado, "persona1")    

    def test_persona2(self):
        resultado = busqueda_de_datos("Gabriel", "", "Tarantoviez", **database)
        self.assertEqual(resultado, "persona2")
        
    def test_persona3(self):
        resultado = busqueda_de_datos("Agustin", "Damian", "Blandini", **database)
        self.assertEqual(resultado, "persona3")
        
    def test_persona4(self):
        resultado = busqueda_de_datos("Nehuen", "", "Donozo", **database)
        self.assertEqual(resultado, "persona4")
        
    def test_persona5(self):
        resultado = busqueda_de_datos("Franco", "", "Quiroga", **database)
        self.assertEqual(resultado, "persona5")
        
    def test_persona6(self):
        resultado = busqueda_de_datos("Tomas", "", "Liza", **database)
        self.assertEqual(resultado, "persona6")
        
    def test_persona7(self):
        resultado = busqueda_de_datos("Diego", "", "Xuhuang", **database)
        self.assertEqual(resultado, "persona7")
        
    def test_no_existe_la_persona_1(self):
        resultado = busqueda_de_datos("Julio", "Argenino", "Roca", **database)
        self.assertEqual(resultado, "La persona no está")

    def test_no_existe_la_persona_2(self):
        resultado = busqueda_de_datos("Juan", "Domingo", "Peron", **database)
        self.assertEqual(resultado, "La persona no está")

unittest.main()