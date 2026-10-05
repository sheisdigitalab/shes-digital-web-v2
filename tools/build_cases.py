"""Genera las páginas de proyecto (proyectos/<slug>/index.html) desde una plantilla común.

Uso:  python tools/build_cases.py
Los textos de cada proyecto están en CASES; las imágenes, en assets/img/cases/<slug>/.
"""
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

ARROW = '<span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>'
ARROW_OUT = '<span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></svg></span>'
WA_ICON = ('<span class="btn__wa" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg></span>')

CASES = [
    {
        'slug': 'martilota', 'name': 'Martilota', 'cover': 'martilota.webp',
        'sector': 'Restauración', 'place': 'Alcalá de Henares', 'client': 'Restaurante Martilota',
        'did': 'Diseño web · Desarrollo · SEO local', 'status': 'Prototipo web',
        'url': 'https://jenn-jt.github.io/martilota/', 'url_label': 'Ver el prototipo',
        'cover_alt': 'Portada de la web de Martilota: terraza ajardinada con el titular «La experiencia Martilota, llega a tu mesa»',
        'lead': 'Una experiencia única, también en la web. Cinco espacios, cocina mediterránea de raíz y un restaurante con historia desde 2014: el reto era que la web lo transmitiera antes de que el cliente cruzara la puerta.',
        'facts': [('5', 'espacios con personalidad propia'), ('2014', 'cocinando en Alcalá de Henares'), ('0 €', 'de comisión por reserva: directa por WhatsApp')],
        'reto_h': ('Una experiencia', 'excelente en la mesa.'),
        'reto_statement': 'Martilota no es un restaurante cualquiera: son cinco espacios, cada uno para un plan distinto, bajo la misma cocina mediterránea de producto. Su web anterior no transmitía nada de eso.',
        'reto_text': 'Era visualmente plana, costaba navegarla y no tenía llamadas a la acción claras. Quien llegaba no sabía qué espacio reservar ni si encajaba con su ocasión. La experiencia en la mesa era excelente; la digital, olvidable. El objetivo: una web que venda la experiencia antes de la reserva.',
        'steps': ['La emoción primero: la terraza y la reserva a un clic.', 'Cinco escenarios para elegir dónde sentarse.', 'La carta, clara y fácil de actualizar.', 'Coffee, Alcalá y el cierre con la reserva.'],
        'sol_h': ('Seis decisiones', 'que llenan mesas.'),
        'points': [
            ('Identidad de restaurante premium', 'Serif elegante, paleta cálida de tierra y crema y fotografía de ambiente. Un aspecto que posiciona sin excluir.'),
            ('Los cinco espacios, protagonistas', 'Cada uno con su nombre, su carácter y su mejor momento. El cliente llega sabiendo dónde quiere sentarse.'),
            ('Una carta viva', 'Carta, menú del día, desayunos, postres, vinos y coctelería por categorías, fácil de actualizar desde WordPress.'),
            ('Reserva directa', 'WhatsApp integrado y un botón de reserva siempre a mano. Sin plataformas que se lleven comisión.'),
            ('SEO local en Alcalá', 'Estructura pensada para búsquedas como «restaurante en Alcalá de Henares», con datos estructurados de restaurante.'),
            ('Coffee, con voz propia', 'Desayunos, café de especialidad y meriendas en una sección aparte para captar al público de día.'),
        ],
        'wide': ('espacios.webp', 1440, 2800, 'Sección «Cinco escenarios, una misma pasión» con la Terraza Mirador, el Restaurante, La Chimenea y La Barra', 'Los cinco espacios, cada uno con su foto, su carácter y para qué plan encaja.'),
        'design_h': ('Huele a mediterráneo', 'antes del scroll.'),
        'fonts': [("'Cormorant Infant', Georgia, serif", 'italic', 400, 'Cormorant Infant', 'Titulares: elegancia y ritmo'),
                  ("'Libre Franklin', Arial, sans-serif", 'normal', 400, 'Libre Franklin', 'Texto: claridad para informar')],
        'gfonts': 'family=Cormorant+Infant:ital,wght@0,400;1,400&family=Libre+Franklin:wght@400;500',
        'palette': [('Carbón', '#1A1A1A'), ('Terracota', '#CB6037'), ('Oro', '#D6B46A'), ('Rubor', '#E5C3B8'), ('Mantel', '#FFFFFF')],
        'design_text': 'El recorrido sigue a quien está decidiendo si reservar: primero la emoción de la terraza, después la historia de la casa, los cinco espacios para elegir el suyo, la carta para confirmar que la cocina está a la altura y, al final, la reserva. Un embudo de conversión disfrazado de experiencia.',
        'duo': [('carta.webp', 1440, 1075, 'Sección de la carta sobre fondo oscuro con plato de pulpo y categorías del menú', 'La carta, sobre fondo oscuro para que mande la comida.'),
                ('coffee.webp', 1440, 1050, 'Sección Martilota Coffee con taza de café sobre granos', 'Martilota Coffee, la línea de mañana con identidad propia.')],
        'phones_h': ('Pensada para', 'reservar desde la calle.'),
        'phones_alt': ['portada con botones Reservar mesa y Ver la carta', 'sección Cinco escenarios con la Terraza Mirador', 'sección de la carta en fondo oscuro', 'sección Martilota Coffee'],
        'cta': '¿Tu negocio merece una web así?',
    },
    {
        'slug': 'alma-salinas', 'name': 'Alma Salinas', 'cover': 'alma-salinas.webp',
        'sector': 'Belleza', 'place': 'Valencia', 'client': 'Salón ficticio para la demo',
        'did': 'Diseño web · Desarrollo · SEO local', 'status': 'Proyecto demo',
        'url': 'https://sheisdigitalab.github.io/alma-salinas-web/', 'url_label': 'Ver la demo',
        'cover_alt': 'Portada de la web de Alma Salinas: interior del salón en blanco y negro con el titular «Belleza con carácter propio»',
        'lead': 'Un salón con personalidad, visible en el mundo digital. Una web demo para peluquerías y centros de belleza: cálida, editorial y pensada para que pedir cita cueste lo mismo que mandar un WhatsApp.',
        'facts': [('1 clic', 'para pedir cita por WhatsApp'), ('4', 'áreas de servicio claras de un vistazo'), ('1 página', 'rápida y ligera, también en el móvil')],
        'reto_h': ('Del Instagram', 'a la agenda llena.'),
        'reto_statement': 'Muchas peluquerías tienen clientas fieles, trabajo cuidado y buenas reseñas, pero en internet se quedan en un perfil de Instagram y una ficha de Google.',
        'reto_text': 'Instagram enseña el trabajo, pero no convierte: no hay horario a la vista, ni lista de servicios, ni una forma rápida de pedir cita. Quien busca «peluquería cerca de mí» encuentra el salón en el mapa, pero no tiene dónde confirmar que es lo que busca. El objetivo de la demo: transmitir el cuidado del salón desde el primer segundo y convertir visitas en citas sin fricciones.',
        'steps': ['Belleza con carácter: la cita a un clic desde la portada.', 'Servicios y el salón, explicados con fotos.', 'Galería de trabajos y opiniones de clientas.', 'Horario, mapa y cierre con la cita.'],
        'sol_h': ('Seis decisiones', 'que llenan la agenda.'),
        'points': [
            ('Identidad cálida y cuidada', 'Crema, carbón y terracota con un toque de salvia. Calidez y sofisticación sin resultar fría ni inalcanzable.'),
            ('Servicios de un vistazo', 'Peluquería, color, manicura y maquillaje en cuatro tarjetas con foto. La clienta sabe enseguida si el salón hace lo que busca.'),
            ('Galería que enamora', 'Mosaico de trabajos por técnica, preparado para cargar las fotos del propio salón sin tocar código.'),
            ('Cita directa por WhatsApp', 'Botón flotante y «Pedir cita» en cada sección. Cero fricción entre el interés y la reserva.'),
            ('Lista para el SEO local', 'Estructura semántica y datos de peluquería con dirección, horario y valoraciones, pensada para Google Maps.'),
            ('Confianza a la vista', 'Reseñas, horario y mapa integrados: lo que una clienta nueva busca antes de reservar, sin salir de la web.'),
        ],
        'design_h': ('Una web que huele bien', 'antes de leerla.'),
        'fonts': [("'Fraunces', Georgia, serif", 'italic', 400, 'Fraunces', 'Titulares: el letrero de un atelier'),
                  ("'Inter', Arial, sans-serif", 'normal', 400, 'Inter', 'Texto: limpio y legible')],
        'gfonts': 'family=Fraunces:ital,wght@0,400;1,400',
        'palette': [('Crema', '#FBF7F1'), ('Carbón', '#1A1A1A'), ('Terracota', '#C66B4F'), ('Salvia', '#ECEFE5'), ('Oro', '#C9A86A')],
        'design_text': 'La paleta es la de un salón cuidado: crema cálida como el aceite de argán, carbón para el contraste, terracota para la acción y un toque de salvia que aporta calma. Fraunces pone el carácter en los titulares y Inter, la claridad en el texto.',
        'duo_alts': [('Galería «Resultados que hablan por sí solos» con fotos de cortes, color y peinados', 'La galería, ordenada por técnica.'),
                     ('Sección de contacto con horario, dirección y mapa del salón', 'Horario, dirección y mapa para quien llega por primera vez.')],
        'wide_alt': ('Sección de servicios con tarjetas de Peluquería, Color, Manicura y Maquillaje', 'Los servicios, cada uno con su foto y lo que incluye.'),
        'phones_h': ('Pensada para', 'pedir cita desde el sofá.'),
        'phones_alt': ['portada con el botón Pedir cita por WhatsApp', 'tarjetas de servicios', 'opiniones de clientas', 'sección El centro'],
        'cta': '¿Tu peluquería merece una web así?',
    },
    {
        'slug': 'taxi-santa-susanna', 'name': 'Taxi Santa Susanna', 'cover': 'taxi.webp',
        'sector': 'Transporte', 'place': 'Santa Susanna', 'client': 'Taxi Santa Susanna',
        'did': 'Diseño web · Reservas · SEO local · Multidioma', 'status': 'Web publicada',
        'url': 'https://nueva.taxisantasusanna.com/', 'url_label': 'Ver la web',
        'cover_alt': 'Portada de la web de Taxi Santa Susanna: taxis aparcados al atardecer con el titular «Tu transfer»',
        'lead': 'Reservas sin llamar. Un servicio de taxi local de la costa del Maresme que no existía en internet: ahora tiene web propia con reservas online, tarifas claras y cuatro idiomas para el turismo.',
        'facts': [('24/7', 'reservas online, sin llamar'), ('4', 'idiomas: catalán, castellano, inglés y francés'), ('0 €', 'de comisión: reservas propias, sin plataformas')],
        'reto_h': ('Un buen servicio', 'que nadie encontraba.'),
        'reto_statement': 'Taxi Santa Susanna llevaba años trabajando con su flota local, pero su presencia digital era cero: ni web ni reservas online. Todo dependía del boca a boca.',
        'reto_text': 'Los turistas que llegaban a la costa buscaban «taxi Santa Susanna» o «transfer aeropuerto Barcelona» y no lo encontraban, mientras la competencia y las apps se quedaban con esas búsquedas. El objetivo: una web que se encuentre en Google y que reserve sola.',
        'steps': ['Tu transfer, 24/7: la reserva arriba del todo.', 'Salidas y trayectos con precio cerrado.', 'Destinos y ciudades más pedidos.', 'Ventajas, eventos y contacto.'],
        'sol_h': ('Seis decisiones', 'para reservar sin llamar.'),
        'points': [
            ('Web orientada a reservar', 'Llamadas a la acción directas («reservar», «llamar») y tarifas a la vista. Pensada primero para el móvil.'),
            ('Reservas online propias', 'Sistema de reservas con confirmación, sin comisiones de plataformas externas.'),
            ('Trayectos con precio', 'Aeropuerto, Barcelona, Girona y destinos frecuentes con su tarifa, para decidir sin preguntar.'),
            ('Cuatro idiomas', 'Catalán, castellano, inglés y francés, cada uno con su propio SEO, para el turismo internacional.'),
            ('SEO local', 'Datos estructurados de servicio de taxi y negocio local, y contenido por zonas de la costa.'),
            ('Confianza a la vista', 'Ventajas del servicio, pago seguro y atención por una persona, no por un robot.'),
        ],
        'design_h': ('Verde de la costa,', 'amarillo de taxi.'),
        'fonts': [("'Montserrat', Arial, sans-serif", 'normal', 800, 'Montserrat Extra Bold', 'Titulares: rotundos y legibles'),
                  ("'Montserrat', Arial, sans-serif", 'normal', 400, 'Montserrat Regular', 'Texto: la misma familia, más calma')],
        'gfonts': 'family=Montserrat:wght@400;800',
        'palette': [('Verde noche', '#002313'), ('Verde', '#008244'), ('Amarillo taxi', '#F3C800'), ('Tinta', '#1F2A24'), ('Blanco', '#FFFFFF')],
        'design_text': 'Una sola familia tipográfica en dos pesos y una paleta que sale del propio servicio: el verde de la marca para dar confianza y el amarillo del taxi para todo lo que es acción. Una web que se entiende con prisa, en el móvil y en cualquiera de sus cuatro idiomas.',
        'duo_alts': [('Destinos más pedidos: Barcelona, Girona y compras, con sus salidas', 'Los destinos más pedidos, con sus salidas.'),
                     ('Sección de eventos con transfer para grandes citas deportivas', 'Transfer para eventos: otra puerta de entrada.')],
        'wide_alt': ('Sección «Reserva online tu taxi» con salidas desde el aeropuerto y precios por trayecto', 'La reserva online con trayectos y precios cerrados.'),
        'phones_h': ('Pensada para', 'reservar con prisa.'),
        'phones_alt': ['portada con el titular Tu transfer profesional', 'trayectos al aeropuerto', 'ventajas del servicio', 'destinos con fotos de Barcelona y Girona'],
        'cta': '¿Quieres una web así para tu negocio?',
    },
    {
        'slug': 'olia-workplace', 'name': 'Olia Workplace', 'cover': 'olia.webp',
        'sector': 'Salud y bienestar', 'place': 'Barcelona', 'client': 'Olia Workplace',
        'did': 'Branding · Diseño web · Bilingüe', 'status': 'Web publicada',
        'url': 'https://oliaworkplace.com/', 'url_label': 'Ver la web',
        'cover_alt': 'Portada de la web de Olia: «Osteopatía en la empresa» sobre fondo verde salvia junto a una sesión de osteopatía',
        'lead': 'Osteopatía en la empresa. Un servicio nuevo, con marca nueva, que tenía que convencer a empresas desde el primer día: profesionalidad clínica, tono cercano y un camino claro hasta pedir propuesta.',
        'facts': [('2', 'idiomas: castellano y catalán'), ('+10', 'años de experiencia clínica a la vista'), ('1', 'formulario pensado para empresas')],
        'reto_h': ('Vender a empresas', 'un servicio nuevo.'),
        'reto_statement': 'Olia es osteópata con más de diez años de experiencia clínica y decidió llevar su trabajo a las empresas: sesiones en la propia oficina para el equipo.',
        'reto_text': 'Servicio nuevo, marca nueva y sin clientes. La web tenía que vender la idea a empresas, con un recorrido de compra muy distinto al de un paciente, transmitir profesionalidad clínica y captar contactos de calidad desde el primer día.',
        'steps': ['Osteopatía en la empresa, en una frase.', 'El problema y qué es la osteopatía laboral.', 'Beneficios y cómo funciona el servicio.', 'Prueba piloto, quién soy y la propuesta.'],
        'sol_h': ('Seis decisiones', 'para convencer a una empresa.'),
        'points': [
            ('Marca B2B con tono cálido', 'Confianza clínica y cercanía humana a la vez: salvia y crema para hablar de bienestar sin estridencias.'),
            ('Un argumento por pasos', 'Problema, solución, beneficios y proceso, en el orden en que una empresa toma la decisión.'),
            ('Bilingüe castellano y catalán', 'Toda la web en los dos idiomas, con un selector siempre a mano.'),
            ('Propuesta para empresas', 'Un formulario con lo que importa (equipo, ubicación, frecuencia) para llegar a la primera llamada con contexto.'),
            ('Prueba piloto', 'Una forma de empezar con poco riesgo, explicada con claridad para quien tiene que aprobarla.'),
            ('Credenciales visibles', 'Registro de osteópatas, años de experiencia y quién hay detrás, desde el primer scroll.'),
        ],
        'design_h': ('Bienestar', 'sin estridencias.'),
        'fonts': [("'Questrial', Arial, sans-serif", 'normal', 400, 'Questrial', 'Titulares: suaves y cercanos'),
                  ("'Open Sans', Arial, sans-serif", 'normal', 400, 'Open Sans', 'Texto: claro y profesional')],
        'gfonts': 'family=Questrial&family=Open+Sans:wght@400',
        'palette': [('Salvia', '#9AB29A'), ('Crema', '#FAF0D7'), ('Coral', '#E37C5C'), ('Rojo acción', '#DB3F1F'), ('Verde tinta', '#3D4A3D')],
        'design_text': 'Salvia y crema para la calma de un tratamiento, coral para las secciones que invitan a dar el paso y un rojo decidido para cada botón. La tipografía redondeada suaviza el mensaje clínico sin restarle seriedad.',
        'duo_alts': [('Sección de proceso con los pasos del servicio en la empresa', 'Cómo funciona, paso a paso.'),
                     ('Sección «Quién soy» con la foto y la trayectoria de la osteópata', 'Quién hay detrás: la confianza también se diseña.')],
        'wide_alt': ('Sección «La solución» que explica qué es la osteopatía en la empresa', 'Qué es la osteopatía laboral, explicado para RR. HH.'),
        'phones_h': ('Pensada para', 'convencer en el móvil.'),
        'phones_alt': ['portada Osteopatía en la empresa', 'datos sobre dolor de espalda en el trabajo', 'beneficios para la empresa', 'prueba piloto'],
        'cta': '¿Vas a lanzar un servicio nuevo?',
    },
    {
        'slug': 'juli-manitas', 'name': 'Juli Manitas', 'cover': 'juli-manitas.webp',
        'sector': 'Servicios del hogar', 'place': 'Barcelona, Vallès y Maresme', 'client': 'Juli Manitas',
        'did': 'Diseño web · Desarrollo · SEO local', 'status': 'Propuesta web',
        'url': 'https://jenn-jt.github.io/juli-manitas-v1/', 'url_label': 'Ver el prototipo',
        'cover_alt': 'Portada de la web de Juli Manitas: «Tus arreglos pendientes, tachados en una mañana» con una lista de tareas',
        'lead': 'Un oficio de confianza que merece una web a la altura. Juli lleva años haciendo montajes, carpintería y reformas con quince reseñas de cinco estrellas y ninguna presencia online.',
        'facts': [('5,0 ★', '15 reseñas en Google'), ('+63', 'municipios en el buscador de zona'), ('18', 'fotos de trabajos reales')],
        'reto_h': ('Una buena reputación', 'que nadie encontraba.'),
        'reto_statement': 'Juli tiene algo difícil de construir: reputación real. Quince clientes que volvieron a Google a dejar cinco estrellas. El problema: nadie más podía encontrarlo.',
        'reto_text': 'Sin web, sin redes y sin carta de servicios online, todo dependía del boca a boca. La gente que busca «manitas Barcelona» o «montaje de muebles Sabadell» acababa en la competencia. El objetivo: convertir su reputación en encargos sin perder la voz personal que hace que sus clientes confíen en él.',
        'steps': ['La lista de pendientes que se tacha sola.', 'Servicios y la lista para pedir presupuesto.', 'Trabajos reales y reseñas de Google.', 'Zona de trabajo, preguntas y llamada.'],
        'sol_h': ('Seis decisiones', 'para pedir presupuesto.'),
        'points': [
            ('Trabajos reales', 'Fotos de sus propios montajes, persianas, pintura y carpintería. Ni una foto de banco de imágenes.'),
            ('«¿Llego a tu casa?»', 'Un buscador con más de 63 municipios que perdona las faltas: en dos segundos sabes si Juli trabaja en tu zona.'),
            ('Presupuesto por WhatsApp', 'Marcas lo que necesitas y la web escribe el mensaje. Sin formularios y sin esperas.'),
            ('Voz en primera persona', 'Textos escritos como habla Juli: sin tecnicismos ni tono corporativo.'),
            ('Reseñas de Google', 'Sus quince valoraciones de cinco estrellas, integradas en la página.'),
            ('Preguntas antes de llamar', 'Las dudas de siempre resueltas antes del primer contacto.'),
        ],
        'design_h': ('Huele a oficio', 'bien hecho.'),
        'fonts': [("'Bricolage Grotesque', Arial, sans-serif", 'normal', 700, 'Bricolage Grotesque', 'Titulares: confianza de oficio'),
                  ("'JetBrains Mono', monospace", 'normal', 400, 'JetBrains Mono', 'Detalles: calculado al milímetro')],
        'gfonts': 'family=Bricolage+Grotesque:wght@700&family=JetBrains+Mono:wght@400',
        'palette': [('Rojo llave', '#B21815'), ('Tinta', '#1C232B'), ('Papel', '#F4F0E8'), ('Amarillo metro', '#F2B81C'), ('Arena', '#D8CFBF')],
        'design_text': 'El punto de partida fue el logo: el rojo exacto de su llave inglesa. Papel crema y tinta oscura como base, los colores del cuaderno de un profesional. El metro que se despliega al cargar, la lista de pendientes que se tacha sola y el generador de presupuesto tienen una función; ninguno es decoración.',
        'duo_alts': [('Sección de servicios con iconos: montaje, persianas, pintura, carpintería', 'Los servicios, uno a uno.'),
                     ('Mapa de la zona de trabajo con el buscador de municipios', 'La zona de trabajo, con buscador de municipios.')],
        'wide_alt': ('Galería «Mis trabajos. Fotos reales.» con montajes, persianas y carpintería', 'La galería: solo trabajos reales.'),
        'phones_h': ('Pensada para', 'pedir presupuesto en un minuto.'),
        'phones_alt': ['portada con la lista de arreglos pendientes', 'servicios de cocina, baño y terraza', 'galería de trabajos', 'reseñas de clientes'],
        'cta': '¿Tu negocio también merece una web así?',
    },
    {
        'slug': 'punt-i-copia', 'name': 'Punt i Còpia', 'cover': 'punt-i-copia.webp',
        'sector': 'Copistería', 'place': 'Barcelona', 'client': 'Copistería ficticia para la demo',
        'did': 'Diseño web · Desarrollo · Bilingüe', 'status': 'Proyecto demo',
        'url': 'https://sheisdigitalab.github.io/punt-i-copia-web/', 'url_label': 'Ver la demo',
        'cover_alt': 'Portada de la web de Punt i Còpia: titular «Còpies, imatge i imprenta a un sol lloc» con tipografía editorial',
        'lead': 'Una copistería de barrio con web de revista. Una demo bilingüe para copisterías, fotografía e imprentas, pensada para que pedir un presupuesto cueste lo mismo que mandar un mensaje.',
        'facts': [('2', 'idiomas: catalán y castellano'), ('12', 'servicios en el catálogo'), ('3', 'pasos para pedir presupuesto')],
        'reto_h': ('Hacen de todo,', 'pero no se ve.'),
        'reto_statement': 'Las copisterías de barrio hacen de todo: apuntes, trabajos de fin de grado, fotos de carnet, flyers, pancartas. Pero en internet suelen quedarse en una ficha de Google Maps.',
        'reto_text': 'Quien busca «imprimir TFG» o «imprenta flyers» no sabe si ese local hace lo que necesita, cuánto tarda o cómo enviar el archivo, así que llama o se va a una imprenta online. Y en zonas bilingües, la web tiene que hablar catalán y castellano sin que ninguno parezca de segunda.',
        'steps': ['Portada de revista y el catálogo completo.', 'Tres oficios: copistería, fotografía e imprenta.', 'Presupuesto en tres pasos.', 'Contacto y cierre con WhatsApp.'],
        'sol_h': ('Seis decisiones', 'de imprenta.'),
        'points': [
            ('Bilingüe de verdad', 'Catalán y castellano con un selector que recuerda el idioma. Hasta el mensaje de WhatsApp cambia.'),
            ('Catálogo de 12 servicios', 'Una tira editorial con todo lo que se hace en el local, de las fotocopias a los roll-ups.'),
            ('Tres oficios, una web', 'Copistería, fotografía e imprenta con su ficha, sus fotos y sus servicios.'),
            ('Presupuesto en tres pasos', 'Envías el archivo, recibes el precio y recoges o pides entrega. Sin miedo a preguntar.'),
            ('WhatsApp siempre a mano', 'Botón flotante con el mensaje ya escrito en el idioma de quien visita.'),
            ('Pensada para el barrio', 'Dirección, horario y cómo llegar, con estructura lista para «copistería cerca de mí».'),
        ],
        'design_h': ('Huele a tinta', 'recién impresa.'),
        'fonts': [("'Fraunces', Georgia, serif", 'italic', 400, 'Fraunces', 'Titulares: cursivas de revista'),
                  ("'Geist', Arial, sans-serif", 'normal', 400, 'Geist', 'Texto: lectura cómoda')],
        'gfonts': 'family=Fraunces:ital,wght@0,400;1,400&family=Geist:wght@400',
        'palette': [('Papel', '#F0EDE5'), ('Negro tinta', '#131210'), ('Magenta', '#E63946'), ('Cian', '#2A9DF4'), ('Amarillo', '#FFD23F')],
        'design_text': 'La paleta sale del oficio: las tintas de impresión sobre fondo de papel, en la franja superior, en la numeración de cada sección y en los cuatro puntos del logo. La página se lee como la portada de una revista de barrio y se usa como una tienda.',
        'duo_alts': [('Franja «El teu lloc d’impressió de confiança, al barri» con ventajas', 'La propuesta de valor, en catalán.'),
                     ('Sección «Tres maneres. Sense fricció.» con los pasos para pedir', 'Tres pasos para pedir, sin fricción.')],
        'wide_alt': ('Sección «Tres oficis. Una mateixa cura.» con copistería, fotografía e imprenta', 'Tres oficios con su ficha y sus servicios.'),
        'phones_h': ('Pensada para', 'pedir desde el móvil.'),
        'phones_alt': ['portada Còpies, imatge i imprenta', 'ventajas del local', 'servicio de fotografía', 'pasos para pedir'],
        'cta': '¿Tu negocio necesita una web así?',
    },
]

HEAD = Template('''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>$name · Proyecto · She's Digital</title>
  <meta name="description" content="Proyecto: web de $name ($sector_l, $place), diseñada y desarrollada por She's Digital." />
  <meta name="robots" content="noindex, nofollow" />
  <link rel="canonical" href="https://sheisdigitalab.com/proyectos/$slug/" />
  <meta property="og:title" content="$name · Proyecto · She's Digital" />
  <meta property="og:image" content="../../assets/img/work/$cover" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../../assets/img/favicon.svg" type="image/svg+xml" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@400;500;600&$gfonts&display=swap" />
  <link rel="preload" as="image" href="../../assets/img/work/$cover" />
  <link rel="stylesheet" href="../../assets/css/styles.css" />
  <link rel="stylesheet" href="../../assets/css/case.css" />
  <script>
    (function (d) {
      var r = d.documentElement; r.classList.add('js');
      if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
        r.classList.add('is-anim');
        setTimeout(function () { if (!window.gsap) r.classList.remove('is-anim'); }, 3000);
      }
    })(document);
  </script>
</head>''')


def e(s):
    return escape(s, quote=True)


def h2(pair):
    return f'{e(pair[0])}<br /><em>{e(pair[1])}</em>'


def page(i, c, nxt):
    num = f'{i + 1:02d}'
    base = f'../../assets/img/cases/{c["slug"]}/'
    wa = 'https://wa.me/34637889942?text=' + quote(f'Hola Jenifer, he visto el proyecto de {c["name"]} y me gustaría hablar de mi web.')

    # Imágenes: Martilota guarda nombres propios; el resto usa wide/duo-1/duo-2
    if 'wide' in c:
        wide = c['wide']
        duo = c['duo']
        full_h = 7849
    else:
        info = __import__('json').load(open(ROOT / 'assets/img/cases' / c['slug'] / 'info.json'))
        wide = ('wide.webp', *info['wide'], *c['wide_alt'])
        duo = [(f'duo-{k + 1}.webp', *info['duo'][k], *c['duo_alts'][k]) for k in range(2)]
        full_h = info['fullw'][1]

    facts = '\n'.join(f'        <li data-reveal><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in c['facts'])
    active = ' class="is-active"'
    steps = '\n'.join(f'              <li{active if k == 0 else ""}><span>{k + 1:02d}</span>{e(s)}</li>' for k, s in enumerate(c['steps']))
    points = '\n'.join(f'''          <li data-reveal>
            <span class="cs-points__n">{k + 1:02d}</span>
            <h3>{e(t)}</h3>
            <p>{e(d)}</p>
          </li>''' for k, (t, d) in enumerate(c['points']))
    fonts = '\n'.join(f'''            <div class="cs-type__item">
              <span class="cs-type__sample" style="font-family: {f[0]}; font-style: {f[1]}; font-weight: {f[2]}" aria-hidden="true">Aa</span>
              <p><strong>{e(f[3])}</strong><span>{e(f[4])}</span></p>
            </div>''' for f in c['fonts'])
    palette = '\n'.join(f'            <li style="--c:{hx}"><span>{e(n)}</span><code>{hx}</code></li>' for n, hx in c['palette'])
    duo_html = '\n'.join(f'''          <figure data-reveal>
            <div class="cs-duo__media" data-zoom><img src="{base}{d[0]}" alt="{e(d[3])}" width="{d[1]}" height="{d[2]}" loading="lazy" /></div>
            <figcaption>{e(d[4])}</figcaption>
          </figure>''' for d in duo)
    phones = '\n'.join(f'          <figure class="phone" data-phone="{k}"><img src="{base}mobile-{k + 1}.webp" alt="Móvil: {e(a)}" width="585" height="1266" loading="lazy" /></figure>' for k, a in enumerate(c['phones_alt']))
    host = c['url'].split('//', 1)[1].rstrip('/')

    head = HEAD.substitute(name=e(c['name']), slug=c['slug'], cover=c['cover'], gfonts=c['gfonts'],
                           sector_l=e(c['sector'].lower()), place=e(c['place']))
    return f'''{head}
<body class="case-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <!-- ============ Cabecera ============ -->
  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="../../" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="../../assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="../../#servicios">Servicios</a>
        <a href="../../#proyectos">Proyectos</a>
        <a href="../../#proceso">Proceso</a>
        <a href="../../#sobre-mi">Sobre mí</a>
        <a href="../../#tarifas">Tarifas</a>
        <a href="../../#faq">FAQ</a>
        <a href="#contacto" class="btn btn--dark nav__cta-mobile">Hablemos {ARROW}</a>
      </nav>
      <a href="#contacto" class="btn btn--dark nav__cta">Hablemos {ARROW}</a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
        <span class="sr-only">Abrir menú</span>
        <span class="nav__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </header>

  <main id="main">

    <!-- ============ Cabecera del proyecto ============ -->
    <section class="cs-hero" id="top" aria-labelledby="cs-title">
      <div class="wrap">
        <a class="cs-back" href="../../#proyectos" data-hero="fade">
          <span aria-hidden="true">←</span> Todos los proyectos
        </a>

        <div class="cs-hero__grid">
          <div>
            <p class="eyebrow" data-hero="fade">Caso {num} · {e(c['sector'])}</p>
            <h1 class="cs-hero__title" id="cs-title">
              <span class="hero__line"><span class="hero__line-in" data-hero="line">{e(c['name'])}</span></span>
            </h1>
            <p class="cs-hero__lead" data-hero="fade">{e(c['lead'])}</p>
          </div>

          <dl class="cs-meta" data-hero="fade">
            <div><dt>Cliente</dt><dd>{e(c['client'])}</dd></div>
            <div><dt>Lugar</dt><dd>{e(c['place'])}</dd></div>
            <div><dt>Qué hicimos</dt><dd>{e(c['did'])}</dd></div>
            <div><dt>Estado</dt><dd>{e(c['status'])}</dd></div>
            <div class="cs-meta__actions">
              <a href="{c['url']}" class="btn btn--dark btn--magnetic" target="_blank" rel="noopener">{e(c['url_label'])} {ARROW_OUT}<span class="sr-only">(se abre en una pestaña nueva)</span></a>
            </div>
          </dl>
        </div>
      </div>

      <figure class="cs-cover" data-cover>
        <img style="view-transition-name: case-{c['slug']}" src="../../assets/img/work/{c['cover']}" alt="{e(c['cover_alt'])}" width="1440" height="900" fetchpriority="high" />
      </figure>

      <ul class="wrap cs-facts" aria-label="Datos del proyecto">
{facts}
      </ul>
    </section>

    <!-- ============ El reto ============ -->
    <section class="section cs-block" aria-labelledby="reto-title">
      <div class="wrap cs-block__grid">
        <header class="cs-block__head">
          <p class="eyebrow" data-reveal>01 — El reto</p>
          <h2 class="h2" id="reto-title" data-split>{h2(c['reto_h'])}</h2>
        </header>
        <div class="cs-block__body">
          <p class="cs-statement" data-words>{e(c['reto_statement'])}</p>
          <p data-reveal>{e(c['reto_text'])}</p>
        </div>
      </div>
    </section>

    <!-- ============ Recorrido por la web ============ -->
    <section class="cs-tour" aria-labelledby="tour-title" data-tour>
      <div class="cs-tour__pin">
        <div class="wrap cs-tour__grid">
          <div class="cs-tour__copy">
            <p class="eyebrow" data-reveal>Recorrido</p>
            <h2 class="h2" id="tour-title" data-split>La web,<br /><em>de arriba abajo.</em></h2>
            <ol class="cs-tour__steps" data-tour-steps>
{steps}
            </ol>
          </div>
          <div class="cs-browser" aria-label="Captura completa de la web de {e(c['name'])}" role="img">
            <div class="cs-browser__bar" aria-hidden="true">
              <i></i><i></i><i></i>
              <span>{e(host)}</span>
            </div>
            <div class="cs-browser__screen" data-tour-screen tabindex="0" aria-label="Captura desplazable de la web completa">
              <img src="{base}full.webp" alt="" width="1200" height="{full_h}" loading="lazy" data-tour-img />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ La solución ============ -->
    <section class="section cs-block" aria-labelledby="sol-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow" data-reveal>02 — La solución</p>
          <h2 class="h2" id="sol-title" data-split>{h2(c['sol_h'])}</h2>
        </header>

        <ol class="cs-points">
{points}
        </ol>
      </div>

      <figure class="wrap cs-wide" data-reveal>
        <div class="cs-wide__media" data-zoom>
          <img src="{base}{wide[0]}" alt="{e(wide[3])}" width="{wide[1]}" height="{wide[2]}" loading="lazy" />
        </div>
        <figcaption>{e(wide[4])}</figcaption>
      </figure>
    </section>

    <!-- ============ El diseño ============ -->
    <section class="section cs-design" aria-labelledby="design-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow eyebrow--light" data-reveal>03 — El diseño</p>
          <h2 class="h2" id="design-title" data-split>{h2(c['design_h'])}</h2>
        </header>

        <div class="cs-design__grid">
          <div class="cs-type" data-reveal>
{fonts}
          </div>

          <ul class="cs-palette" aria-label="Paleta de color de {e(c['name'])}" data-reveal>
{palette}
          </ul>
        </div>

        <p class="cs-design__text" data-reveal>{e(c['design_text'])}</p>

        <div class="cs-duo">
{duo_html}
        </div>
      </div>
    </section>

    <!-- ============ En el móvil ============ -->
    <section class="section cs-phones" aria-labelledby="phones-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow" data-reveal>04 — En el móvil</p>
          <h2 class="h2" id="phones-title" data-split>{h2(c['phones_h'])}</h2>
        </header>
        <div class="cs-phones__row">
{phones}
        </div>
      </div>
    </section>

    <!-- ============ Siguiente proyecto ============ -->
    <section class="cs-next" aria-label="Siguiente proyecto">
      <a class="cs-next__link" href="../{nxt['slug']}/" data-cursor-label="Siguiente">
        <span class="wrap cs-next__inner">
          <span class="eyebrow">Siguiente proyecto</span>
          <span class="cs-next__title">{e(nxt['name'])} <span aria-hidden="true">→</span></span>
          <span class="cs-next__sector">{e(nxt['sector'])} · {e(nxt['status'])}</span>
        </span>
        <span class="cs-next__media" aria-hidden="true"><img src="../../assets/img/work/{nxt['cover']}" alt="" width="1440" height="900" loading="lazy" /></span>
      </a>
    </section>

    <!-- ============ CTA ============ -->
    <section class="audit cs-cta" id="contacto" aria-labelledby="cta-title">
      <div class="wrap audit__inner">
        <div>
          <p class="eyebrow" data-reveal>¿Te imaginas la tuya?</p>
          <h2 class="h2" id="cta-title" data-split>{e(c['cta'])}</h2>
        </div>
        <div class="audit__body" data-reveal>
          <p>Cuéntame qué necesitas y te propongo el camino más corto para conseguirlo. Presupuesto cerrado en 24 horas.</p>
          <div class="cs-cta__actions">
            <a class="btn btn--dark btn--magnetic" href="{wa}">
              {WA_ICON}
              Quiero algo similar
            </a>
            <a class="btn btn--line" href="../../#contacto">Escribirte un mensaje</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- ============ Pie ============ -->
  <footer class="footer">
    <div class="wrap">
      <div class="footer__cols">
        <div>
          <img src="../../assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Agencia digital de Jenifer Jaldo.<br />Branding · Web · Ecommerce · SEO/GEO · Social.</p>
        </div>
        <nav aria-label="Pie: navegación">
          <h3>Navegación</h3>
          <ul>
            <li><a href="../../#servicios">Servicios</a></li>
            <li><a href="../../#proyectos">Proyectos</a></li>
            <li><a href="../../#sobre-mi">Sobre mí</a></li>
            <li><a href="https://sheisdigitalab.com/blog/">Blog</a></li>
          </ul>
        </nav>
        <div>
          <h3>Contacto</h3>
          <ul>
            <li><a href="mailto:hola@sheisdigitalab.com">hola@sheisdigitalab.com</a></li>
            <li><a href="tel:+34637889942">+34 637 889 942</a></li>
            <li>Barcelona</li>
          </ul>
        </div>
        <nav aria-label="Pie: legal">
          <h3>Legal</h3>
          <ul>
            <li><a href="https://sheisdigitalab.com/legal/aviso-legal/">Aviso legal</a></li>
            <li><a href="https://sheisdigitalab.com/legal/privacidad/">Privacidad</a></li>
            <li><a href="https://sheisdigitalab.com/legal/cookies/">Cookies</a></li>
          </ul>
        </nav>
      </div>
      <div class="footer__bottom">
        <p>© 2026 She's Digital · Jenifer Jaldo</p>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="../../assets/js/main.js" defer></script>
  <script src="../../assets/js/case.js" defer></script>
</body>
</html>
'''


if __name__ == '__main__':
    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]
        out = ROOT / 'proyectos' / c['slug'] / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(i, c, nxt), encoding='utf-8')
        print('ok', out.relative_to(ROOT))
