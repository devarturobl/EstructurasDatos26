import streamlit as st

# crear un direcorio de productos de una tienda de abarrotes
#Paso 1 crear la el arreglo de productos
productos = [
  {
    "codigo": "ART-001",
    "nombre": "Coca-Cola Original 600 ml",
    "precio": 18.00,
    "descripcion": "Refresco de cola en botella no retornable de 600 ml.",
    "stock": 48
  },
  {
    "codigo": "ART-002",
    "nombre": "Sabritas Sal 45 g",
    "precio": 19.50,
    "descripcion": "Papas fritas clásicas con sal de grano.",
    "stock": 35
  },
  {
    "codigo": "ART-003",
    "nombre": "Doritos Nacho 58 g",
    "precio": 19.50,
    "descripcion": "Totopos de maíz nixtamalizado con sabor a queso y chile.",
    "stock": 40
  },
  {
    "codigo": "ART-004",
    "nombre": "Leche Entera Lala 1 L",
    "precio": 27.50,
    "descripcion": "Leche ultrapasteurizada adicionada con vitaminas A y D.",
    "stock": 24
  },
  {
    "codigo": "ART-005",
    "nombre": "Pan Blanco Bimbo Grande 680 g",
    "precio": 48.00,
    "descripcion": "Pan de caja clásico fortificado con vitaminas y minerales.",
    "stock": 15
  },
  {
    "codigo": "ART-006",
    "nombre": "Huevo Blanco San Juan (1 kg)",
    "precio": 46.00,
    "descripcion": "Paquete con aproximadamente 16 piezas de huevo blanco fresco.",
    "stock": 20
  },
  {
    "codigo": "ART-007",
    "nombre": "Agua Purificada Bonafont 1 L",
    "precio": 14.00,
    "descripcion": "Agua ligera natural en botella de plástico.",
    "stock": 30
  },
  {
    "codigo": "ART-008",
    "nombre": "Galletas Chokis 76 g",
    "precio": 18.00,
    "descripcion": "Galletas con chispas de chocolate horneadas.",
    "stock": 25
  },
  {
    "codigo": "ART-009",
    "nombre": "Galletas Marías Gamesa 170 g",
    "precio": 17.50,
    "descripcion": "Galletas clásicas dulces sabor vainilla.",
    "stock": 30
  },
  {
    "codigo": "ART-010",
    "nombre": "Frijoles Negros Refritos Isadora 430 g",
    "precio": 21.00,
    "descripcion": "Bolsa de frijoles refritos listos para calentar y servir.",
    "stock": 18
  },
  {
    "codigo": "ART-011",
    "nombre": "Atún en Agua Dolores 140 g",
    "precio": 22.00,
    "descripcion": "Lata de lomo de atún aleta amarilla en agua.",
    "stock": 45
  },
  {
    "codigo": "ART-012",
    "nombre": "Aceite Vegetal 1-2-3 1 L",
    "precio": 42.00,
    "descripcion": "Aceite comestible puro de soya y canola.",
    "stock": 16
  },
  {
    "codigo": "ART-013",
    "nombre": "Café Soluble Nescafé Clásico 120 g",
    "precio": 74.00,
    "descripcion": "Café soluble soluble instantáneo en frasco de vidrio.",
    "stock": 12
  },
  {
    "codigo": "ART-014",
    "nombre": "Azúcar Estándar Zulka (1 kg)",
    "precio": 32.00,
    "descripcion": "Azúcar morena refinada para uso doméstico.",
    "stock": 22
  },
  {
    "codigo": "ART-015",
    "nombre": "Sal Marina La Fina 1 kg",
    "precio": 16.50,
    "descripcion": "Sal yodada y fluorurada en bolsa.",
    "stock": 28
  },
  {
    "codigo": "ART-016",
    "nombre": "Sopa de Pasta Fideo La Moderna 200 g",
    "precio": 9.50,
    "descripcion": "Pasta de sémola de trigo para sopa aguada de fideo.",
    "stock": 50
  },
  {
    "codigo": "ART-017",
    "nombre": "Puré de Tomate Del Fuerte 210 g",
    "precio": 10.00,
    "descripcion": "Puré de tomate sazonado en tetra pack.",
    "stock": 40
  },
  {
    "codigo": "ART-018",
    "nombre": "Mayonesa Hellmann's con Limón 390 g",
    "precio": 43.00,
    "descripcion": "Aderezo cremoso de mayonesa con toque de jugo de limón.",
    "stock": 14
  },
  {
    "codigo": "ART-019",
    "nombre": "Salsa Picante Valentina Amarilla 370 ml",
    "precio": 15.00,
    "descripcion": "Salsa picante de mesa tradicional para botanas.",
    "stock": 26
  },
  {
    "codigo": "ART-020",
    "nombre": "Chiles Jalapeños en Escabeche La Costeña 220 g",
    "precio": 16.50,
    "descripcion": "Rajas de chile jalapeño con zanahoria y cebolla.",
    "stock": 32
  },
  {
    "codigo": "ART-021",
    "nombre": "Arroz Blanco Verde Valle 900 g",
    "precio": 31.00,
    "descripcion": "Arroz súper grano largo seleccionado.",
    "stock": 20
  },
  {
    "codigo": "ART-022",
    "nombre": "Papel Higiénico Pétalo Rendimax 4 rollos",
    "precio": 36.00,
    "descripcion": "Paquete de papel higiénico con 320 hojas dobles por rollo.",
    "stock": 18
  },
  {
    "codigo": "ART-023",
    "nombre": "Jabón de Lavandería Zote Blanco 400 g",
    "precio": 23.00,
    "descripcion": "Barra tradicional de jabón multiusos para ropa delicada.",
    "stock": 35
  },
  {
    "codigo": "ART-024",
    "nombre": "Detergente en Polvo Ariel 1 kg",
    "precio": 46.00,
    "descripcion": "Detergente multiusos con fórmula removedora de manchas.",
    "stock": 22
  },
  {
    "codigo": "ART-025",
    "nombre": "Limpiador Fabuloso Lavanda 1 L",
    "precio": 26.00,
    "descripcion": "Limpiador líquido aromatizante antibacterial para pisos.",
    "stock": 19
  },
  {
    "codigo": "ART-026",
    "nombre": "Cloro Cloralex El Rendidor 950 ml",
    "precio": 19.00,
    "descripcion": "Blanqueador y desinfectante multiusos de uso doméstico.",
    "stock": 24
  },
  {
    "codigo": "ART-027",
    "nombre": "Lavavajillas Líquido Axion Limón 750 ml",
    "precio": 38.00,
    "descripcion": "Jabón líquido arranca grasa concentrado para trastes.",
    "stock": 15
  },
  {
    "codigo": "ART-028",
    "nombre": "Jabón de Tocador Palmolive Clásico 100 g",
    "precio": 16.00,
    "descripcion": "Jabón corporal en barra con extracto de oliva y aloe.",
    "stock": 42
  },
  {
    "codigo": "ART-029",
    "nombre": "Pasta Dental Colgate Triple Acción 75 ml",
    "precio": 24.50,
    "descripcion": "Crema dental con protección anticaries, blancura y aliento fresco.",
    "stock": 28
  },
  {
    "codigo": "ART-030",
    "nombre": "Shampoo Head & Shoulders Limpieza Renovadora 375 ml",
    "precio": 68.00,
    "descripcion": "Shampoo anticaspa de uso diario.",
    "stock": 10
  },
  {
    "codigo": "ART-031",
    "nombre": "Gansito Marinela 50 g",
    "precio": 17.00,
    "descripcion": "Pastelito relleno de crema y mermelada cubierto de chocolate.",
    "stock": 30
  },
  {
    "codigo": "ART-032",
    "nombre": "Bitoque / Donas Bimbo 105 g",
    "precio": 22.00,
    "descripcion": "Paquete con 4 donas espolvoreadas con azúcar glass.",
    "stock": 16
  },
  {
    "codigo": "ART-033",
    "nombre": "Mantecadas Bimbo 125 g",
    "precio": 24.00,
    "descripcion": "Pan dulce tipo muffin sabor vainilla con 4 piezas.",
    "stock": 18
  },
  {
    "codigo": "ART-034",
    "nombre": "Chicles Trident Menta 4s",
    "precio": 5.00,
    "descripcion": "Tira con 4 gomas de mascar sabor menta sin azúcar.",
    "stock": 60
  },
  {
    "codigo": "ART-035",
    "nombre": "Paleta Tutsi Pop 20 g",
    "precio": 6.50,
    "descripcion": "Paleta dura de caramelo sabor cereza con centro de chicle.",
    "stock": 75
  },
  {
    "codigo": "ART-036",
    "nombre": "Mazapán De la Rosa 28 g",
    "precio": 6.00,
    "descripcion": "Dulce típico de cacahuate tostado y azúcar molida.",
    "stock": 80
  },
  {
    "codigo": "ART-037",
    "nombre": "Chocolate Carlos V 18 g",
    "precio": 11.00,
    "descripcion": "Barra pequeña de chocolate con leche estilo suizo.",
    "stock": 45
  },
  {
    "codigo": "ART-038",
    "nombre": "Cerveza Corona Extra 355 ml",
    "precio": 22.00,
    "descripcion": "Cerveza clara tipo pilsner en botella de vidrio no retornable.",
    "stock": 48
  },
  {
    "codigo": "ART-039",
    "nombre": "Bebida Hidratante Electrolit Fresa 625 ml",
    "precio": 32.00,
    "descripcion": "Solución rehidratante oral con electrólitos sabor fresa.",
    "stock": 20
  },
  {
    "codigo": "ART-040",
    "nombre": "Jugo Del Valle Manzana 413 ml",
    "precio": 16.00,
    "descripcion": "Néctar elaborado con concentrado de jugo de manzana.",
    "stock": 25
  },
  {
    "codigo": "ART-041",
    "nombre": "Yogurt para Beber Danone Fresa 220 g",
    "precio": 14.50,
    "descripcion": "Yogurt bebible endulzado con trozos de fresa.",
    "stock": 22
  },
  {
    "codigo": "ART-042",
    "nombre": "Jamón de Pavo Fud Virginia 250 g",
    "precio": 38.00,
    "descripcion": "Rebanadas delgadas de jamón de pavo cocido empacadas al alto vacío.",
    "stock": 14
  },
  {
    "codigo": "ART-043",
    "nombre": "Salchicha de Pavo San Rafael 500 g",
    "precio": 45.00,
    "descripcion": "Paquete de salchichas tipo viena de carne de pavo.",
    "stock": 12
  },
  {
    "codigo": "ART-044",
    "nombre": "Queso Panela NocheBuena 400 g",
    "precio": 62.00,
    "descripcion": "Queso fresco de vaca pasteurizado en empaque individual.",
    "stock": 9
  },
  {
    "codigo": "ART-045",
    "nombre": "Mantequilla con Sal Gloria 90 g",
    "precio": 21.00,
    "descripcion": "Barra de mantequilla de grasa de leche de vaca.",
    "stock": 18
  },
  {
    "codigo": "ART-046",
    "nombre": "Encendedor Bic Clásico Maxi",
    "precio": 20.00,
    "descripcion": "Encendedor de gas butano desechable con seguro infantil.",
    "stock": 35
  },
  {
    "codigo": "ART-047",
    "nombre": "Fósforos La Central Clásicos 50 piezas",
    "precio": 4.00,
    "descripcion": "Caja pequeña de cerillos de madera encerada.",
    "stock": 50
  },
  {
    "codigo": "ART-048",
    "nombre": "Pilas Alcalinas Duracell AA 2 piezas",
    "precio": 48.00,
    "descripcion": "Blíster con 2 pilas cilíndricas tamaño AA de larga duración.",
    "stock": 16
  },
  {
    "codigo": "ART-049",
    "nombre": "Servilletas Pétalo 100 piezas",
    "precio": 18.50,
    "descripcion": "Paquete de servilletas de papel absorbente cuadradas.",
    "stock": 26
  },
  {
    "codigo": "ART-050",
    "nombre": "Alimento para Perro Pedigree Adulto 1 kg",
    "precio": 52.00,
    "descripcion": "Croquetas balanceadas sabor res y vegetales para perro adulto.",
    "stock": 11
  }
]


st.title("Directorio de Productos de Abarrotes")
st.header("Sistema de Búsqueda de Productos")

idpro = st.text_input("Ingrese el código del producto:")

def buscar_producto(codigo):
    ban = 0
    for producto in productos:
        if producto["codigo"] == idpro:
            st.text(f"Producto encontrado: {producto['nombre']}")
            st.text(f"Precio de: {producto['precio']}")
            st.text(f"Descripción: {producto['descripcion']}")
            ban = 1
            break

    if ban == 0:
        st.write("Producto no encontrado")

st.button("Buscar", on_click=buscar_producto, args=(idpro,))