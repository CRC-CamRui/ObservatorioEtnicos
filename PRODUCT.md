# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

HTML, CSS y JavaScript estáticos, sin proceso de compilación. Decisión
explícita del usuario (12 de agosto de 2026), tomada para que el material se
pueda entregar y abrir sin dependencias.

**Decisión abierta:** si la propuesta se aprueba y aterriza como subsitio de
`defensoria.gov.co`, el destino real será el CMS del portal de la entidad, no
estos archivos. Nadie ha confirmado cuál es ese CMS ni qué margen deja. Hasta
saberlo, los archivos estáticos son un prototipo de presentación, no el
entregable de producción.

## Users

**Usuario principal confirmado: ciudadanía general.** Persona sin formación
jurídica ni conocimiento previo del sistema de derechos étnicos, que llega a
entender qué está pasando con los derechos de los pueblos indígenas, negros,
afrocolombianos, raizales, palenqueros y Rrom en Colombia. Su tarea es
comprender, no tramitar.

El material de origen nombraba además autoridades tradicionales, consejos
comunitarios, cabildos, kumpañy, servidores públicos e investigadores. **No
están confirmados como audiencia principal** y no deben tratarse como tal:
al escribir para cinco audiencias a la vez el borrador inicial quedó en un
registro institucional que la ciudadanía general no sostiene.

## Product Purpose

TRENZAS es un observatorio de la Defensoría del Pueblo que hace seguimiento a
la situación de derechos humanos de los pueblos y comunidades étnicas de
Colombia, y reúne en un solo lugar información que hoy está dispersa entre
registros de la entidad, jurisprudencia y reportes de organizaciones propias
de los pueblos.

El propósito declarado en el material de origen no se agota en documentar:
la información existe para quedar en manos de quien la necesita al momento de
exigir garantías. Con la ciudadanía general como usuario principal, el éxito
se mide en comprensión, no en descargas.

## Positioning

Lo que ninguna otra organización puede replicar es la fuente: los registros
que las duplas de atención de la Defensoría producen en territorio. Un
observatorio académico o de sociedad civil puede analizar, litigar o
denunciar; no tiene esa red de captura propia con presencia institucional
permanente en las regiones.

## Operating Context

Hoy el proyecto es **una propuesta para presentar**, no un encargo en
ejecución. Su trabajo inmediato es convencer a quien decide dentro de la
entidad.

El destino declarado si se aprueba es **un subsitio dentro de
`defensoria.gov.co`**, heredando plantilla, CMS y restricciones del portal
existente.

**Tensión estructural que todo trabajo futuro debe tener presente:** una
propuesta gana aprobación mostrando algo distintivo, y un subsitio de
`.gov.co` probablemente no puede ser distintivo. Una propuesta que enseña algo
que después no se puede implementar traslada el fracaso a la fase de
ejecución. Cualquier pieza de presentación debería separar con claridad qué
es concepto y qué es implementable.

## Capabilities and Constraints

Estructura de contenido definida por el usuario, nueve bloques en una sola
página:

1. Encabezado
2. Qué es el Observatorio
3. Cómo funciona (metodología)
4. Ejes temáticos: Igualdad y No Discriminación, Participación Política de
   las Mujeres Étnicas, Autonomía y Gobierno Propio
5. Recursos: contexto territorial, visualizaciones e infografías, productos
   de investigación, repositorio documental, enlaces de interés

Decisiones del usuario que el trabajo posterior debe respetar salvo
instrucción contraria:

- Sin menú de anclas fijo.
- Sin pie de página institucional.
- El orden de los tres ejes se mantiene como en el material de origen.

**Restricción normativa sin resolver, y es la más importante:** la Ley 2345
de 2023 ("Chao marcas") unifica la identidad visual de las entidades del
Estado colombiano y restringe las marcas propias de programas y dependencias;
el Manual de Identidad Visual del Gobierno de Colombia 2024 y los estándares
GOV.CO fijan cómo debe verse un sitio estatal. No se verificó el alcance
exacto: los PDF normativos no fueron accesibles. Si aplican, un wordmark
propio con paleta propia para TRENZAS no es viable en `.gov.co`.
**Nadie debe asumir que esto está resuelto. Lo resuelve el área jurídica o de
comunicaciones de la Defensoría, no el equipo de diseño.**

## Brand Commitments

- El nombre **TRENZAS** está dado y es vinculante.
- La entidad responsable es la **Defensoría del Pueblo** de Colombia.
- No se ha entregado manual de identidad, logo institucional ni paleta
  oficial. Lo que existe hoy en el prototipo lo propuso el diseño, no la
  entidad.

## Evidence on Hand

**El proyecto no tiene todavía ningún material real. Esto es lo más
importante de este documento.**

- **No hay texto oficial.** Todo el contenido visible del prototipo es
  borrador inventado para revisar maquetación. No proviene de la Defensoría y
  no ha sido validado por nadie.
- **No hay cifras.** Se decidió deliberadamente no inventar ninguna
  estadística. Una cifra falsa sobre violencia contra lideresas étnicas,
  atribuida a la Defensoría, no es un marcador de posición inocuo.
- **No hay fotografía.** El prototipo usa `picsum.photos`. Cualquier imagen
  real de comunidades exige derechos y consentimiento de las personas
  retratadas.
- **No hay enlaces reales.** Los cinco recursos apuntan a `#`.
- **No hay logo institucional.**
- El relato sobre mujeres esclavizadas que tejían rutas de huida en sus
  trenzas, usado para explicar el nombre, es **tradición oral palenquera con
  respaldo documental débil**. No debe presentarse como hecho histórico
  verificado sin revisión.

Nada de lo anterior puede fabricarse en trabajo futuro.

## Product Principles

1. **Comprender antes que consultar.** El usuario principal viene a entender,
   no a citar. El núcleo educativo manda sobre la capa documental.
2. **Ninguna afirmación sin fuente.** Es un observatorio de derechos humanos
   de una entidad del Estado. Un dato sin respaldo es un pasivo institucional,
   no un detalle de contenido.
3. **La restricción normativa se verifica, no se supone.** Ningún trabajo
   visual debe apoyarse en la esperanza de que Ley 2345 y GOV.CO no apliquen.
4. **Distinguir siempre concepto de entregable.** Mientras esto sea propuesta,
   toda pieza debe dejar explícito qué es demostración y qué es producción.
5. **Lenguaje de ciudadanía, no de expediente.** Términos como consulta
   previa, jurisdicción especial indígena o enfoque diferencial se explican
   cuando aparecen, o no aparecen.

## Accessibility & Inclusion

Por tratarse de una entidad del Estado colombiano aplica la Resolución 1519
de 2020 del MinTIC, que remite a la NTC 5854 en nivel AA. El usuario declinó
una auditoría formal de conformidad; aun así el prototipo se construyó con
HTML semántico y los catorce pares de color reales se verificaron contra WCAG
AA, con 5.43:1 como el más ajustado.

Consideración específica del dominio, no confirmada como requisito: parte de
la población destinataria pertenece a pueblos con lengua propia y hay
comunidades con conectividad limitada. Ni la política de idiomas ni un
presupuesto de peso de página han sido definidos.
