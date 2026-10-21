#!/usr/bin/env python3
"""Genera blog/index.html y blog/{slug}/index.html"""

import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---------------------------------------------------------------------------
# Datos de artículos
# ---------------------------------------------------------------------------
ARTICLES = [
    {
        "slug": "cuanto-cuesta-una-pagina-web",
        "title": "¿Cuánto cuesta una página web en 2026?",
        "category": "Guía de precios",
        "category_slug": "guia-de-precios",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "4 min de lectura",
        "description": "Rangos de precio reales para webs en España en 2026. Landing, multi-página, tienda online y a medida. Sin letra pequeña.",
        "body": """
<p>Es la primera pregunta que me hace casi todo el mundo. Y la respuesta sincera no le gusta a nadie: depende. Pero tranquila, que no te dejo así. Te cuento de qué depende y te doy rangos reales, que para eso has entrado.</p>

<h2>De qué depende el precio</h2>

<p>Cuando alguien me pregunta el precio de "una web", yo le pregunto de vuelta: ¿qué web? Porque no es lo mismo una página sencilla para presentar tu negocio que una tienda online con cientos de productos, pagos y envíos. Ahí está la clave.</p>

<p>Lo que más mueve el precio es el tipo de web y todo lo que tiene que hacer: cuántas páginas, si el diseño es propio o una plantilla, si necesitas reservas, pagos, varios idiomas… Y un detalle que mucha gente no valora: si hay que escribir los textos y conseguir buenas fotos, porque eso también es trabajo.</p>

<h2>Rangos reales en 2026</h2>

<p>Vamos a lo que te interesa. Estos son los precios que se manejan hoy en España, para que vayas con una idea:</p>

<ul>
  <li>Una página sencilla (landing): entre <strong>450 € y 900 €</strong></li>
  <li>Web de varias páginas para tu negocio: de <strong>1.200 € a 3.000 €</strong></li>
  <li>Tienda online: de <strong>1.500 € a 5.000 €</strong>, según lo que vendas</li>
  <li>Algo a medida o más complejo: <strong>a partir de 3.000 €</strong></li>
</ul>

<p>Y un aviso de amiga: si ves una web profesional por 150 €, huye. O es una plantilla rellenada en un rato, o te van a ir cobrando "extras" que nadie te avisó.</p>

<h2>¿Por qué tanta diferencia?</h2>

<p>Porque "página web" significa cosas muy distintas. Una plantilla genérica montada en una tarde no tiene nada que ver con una web pensada para tu sector, que carga rápida y que está hecha para que te llamen. Lo barato sale caro el día que te das cuenta de que esa web no te ha traído ni un solo cliente.</p>

<h2>Lo que casi nadie te cuenta</h2>

<p>Aparte del diseño, una web tiene unos gastillos que conviene que sepas desde el principio. El dominio (el nombre de tu web) ronda los 12 € al año. El hosting, donde vive tu web, va de 5 a 20 € al mes según dónde la alojes. Y luego está el mantenimiento, para que todo siga actualizado y seguro.</p>

<p>Te lo digo de entrada porque odio las sorpresas y supongo que tú también.</p>

<h2>Cómo lo hago yo</h2>

<p>En She's Digital te doy el precio cerrado en 24 horas. Me cuentas qué necesitas, le doy una vuelta, y te digo lo que cuesta. Punto. Sin letra pequeña y sin que la cifra crezca por el camino. Lo que te digo es lo que pagas.</p>

<p>Si lo que te frena no es el precio sino el tiempo, te recomiendo leer también <a href="../../blog/cuanto-tarda-pagina-web/">cuánto tarda en hacerse una página web</a>. Y si quieres ver mis servicios al detalle, pásate por <a href="../../servicios/diseno-web/">diseño y desarrollo web</a>.</p>
""",
    },
    {
        "slug": "wordpress-o-web-a-medida",
        "title": "WordPress o web a medida: ¿cuál elegir para tu negocio?",
        "category": "Cómo elegir",
        "category_slug": "como-elegir",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "4 min de lectura",
        "description": "Las dos opciones son buenas. La mala es elegir la que no toca. Te lo explico sin tecnicismos para que decidas con criterio.",
        "body": """
<p>Las dos opciones son buenas, que quede claro. La mala es elegir la que no toca para tu caso. Así que te lo explico en cristiano, sin tecnicismos, para que decidas tú con criterio y no porque lo diga el primero que pase.</p>

<h2>Qué es WordPress</h2>

<p>Seguramente lo has oído mil veces. WordPress es el sistema con el que está hecha casi la mitad de las webs del mundo, y por algo será. Lo bueno es que después puedes entrar tú y cambiar textos o fotos sin saber programar ni llamar a nadie. Y tiene complementos para casi todo lo que se te ocurra: tienda, reservas, formularios, varios idiomas…</p>

<p>Si quieres una web profesional, con buena relación entre lo que pagas y lo que consigues, y poder retocarla tú después, WordPress suele ser tu sitio.</p>

<h2>Qué es una web a medida</h2>

<p>Aquí no partimos de ninguna base: se programa todo desde cero. Eso te da control absoluto sobre cómo se ve y cómo funciona, sin las limitaciones de una plantilla. ¿El pero? Cuesta más y normalmente no la editas tú sin ayuda.</p>

<p>Tiene sentido cuando necesitas algo realmente único, una experiencia muy concreta, o exprimir la velocidad al máximo.</p>

<h2>En qué se diferencian, al grano</h2>

<p>Si tuviera que resumírtelo: WordPress suele salir más a cuenta y se pone en marcha antes, pero pide algún mantenimiento de vez en cuando. La web a medida es más inversión y más técnica, a cambio de poder afinarla al milímetro. La gran ventaja de WordPress para ti es que podrás cambiar cosas tú misma; con una web a medida eso depende de cómo se haya montado.</p>

<h2>Entonces, ¿cuál elijo?</h2>

<p>Te lo digo claro: para la mayoría de negocios, WordPress. Es profesional, lo editas tú y la relación calidad-precio es difícil de batir. La web a medida la dejo para cuando de verdad hace falta algo especial o un rendimiento de otro nivel.</p>

<p>Y si sigues con dudas, no pasa nada. En una llamada de 15 minutos te digo qué encaja mejor contigo según tu proyecto, tu presupuesto y lo que quieras poder tocar después. Sin venderte humo, que de eso ya hay bastante.</p>

<p>¿Quieres profundizar antes? Léete también <a href="../../blog/cuanto-cuesta-una-pagina-web/">cuánto cuesta una web en 2026</a> y mira mis <a href="../../servicios/diseno-web/">servicios de diseño web</a>.</p>
""",
    },
    {
        "slug": "cuanto-tarda-pagina-web",
        "title": "¿Cuánto tarda en hacerse una página web?",
        "category": "Plazos",
        "category_slug": "plazos",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "3 min de lectura",
        "description": "Plazos reales para webs en España en 2026: desde una landing en 1 semana hasta proyectos complejos. Y cómo puedes acelerarlo sin sacrificar calidad.",
        "body": """
<p>Si me preguntas el precio, te diré que depende. Si me preguntas cuánto tarda, también. Pero como con los precios, te doy plazos reales para que tengas una idea clara antes de meterte en faena.</p>

<h2>De qué depende el tiempo</h2>

<p>El tiempo de una web va de la mano del tipo: no es lo mismo una sola página que una tienda con cien productos. Y tampoco depende solo de quien la hace. Una parte importante depende de ti: tus decisiones, los textos y las fotos. La diferencia entre tardar dos semanas o seis suele estar más en ese lado del que la gente cree.</p>

<h2>Plazos que se manejan hoy</h2>

<p>Para que vayas con una idea, estos son los tiempos típicos en proyectos bien llevados:</p>

<ul>
  <li>Una landing o página sencilla: <strong>1 o 2 semanas</strong></li>
  <li>Web de varias páginas para tu negocio: <strong>3 a 5 semanas</strong></li>
  <li>Tienda online: <strong>4 a 8 semanas</strong>, según lo que vendas y cómo gestiones envíos y pagos</li>
  <li>Algo a medida o muy específico: <strong>desde 6 semanas</strong> en adelante</li>
</ul>

<p>Si alguien te promete "una web en 48 horas" mientras te cobra como una a medida, ya sabes lo que va a pasar: plantilla genérica rellenada deprisa. Las cosas hechas en serio llevan su tiempo.</p>

<h2>Cómo acelerar el proyecto (sin sacrificar calidad)</h2>

<p>Mira, esto es importante porque muchos proyectos se atascan en lo mismo. Lo que más ayuda a que vaya rápido es bastante prosaico:</p>

<ul>
  <li>Tener los textos a mano (o aceptar que los hagamos juntas y reservar un rato para eso).</li>
  <li>Tener fotos decentes. Si no las tienes, lo hablamos al principio y vemos opciones.</li>
  <li>Responder cuando te pasan algo para revisar. Una semana de silencio = una semana de retraso.</li>
  <li>Tener claro qué quieres antes de empezar. Cambios de idea a mitad cuestan tiempo (y dinero).</li>
</ul>

<h2>Cómo lo hago yo</h2>

<p>Te doy el plazo cerrado en el presupuesto. Si te digo que tu web está lista en 4 semanas, está en 4 semanas. Si en mitad del proyecto cambias el alcance, te aviso de cómo afecta y decidimos. Pero el plan inicial se cumple. Por algo lo prometo en la home.</p>

<p>Si todavía no tienes claro el presupuesto, échale un ojo a <a href="../../blog/cuanto-cuesta-una-pagina-web/">cuánto cuesta una web en 2026</a>. Y si quieres ver mis servicios de diseño web, <a href="../../servicios/diseno-web/">ahí está todo</a>.</p>
""",
    },
    {
        "slug": "senales-web-pierde-clientes",
        "title": "10 señales de que tu web está perdiendo clientes",
        "category": "Diagnóstico",
        "category_slug": "diagnostico",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "4 min de lectura",
        "description": "¿Tu web trabaja a tu favor o en tu contra? 10 señales concretas para saberlo. Si reconoces tres o más, algo hay que cambiar.",
        "body": """
<p>Lo más probable es que tu web esté jugando en tu contra y tú ni te hayas enterado. Pasa más de lo que crees. Si reconoces varias de estas señales, cada día se te escapan clientes (y dinero). Léelas sin hacerte trampas al solitario:</p>

<h2>Las 10 señales</h2>

<ol>
  <li><strong>Tarda una eternidad en abrir.</strong> Si pasa de 3 segundos, la mayoría se va antes de ver nada.</li>
  <li><strong>En el móvil se ve fatal.</strong> Y más de la mitad de la gente te visita desde el móvil, así que échale cuentas.</li>
  <li><strong>No se ve claro cómo contactarte.</strong> Si hay que buscar el teléfono con lupa, nadie te escribe.</li>
  <li><strong>No sales en Google.</strong> Cuando alguien busca tu servicio en tu zona y no apareces, para el cliente es como si no existieras.</li>
  <li><strong>Tiene pinta de los años 2000.</strong> Una web vieja da la sensación de que el negocio también lo está.</li>
  <li><strong>No tienes ni idea de quién entra.</strong> Sin una herramienta de medición vas a ciegas y no puedes mejorar.</li>
  <li><strong>Los textos no dicen nada.</strong> Si solo hablas de ti y no de lo que tu cliente necesita, no conectas.</li>
  <li><strong>No da confianza.</strong> Sin testimonios, sin tu cara, sin trabajos reales, la gente duda.</li>
  <li><strong>Cambiar algo es una odisea.</strong> Si no puedes tocar ni una foto sin llamar a alguien, está mal montada.</li>
  <li><strong>No le dice a la gente qué hacer.</strong> Una web sin un "pide presupuesto" o "reserva" bien visible deja al cliente perdido.</li>
</ol>

<h2>¿Cuántas te suenan?</h2>

<p>Si has dicho que sí a tres o más, tu web te está costando clientes ahora mismo, mientras lees esto. La buena noticia es que casi todo tiene arreglo, y muchas veces ni hace falta empezar de cero.</p>

<h2>Te la miro gratis</h2>

<p>Si quieres salir de dudas, te hago una auditoría gratis de tu web en 24 h. La reviso, y te doy mi opinión profesional. Sin compromiso y hablándote claro, sin tecnicismos raros. Escríbeme y te cuento.</p>

<p>Si lo que te interesa es saber qué pasa con la velocidad o cómo te ve Google, mira también <a href="../../blog/aparecer-en-google/">cómo conseguir que tu negocio aparezca en Google</a>.</p>

<p>Y si decides renovarla, en <a href="../../servicios/diseno-web/">diseño y desarrollo web</a> te explico cómo lo hago. Si también quieres mejorar tu visibilidad en Google, échale un ojo al <a href="../../servicios/seo/seo-local/">SEO local</a>.</p>
""",
    },
    {
        "slug": "aparecer-en-google",
        "title": "Cómo conseguir que tu negocio aparezca en Google",
        "category": "Visibilidad",
        "category_slug": "visibilidad",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "5 min de lectura",
        "description": "Los pasos que sí mueven la aguja en Google para un negocio local: Google Business Profile, web optimizada, reseñas y contenido útil.",
        "body": """
<p>Si buscas el nombre de tu negocio en Google y no apareces (o apareces enterrado), tienes un problema gordo. Y si buscas tu servicio en tu zona y tampoco sales, peor todavía. Para tus clientes potenciales, no existes. Te cuento lo que sí mueve la aguja, por orden de importancia.</p>

<h2>Lo primero: tu ficha de Google Business Profile</h2>

<p>Antes que la web, antes que nada. Es la fichita que sale a la derecha cuando alguien busca tu negocio en Google. Si no la tienes creada, es donde tienes que empezar. Es gratis, la tienes en una tarde y, si la cuidas, es de lo que más visitas te trae. Sobre todo si tu negocio es local.</p>

<p>Lo importante de la ficha: que esté completa de verdad. Categoría correcta, descripción con palabras clave de lo que haces, fotos buenas, horario, zona de servicio, servicios concretos. No vale ponerla y dejarla.</p>

<h2>Tu web bien optimizada para tu zona</h2>

<p>El segundo paso es que tu web le diga claramente a Google qué haces y dónde. Eso significa que cosas como el título de tu página y el texto principal mencionen tu servicio y tu ciudad. Sin pasarse, sin forzarlo, pero que esté.</p>

<p>Si vendes muebles en Barcelona, tu web no puede tener un título tipo "Bienvenidos a nuestra empresa". Tiene que decir lo que haces y dónde, en cristiano.</p>

<h2>Las reseñas son lo que más manda en local</h2>

<p>Aquí mucha gente subestima la importancia. Si dos negocios compiten por aparecer cuando alguien busca, Google se fija mucho en quién tiene más reseñas (y mejores). Es el factor número uno del posicionamiento local.</p>

<p>Pide reseñas a tus clientes contentos. No te cortes. Manda un mensaje amable explicándoles cómo dejarla, con el enlace directo. La diferencia entre tener 5 reseñas o 50 es enorme en cómo te ve Google.</p>

<h2>Contenido que responda a lo que buscan</h2>

<p>Cuando alguien escribe en Google una pregunta relacionada con tu sector y tú tienes un artículo en tu web que la responde, Google te premia. Por eso un blog útil tiene sentido. No para escribir por escribir, sino para responder lo que de verdad busca tu cliente.</p>

<p>Si vendes seguros, un artículo tipo "qué seguro de hogar necesito si vivo de alquiler" te trae justo a la gente que está pensando en contratar uno.</p>

<h2>Paciencia y constancia</h2>

<p>Esto no es de hoy para mañana. Google tarda semanas o meses en ver y posicionar lo que haces, sobre todo si tu web es nueva. La gente abandona aquí: lleva un mes con una ficha de Google y se desanima. Aguanta. Lo que se hace bien funciona, solo necesita tiempo.</p>

<h2>Si quieres saber por dónde empezar tú</h2>

<p>Cada negocio está en un punto distinto. Si quieres, le echo un vistazo al tuyo y te doy una valoración rápida gratis. Para que no des palos de ciego.</p>

<p>Si tu enfoque es SEO local de verdad, mira mis <a href="../../servicios/seo/seo-local/">servicios de SEO Local</a>. Y si tu negocio está en Barcelona, te interesa también <a href="../../diseno-web-barcelona/">diseño web en Barcelona</a>.</p>
""",
    },
    {
        "slug": "web-para-restaurante",
        "title": "Qué necesita la web de un restaurante para llenarlo",
        "category": "Para tu negocio",
        "category_slug": "para-tu-negocio",
        "date": "28 de mayo de 2026",
        "date_iso": "2026-05-28",
        "read_time": "4 min de lectura",
        "description": "Lo que necesita la web de un restaurante para convertir visitas en reservas: carta visible, reservas sin comisiones, fotos reales y SEO local.",
        "body": """
<p>Si tienes un restaurante y tu web es una sola página con la carta en PDF y el teléfono perdido en una esquina, te estás dejando reservas encima de la mesa. La cuenta es fácil de hacer: cada cliente que se va a la competencia porque ahí sí encuentra lo que busca, es uno que no entra por tu puerta.</p>

<h2>Una carta que se vea, no un PDF que nadie abre</h2>

<p>El PDF de la carta es el clásico error. La gente lo abre en el móvil, tarda en cargar, se ve diminuto, y se va. La carta tiene que verse directamente en la web, bien legible y fácil de actualizar cuando cambias platos. Si tienes que llamar al "informático" cada vez que subes el precio del menú, está mal montada.</p>

<h2>Reservar tiene que ser fácil y sin intermediarios</h2>

<p>Si la gente reserva por tu web, no pagas comisiones a nadie. Es así de simple. Un buen sistema de reservas online en tu propia web te ahorra entre un 10 y un 15 % que ahora se llevan las plataformas. Y de paso te quedas con los datos del cliente, en vez de regalárselos a un tercero.</p>

<h2>Fotos buenas, no las del móvil del dueño</h2>

<p>Lo siento si te toca. Pero los platos a contraluz, mal enfocados o con flash directo, restan tanto que mejor no tener foto. Una sesión profesional de cuatro o cinco horas con tus platos estrella te dura años. Es la inversión más rentable que puedes hacer después de la web.</p>

<h2>Móvil, móvil, móvil</h2>

<p>La gente busca dónde comer desde el sofá, desde el coche o desde la cola del médico. Si tu web no carga rápido y bonita en el móvil, te buscan por encima. Es la primera cosa que reviso en una auditoría.</p>

<h2>Que Google te encuentre</h2>

<p>Cuando alguien busca "restaurante italiano [tu barrio]" tienes que salir. Para eso necesitas dos cosas: una web bien hecha para SEO local y, sobre todo, una ficha de Google Business Profile cuidada, con fotos, horario y reseñas. Sin esto, no existes para Google.</p>

<h2>Datos de contacto que no haya que buscar</h2>

<p>Teléfono visible. Dirección con el mapa. Botón de WhatsApp. La gente decide en segundos. Si tiene que pelearse para encontrarte, se rinde y se va al de al lado.</p>

<h2>¿Tu web cumple todo esto?</h2>

<p>Si has dicho que no a más de dos, te conviene darle una vuelta. Si quieres que la revise yo, te hago una valoración gratis y te digo por dónde podrías empezar. Sin compromiso ni informes interminables.</p>

<p>Trabajo con mucha hostelería en Cataluña: si te interesa lo que ofrezco para <a href="../../sectores/restaurantes/">restaurantes</a> o lo que estoy haciendo en <a href="../../diseno-web-barcelona/">Barcelona</a>, lo tienes en un par de clics.</p>
""",
    },
    {
        "slug": "seo-local-google-maps",
        "title": "SEO local: cómo aparecer en Google Maps y el mapa de resultados",
        "category": "SEO",
        "category_slug": "seo",
        "date": "Septiembre 2026",
        "date_iso": "2026-09-01",
        "read_time": "7 min de lectura",
        "description": "Cómo funciona el local pack de Google, por qué estar en el mapa es clave para negocios locales y qué pasos concretos dan resultado.",
        "body": """
<p>Cuando alguien escribe «peluquería cerca» o «fontanero urgente Barcelona» en Google, lo primero que aparece es un mapa con tres negocios destacados. Eso se llama local pack. Aparecer ahí con el SEO local bien trabajado es la diferencia entre recibir llamadas todos los días o depender de que alguien ya te conozca de antes.</p>

<h2>Qué es el local pack y por qué todo negocio local quiere estar ahí</h2>

<p>El local pack son los tres resultados con el mapa que aparecen en la primera pantalla de Google cuando alguien hace una búsqueda con intención local. Salen antes que cualquier resultado orgánico normal, ocupan más espacio visual y tienen el botón de llamada directo en el móvil.</p>

<p>Entre el 30 y el 40 % de los clics en búsquedas locales van a esos tres resultados. Si estás ahí, eres visible. Si no estás, empiezas desde el cuarto puesto hacia abajo, y la mayoría de la gente no llega. El SEO local no es suerte ni magia. Es trabajo concreto sobre tu ficha, tu web y tu reputación online.</p>

<h2>Google Business Profile: el punto de partida</h2>

<p>El primer paso para aparecer en el mapa de resultados es tener la ficha de Google Business Profile reclamada, verificada y completa. Suena básico, pero el 60 % de los negocios que me llegan la tienen incompleta, con el horario desactualizado o con fotos de hace cuatro años.</p>

<p>Una ficha bien trabajada tiene: nombre del negocio correcto, categoría principal y secundarias bien elegidas, descripción con palabras clave naturales, horario actualizado incluyendo festivos, mínimo diez fotos subidas por el propio negocio, y el enlace a tu web. Sin ese enlace, la ficha flota sola sin ancla y Google no sabe bien qué eres ni dónde estás.</p>

<p>Publicar actualizaciones regulares en la ficha también ayuda: novedades, ofertas, cambios de horario. No hace falta hacerlo cada día, pero sí cada dos o tres semanas. Google interpreta esa actividad como señal de que el negocio está vivo y atendido.</p>

<h2>Tu web y el SEO local van de la mano</h2>

<p>Google no solo mira tu ficha: mira también tu web para decidir si eres relevante para esa búsqueda local. Una web rápida, bien estructurada y con contenido que menciona tu ciudad y tus servicios refuerza tu posición en el mapa.</p>

<p>Un diseño web pensado para SEO local no es solo estética: es estructura de URL, datos estructurados que Google puede leer, velocidad de carga y contenido que responde a cómo buscan tus clientes reales. Si quieres entender en detalle cómo se trabaja el SEO local para negocios con ubicación física, lo tienes en la <a href="../../servicios/seo/seo-local/">página de servicio</a> con ejemplos concretos.</p>

<h2>Las reseñas: el factor que más mueve el mapa</h2>

<p>Las reseñas de Google son uno de los factores con más peso en el ranking local. Un negocio con 30 reseñas de este año tiene más peso que uno con 200 de hace tres años. Google quiere ver que eres un negocio activo con clientes reales satisfechos. Y responder a las reseñas, tanto a las buenas como a las malas, también suma señales positivas.</p>

<p>La pregunta que siempre me hacen es cómo pedirlas sin resultar pesado. La respuesta es simple: en el momento en que el cliente está satisfecho. Al acabar el servicio, cuando recibes un mensaje de agradecimiento, cuando alguien te recomienda. Hay una forma natural de hacerlo que da resultado sin molestar.</p>

<h2>Palabras clave locales: cuanto más concreto, mejor</h2>

<p>Para el SEO local, las búsquedas más valiosas no son las genéricas. «Peluquería Barcelona» tiene competencia brutal. «Peluquería vegana Gràcia» o «corte mujer sin cita Sant Cugat» tienen menos volumen pero más intención de compra y menos negocios optimizados para ellas.</p>

<p>El trabajo de SEO local consiste en identificar esas búsquedas concretas que tus clientes reales hacen y asegurarte de que tu ficha y tu web están alineadas con ellas. No se trata de forzar palabras clave en todos lados, sino de hablar el idioma de la gente que ya te busca.</p>

<h2>Cuánto tarda el SEO local en dar resultados</h2>

<p>La respuesta honesta: entre dos y cuatro meses para ver movimiento visible, seis para resultados sólidos. Depende de cuánta competencia hay en tu sector y ciudad, del estado de partida de tu ficha y de si tienes web trabajada o no.</p>

<p>Lo que sí es cierto es que el SEO local tiene efecto acumulativo. Cada mes que trabajas en él, la posición mejora. Y a diferencia de la publicidad de pago, cuando dejas de invertir no te caes del mapa de un día para otro.</p>

<h2>Ya tienes web pero no apareces en el mapa</h2>

<p>Si este es tu caso, empieza por leer el artículo sobre <a href="../../blog/aparecer-en-google/">cómo aparecer en Google</a>. Explica los pasos concretos y los errores más comunes que hacen que una web con años de vida siga sin aparecer donde debería.</p>

<p>Y si prefieres que lo revise directamente, me escribes y hacemos una valoración de tu ficha y tu web. Te digo exactamente qué está fallando y qué habría que hacer primero. Sin informe interminable ni compromiso.</p>
""",
    },
    {
        "slug": "web-para-peluqueria",
        "title": "Web para peluquería: qué debe tener y cuánto cuesta en 2026",
        "category": "Diseño web · Sectores",
        "category_slug": "sectores",
        "date": "Septiembre 2026",
        "date_iso": "2026-09-01",
        "read_time": "6 min de lectura",
        "description": "Lo que no puede faltar en la web de una peluquería: precios visibles, reservas sin comisiones, galería real y SEO local. Y cuánto cuesta hacerla bien.",
        "body": """
<p>Si tienes una peluquería y tu única presencia online es Instagram y una ficha de Google con el horario desactualizado, estás dejando que la competencia se lleve a tus clientes más fáciles: los que están buscando ahora mismo dónde cortarse el pelo en tu barrio. La web para peluquería bien hecha no es un capricho, es la diferencia entre una agenda llena y otra a medias.</p>

<h2>Qué debe tener la web de una peluquería (sin excusas)</h2>

<p>Primero lo básico: los servicios y los precios, visibles y claros. La gente no llama para preguntar cuánto cuesta un mechas. O encuentra el precio en tu web o busca en la del salón de al lado. No es personal, es cómo funciona Internet en 2026.</p>

<p>Un sistema de reserva online integrado en tu propia web, no una plataforma de terceros que te cobra comisión por cada cita. Con el formulario correcto y tu calendario sincronizado, las reservas llegan aunque estés con las manos en el tinte y el móvil guardado.</p>

<p>Una galería de trabajos real. En peluquería el portfolio es más importante que en casi cualquier otro sector. La gente quiere ver exactamente qué vas a hacerle al pelo antes de decidir. Fotos propias, bien hechas, que muestren tu estilo y tu nivel. Nada de stock.</p>

<p>Y claro: horario actualizado, dirección con mapa integrado, número de teléfono y WhatsApp en un sitio visible, sin tener que bajar hasta el pie de página para encontrarlos.</p>

<h2>La imagen lo es todo en una peluquería</h2>

<p>Una peluquería no vende solo servicios: vende una experiencia, una estética, una sensación. Tu web tiene que transmitir eso desde el primer segundo. Si la paleta de colores no tiene nada que ver con la decoración del local, si las fotos parecen de banco de imágenes y las tipografías son las que vienen por defecto en cualquier plantilla… ya has perdido.</p>

<p>Esto es branding, y en tu sector es fundamental. Una identidad de marca bien trabajada alinea lo que ven en tu web, en tu Instagram, en tus tarjetas y cuando entran por la puerta. Cuando todo es coherente, la confianza llega sola y la decisión de reservar se acelera.</p>

<h2>Cuánto cuesta en 2026</h2>

<p>Depende de lo que necesitas, pero para darte una referencia real: una web profesional para peluquería, con reservas online, galería y SEO básico bien hecho, suele moverse entre <strong>900 y 2.200 €</strong>. El rango es amplio porque no es lo mismo un estudio unipersonal que un salón con varios estilistas y venta de productos.</p>

<p>Lo que sí te digo: por debajo de 600 € estás comprando problemas. Los creadores de páginas baratos te dan una plantilla que parece de 2014, sin posicionamiento, sin reservas reales integradas y con un panel que no sabrás manejar. Al año la estás rehaciendo.</p>

<p>Un diseño web bien planteado desde el principio te dura cinco años sin tocarla más allá de actualizar contenido. Eso lo amortizas en los primeros meses si la web trae aunque sea dos clientes nuevos al mes que de otra forma no habrían llegado.</p>

<h2>Los errores más comunes que veo en webs de peluquería</h2>

<p>El primero: depender solo de Instagram. Sí, es necesario tenerlo. Pero Instagram no posiciona en Google. Lo que tienes ahí depende del algoritmo para llegar a tu audiencia. Tu web es tuya: aparece cuando alguien la busca, sin pagar publicidad y sin depender de subir contenido tres veces por semana para que te vean.</p>

<p>El segundo: fotos malas. Un primer plano de un corte con luz de neón directa y fondo desordenado resta más de lo que suma. Si no tienes fotos buenas, mejor empieza con menos y bien que con mucho y mal.</p>

<p>El tercero: la web existe pero nadie la encuentra. Sin trabajar el SEO local mínimo, tu web flota sola en Internet. Hay que decirle a Google que estás en tu barrio, que haces lo que haces y que eres la mejor opción.</p>

<h2>Si eres autónoma o tienes un centro pequeño</h2>

<p>Sé que el presupuesto es ajustado cuando trabajas sola o con una persona más. Lo entiendo. Pero la realidad es que una web bien posicionada en tu zona puede traerte cuatro o cinco clientes nuevos al mes sin pagar un solo euro en publicidad.</p>

<p>Si quieres saber exactamente qué necesitas para tu peluquería, escríbeme. Te preparo un presupuesto cerrado en 24 horas, sin sorpresas y sin compromiso. También puedes ver lo que hago para el <a href="../../sectores/servicios-locales/">sector de servicios locales</a>.</p>
""",
    },
    {
        "slug": "cuando-renovar-tu-web",
        "title": "¿Cuándo toca renovar la web de tu negocio?",
        "category": "Estrategia",
        "category_slug": "estrategia",
        "date": "18 de septiembre de 2026",
        "date_iso": "2026-09-18",
        "read_time": "4 min de lectura",
        "description": "Las señales que avisan de que tu web frena más de lo que empuja, y cómo saber si necesitas un retoque o una renovación completa.",
        "body": """
<p>La respuesta corta: cuando tu web frena más de lo que empuja. La respuesta larga es esta: hay señales bastante claras de que ha llegado el momento, y la mayoría de negocios las tienen y no las están viendo.</p>

<h2>Tres años es el límite general</h2>

<p>El diseño web envejece rápido. Lo que en 2021 parecía moderno, hoy parece de otra época. Pero más allá del aspecto, lo que cambia son los estándares técnicos: velocidad de carga, adaptación al móvil, posicionamiento en Google. Una web de más de tres años sin tocar casi siempre tiene problemas en alguno de estos tres puntos.</p>

<p>No es una regla fija, hay webs de cuatro años que siguen funcionando bien. Pero si llevas tres años sin actualizarla y no tienes datos de cómo está rindiendo, es buen momento para revisarla.</p>

<h2>Las señales que no mienten</h2>

<p><strong>Tarda en cargar.</strong> Si en el móvil tarda más de tres segundos en aparecer algo, estás perdiendo visitas antes de que nadie te lea.</p>

<p><strong>Se ve mal en el teléfono.</strong> Textos que salen cortados, botones que no funcionan, imágenes que no se adaptan. Si pasa alguna de estas cosas, Google lo sabe y te penaliza.</p>

<p><strong>No puedes cambiar nada tú solo.</strong> Si para actualizar el precio de un servicio o cambiar una foto tienes que llamar a alguien, la web está mal montada.</p>

<p><strong>No sale en Google.</strong> Si buscas tu negocio por el nombre y no apareces, o si buscas tu servicio en tu ciudad y sales en la segunda página, hay un problema real.</p>

<h2>Renovar no siempre es empezar de cero</h2>

<p>A veces lo que hay que hacer es actualizar el diseño manteniendo la estructura. A veces es cambiar el gestor de contenidos por uno que puedas manejar tú. A veces es solo trabajar el SEO de lo que ya tienes. Y a veces sí hay que tirar y empezar desde cero porque la base está tan mal montada que parchear cuesta más que rehacerla.</p>

<p>Lo primero que hago cuando alguien me trae su web es entender qué está funcionando para no tirarlo, y qué hay que cambiar sí o sí.</p>

<h2>El coste de no renovarla</h2>

<p>Cada mes con una web que no funciona es un mes de clientes que llegaron, vieron algo que no les convenció, y se fueron al competidor. Es difícil poner número a eso, pero si haces la cuenta de cuánto vale un cliente nuevo para tu negocio y cuántos se te pueden escapar por una web mala, la inversión en renovarla se amortiza bastante rápido.</p>

<h2>Por dónde empezar</h2>

<p>Si tienes dudas de si la tuya necesita una renovación, léete las <a href="../../blog/senales-web-pierde-clientes/">10 señales de que tu web está perdiendo clientes</a>. Si reconoces tres o más, ya tienes la respuesta. Y si quieres que la revise yo, te hago una valoración gratis y te digo exactamente qué cambiaría y por qué. Puedes ver también <a href="../../servicios/diseno-web/">cómo trabajo las renovaciones web</a> si quieres hacerte una idea antes de escribirme.</p>
""",
    },
    {
        "slug": "tienda-online-negocio-local",
        "title": "Tienda online para un pequeño negocio: cuándo tiene sentido y cuándo no",
        "category": "Ecommerce",
        "category_slug": "ecommerce",
        "date": "17 de septiembre de 2026",
        "date_iso": "2026-09-17",
        "read_time": "4 min de lectura",
        "description": "Cuándo un ecommerce tiene sentido para un negocio pequeño y cuándo es un gasto innecesario. Y los errores que más veo en tiendas online que no venden.",
        "body": """
<p>Me preguntan mucho si deberían montar una tienda online. A veces la respuesta es sí y a veces es un no claro. Lo malo es que hay mucha gente que monta una tienda online porque «hay que estar en internet», gasta dinero y tiempo, y luego no vende nada porque no era lo que su negocio necesitaba.</p>

<h2>Cuándo tiene sentido montarla</h2>

<p>Un ecommerce tiene sentido cuando vendes un producto físico que se puede enviar sin problema, tienes margen suficiente para absorber los costes de envío y devoluciones, y hay demanda online para lo que ofreces. Si las tres cosas son verdad, una tienda online puede multiplicar tus ventas sin depender del local.</p>

<p>También tiene sentido si vendes productos digitales (plantillas, formaciones, recursos descargables) o si tienes una marca con seguidores que te comprarían desde cualquier punto de España.</p>

<h2>Cuándo no tiene sentido</h2>

<p>Si lo que haces es un servicio local —un taller mecánico, una peluquería, una clínica— montar un ecommerce es gastar dinero en algo que no te va a traer clientes. Lo que necesitas en ese caso es una web bien hecha con SEO local, no una tienda.</p>

<p>Tampoco tiene sentido si vendes algo que necesita que el cliente lo vea y lo toque antes de comprarlo, o si el coste del envío hace que el precio final no sea competitivo.</p>

<h2>Lo que falla en el 80 % de los ecommerce pequeños</h2>

<p><strong>Fotos malas.</strong> Las fotos de catálogo que te pasa el proveedor son las mismas que tiene todo el mundo. Si tus fotos no son tuyas, nadie entiende por qué comprarte a ti y no a quien tiene el mismo producto más barato en Amazon.</p>

<p><strong>Textos copiados de la ficha del fabricante.</strong> Ni posicionan en Google ni convencen a nadie.</p>

<p><strong>Ningún trabajo de SEO.</strong> Una tienda sin SEO es un escaparate con el toldo bajado. Nadie la ve si nadie llega hasta ella.</p>

<h2>No todo es WooCommerce o Shopify</h2>

<p>La plataforma importa, pero menos de lo que se cree. Lo que importa es elegir la que se adapta a tu volumen, a tu presupuesto y a lo que puedas gestionar tú mismo. Montar una tienda en Shopify con cien referencias para un negocio que vende veinte productos al mes es matar moscas a cañonazos.</p>

<h2>El coste real no es solo la plataforma</h2>

<p>Hay que contar: la plataforma, las fotos, el SEO inicial, el mantenimiento, la pasarela de pago, los gastos de envío y la dedicación tuya para gestionar pedidos. Un ecommerce pequeño bien montado y bien gestionado puede ser muy rentable. Mal montado, es solo un gasto.</p>

<h2>Si tienes dudas</h2>

<p>Si no sabes si tu negocio necesita una tienda o una web de servicios, cuéntame qué tienes entre manos y te doy mi opinión. Puedes ver cómo trabajo los proyectos de <a href="../../servicios/ecommerce/">ecommerce</a> y también el <a href="../../servicios/diseno-web/">diseño web para negocios que no necesitan tienda online</a>.</p>
""",
    },
    {
        "slug": "web-para-abogados",
        "title": "La web de un abogado: qué necesita para que el cliente llame",
        "category": "Para tu negocio",
        "category_slug": "para-tu-negocio",
        "date": "12 de septiembre de 2026",
        "date_iso": "2026-09-12",
        "read_time": "4 min de lectura",
        "description": "Lo que hace que un cliente llame a un abogado que no conoce de nada: especialidad clara, cara visible, casos reales y contacto fácil.",
        "body": """
<p>Cuando alguien necesita un abogado, primero busca en Google. Lee dos o tres webs, mira quién le inspira más confianza, y llama. En ese momento decides tú si consigues el cliente o no. Lo que hace que alguien llame a un abogado que no conoce de nada es, casi siempre, la primera impresión de la web.</p>

<h2>Tu especialidad, sin rodeos</h2>

<p>Nadie contrata a un abogado que hace «todo tipo de derecho». La gente que llega con un problema concreto busca a alguien que lo resuelva en esa área concreta. Si te especializas en divorcios, en derecho laboral, en herencias o en arrendamientos, ponlo en el título de la página, no enterrado en el quinto párrafo.</p>

<p>Y sin tecnicismos. Los textos tienen que hablar como habla tu cliente, no como un escrito judicial.</p>

<h2>Tu cara y tu historia importan</h2>

<p>Contratar un abogado es una decisión de mucha confianza. La gente quiere saber quién eres, de dónde vienes y por qué te dedicas a lo que te dedicas. Una foto tuya bien hecha —no la del carnet— y dos párrafos honestos sobre tu trayectoria hacen más que una lista de títulos y diplomas.</p>

<h2>Casos resueltos, aunque sea en genérico</h2>

<p>No hace falta nombrar clientes. Basta con ejemplos del tipo: «ayudé a un autónomo a recuperar 8.000 € en una disputa laboral» o «conseguimos mantener la vivienda familiar en un proceso de divorcio complicado». Eso es lo que necesita leer alguien que tiene un problema parecido para decidir que llamas tú.</p>

<h2>Cómo contactar, bien visible</h2>

<p>Teléfono visible. WhatsApp si lo usas. Un formulario sencillo para quien prefiera no llamar. Nada de esconder el contacto o poner solo un correo electrónico que nadie va a usar. La persona que necesita un abogado quiere respuesta rápida, no una espera de dos días.</p>

<h2>SEO local para tu ciudad</h2>

<p>Si no sales cuando alguien busca «abogado divorcio [tu ciudad]», esos clientes no existen para ti. Para eso necesitas una web bien optimizada para SEO local y una ficha de Google Business Profile cuidada. Muchos despachos tienen webs discretas pero salen muy bien en Google porque trabajaron bien estas dos piezas.</p>

<h2>¿Quieres que lo revise?</h2>

<p>Si tienes web y no te está dando resultados, o si estás pensando en hacerla desde cero, cuéntame qué tienes y te doy mi opinión. Puedes ver cómo trabajo el <a href="../../servicios/diseno-web/">diseño web</a> y el <a href="../../servicios/branding/">branding</a> para negocios profesionales, y si algo te encaja, hablamos.</p>
""",
    },
    {
        "slug": "web-para-arquitecto",
        "title": "La web de un arquitecto: portfolio que consigue encargos",
        "category": "Para tu negocio",
        "category_slug": "para-tu-negocio",
        "date": "20 de septiembre de 2026",
        "date_iso": "2026-09-20",
        "read_time": "4 min de lectura",
        "description": "La mayoría de webs de arquitectos son portfolios bonitos que no consiguen encargos. Esto es lo que marca la diferencia.",
        "body": """
<p>La mayoría de webs de arquitectos son portfolios bonitos que no consiguen encargos. Hay buenas fotos, proyectos bien presentados, y aun así el teléfono no suena. El problema casi siempre es el mismo: la web muestra el trabajo, pero no le habla a quien tiene que contratar.</p>

<h2>El portfolio tiene que contar la historia del proyecto</h2>

<p>Una galería de fotos sin contexto no convence a nadie. Lo que engancha a un cliente potencial es entender qué problema había, qué decidiste y por qué, y cómo quedó el resultado. Tres o cuatro párrafos por proyecto, con las fotos bien, hacen que alguien que está buscando a quién contratar se quede leyendo en vez de pasar.</p>

<p>No hace falta publicar todos los proyectos. Mejor diez bien contados que treinta que son solo imágenes.</p>

<h2>Tu especialización, clara desde el principio</h2>

<p>Si te especializas en vivienda de obra nueva, en reformas de pisos, en rehabilitación de edificios o en locales comerciales, ponlo en la portada. La gente que llega buscando un arquitecto para reformar su casa no quiere leer toda la web para saber si haces reformas o solo obra nueva.</p>

<p>La especialización también ayuda mucho en SEO: «arquitecto reformas Barcelona» posiciona mucho mejor que «arquitecto Barcelona».</p>

<h2>Tu proceso de trabajo</h2>

<p>Una reforma o una obra nueva es una decisión grande y larga. La gente no sabe cómo funciona trabajar con un arquitecto: cuánto tarda cada fase, qué tiene que aportar el cliente, cuándo empieza a costar dinero. Explicar tu proceso en la web reduce la incertidumbre y genera confianza. El cliente llega ya con expectativas reales.</p>

<h2>Contactar sin rollos</h2>

<p>Un WhatsApp o un formulario simple con nombre, tipo de proyecto y localización. Nada más. Los formularios de treinta campos asustan. Si alguien quiere pedirte presupuesto, que pueda hacerlo en un minuto. Luego ya habláis por teléfono y recopilas toda la información que necesitas.</p>

<h2>Las fotos marcan la diferencia</h2>

<p>En arquitectura, el fotógrafo de obra es tan importante como el diseñador web. Una misma casa fotografiada por un profesional y por alguien con el móvil son dos webs distintas. Si no tienes fotos buenas de tus proyectos, ese es el primer sitio donde invertir antes de hacer nada más con la web.</p>

<h2>SEO local para conseguir encargos cerca</h2>

<p>La mayoría de encargos de arquitectura son locales. Si no apareces cuando alguien busca «arquitecto [tu ciudad]» o «arquitecto reformas [tu ciudad]», te estás perdiendo los clientes que tienes más cerca. Para eso necesitas SEO local bien trabajado y una ficha de Google Business activa.</p>

<h2>¿Quieres que lo mire yo?</h2>

<p>Si tienes web de arquitecto y no te está dando encargos, o si quieres hacerla de cero con un diseño que transmita tu nivel de trabajo, escríbeme. Puedes ver cómo trabajo el <a href="../../servicios/diseno-web/">diseño web</a> y también el <a href="../../servicios/branding/">branding</a> para profesionales que viven de su imagen. Te hago una valoración gratis y te digo por dónde empezaría.</p>
""",
    },
    {
        "slug": "web-para-clinica-dental",
        "title": "Web para clínica dental: qué necesita para que el paciente reserve",
        "category": "Para tu negocio",
        "category_slug": "para-tu-negocio",
        "date": "10 de septiembre de 2026",
        "date_iso": "2026-09-10",
        "read_time": "4 min de lectura",
        "description": "Lo que necesita la web de una clínica dental para generar confianza y que el paciente reserve: equipo visible, especialidades claras y reserva fácil.",
        "body": """
<p>Cuando alguien busca un dentista en Google, lo primero que hace es mirar quién tiene buena pinta. No el que sale primero necesariamente, sino el que al entrar en su web le transmite que ahí va a estar en buenas manos. Si tu clínica no da esa sensación en los primeros cinco segundos, ese paciente va a la siguiente.</p>

<h2>Cara y nombre de los dentistas, siempre</h2>

<p>La gente no quiere que la trate «un profesional del equipo». Quiere saber quién le va a meter las manos en la boca. Una foto decente de cada dentista, su nombre y en qué se especializa es lo mínimo. Sin eso, la clínica más bonita del mundo genera desconfianza.</p>

<h2>Las especialidades, claras y sin tecnicismos</h2>

<p>Ortodoncia invisible, implantes, blanqueamiento, odontopediatría… la gente busca exactamente lo que necesita. Si tu web no lo dice con esas palabras, no apareces cuando alguien escribe «ortodoncia invisible [tu ciudad]» en Google. Los textos tienen que hablarle a quien tiene ese problema, no sonar a folleto de congreso médico.</p>

<h2>Reservar cita tiene que ser sencillo</h2>

<p>Si para pedir cita hay que llamar en horario de oficina o mandar un correo y esperar, pierdes a la mitad. Un botón de WhatsApp bien visible o un formulario de reserva que funcione en móvil hace que la gente actúe en el momento en que decide. Ese momento no dura mucho.</p>

<h2>Fotos del espacio, no del banco de imágenes</h2>

<p>Las fotos de clínicas de stock son todas iguales. La gente ya las reconoce y las ignora. Cuatro fotos reales de tu clínica, la sala de espera, el box de trabajo —aunque no sean perfectas— transmiten más que veinte imágenes de archivo. La autenticidad vende más que la perfección.</p>

<h2>Las reseñas de Google no son opcionales</h2>

<p>Una clínica dental con menos de cuatro estrellas en Google o con diez reseñas pierde pacientes cada día. Tu ficha de Google Business Profile tiene que estar cuidada: fotos actualizadas, descripción de servicios, y respuesta a cada reseña, buena o mala.</p>

<h2>Que se vea bien en el móvil, sin discusión</h2>

<p>Más del 60 % de las búsquedas de salud se hacen desde el móvil. Si tu web tarda más de tres segundos en cargar o los botones son del tamaño de una hormiga, la gente se va. Es así de simple y es uno de los primeros puntos que reviso cuando audito una web de clínica.</p>

<h2>Si quieres que lo revise yo</h2>

<p>Trabajo con clínicas y negocios de salud y sé bien qué funciona y qué no en este sector. Si quieres que eche un ojo a la tuya, te hago una valoración gratis y te digo por dónde empezaría. Sin rollos ni informes de cien páginas.</p>

<p>Si te interesa ver cómo trabajo este tipo de webs, mira lo que hago para <a href="../../sectores/clinicas-y-salud/">clínicas y negocios de salud</a>. Y si también quieres aparecer bien en Google, el <a href="../../servicios/seo/seo-local/">SEO local</a> es por donde empezaría.</p>
""",
    },
    {
        "slug": "web-para-gimnasio",
        "title": "La web de un gimnasio: lo que los socios buscan antes de apuntarse",
        "category": "Para tu negocio",
        "category_slug": "para-tu-negocio",
        "date": "15 de septiembre de 2026",
        "date_iso": "2026-09-15",
        "read_time": "4 min de lectura",
        "description": "Horarios sin PDF, precios visibles, fotos reales y SEO local: esto es lo que necesita la web de un gimnasio para convertir curiosos en socios.",
        "body": """
<p>Antes de entrar a un gimnasio a preguntar, la gente pasa diez minutos mirando la web desde el sofá. Mira los precios, los horarios, las clases que hay, cómo es el sitio. Si no encuentra lo que busca en esos diez minutos, llama al siguiente. La web de un gimnasio tiene una función muy concreta: convertir esa curiosidad en un «vale, voy a apuntarme».</p>

<h2>Los horarios y las clases, sin PDF</h2>

<p>El PDF del horario de clases es el error más repetido que veo. En el móvil se abre mal, hay que hacer zoom para leer algo, y si tienes que actualizarlo cada mes, termina siendo el PDF de hace seis meses. Los horarios tienen que estar en la web, visibles directamente, fáciles de actualizar y bien organizados por tipo de clase o día.</p>

<h2>Los precios, visibles</h2>

<p>Mucha gente oculta los precios pensando que así obligan al cliente a llamar. Lo que hacen en realidad es perderlo. Si para saber cuánto cuesta la mensualidad hay que llamar o ir en persona, la mitad de la gente se va. Los precios visibles generan más confianza y más consultas reales de gente que ya ha decidido.</p>

<h2>Apuntarse sin llamar</h2>

<p>Un botón de WhatsApp o un formulario de «quiero información» que alguien pueda rellenar un domingo a las diez de la noche marca la diferencia. No todo el mundo quiere llamar. La gente que está decidida no quiere esperar al lunes para preguntar, y si no puede actuar en ese momento, muchas veces no actúa nunca.</p>

<h2>Fotos reales del espacio</h2>

<p>Las fotos de máquinas de stock son invisibles. Lo que la gente quiere ver es cómo es tu gimnasio en concreto: el espacio de pesas, la sala de clases, si hay duchas decentes. Cuatro fotos bien hechas de tu local valen mucho más que cualquier imagen de banco de imágenes.</p>

<h2>Que Google te encuentre cerca</h2>

<p>La mayoría de la gente busca «gimnasio cerca de mí» o «gimnasio [barrio o ciudad]». Para eso necesitas dos cosas: la web bien optimizada para SEO local y tu ficha de Google Business con fotos actualizadas, horario real y reseñas trabajadas. Sin esto no apareces en el mapa de Google.</p>

<h2>Móvil primero, siempre</h2>

<p>La gente te busca desde el teléfono, muchas veces mientras hace deporte o va de camino al trabajo. Si la web tarda, se ve mal o los botones son pequeños, se va. Es el primer punto que miro en cualquier auditoría de web local.</p>

<h2>Si quieres que lo revise</h2>

<p>Si tienes un gimnasio y tu web no te está trayendo socios nuevos, cuéntame. Te hago una valoración gratis y te digo exactamente qué cambiaría. Si quieres ver cómo trabajo este tipo de proyectos, mira la página de <a href="../../sectores/servicios-locales/">diseño web para negocios locales</a>.</p>
""",
    },
]


# ---------------------------------------------------------------------------
# Plantilla de artículo
# ---------------------------------------------------------------------------
def render_article(a):
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{a['title']} | She's Digital</title>
  <meta name="description" content="{a['description']}" />
  <link rel="canonical" href="https://sheisdigitalab.com/blog/{a['slug']}/" />
  <meta property="og:title" content="{a['title']} | She's Digital" />
  <meta property="og:description" content="{a['description']}" />
  <meta property="og:image" content="../../assets/img/og-cover.jpg" />
  <meta property="og:type" content="article" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../../assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../../assets/css/v2.css?v=17" />
  <link rel="stylesheet" href="../../assets/css/service.css" />
  <link rel="stylesheet" href="../../assets/css/blog.css" />
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
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{a['title']}",
    "description": "{a['description']}",
    "datePublished": "{a['date_iso']}",
    "author": {{"@type": "Person", "name": "Jenifer Jaldo"}},
    "publisher": {{"@type": "Organization", "name": "She's Digital", "url": "https://sheisdigitalab.com"}}
  }}
  </script>
</head>
<body class="service-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="../../" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="../../assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="../../#servicios">Servicios y precios</a>
        <a href="../../#proyectos">Proyectos</a>
        <a href="../../#proceso">Proceso</a>
        <a href="../../#sobre-mi">Sobre mí</a>
        <a href="../../#faq">FAQ</a>
        <a href="#contacto" class="btn btn--dark nav__cta-mobile">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      </nav>
      <a href="#contacto" class="btn btn--dark nav__cta">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
        <span class="sr-only">Abrir menú</span>
        <span class="nav__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </header>

  <main id="main">

    <article class="bl-article">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta">
          <ol>
            <li><a href="../../">Inicio</a></li>
            <li><a href="../../blog/">Blog</a></li>
            <li aria-current="page">{a['category']}</li>
          </ol>
        </nav>

        <header class="bl-header">
          <p class="eyebrow bl-eyebrow">{a['category']}</p>
          <h1 class="bl-title">{a['title']}</h1>
          <p class="bl-meta">Por <strong>Jenifer Jaldo</strong> · {a['date']} · {a['read_time']}</p>
        </header>

        <div class="bl-body">
          {a['body'].strip()}
        </div>

        <div class="bl-cta-inline">
          <p>¿Hablamos de tu web?</p>
          <a href="#contacto" class="btn btn--dark btn--magnetic">Pedir presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
          <a href="../../blog/" class="btn btn--line">Ver más artículos</a>
        </div>
      </div>
    </article>

    <section class="section" id="contacto" aria-labelledby="contacto-title" data-reveal>
      <div class="wrap wrap--narrow">
        <header class="section__head">
          <p class="eyebrow">Contacto</p>
          <h2 class="h2" id="contacto-title">¿Hablamos de tu web?</h2>
          <p class="section__lead">Cuéntame qué necesitas y te envío un presupuesto cerrado en 24&nbsp;h. Sin compromiso.</p>
        </header>
        <form class="form" id="contact-form" method="post" novalidate data-reveal>
          <p class="form__note" id="form-note">Todos los campos son obligatorios.</p>
          <div class="field">
            <label for="f-name">¿Cómo te llamas?</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="f-name-err" />
            <p class="field__err" id="f-name-err" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="f-msg">Cuéntame tu proyecto</label>
            <textarea id="f-msg" name="message" rows="4" required aria-describedby="f-msg-err"></textarea>
            <p class="field__err" id="f-msg-err" aria-live="polite"></p>
          </div>
          <div class="field field--check">
            <input id="f-privacy" name="privacy" type="checkbox" required aria-describedby="f-privacy-err" />
            <label for="f-privacy">He leído y acepto la <a href="https://sheisdigitalab.com/legal/privacidad/">política de privacidad</a>.</label>
            <p class="field__err" id="f-privacy-err" aria-live="polite"></p>
          </div>
          <button type="submit" class="btn btn--dark btn--block">
            <span data-btn-label>Enviar por WhatsApp</span>
            <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
          </button>
          <p class="form__wa-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p>
          <p class="form__status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__cols">
        <div>
          <img src="../../assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Diseño web, marca y marketing digital en Barcelona.<br />Web · Ecommerce · SEO · Branding · Redes · IA y apps a medida.</p>
        </div>
        <nav aria-label="Pie: servicios">
          <h3>Servicios</h3>
          <ul>
            <li><a href="../../servicios/branding/">Branding</a></li>
            <li><a href="../../servicios/diseno-web/">Diseño web</a></li>
            <li><a href="../../servicios/ecommerce/">Ecommerce</a></li>
            <li><a href="../../servicios/seo/seo-local/">SEO local</a></li>
            <li><a href="../../servicios/redes-sociales/">Redes sociales</a></li>
          </ul>
        </nav>
        <nav aria-label="Pie: sectores">
          <h3>Sectores</h3>
          <ul>
            <li><a href="../../sectores/autonomos/">Autónomos</a></li>
            <li><a href="../../sectores/clinicas-y-salud/">Clínicas y salud</a></li>
            <li><a href="../../sectores/restaurantes/">Restaurantes</a></li>
            <li><a href="../../sectores/servicios-locales/">Servicios locales</a></li>
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
        <p>© 2026 She's Digital · She is Digital Lab</p>
        <button class="motion-toggle" type="button" aria-pressed="false" data-motion-toggle>Reducir animaciones</button>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <a class="wa-fab" href="https://wa.me/34637889942?text=Hola%20Jenifer%2C%20quiero%20pedir%20presupuesto%20para%20mi%20web" target="_blank" rel="noopener noreferrer" aria-label="Escríbenos por WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg>
  </a>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="../../assets/js/main.js" defer></script>
  <script src="../../assets/js/service.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Plantilla de blog/index.html
# ---------------------------------------------------------------------------
def render_index():
    cards = ""
    for a in ARTICLES:
        cards += f"""
          <li>
            <a href="{a['slug']}/" class="bl-card">
              <p class="eyebrow bl-card__cat">{a['category']}</p>
              <h2 class="bl-card__title">{a['title']}</h2>
              <p class="bl-card__meta">{a['date']} · {a['read_time']}</p>
              <span class="bl-card__arrow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
            </a>
          </li>"""

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Blog de diseño web y marketing digital | She's Digital</title>
  <meta name="description" content="Artículos prácticos sobre diseño web, SEO local y marketing digital para pequeñas empresas y autónomos. Sin tecnicismos." />
  <link rel="canonical" href="https://sheisdigitalab.com/blog/" />
  <meta property="og:title" content="Blog · She's Digital" />
  <meta property="og:description" content="Artículos prácticos sobre diseño web, SEO local y marketing digital para pequeñas empresas y autónomos." />
  <meta property="og:image" content="../assets/img/og-cover.jpg" />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="theme-color" content="#FAF8F4" />
  <link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../assets/css/v2.css?v=17" />
  <link rel="stylesheet" href="../assets/css/service.css" />
  <link rel="stylesheet" href="../assets/css/blog.css" />
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
</head>
<body class="service-page">
  <a class="skip" href="#main">Saltar al contenido</a>

  <header class="nav" data-nav>
    <div class="nav__inner wrap">
      <a href="../" class="nav__logo" aria-label="She's Digital, inicio">
        <img src="../assets/img/logo-stacked.svg" alt="" width="112" height="63" />
      </a>
      <nav class="nav__links" id="nav-menu" aria-label="Principal">
        <a href="../#servicios">Servicios y precios</a>
        <a href="../#proyectos">Proyectos</a>
        <a href="../#proceso">Proceso</a>
        <a href="../#sobre-mi">Sobre mí</a>
        <a href="../#faq">FAQ</a>
        <a href="#contacto" class="btn btn--dark nav__cta-mobile">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      </nav>
      <a href="#contacto" class="btn btn--dark nav__cta">Pide tu presupuesto gratis <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span></a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
        <span class="sr-only">Abrir menú</span>
        <span class="nav__bars" aria-hidden="true"><i></i><i></i></span>
      </button>
    </div>
  </header>

  <main id="main">

    <section class="cs-hero sv-hero sv-hero--index" id="top" aria-labelledby="blog-title">
      <div class="wrap">
        <nav class="sv-crumbs" aria-label="Ruta" data-hero="fade">
          <ol>
            <li><a href="../">Inicio</a></li>
            <li aria-current="page">Blog</li>
          </ol>
        </nav>
        <p class="eyebrow" data-hero="fade">Blog</p>
        <h1 class="sv-title" id="blog-title">
          <span class="hero__line"><span class="hero__line-in" data-hero="line">Diseño web,</span></span>
          <span class="hero__line"><span class="hero__line-in" data-hero="line"><span class="sv-mark">sin rodeos.</span></span></span>
        </h1>
        <div class="sv-hero__grid sv-hero__grid--slim">
          <p class="cs-hero__lead" data-hero="fade">Artículos prácticos sobre diseño web, SEO local y marketing digital para pequeñas empresas y autónomos. Sin tecnicismos.</p>
        </div>
      </div>
    </section>

    <section class="section bl-listing" id="articulos" aria-labelledby="arts-title" data-reveal>
      <div class="wrap">
        <h2 class="sr-only" id="arts-title">Artículos</h2>
        <ul class="bl-grid">
          {cards.strip()}
        </ul>
      </div>
    </section>

    <section class="section" id="contacto" aria-labelledby="contacto-title" data-reveal>
      <div class="wrap wrap--narrow">
        <header class="section__head">
          <p class="eyebrow">Contacto</p>
          <h2 class="h2" id="contacto-title">¿Hablamos de tu web?</h2>
          <p class="section__lead">Cuéntame qué necesitas y te envío un presupuesto cerrado en 24&nbsp;h. Sin compromiso.</p>
        </header>
        <form class="form" id="contact-form" method="post" novalidate data-reveal>
          <p class="form__note" id="form-note">Todos los campos son obligatorios.</p>
          <div class="field">
            <label for="f-name">¿Cómo te llamas?</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="f-name-err" />
            <p class="field__err" id="f-name-err" aria-live="polite"></p>
          </div>
          <div class="field">
            <label for="f-msg">Cuéntame tu proyecto</label>
            <textarea id="f-msg" name="message" rows="4" required aria-describedby="f-msg-err"></textarea>
            <p class="field__err" id="f-msg-err" aria-live="polite"></p>
          </div>
          <div class="field field--check">
            <input id="f-privacy" name="privacy" type="checkbox" required aria-describedby="f-privacy-err" />
            <label for="f-privacy">He leído y acepto la <a href="https://sheisdigitalab.com/legal/privacidad/">política de privacidad</a>.</label>
            <p class="field__err" id="f-privacy-err" aria-live="polite"></p>
          </div>
          <button type="submit" class="btn btn--dark btn--block">
            <span data-btn-label>Enviar por WhatsApp</span>
            <span class="btn__icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></span>
          </button>
          <p class="form__wa-note">Se abrirá WhatsApp con tu mensaje listo para enviar.</p>
          <p class="form__status" role="status" aria-live="polite"></p>
        </form>
      </div>
    </section>

  </main>

  <footer class="footer">
    <div class="wrap">
      <div class="footer__cols">
        <div>
          <img src="../assets/img/logo-stacked-light.svg" alt="She's Digital" width="150" height="84" loading="lazy" />
          <p>Diseño web, marca y marketing digital en Barcelona.<br />Web · Ecommerce · SEO · Branding · Redes · IA y apps a medida.</p>
        </div>
        <nav aria-label="Pie: servicios">
          <h3>Servicios</h3>
          <ul>
            <li><a href="../servicios/branding/">Branding</a></li>
            <li><a href="../servicios/diseno-web/">Diseño web</a></li>
            <li><a href="../servicios/ecommerce/">Ecommerce</a></li>
            <li><a href="../servicios/seo/seo-local/">SEO local</a></li>
            <li><a href="../servicios/redes-sociales/">Redes sociales</a></li>
          </ul>
        </nav>
        <nav aria-label="Pie: sectores">
          <h3>Sectores</h3>
          <ul>
            <li><a href="../sectores/autonomos/">Autónomos</a></li>
            <li><a href="../sectores/clinicas-y-salud/">Clínicas y salud</a></li>
            <li><a href="../sectores/restaurantes/">Restaurantes</a></li>
            <li><a href="../sectores/servicios-locales/">Servicios locales</a></li>
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
        <p>© 2026 She's Digital · She is Digital Lab</p>
        <button class="motion-toggle" type="button" aria-pressed="false" data-motion-toggle>Reducir animaciones</button>
        <p>Hecho a mano en Barcelona ✦</p>
      </div>
    </div>
  </footer>

  <div class="cursor-badge" data-cursor aria-hidden="true"></div>

  <a class="wa-fab" href="https://wa.me/34637889942?text=Hola%20Jenifer%2C%20quiero%20pedir%20presupuesto%20para%20mi%20web" target="_blank" rel="noopener noreferrer" aria-label="Escríbenos por WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.5-.3Z"/></svg>
  </a>

  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js" defer></script>
  <script src="https://cdn.jsdelivr.net/npm/lenis@1.3.4/dist/lenis.min.js" defer></script>
  <script src="../assets/js/main.js" defer></script>
  <script src="../assets/js/service.js" defer></script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Generar ficheros
# ---------------------------------------------------------------------------
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK  {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    print("=== build_blog.py ===")
    # blog/index.html
    write(os.path.join(ROOT, "blog", "index.html"), render_index())
    # Artículos
    for article in ARTICLES:
        path = os.path.join(ROOT, "blog", article["slug"], "index.html")
        write(path, render_article(article))
    print(f"\nGenerados: 1 índice + {len(ARTICLES)} artículos")
