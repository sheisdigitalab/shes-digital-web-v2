"""Genera las páginas de servicio (servicios/<ruta>/index.html) desde una plantilla común.

Uso:  python tools/build_services.py
Los textos y precios de cada servicio están en SERVICES.
"""
import json
import re
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://sheisdigitalab.com'

ARROW = '<span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>'
WA_ICON = ('<span class="btn__wa" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg></span>')

CASES = {
    'martilota': ('Martilota', 'Restauración', 'martilota.webp', 'Cinco espacios, la carta y la reserva directa en un solo scroll.'),
    'juli-manitas': ('Juli Manitas', 'Servicios del hogar', 'juli-manitas.webp', 'Presupuesto por WhatsApp y buscador de zona con más de 63 municipios.'),
    'olia-workplace': ('Olia Workplace', 'Salud y bienestar', 'olia.webp', 'Marca y web para un servicio nuevo, explicado paso a paso y en dos idiomas.'),
    'taxi-santa-susanna': ('Taxi Santa Susanna', 'Transporte', 'taxi.webp', 'Reservas online, cuatro idiomas y SEO local para la costa del Maresme.'),
    'alma-salinas': ('Alma Salinas', 'Belleza · Proyecto demo', 'alma-salinas.webp', 'Cita por WhatsApp y estructura lista para Google Maps.'),
    'punt-i-copia': ('Punt i Còpia', 'Copistería · Proyecto demo', 'punt-i-copia.webp', 'Bilingüe, con catálogo de 12 servicios y presupuesto en un mensaje.'),
}

# El pack lanzamiento se repite en Diseño web y en Branding
PACK_LANZAMIENTO = {
    'tag': 'Pack lanzamiento', 'badge': 'Ahorras 290 €',
    'name': '¿Empiezas de cero? Logo y web juntos',
    'desc': 'El pack Logo de branding y la web WordPress de varias páginas, diseñados a la vez para que todo encaje desde el primer día.',
    'price': '1.590 €', 'suffix': '+ IVA', 'was': 'En vez de 1.880 € por separado',
    'cta': 'Quiero el pack', 'wa': 'Hola Jenifer, me interesa el pack lanzamiento (logo + web).',
}

SERVICES = [
    # ------------------------------------------------------------------ Diseño web
    {
        'path': 'diseno-web', 'label': 'Diseño web', 'kicker': 'Diseño y desarrollo web',
        'title': 'Diseño web en Barcelona · WordPress y a medida · She\'s Digital',
        'description': 'Diseño y desarrollo web profesional en Barcelona: WordPress, landings y webs a medida, rápidas, accesibles y pensadas para convertir. Desde 450 € + IVA.',
        'service_type': 'Diseño web',
        'h1': ('Webs que venden,', 'hechas a medida.'),
        'lead': 'Diseño y desarrollo web profesional en Barcelona: rápidas, accesibles y pensadas para convertir visitas en clientes. Sin plantillas y sin humo. Desde 450 € en una semana.',
        'cta_primary': 'Pedir presupuesto en 24 h', 'wa': 'Hola Jenifer, me interesa una web. ¿Podemos hablar?',
        'meta': [('Desde', '450 € + IVA'), ('Entrega', 'De 1 a 5 semanas'), ('Para', 'Negocios locales y servicios'), ('Garantía', 'Te devuelvo el 100 % si la primera fase no te convence')],
        'strip': ['martilota', 'juli-manitas', 'olia-workplace', 'punt-i-copia', 'taxi-santa-susanna', 'alma-salinas'],
        'facts': [('+30', 'webs lanzadas'), ('24 h', 'para tener tu presupuesto cerrado'), ('100 %', 'tuya: dominio, hosting y código a tu nombre')],
        'focus': {'h': ('No es solo', 'que sea bonita.'),
                  'statement': 'Una web profesional posiciona tu marca, convierte visitas en clientes y aguanta el paso del tiempo cuando tu negocio crece.',
                  'text': 'Cada proyecto empieza con una conversación, una estrategia y un diseño pensado para tu sector, sin plantillas recicladas. Después lo construyo en WordPress o con código propio, según lo que necesites editar tú después. El resultado: una web que carga rápido, se ve bien en cualquier pantalla, aparece en Google y cuenta tu marca con coherencia.'},
        'includes_h': ('Sin letra', 'pequeña.'),
        'includes': [
            ('Diseño a medida en Figma', 'Ves la web completa antes de programar nada: tipografía, color y jerarquía pensados para tu marca y tu cliente.'),
            ('Adaptada a cualquier pantalla', 'Móvil, tablet y ordenador, probada en navegadores reales y optimizada para que cargue rápido.'),
            ('SEO técnico desde el primer día', 'Estructura semántica, metaetiquetas, datos estructurados, sitemap y enlazado interno.'),
            ('Accesible para todo el mundo', 'Contraste, teclado y lectores de pantalla según WCAG 2.2 AA. Más gente puede usarla, y Google lo agradece.'),
            ('Formulario y analítica', 'Formulario con antispam, Google Analytics 4 y Search Console configurados para que sepas qué funciona.'),
            ('Acompañamiento después', 'De 1 a 6 meses según la opción: resuelvo dudas, hago pequeños ajustes y te enseño a editarla.'),
        ],
        'plans_h': ('Tres formas de', 'hacer tu web.'),
        'plans_sub': 'Según tu momento y tu presupuesto. En la primera llamada te digo cuál te encaja mejor.',
        'plans': [
            {'tag': 'A · Landing', 'name': 'Landing de una página', 'price': '450 €', 'num': 450, 'suffix': '+ IVA',
             'desc': 'Una sola página, larga y bien estructurada. Para profesionales y servicios concretos que quieren estar en internet sin complicarse.',
             'checks': ['Hasta 6 secciones', 'WordPress', 'Formulario de contacto', 'Lista en 1 semana'],
             'cta': 'Empezar mi landing', 'wa': 'Hola Jenifer, me interesa una landing.'},
            {'tag': 'B · Varias páginas', 'name': 'Web WordPress de varias páginas', 'price': '1.290 €', 'num': 1290, 'suffix': '+ IVA', 'featured': True,
             'desc': 'Editable por ti, con blog opcional, SEO técnico avanzado y diseño 100 % a medida en Figma.',
             'checks': ['Hasta 6 páginas', 'Blog preparado para SEO', 'Tu logo y tus colores aplicados', 'Lista en 3-5 semanas'],
             'cta': 'Quiero esta opción', 'wa': 'Hola Jenifer, me interesa una web de varias páginas.'},
            {'tag': 'C · A medida', 'name': 'Web a medida con código propio', 'price': '2.890 €', 'num': 2890, 'suffix': '+ IVA',
             'desc': 'Para marcas que quieren algo único: animaciones, microinteracciones, máximo rendimiento y un diseño imposible con plantillas.',
             'checks': ['Diseño y código únicos', 'Animaciones a medida', 'Rendimiento optimizado', 'Lista en 6-10 semanas'],
             'cta': 'Hablar de mi proyecto', 'wa': 'Hola Jenifer, me interesa una web a medida.'},
        ],
        'pack': PACK_LANZAMIENTO,
        'guarantees': ['Pago en 2 plazos: 50 % al firmar y 50 % al lanzar', 'Si la primera fase no te convence, te devuelvo el 100 %',
                       '¿Vas a vender online? Tiendas desde 1.490 €. <a class="link" href="../ecommerce/">Ver Ecommerce</a>'],
        'work': ['martilota', 'juli-manitas', 'olia-workplace'], 'work_h': ('Webs que ya', 'están funcionando.'),
        'process_h': ('Sabes qué pasa', 'y cuándo.'),
        'process': [
            ('Descubrimiento', 'Día 1', 'Videollamada de 30-45 minutos sobre tu negocio, tu cliente y tus objetivos. Si encajamos, presupuesto cerrado en 24 horas.'),
            ('Estrategia y diseño', 'Semanas 1-2', 'Mapa de la web, textos clave y diseño en Figma. Lo revisamos hasta que esté perfecto, antes de programar.'),
            ('Desarrollo', 'Semanas 2-4', 'Código limpio en WordPress o a medida, pruebas en navegadores reales, velocidad y SEO técnico.'),
            ('Lanzamiento', 'Semana 5 en adelante', 'Hosting, dominio, analítica y Search Console listos, un vídeo para que la edites y acompañamiento de 1 a 6 meses.'),
        ],
        'extra': {'eyebrow': 'Tecnología', 'h': ('La herramienta,', 'según tu caso.'), 'rows': [
            ('WordPress', 'La mayoría de mis proyectos. Editas textos e imágenes sin tocar código y hay solución para casi todo: reservas, varios idiomas o formularios avanzados.'),
            ('HTML, CSS y JavaScript', 'Cuando hace falta algo único en rendimiento, animación o diseño. Código limpio, sin dependencias innecesarias.'),
            ('React y Next.js', 'Para webs más complejas o aplicaciones, con SEO desde el principio.'),
            ('Shopify y WooCommerce', 'Si vas a vender online, te ayudo a elegir según tu producto y tu volumen, y dejo listos pagos, impuestos y envíos.'),
        ]},
        'faq_h': ('Lo que siempre', 'me preguntan.'),
        'faq': [
            ('¿Cuánto cuesta una web profesional?', 'Una landing de una página cuesta desde <strong>450 €</strong>, una web WordPress de hasta 6 páginas desde <strong>1.290 €</strong> y una web a medida con código propio desde <strong>2.890 €</strong>, siempre + IVA. Si además necesitas logo, el pack lanzamiento (logo + web) sale por <strong>1.590 €</strong>. Las tiendas online empiezan en 1.490 €. El precio final depende del número de páginas, las integraciones y los idiomas.'),
            ('¿Cuánto tarda en estar lista mi web?', 'Una landing, <strong>1 semana</strong>. Una web de varias páginas, <strong>de 3 a 5 semanas</strong>. Una web a medida, <strong>de 6 a 10 semanas</strong>. Los plazos van cerrados en el presupuesto.'),
            ('¿Trabajas con WordPress o con código a medida?', 'Con los dos. WordPress si quieres editar los contenidos tú; código a medida si necesitas el máximo rendimiento o un diseño único. Te recomiendo lo que encaja con tu caso.'),
            ('¿Podré editar la web después?', 'Sí. Con WordPress puedes cambiar textos, imágenes, el blog y crear páginas sin saber código, y te dejo un vídeo tutorial de tu propia web.'),
            ('¿De quién es la web cuando termines?', 'Tuya al <strong>100 %</strong>: dominio a tu nombre, hosting en tu cuenta y el código de tu propiedad. Sin permanencias.'),
            ('¿Trabajas con clientes fuera de Barcelona?', 'Sí. Trabajo en remoto con marcas de toda España y de fuera, con videollamadas siempre que haga falta.'),
        ],
        'cta': {'eyebrow': 'Primera consulta sin compromiso', 'h': '¿Empezamos tu web?', 'text': 'Cuéntame tu proyecto y te respondo el mismo día. Presupuesto cerrado en 24 horas.', 'btn': 'Pedir presupuesto'},
    },
    # ------------------------------------------------------------------ Branding
    {
        'path': 'branding', 'label': 'Branding', 'kicker': 'Branding y diseño de marca',
        'title': 'Branding y diseño de marca en Barcelona · She\'s Digital',
        'description': 'Diseño de marca en Barcelona: logotipo, paleta, tipografía y manual de identidad. Marcas con personalidad propia que se recuerdan. Desde 590 € + IVA.',
        'service_type': 'Diseño de marca',
        'h1': ('Marcas que', 'se recuerdan.'),
        'lead': 'Logo, paleta, tipografía y manual de identidad para que tu negocio se distinga a primera vista. Marcas con personalidad propia, sin plantillas. Desde 590 €.',
        'cta_primary': 'Pedir presupuesto en 24 h', 'wa': 'Hola Jenifer, me interesa crear o renovar mi marca.',
        'meta': [('Desde', '590 € + IVA'), ('Entrega', 'De 1 a 4 semanas'), ('Revisiones', '3 rondas incluidas'), ('Recibes', 'Archivos SVG, PNG, JPG y PDF')],
        'strip': None,
        'facts': [('3', 'rondas de revisión incluidas en todos los packs'), ('100 %', 'tuya: cesión total de derechos al terminar'), ('24 h', 'para tener tu presupuesto cerrado')],
        'focus': {'h': ('No es solo', 'un logo bonito.'),
                  'statement': 'El branding es el sistema visual y verbal que hace que tu marca se distinga y conecte con la gente correcta, antes incluso de leer una palabra.',
                  'text': 'Empiezo escuchando tu negocio y entendiendo a tu cliente, y construyo una identidad que funcione igual de bien en una tarjeta, en una web o en una story de Instagram. Cada marca es única y atemporal, sin el estilo de moda que envejece en seis meses, y te la dejo lista para que la uses con autonomía.'},
        'includes_h': ('Todo para usar tu marca', 'sin depender de nadie.'),
        'includes': [
            ('Investigación y estrategia', 'Antes de diseñar, escucho: briefing, competencia, perfil de cliente y posicionamiento. Sin esto, el diseño es decoración.'),
            ('Naming (en el pack Premium)', 'Si aún no tienes nombre o quieres cambiarlo: propuestas, validación y comprobación de dominio disponible.'),
            ('Logotipo y variantes', 'Logo principal y sus versiones horizontal, vertical, en un color, sobre fondo oscuro y mínima para el favicon.'),
            ('Paleta de color', 'Color principal, secundarios y neutros, con códigos HEX, RGB y CMYK para web e imprenta, y reglas de contraste accesible.'),
            ('Tipografía', 'Tipografías con licencia comprobada y una guía de uso por tamaño y peso.'),
            ('Manual de marca', 'Un PDF con todas las reglas: usos correctos, errores comunes, paleta, tipografías y aplicaciones reales.'),
        ],
        'plans_h': ('Tres formas de', 'diseñar tu marca.'),
        'plans_sub': 'Precio cerrado antes de empezar, sin sobrecostes a mitad de camino.',
        'plans': [
            {'tag': 'A · Esencial', 'name': 'Pack Logo', 'price': '590 €', 'num': 590, 'suffix': '+ IVA',
             'desc': 'Para proyectos que ya tienen nombre y necesitan una marca visual coherente.',
             'checks': ['Logo principal y 2 variantes', 'Paleta de color', 'Tipografías', 'Lista en 1-2 semanas'],
             'cta': 'Empezar mi logo', 'wa': 'Hola Jenifer, me interesa el pack Logo.'},
            {'tag': 'B · Profesional', 'name': 'Pack Identidad', 'price': '1.290 €', 'num': 1290, 'suffix': '+ IVA', 'featured': True,
             'desc': 'Identidad completa con sistema visual, manual de marca y aplicaciones reales.',
             'checks': ['Todo lo del pack Logo', 'Sistema visual completo', 'Manual de marca en PDF', 'Tarjeta, post de Instagram y firma de email', 'Lista en 2-3 semanas'],
             'cta': 'Quiero este pack', 'wa': 'Hola Jenifer, me interesa el pack Identidad.'},
            {'tag': 'C · Premium', 'name': 'Pack Marca completa', 'price': '2.490 €', 'num': 2490, 'suffix': '+ IVA',
             'desc': 'Naming desde cero, sistema visual amplio, estrategia y aplicaciones para crecer.',
             'checks': ['Naming y comprobación de dominio', 'Identidad visual completa', 'Estrategia de marca y tono', 'Más de 8 aplicaciones a medida', 'Lista en 3-4 semanas'],
             'cta': 'Hablar de mi marca', 'wa': 'Hola Jenifer, me interesa el pack Marca completa.'},
        ],
        'pack': PACK_LANZAMIENTO,
        'guarantees': ['Pago en 2 plazos: 50 % al firmar y 50 % al entregar', 'Si la primera ronda no te convence, te devuelvo el 100 %',
                       'Cesión total y exclusiva de derechos al pagar la última cuota'],
        'work': ['olia-workplace', 'juli-manitas', 'punt-i-copia'], 'work_h': ('Marcas con', 'su propia voz.'),
        'process_h': ('Validamos cada paso', 'antes de avanzar.'),
        'process': [
            ('Briefing y estrategia', 'Semana 1', 'Te entrevisto sobre tu negocio, tu cliente y tu visión, analizo la competencia y defino el posicionamiento visual.'),
            ('Conceptos visuales', 'Semanas 1-2', 'Te presento 2-3 caminos con referencias y bocetos de logo, y eliges la dirección conmigo.'),
            ('Diseño y ajustes', 'Semanas 2-3', 'Desarrollo el sistema completo (logo, color y tipografía) con 3 rondas de revisión para afinar cada detalle.'),
            ('Manual y entrega', 'Semana 4', 'Lo recojo todo en el manual y te entrego los archivos en SVG, PNG, JPG y PDF, explicándote cómo usarlos.'),
        ],
        'extra': None,
        'faq_h': ('Lo que siempre', 'me preguntan.'),
        'faq': [
            ('¿Qué incluye un servicio de branding?', 'Investigación, logotipo y variantes, paleta de color, tipografía, manual de marca y archivos editables. El naming se incluye en el pack Premium. Te entrego todo lo necesario para usar tu marca sin depender de nadie.'),
            ('¿Cuánto cuesta diseñar una marca?', 'El pack Logo, desde <strong>590 €</strong>; la identidad completa con manual, desde <strong>1.290 €</strong>, y la marca completa con naming, desde <strong>2.490 €</strong>, siempre + IVA. Si además necesitas web, el pack lanzamiento (logo + web) sale por <strong>1.590 €</strong>.'),
            ('¿Cuánto tarda?', 'El pack Logo, <strong>1-2 semanas</strong>; la identidad completa, <strong>2-3 semanas</strong>, y la marca completa con naming, <strong>3-4 semanas</strong>. Si tienes prisa, dímelo y miro si es posible.'),
            ('¿Cuántas revisiones puedo pedir?', '<strong>3 rondas</strong> en cualquier pack. Si necesitas más, se añaden al presupuesto sin sorpresas.'),
            ('¿Diseñas marcas para cualquier sector?', 'Sí, con más experiencia en servicios profesionales, hostelería, bienestar y comercio local. Si tu sector es muy técnico, valoramos juntos si encajamos.'),
            ('¿Me cedes los derechos del logo?', 'Sí: cesión total y exclusiva al pagar la última cuota, con documento firmado. Puedes registrarla, modificarla o venderla.'),
        ],
        'cta': {'eyebrow': 'Primera consulta sin compromiso', 'h': '¿Creamos tu marca?', 'text': 'Cuéntame tu proyecto y te paso presupuesto cerrado en 24 horas.', 'btn': 'Pedir presupuesto'},
    },
    # ------------------------------------------------------------------ Ecommerce
    {
        'path': 'ecommerce', 'label': 'Ecommerce', 'kicker': 'Tiendas online',
        'title': 'Tiendas online con WooCommerce y Shopify en Barcelona · She\'s Digital',
        'description': 'Diseño de tiendas online con WooCommerce y Shopify en Barcelona: pagos, envíos y SEO para vender desde el primer día. Desde 1.490 € + IVA.',
        'service_type': 'Diseño de tiendas online',
        'h1': ('Tu tienda online,', 'lista para vender.'),
        'lead': 'WooCommerce o Shopify a medida, con pagos, envíos, gestión de stock y SEO, y un diseño pensado para que comprar sea fácil. Desde 1.490 €.',
        'cta_primary': 'Pedir presupuesto en 24 h', 'wa': 'Hola Jenifer, quiero montar una tienda online.',
        'meta': [('Desde', '1.490 € + IVA'), ('Entrega', 'De 3 a 6 semanas'), ('Plataformas', 'WooCommerce o Shopify'), ('Soporte', '3 meses después del lanzamiento')],
        'strip': ['martilota', 'olia-workplace', 'juli-manitas', 'taxi-santa-susanna', 'punt-i-copia', 'alma-salinas'],
        'facts': [('3 meses', 'de soporte incluidos después del lanzamiento'), ('30', 'productos subidos por mí en la tienda básica'), ('0 %', 'de comisión mía sobre tus ventas')],
        'focus': {'h': ('Vender online', 'sin complicaciones.'),
                  'statement': 'Una tienda que funciona no es solo un catálogo: es un camino claro desde que alguien ve tu producto hasta que lo paga y le llega a casa.',
                  'text': 'Diseño, desarrollo, configuración y pruebas reales de compra antes de lanzar. Te dejo un panel en el que subes productos, cambias precios y gestionas pedidos sin tocar código, y la tienda es tuya desde el primer día.'},
        'includes_h': ('Todo lo necesario', 'para empezar a vender.'),
        'includes': [
            ('Diseño a medida', 'Un tema propio adaptado a tu marca, con una jerarquía clara para que encontrar y comprar sea rápido.'),
            ('Pagos', 'Tarjeta, Bizum, PayPal, Apple Pay y Google Pay, y pago aplazado si lo necesitas. Pruebas reales antes de abrir.'),
            ('Envíos', 'Tarifas, zonas y transportistas configurados, con etiquetas y seguimiento.'),
            ('SEO para tiendas', 'URLs claras, datos estructurados de producto, sitemap y metaetiquetas por producto y categoría.'),
            ('Emails de pedido', 'Confirmación, envío y recibo con tu marca, conectados con tu herramienta de email marketing.'),
            ('Panel editable', 'Subes productos y gestionas pedidos sin código, con un tutorial grabado para tu tienda.'),
        ],
        'plans_h': ('Tres niveles', 'según tu catálogo.'),
        'plans_sub': 'Precio cerrado antes de empezar. Shopify tiene además su propia cuota mensual, que pagas directamente a la plataforma.',
        'plans': [
            {'tag': 'A · Básica', 'name': 'Tienda básica', 'price': '1.490 €', 'num': 1490, 'suffix': '+ IVA',
             'desc': 'Para empezar a vender con un catálogo pequeño y bien presentado.',
             'checks': ['Hasta 30 productos', 'Pagos y envíos configurados', 'SEO para tiendas', 'Lista en 3-4 semanas'],
             'cta': 'Empezar mi tienda', 'wa': 'Hola Jenifer, me interesa una tienda básica.'},
            {'tag': 'B · Media', 'name': 'Tienda con integraciones', 'price': '2.490 €', 'num': 2490, 'suffix': '+ IVA', 'featured': True,
             'desc': 'Más catálogo y tu tienda conectada con las herramientas que ya usas.',
             'checks': ['Hasta 100 productos', 'Integraciones de envío y email', 'Pago aplazado', 'Lista en 4-5 semanas'],
             'cta': 'Quiero esta opción', 'wa': 'Hola Jenifer, me interesa una tienda con integraciones.'},
            {'tag': 'C · Pro', 'name': 'Tienda Pro', 'price': '3.990 €', 'num': 3990, 'suffix': '+ IVA',
             'desc': 'Catálogo amplio y venta también en marketplaces, con el stock sincronizado.',
             'checks': ['Catálogo amplio', 'Marketplaces como Amazon o Etsy', 'Stock sincronizado', 'Lista en 5-6 semanas'],
             'cta': 'Hablar de mi tienda', 'wa': 'Hola Jenifer, me interesa una tienda Pro.'},
        ],
        'pack': {'tag': 'Mantenimiento', 'badge': 'Sin permanencia', 'name': 'Tu tienda siempre al día',
                 'desc': 'Actualizaciones, copias de seguridad, vigilancia y 2 horas al mes para cambios y soporte.',
                 'price': '90 €', 'suffix': '/mes + IVA', 'was': 'Puedes darlo de baja cuando quieras',
                 'cta': 'Me interesa', 'wa': 'Hola Jenifer, me interesa el mantenimiento de tienda online.'},
        'guarantees': ['Pago en 2 plazos: 50 % al firmar y 50 % al lanzar', 'Si la fase de diseño no te convence, te devuelvo el 100 %',
                       'Las comisiones de pago las cobra cada pasarela, no yo'],
        'work': ['martilota', 'olia-workplace', 'juli-manitas'], 'work_h': ('Más trabajo', 'de la agencia.'),
        'process_h': ('Tu tienda lista', 'en 3-6 semanas.'),
        'process': [
            ('Estrategia y diseño', 'Semanas 1-2', 'Definimos catálogo, categorías y el camino de compra, y diseño la tienda completa antes de programar.'),
            ('Desarrollo y configuración', 'Semanas 2-4', 'Monto la tienda con el diseño propio y configuro pagos, envíos e impuestos.'),
            ('Carga de productos', 'Semanas 4-5', 'Subo tu catálogo (30 productos incluidos en la básica) con fotos optimizadas y descripciones pensadas para Google.'),
            ('Pruebas y lanzamiento', 'Semanas 5-6', 'Compras y envíos de prueba reales, formación en el panel y lanzamiento cuando tú lo apruebes. 3 meses de soporte.'),
        ],
        'extra': {'eyebrow': 'WooCommerce o Shopify', 'h': ('¿Cuál te', 'conviene?'), 'rows': [
            ('WooCommerce', 'Si quieres control total, ya usas WordPress o vas a tener blog, y prefieres no pagar cuota mensual de plataforma: solo hosting, dominio y la comisión de la pasarela.'),
            ('Shopify', 'Si priorizas la facilidad de uso, vendes fuera de España, manejas un inventario complejo o quieres un TPV para tienda física. Tiene cuota mensual según el plan.'),
            ('Cobro lo mismo en los dos', 'Por eso te recomiendo el que de verdad encaja con tu caso en la primera llamada, sin intereses de por medio.'),
        ]},
        'faq_h': ('Lo que siempre', 'me preguntan.'),
        'faq': [
            ('¿WooCommerce o Shopify?', 'WooCommerce si quieres control total y sin cuota mensual de plataforma; Shopify si priorizas la facilidad y vendes fuera. Te lo recomiendo según tu caso en la primera llamada.'),
            ('¿Cuánto cuesta una tienda online?', 'La tienda básica, desde <strong>1.490 €</strong>; con integraciones, desde <strong>2.490 €</strong>, y la Pro, desde <strong>3.990 €</strong>, siempre + IVA. Shopify tiene además su cuota mensual.'),
            ('¿Incluye los pagos?', 'Sí: tarjeta, Bizum, PayPal y pago aplazado si lo necesitas. Las comisiones las cobra cada pasarela directamente, no yo.'),
            ('¿Puedo añadir productos yo después?', 'Sí. Te dejo el panel preparado y un tutorial para añadir productos, cambiar precios y gestionar pedidos sin código.'),
            ('¿Está pensada para el móvil?', 'Sí. Diseño primero la versión de móvil, porque es donde empiezan la mayoría de las compras, y después la adapto al ordenador.'),
            ('¿Tienes mantenimiento mensual?', 'Sí, desde <strong>90 €/mes</strong>: actualizaciones, copias de seguridad, vigilancia y 2 horas de cambios al mes, sin permanencia.'),
        ],
        'cta': {'eyebrow': 'Primera consulta sin compromiso', 'h': '¿Vendes online? Hagámoslo bien.', 'text': 'Cuéntame qué vendes y cómo trabajas ahora. Te respondo con un presupuesto cerrado en 24 horas.', 'btn': 'Pedir presupuesto'},
    },
    # ------------------------------------------------------------------ SEO local
    {
        'path': 'seo/seo-local', 'label': 'SEO local', 'kicker': 'SEO local · GEO',
        'title': 'SEO local en Barcelona · Google Business Profile · She\'s Digital',
        'description': 'Posicionamiento SEO local en Barcelona: que te encuentren cuando buscan tu servicio en tu zona. Ficha de Google, reseñas y mapas. Desde 290 € + IVA.',
        'service_type': 'SEO local',
        'h1': ('Que te encuentren', 'en tu zona.'),
        'lead': 'Posicionamiento local en Barcelona y Cataluña para aparecer cuando alguien busca tu servicio cerca: más llamadas, más visitas y más clientes reales. Desde 290 €.',
        'cta_primary': 'Pedir valoración gratis', 'wa': 'Hola Jenifer, me gustaría la valoración gratuita de mi ficha de Google.',
        'meta': [('Desde', '290 € + IVA'), ('Primeras mejoras', 'Entre 4 y 8 semanas'), ('Ideal para', 'Negocios con clientes cerca'), ('Permanencia', 'Ninguna')],
        'strip': None,
        'facts': [('Gratis', 'primera valoración de tu ficha de Google'), ('4-8', 'semanas para notar las primeras mejoras'), ('0', 'permanencia: pausas cuando quieras')],
        'focus': {'h': ('Compites con', 'quien está cerca.'),
                  'statement': 'El SEO local te pone delante cuando alguien busca «fisio cerca de mí» o «taxi Santa Susanna» y ya está listo para llamar o visitarte.',
                  'text': 'No compites contra todo internet, sino contra los pocos negocios de tu zona que hacen lo mismo que tú. El premio es el bloque de mapa de Google, con foto, valoración y botón de llamar. Para llegar ahí combino tu ficha de Google, contenido local, reseñas, directorios y SEO técnico.'},
        'includes_h': ('Seis frentes', 'que se refuerzan.'),
        'includes': [
            ('Ficha de Google', 'Categorías, atributos, fotos, servicios, horarios y publicaciones semanales. El corazón del SEO local.'),
            ('Reseñas y reputación', 'Una estrategia para conseguir reseñas reales de forma constante, y respuesta a todas en menos de 24 horas.'),
            ('SEO técnico local', 'Datos estructurados de negocio local, nombre, dirección y teléfono coherentes en todas partes, horarios y preguntas frecuentes.'),
            ('Contenido local', 'Páginas por servicio y ciudad o barrio, y artículos sobre lo que de verdad busca la gente de tu zona.'),
            ('Directorios y enlaces', 'Alta en directorios de calidad y sectoriales, y enlaces desde medios, asociaciones y negocios del barrio.'),
            ('Informe y mejora', 'Cada mes, búsquedas, posiciones, llamadas y rutas desde Google, y ajustes según lo que funciona en tu caso.'),
        ],
        'plans_h': ('Según lo que', 'quieras crecer.'),
        'plans_sub': 'Mensualidades sin permanencia: puedes pausar o cancelar cuando quieras.',
        'plans': [
            {'tag': 'A · Esencial', 'name': 'Mantenimiento Esencial', 'price': '290 €', 'num': 290, 'suffix': '/mes + IVA',
             'desc': 'Para mantener tu ficha viva y tus reseñas al día.',
             'checks': ['Ficha de Google al día', 'Gestión de reseñas', '1 publicación por semana', 'Informe mensual'],
             'cta': 'Empezar', 'wa': 'Hola Jenifer, me interesa el SEO local Esencial.'},
            {'tag': 'B · Pro', 'name': 'Mantenimiento Pro', 'price': '490 €', 'num': 490, 'suffix': '/mes + IVA', 'featured': True,
             'desc': 'Para ganar posiciones en tu zona con contenido y enlaces.',
             'checks': ['Todo lo del Esencial', 'Contenido local mensual', 'Directorios y enlaces locales', 'Llamada mensual'],
             'cta': 'Quiero esta opción', 'wa': 'Hola Jenifer, me interesa el SEO local Pro.'},
            {'tag': 'C · Premium', 'name': 'Pack Premium', 'price': '790 €', 'num': 790, 'suffix': '/mes + IVA',
             'desc': 'Para sectores y zonas muy competidos, como estética en el centro de Barcelona.',
             'checks': ['Todo lo del Pro', 'Más servicios y barrios', 'Contenido ampliado', 'Seguimiento quincenal'],
             'cta': 'Hablar de mi caso', 'wa': 'Hola Jenifer, me interesa el SEO local Premium.'},
        ],
        'pack': {'tag': 'Para empezar', 'badge': 'Pago único', 'name': 'Auditoría y puesta a punto',
                 'desc': 'Analizo tu ficha, tu web y tu competencia, y lo dejo todo optimizado: la base para crecer, con o sin mantenimiento después.',
                 'price': '290 €', 'suffix': '+ IVA', 'was': 'Incluye un informe con el plan de acción',
                 'cta': 'Quiero la auditoría', 'wa': 'Hola Jenifer, me interesa la auditoría y puesta a punto de SEO local.'},
        'guarantees': ['Sin permanencia: pausas o cancelas cuando quieras', 'Si en 6 meses no hay mejora medible, te devuelvo 3 mensualidades',
                       'Tu ficha de Google sigue siendo tuya: solo pido acceso de gestor'],
        'work': ['taxi-santa-susanna', 'alma-salinas', 'punt-i-copia'], 'work_h': ('Webs preparadas', 'para el mapa.'),
        'process_h': ('Sabes en qué fase', 'estamos.'),
        'process': [
            ('Auditoría', 'Semanas 1-2', 'Analizo tu ficha, tu web, tu competencia y las búsquedas de tu zona, y te entrego un plan priorizado.'),
            ('Puesta a punto', 'Semanas 2-4', 'Ficha de Google al 100 %, datos estructurados, datos de contacto coherentes y páginas por servicio y zona.'),
            ('Crecimiento', 'Meses 2-4', 'Contenido local, directorios y reseñas. Empiezas a aparecer y a recibir llamadas desde Google.'),
            ('Ampliar', 'Del mes 4 en adelante', 'Más búsquedas, más barrios o más servicios, con un informe mensual de lo que funciona.'),
        ],
        'extra': {'eyebrow': 'Sectores', 'h': ('Donde el SEO local', 'más se nota.'), 'rows': [
            ('Salud y bienestar', 'Clínicas, fisios, dentistas, osteópatas y psicólogos. Aquí la búsqueda local y las reseñas lo son casi todo.'),
            ('Hostelería y comercio', 'Restaurantes, bares, cafeterías y tiendas de barrio. El mapa de Google es tu mejor escaparate.'),
            ('Servicios del hogar', 'Fontaneros, electricistas, reformas o jardinería: búsquedas urgentes con mucha intención de contratar.'),
            ('Belleza', 'Peluquerías, barberías y estética, que viven de las reseñas y de aparecer en «cerca de mí».'),
            ('Transporte', 'Taxis, transfers, alquileres y autoescuelas.'),
            ('Servicios profesionales', 'Gestorías, abogados, asesores o arquitectos: quien busca uno en su ciudad ya quiere contratar.'),
        ]},
        'faq_h': ('Lo que siempre', 'me preguntan.'),
        'faq': [
            ('¿Qué es el SEO local?', 'Es optimizar tu negocio para aparecer en búsquedas con intención local, como «fisio Barcelona» o «fontanero cerca de mí». Combina tu ficha de Google, contenido local, directorios y reseñas.'),
            ('¿Cuándo veré resultados?', 'Las primeras mejoras en tu ficha (llamadas, rutas, visitas) llegan en <strong>4-8 semanas</strong>. Un posicionamiento sólido necesita <strong>3-6 meses</strong> de trabajo constante. Quien promete resultados en una semana no está siendo honesto.'),
            ('¿Cuánto cuesta?', 'La auditoría y puesta a punto, <strong>290 €</strong> en pago único. El mantenimiento, de <strong>290 a 790 €/mes</strong> según lo competido de tu sector y tu zona, siempre + IVA.'),
            ('¿Sirve si trabajo solo en internet?', 'Si vendes a toda España sin foco en una zona, te conviene más el SEO general. Si tus clientes están en un área concreta, aunque trabajes en remoto, el SEO local te trae contactos de allí.'),
            ('¿Tengo que darte acceso a mi ficha de Google?', 'Sí, como gestor, no como propietario: la ficha sigue siendo tuya. Si aún no tienes, te ayudo a crearla y verificarla sin coste extra.'),
            ('¿Me garantizas el primer puesto?', 'No. Nadie puede garantizar honestamente el primer puesto de Google. Lo que sí garantizo es trabajar para mejorar tu visibilidad y tus llamadas: si en 6 meses no hay mejora medible, te devuelvo 3 mensualidades.'),
        ],
        'cta': {'eyebrow': 'Valoración gratuita', 'h': '¿Quieres que te encuentren cuando importa?', 'text': 'Le echo un vistazo a tu ficha de Google y te digo qué mejoraría. Si encajamos, lo planificamos; si no, te quedas con las ideas.', 'btn': 'Pedir valoración gratis'},
    },
    # ------------------------------------------------------------------ Redes sociales
    {
        'path': 'redes-sociales', 'label': 'Redes sociales', 'kicker': 'Gestión de redes sociales',
        'title': 'Gestión de redes sociales en Barcelona · Instagram, TikTok y LinkedIn · She\'s Digital',
        'description': 'Gestión de redes sociales en Barcelona: estrategia, contenido y community management para Instagram, TikTok y LinkedIn. Desde 390 €/mes + IVA, sin permanencia.',
        'service_type': 'Gestión de redes sociales',
        'h1': ('Tu marca, con', 'una voz coherente.'),
        'lead': 'Estrategia, contenido y community management para Instagram, TikTok y LinkedIn. Trabajo por objetivos, no por número de posts. Desde 390 €/mes, sin permanencia.',
        'cta_primary': 'Pedir valoración gratis', 'wa': 'Hola Jenifer, me gustaría una valoración de mis redes sociales.',
        'meta': [('Desde', '390 €/mes + IVA'), ('Resultados', 'Tracción en 2-3 meses'), ('Redes', 'Instagram, TikTok y LinkedIn'), ('Permanencia', 'Ninguna, con 15 días de aviso')],
        'strip': None,
        'facts': [('0', 'permanencia: solo 15 días de aviso'), ('24 h', 'para responder comentarios y mensajes'), ('1', 'informe y llamada de estrategia al mes')],
        'focus': {'h': ('No publico', 'por publicar.'),
                  'statement': 'Cada publicación tiene un objetivo: posicionar tu marca, crear comunidad o atraer clientes. Si no lo tiene, no sale.',
                  'text': 'Antes de crear contenido definimos quién es tu cliente, qué quieres conseguir y en qué redes merece la pena estar. Mi promesa: una voz coherente, contenido con criterio y resultados que se pueden medir, sin perseguir tendencias que no encajan con tu marca.'},
        'includes_h': ('Seis frentes', 'que se refuerzan.'),
        'includes': [
            ('Estrategia y calendario', 'Pilares de contenido, calendario editorial y objetivos medibles para cada red.'),
            ('Diseño visual', 'Posts, carruseles, stories y reels con tu identidad, y plantillas para crecer sin perder coherencia.'),
            ('Textos con criterio', 'Textos que aportan, no relleno, y hashtags investigados para tu sector.'),
            ('Reels y vídeo', 'Guion, edición y publicación. Si grabas tú, te paso una guía para que salgan bien.'),
            ('Community management', 'Respuesta a comentarios y mensajes en menos de 24 horas, con tu tono, no en piloto automático.'),
            ('Análisis y mejora', 'Informe mensual con alcance, interacción y contactos, y ajustes según los datos.'),
        ],
        'plans_h': ('Tres packs', 'según tu momento.'),
        'plans_sub': 'Sin permanencia. Empezamos por donde tiene sentido y crecemos cuando hay tracción.',
        'plans': [
            {'tag': 'A · Esencial', 'name': 'Pack Inicio', 'price': '390 €', 'num': 390, 'suffix': '/mes + IVA',
             'desc': 'Presencia profesional en una red, sin saturarte.',
             'checks': ['1 red: Instagram, TikTok o LinkedIn', '8 posts al mes y stories', 'Calendario editorial', 'Community management', 'Informe mensual'],
             'cta': 'Empezar', 'wa': 'Hola Jenifer, me interesa el pack Inicio de redes.'},
            {'tag': 'B · Profesional', 'name': 'Pack Crecimiento', 'price': '690 €', 'num': 690, 'suffix': '/mes + IVA', 'featured': True,
             'desc': 'Para consolidar dos redes y empezar a generar contactos.',
             'checks': ['2 redes', '16 posts y 4 reels al mes', 'Estrategia trimestral', 'Community management prioritario', 'Informe con indicadores'],
             'cta': 'Quiero este pack', 'wa': 'Hola Jenifer, me interesa el pack Crecimiento de redes.'},
            {'tag': 'C · Premium', 'name': 'Pack Escalado', 'price': '1.190 €', 'num': 1190, 'suffix': '/mes + IVA',
             'desc': 'Para marcas con producto definido que quieren crecer con contenido y anuncios.',
             'checks': ['3 redes', '24 posts y 8 reels al mes', 'Anuncios en Meta y TikTok', 'Colaboraciones con creadores', 'Estrategia mensual'],
             'cta': 'Hablar de mi marca', 'wa': 'Hola Jenifer, me interesa el pack Escalado de redes.'},
        ],
        'pack': None,
        'guarantees': ['Sin permanencia: pausas o cancelas con 15 días de aviso', 'Vista previa semanal para validar antes de publicar',
                       'El presupuesto de anuncios va aparte, directo a la plataforma'],
        'work': ['olia-workplace', 'alma-salinas', 'martilota'], 'work_h': ('Más trabajo', 'de la agencia.'),
        'process_h': ('Cuotas claras,', 'sin sorpresas.'),
        'process': [
            ('Valoración gratuita', 'Día 1', 'Reviso tus redes, tu competencia y tu público, y te paso un plan de acción sin compromiso.'),
            ('Estrategia y arranque', 'Semanas 1-2', 'Pilares de contenido, calendario, tono de voz y referencias visuales. Te pido los accesos.'),
            ('Producción y publicación', 'Cada semana', 'Diseño, escribo y programo el contenido, y te enseño una vista previa para que lo valides.'),
            ('Análisis y ajuste', 'Cada mes', 'Informe y una llamada de estrategia: lo que funciona se repite y lo que no, se cambia.'),
        ],
        'extra': {'eyebrow': 'Redes', 'h': ('Donde está', 'tu cliente.'), 'rows': [
            ('Instagram', 'Para marcas visuales: belleza, moda, decoración, hostelería o salud. Reels, carruseles y mensajes como canal de venta.'),
            ('TikTok', 'Si buscas mucho alcance y tu producto se entiende mejor en vídeo. Ideal para marcas con personalidad y contenido educativo.'),
            ('LinkedIn', 'Imprescindible para servicios profesionales y empresas: posiciona tu autoridad y atrae clientes de empresa.'),
            ('Pinterest', 'Infravalorada. Si vendes productos físicos o tu marca tiene un mundo visual, trae visitas muy cualificadas.'),
        ]},
        'faq_h': ('Lo que siempre', 'me preguntan.'),
        'faq': [
            ('¿En qué redes trabajas?', 'Sobre todo Instagram, TikTok y LinkedIn, y también Pinterest o Facebook si tu sector lo justifica. La estrategia inicial decide en cuáles invertir.'),
            ('¿Cuánto cuesta gestionar las redes?', 'Pack Inicio (1 red), desde <strong>390 €/mes</strong>; Crecimiento (2 redes), <strong>690 €/mes</strong>, y Escalado (3 redes y anuncios), desde <strong>1.190 €/mes</strong>, siempre + IVA y sin permanencia.'),
            ('¿Quién crea el contenido?', 'Yo: diseño, textos, planificación, programación y community. Si necesitas fotos o vídeo profesional, te pongo en contacto con fotógrafos de confianza (presupuesto aparte).'),
            ('¿Cuándo se ven los resultados?', 'La tracción real se nota en <strong>2-3 meses</strong>, y los resultados sostenidos, hacia los <strong>6 meses</strong>. Quien promete explotar en 30 días miente o usa atajos peligrosos.'),
            ('¿Hay permanencia?', 'No. Es una cuota mensual sin contrato de permanencia: puedes pausar o cancelar avisando con 15 días.'),
            ('¿Gestionas anuncios?', 'Sí, en el pack Escalado incluyo anuncios en Meta (Facebook e Instagram) y TikTok. El presupuesto de inversión va aparte y directo a la plataforma.'),
        ],
        'cta': {'eyebrow': 'Valoración gratuita', 'h': '¿Hacemos que tu marca se vea?', 'text': 'Reviso tus redes y te propongo un plan de acción, sin compromiso.', 'btn': 'Pedir valoración gratis'},
    },
]


def e(s):
    return escape(s, quote=True)


def h2(pair):
    return f'{e(pair[0])}<br /><em>{e(pair[1])}</em>'


def wa(text):
    return 'https://wa.me/34637889942?text=' + quote(text)


def plain(html):
    return re.sub(r'<[^>]+>', '', html)


def page(s):
    depth = s['path'].count('/') + 2
    up = '../' * depth
    n = 0

    def num():
        nonlocal n
        n += 1
        return f'{n:02d}'

    offers = [{'@type': 'Offer', 'name': p['name'], 'priceCurrency': 'EUR', 'price': str(p['num']),
               'priceSpecification': {'@type': 'PriceSpecification', 'price': str(p['num']), 'priceCurrency': 'EUR', 'valueAddedTaxIncluded': False}}
              for p in s['plans']]
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'Service', 'name': s['kicker'], 'serviceType': s['service_type'], 'areaServed': {'@type': 'City', 'name': 'Barcelona'},
         'provider': {'@type': 'ProfessionalService', 'name': "She's Digital", 'url': SITE + '/'},
         'offers': offers, 'description': s['description'], 'url': f'{SITE}/servicios/{s["path"]}/'},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Servicios', 'item': SITE + '/servicios/'},
            {'@type': 'ListItem', 'position': 3, 'name': s['label'], 'item': f'{SITE}/servicios/{s["path"]}/'}]},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': plain(a)}} for q, a in s['faq']]},
    ]}

    meta = '\n'.join(f'            <div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in s['meta'])
    facts = '\n'.join(f'        <li data-reveal><strong>{e(a)}</strong><span>{e(b)}</span></li>' for a, b in s['facts'])

    strip = ''
    if s['strip']:
        items = '\n'.join(f'          <li><a href="{up}proyectos/{k}/"><img src="{up}assets/img/work/{CASES[k][2].replace(".webp", "-sm.webp")}" alt="Web de {e(CASES[k][0])}, {e(CASES[k][1].lower())}" width="720" height="450" /></a></li>' for k in s['strip'])
        strip = f'''
      <!-- Tira de proyectos reales: avanza con el scroll -->
      <div class="sv-strip" aria-label="Algunas webs hechas por She's Digital">
        <ul class="sv-strip__track" data-strip>
{items}
        </ul>
      </div>
'''

    focus_n, inc_n, plans_n = num(), num(), num()
    includes = '\n'.join(f'          <li data-reveal><span class="cs-points__n">{k + 1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>' for k, (t, d) in enumerate(s['includes']))

    def plan_html(p):
        featured = p.get('featured')
        badge = ' <span class="plan__badge">La más elegida</span>' if featured else ''
        checks = '\n'.join(f'              <li>{e(c)}</li>' for c in p['checks'])
        btn = (f'<a class="btn btn--dark plan__cta" href="{wa(p["wa"])}">{e(p["cta"])} {ARROW}</a>' if featured
               else f'<a class="btn btn--line plan__cta" href="{wa(p["wa"])}">{e(p["cta"])}</a>')
        return f'''          <li class="plan{' plan--featured' if featured else ''}" data-reveal>
            <p class="plan__tag">{e(p['tag'])}{badge}</p>
            <h3 class="plan__name">{e(p['name'])}</h3>
            <p class="plan__price"><span>desde</span> {e(p['price'])} <small>{e(p['suffix'])}</small></p>
            <p class="plan__desc">{e(p['desc'])}</p>
            <ul class="checks">
{checks}
            </ul>
            {btn}
          </li>'''
    plans = '\n'.join(plan_html(p) for p in s['plans'])

    pack = ''
    if s['pack']:
        k = s['pack']
        pack = f'''
        <div class="pack" data-reveal>
          <div>
            <p class="plan__tag">{e(k['tag'])} <span class="plan__badge">{e(k['badge'])}</span></p>
            <h3 class="plan__name">{e(k['name'])}</h3>
            <p class="plan__desc">{e(k['desc'])}</p>
          </div>
          <div class="pack__price">
            <p class="plan__price">{e(k['price'])} <small>{e(k['suffix'])}</small></p>
            <p class="pack__was">{e(k['was'])}</p>
            <a class="btn btn--dark" href="{wa(k['wa'])}">{e(k['cta'])} {ARROW}</a>
          </div>
        </div>
'''
    guarantees = '\n'.join(f'          <li>{g}</li>' for g in s['guarantees'])

    work_n = num()
    cards = '\n'.join(f'''        <li class="case">
          <a class="case__link" href="{up}proyectos/{k}/">
            <figure class="case__media" data-cursor-label="Ver caso"><img src="{up}assets/img/work/{CASES[k][2]}" alt="Portada de la web de {e(CASES[k][0])}" width="1440" height="900" loading="lazy" /></figure>
            <div class="case__meta"><span class="case__sector">{e(CASES[k][1])}</span><h3 class="case__title">{e(CASES[k][0])}</h3><p class="case__text">{e(CASES[k][3])}</p></div>
          </a>
        </li>''' for k in s['work'])

    proc_n = num()
    steps = '\n'.join(f'''          <li class="step" data-reveal>
            <span class="step__num">{k + 1:02d}</span>
            <h3 class="step__title">{e(t)}</h3>
            <p class="step__when">{e(w)}</p>
            <p>{e(d)}</p>
          </li>''' for k, (t, w, d) in enumerate(s['process']))

    extra = ''
    if s['extra']:
        x = s['extra']
        xn = num()
        rows = '\n'.join(f'          <li class="index__row" data-reveal><div class="index__link sv-tech__row"><span class="index__num">{k + 1:02d}</span><span class="index__name">{e(a)}</span><span class="index__desc">{e(b)}</span></div></li>' for k, (a, b) in enumerate(x['rows']))
        extra = f'''
    <!-- ============ {e(x['eyebrow'])} ============ -->
    <section class="section sv-tech" aria-labelledby="extra-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow" data-reveal>{xn} — {e(x['eyebrow'])}</p>
          <h2 class="h2" id="extra-title" data-split>{h2(x['h'])}</h2>
        </header>
        <ul class="index sv-tech__list">
{rows}
        </ul>
      </div>
    </section>
'''

    faq_n = num()
    faq = '\n'.join(f'''          <details class="qa" data-reveal>
            <summary>{e(q)} <span class="qa__icon" aria-hidden="true"></span></summary>
            <div class="qa__body"><p>{a}</p></div>
          </details>''' for q, a in s['faq'])
    c = s['cta']

    return f'''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(s['title'])}</title>
  <meta name="description" content="{e(s['description'])}" />
  <!-- Versión 2 en revisión: la página oficial sigue en sheisdigitalab.com -->
  <meta name="robots" content="noindex, nofollow" />
  <link rel="canonical" href="{SITE}/servicios/{s['path']}/" />
  <meta property="og:title" content="{e(s['title'])}" />
  <meta property="og:image" content="{up}assets/img/og-cover.jpg" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="{up}assets/img/favicon.svg" type="image/svg+xml" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@400;500;600&display=swap" />
  <link rel="stylesheet" href="{up}assets/css/styles.css" />
  <link rel="stylesheet" href="{up}assets/css/case.css" />
  <link rel="stylesheet" href="{up}assets/css/service.css" />
  <script>
    (function (d) {{
      var r = d.documentElement; r.classList.add('js');
      var manual = false;
      try {{ manual = localStorage.getItem('sd-motion') === 'reduce'; }} catch (e) {{}}
      if (manual) r.classList.add('reduce-motion');
      if (!manual && !matchMedia('(prefers-reduced-motion: reduce)').matches) {{
        r.classList.add('is-anim');
        setTimeout(function () {{ if (!window.gsap) r.classList.remove('is-anim'); }}, 3000);
      }}
    }})(document);
  </script>
  <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body class="service-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <!-- ============ Cabecera ============ -->
  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="{up}" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="{up}assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="{up}#servicios" aria-current="true">Servicios</a>
        <a href="{up}#proyectos">Proyectos</a>
        <a href="{up}#proceso">Proceso</a>
        <a href="{up}#sobre-mi">Sobre mí</a>
        <a href="{up}#tarifas">Tarifas</a>
        <a href="{up}#faq">FAQ</a>
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

    <!-- ============ Cabecera del servicio ============ -->
    <section class="cs-hero sv-hero" id="top" aria-labelledby="sv-title">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta" data-hero="fade">
          <ol>
            <li><a href="{up}">Inicio</a></li>
            <li><a href="{up}#servicios">Servicios</a></li>
            <li aria-current="page">{e(s['label'])}</li>
          </ol>
        </nav>

        <p class="eyebrow" data-hero="fade">Servicio · {e(s['kicker'])}</p>
        <h1 class="sv-title" id="sv-title">
          <span class="hero__line"><span class="hero__line-in" data-hero="line">{e(s['h1'][0])}</span></span>
          <span class="hero__line"><span class="hero__line-in" data-hero="line"><span class="sv-mark">{e(s['h1'][1])}</span></span></span>
        </h1>

        <div class="cs-hero__grid sv-hero__grid">
          <div>
            <p class="cs-hero__lead" data-hero="fade">{e(s['lead'])}</p>
            <div class="sv-actions" data-hero="fade">
              <a href="{wa(s['wa'])}" class="btn btn--dark btn--magnetic">{e(s['cta_primary'])} {ARROW}</a>
              <a href="#opciones" class="btn btn--line">Ver opciones y precios</a>
            </div>
          </div>

          <dl class="cs-meta" data-hero="fade">
{meta}
          </dl>
        </div>
      </div>
{strip}
      <ul class="wrap cs-facts" aria-label="En resumen">
{facts}
      </ul>
    </section>

    <!-- ============ Enfoque ============ -->
    <section class="section cs-block" aria-labelledby="que-title">
      <div class="wrap cs-block__grid">
        <header class="cs-block__head">
          <p class="eyebrow" data-reveal>{focus_n} — El enfoque</p>
          <h2 class="h2" id="que-title" data-split>{h2(s['focus']['h'])}</h2>
        </header>
        <div class="cs-block__body">
          <p class="cs-statement" data-words>{e(s['focus']['statement'])}</p>
          <p data-reveal>{e(s['focus']['text'])}</p>
        </div>
      </div>
    </section>

    <!-- ============ Qué incluye ============ -->
    <section class="section cs-block sv-includes" aria-labelledby="inc-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow" data-reveal>{inc_n} — Qué incluye</p>
          <h2 class="h2" id="inc-title" data-split>{h2(s['includes_h'])}</h2>
        </header>
        <ol class="cs-points">
{includes}
        </ol>
      </div>
    </section>

    <!-- ============ Opciones y precios ============ -->
    <section class="section sv-plans" id="opciones" aria-labelledby="plans-title">
      <div class="wrap">
        <header class="cs-block__head cs-block__head--wide">
          <p class="eyebrow" data-reveal>{plans_n} — Opciones y precios</p>
          <h2 class="h2" id="plans-title" data-split>{h2(s['plans_h'])}</h2>
          <p class="sv-sub" data-reveal>{e(s['plans_sub'])}</p>
        </header>

        <ul class="plans">
{plans}
        </ul>
{pack}
        <ul class="guarantees" data-reveal>
{guarantees}
        </ul>
      </div>
    </section>

    <!-- ============ Proyectos ============ -->
    <section class="work sv-work" aria-labelledby="sv-work-title">
      <div class="wrap work__head">
        <div>
          <p class="eyebrow" data-reveal>{work_n} — Proyectos</p>
          <h2 class="h2" id="sv-work-title" data-split>{h2(s['work_h'])}</h2>
        </div>
        <a class="btn btn--mint" href="{up}#proyectos">Ver todos los proyectos</a>
      </div>
      <ul class="work__track sv-work__grid">
{cards}
      </ul>
    </section>

    <!-- ============ Proceso ============ -->
    <section class="section process" aria-labelledby="sv-process-title">
      <div class="wrap">
        <header class="head">
          <p class="eyebrow eyebrow--light" data-reveal>{proc_n} — Cómo trabajamos</p>
          <h2 class="h2" id="sv-process-title" data-split>{h2(s['process_h'])}</h2>
        </header>
        <div class="process__line" aria-hidden="true"><span data-process-line></span></div>
        <ol class="process__steps">
{steps}
        </ol>
      </div>
    </section>
{extra}
    <!-- ============ FAQ ============ -->
    <section class="section faq" aria-labelledby="faq-title">
      <div class="wrap faq__grid">
        <header class="head head--sticky">
          <p class="eyebrow" data-reveal>{faq_n} — Preguntas frecuentes</p>
          <h2 class="h2" id="faq-title" data-split>{h2(s['faq_h'])}</h2>
        </header>
        <div class="faq__list">
{faq}
        </div>
      </div>
    </section>

    <!-- ============ CTA ============ -->
    <section class="audit cs-cta" id="contacto" aria-labelledby="cta-title">
      <div class="wrap audit__inner">
        <div>
          <p class="eyebrow" data-reveal>{e(c['eyebrow'])}</p>
          <h2 class="h2" id="cta-title" data-split>{e(c['h'])}</h2>
        </div>
        <div class="audit__body" data-reveal>
          <p>{e(c['text'])}</p>
          <div class="cs-cta__actions">
            <a class="btn btn--dark btn--magnetic" href="{wa(s['wa'])}">
              {WA_ICON}
              {e(c['btn'])}
            </a>
            <a class="btn btn--line" href="tel:+34637889942">Llamar al 637 889 942</a>
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
          <img src="{up}assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Agencia digital de Jenifer Jaldo.<br />Branding · Web · Ecommerce · SEO/GEO · Social.</p>
        </div>
        <nav aria-label="Pie: servicios">
          <h3>Servicios</h3>
          <ul>
            <li><a href="{up}servicios/branding/">Branding</a></li>
            <li><a href="{up}servicios/diseno-web/">Diseño web</a></li>
            <li><a href="{up}servicios/ecommerce/">Ecommerce</a></li>
            <li><a href="{up}servicios/seo/seo-local/">SEO local</a></li>
            <li><a href="{up}servicios/redes-sociales/">Redes sociales</a></li>
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
        <button class="motion-toggle" type="button" aria-pressed="false" data-motion-toggle>Reducir animaciones</button>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="{up}assets/js/main.js" defer></script>
  <script src="{up}assets/js/service.js" defer></script>
</body>
</html>
'''


if __name__ == '__main__':
    for s in SERVICES:
        out = ROOT / 'servicios' / s['path'] / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(s), encoding='utf-8')
        print('ok', out.relative_to(ROOT))
