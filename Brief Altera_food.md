# Brief de Proyecto: Altera_FOOD — Transformación Digital & IA Integral para Hostelería
## Caso Piloto: Pizzería Ángela Imaginalia (Albacete) & Modelo Escalable Gastro-Delivery

**Para:** Antigravity / Claude Code (Diseño y desarrollo de propuesta llave en mano)  
**De:** José Miguel Olmeda Pascual (Altera)  
**Fecha:** Octubre 2026  
**Cliente Objetivo Principal:** Pizzería Ángela — il Gusto del’Italia (C. Simone de Beauvoir, 3, 02005 Albacete - Imaginalia)  
**Web actual:** [https://pizzeriaangelaimaginalia.com](https://pizzeriaangelaimaginalia.com)  
**Benchmark / Referencia Local:** Vibra Burger Albacete — [https://vibraburgeralbacete.last.shop/](https://vibraburgeralbacete.last.shop/)  
**Marco de Financiación:** Subvención Bono Crecimiento Pyme — JCCM (Orden 116/2026, 80% a fondo perdido)  

---

## 1. Resumen Ejecutivo & Contexto del Negocio

**Pizzería Ángela** es una pizzería y restaurante italiano de referencia en el barrio de Imaginalia (Albacete), reconocida por sus pizzas artesanales en horno de piedra, pastas caseras, terraza exterior y ambiente familiar acogedor.

A diferencia del sector salud o servicios profesionales (como Adela Fisio o Altera Dental), el negocio de la restauración y pizzerías de barrio se rige por **volumen, rotación horaria concentrada (fines de semana) y velocidad de respuesta**:
1. **Picos de demanda extremos:** El 70% de la facturación semanal se concentra en las franjas de 20:30 a 23:30 de jueves a domingo.
2. **Dependencia tóxica de agregadores (Uber Eats):** Actualmente solo ofrecen entrega a domicilio a través de Uber Eats, plataforma que cobra entre un **25% y un 35% de comisión por pedido**, además de quedarse con la propiedad de los datos y hábitos del cliente final.
3. **Margen por recogida en local ("Take Away"):** Aunque admiten recogida en local, la gestión del pedido sigue dependiendo de llamadas telefónicas manuales o de clientes que se presentan en el local a esperar en cola.
4. **Capacidad de sala y rotación de mesas:** La gestión de reservas de mesa actual es manual o mediante formularios externos de terceros, perdiendo agilidad y provocando mesas vacías por cancelaciones no notificadas.

---

## 2. Diagnóstico Técnico de la Situación Actual

### A. Auditoría de Pizzería Ángela (`pizzeriaangelaimaginalia.com`)

1. **Web obsoleta maquetada con plantilla genérica (Tappens / Kit Digital):**  
   - La web fue desarrollada por la marca *Tappens* (marca comercial de *Advisory for All SL*) utilizando una plantilla estática y gratuita de Bootstrap de 2019/2020 (`templatemo-klassy-cafe.css`).
   - El pie de página exhibe el logotipo de fondos europeos y del Gobierno de España (`identidad_visual_gob.png`), demostrando que fue financiada con cargo a convocatorias pasadas del **Kit Digital estatal** para justificar una presencia web mínima.
   - **Fuga de usuarios y enlaces rotos/externos:** Para ver la carta digital o hacer una reserva, la web redirige fuera del dominio principal a subdominios externos ajenos: `https://carta-digital.tappens.com/pizzeria-angela` y `https://restaurante.tappens.com/pizzeria-angela/reservas`. El cliente abandona la web de la pizzería y pierde la experiencia de marca.
2. **El gran embudo del teléfono fijo (`967 60 12 66`):**  
   - No disponen de teléfono móvil visible ni canal de WhatsApp corporativo.
   - En mitad del servicio de cenas, con el horno a pleno rendimiento y las mesas llenas, el personal no puede atender físicamente el teléfono fijo. Las llamadas comunican o no se responden.
   - Cada llamada desatendida un viernes o sábado noche representa entre **25 € y 45 € de ticket perdido** que se marcha inmediatamente a otra pizzería o a cadenas organizadas (Domino's, Telepizza).
3. **Sin canal propio de venta digital ni pedidos por WhatsApp:**  
   - El consumidor actual (especialmente familias y jóvenes de Imaginalia) demanda hacer pedidos desde el móvil en 30 segundos por WhatsApp o web rápida.
   - No disponer de un canal de pedido directo obliga al cliente a buscar a Pizzería Ángela en Uber Eats, donde la pizzería pierde el 30% del importe en comisiones.
4. **Ausencia de cobro anticipado ("Pedidos Fantasma"):**  
   - Los pedidos telefónicos para recoger en local no se cobran por adelantado. Si el cliente no acude a recoger las pizzas, la pizzería asume el 100% de la merma de materia prima y mano de obra.
5. **Presencia en redes desconectada:**  
   - En la web solo enlaza a una página de Facebook. No hay integración con Instagram Direct (`@pizzeriaangelaimaginalia`), perdiendo todas las consultas que llegan a través de historias, fotos de pizzas o menciones en redes.

---

### B. Análisis Comparativo: Benchmark con Vibra Burger Albacete (`vibraburgeralbacete.last.shop`)

La visita y auditoría a la plataforma de Vibra Burger revela un modelo mucho más moderno, pero con debilidades críticas que Altera_FOOD supera:

| Característica / Funcionalidad | Pizzería Ángela (Actual) | Vibra Burger (Last.app) | Solución Propuesta Altera_FOOD |
| :--- | :--- | :--- | :--- |
| **Canal de Pedido** | Teléfono fijo (`967 60 12 66`) | Tienda web SaaS (`last.shop`) | **WhatsApp Conversacional + Web Propia ultrarrápida** |
| **Modelo Tecnológico** | Web estática Tappens (Kit Digital) | Plataforma SaaS alquilada (Last.app) | **Infraestructura 100% propia (VPS + Coolify + Supabase)** |
| **Costes Recurrentes** | Mínimos (pero pierde 30% en Uber) | Cuota mensual SaaS + comisión por pedido Last.app | **Cero comisiones por comanda (solo pasarela Stripe)** |
| **Atención por Voz IA** | Inexistente (llamada perdida) | Inexistente (no tiene recepcionista de voz) | **Recepcionista de Voz IA 24/7 (ElevenLabs)** |
| **Pedidos por WhatsApp** | No disponible | No disponible (solo carrito web tradicional) | **Bot IA en lenguaje natural (texto y notas de voz)** |
| **Gestión de Reservas de Mesa** | Formulario externo Tappens | No enfocado a mesa (takeaway/delivery) | **Reserva automática conversacional sincronizada** |
| **Redes Sociales (Instagram)** | Desconectado (solo Facebook) | Enlace básico en perfil | **Omnicanalidad nativa con Zernio (DM Instagram = Pedido)** |
| **Propiedad del Dato del Cliente** | Uber se queda los datos | Repartido con Last.app | **100% propiedad del restaurante (CRM propio en Supabase)** |
| **Financiación Subvencionada** | Kit Digital básico ya consumido | Financiado a pulmón | **80% a fondo perdido (Bono Crecimiento Pyme JCCM)** |

---

## 3. Alcance de la Solución Llave en Mano: Los 6 Pilares de Altera_FOOD

Altera_FOOD implanta un ecosistema tecnológico unificado, sin cuotas abusivas por pedido ni comisiones a intermediarios:

```
                  ┌──────────────────────────────────────────────┐
                  │            CANALES DE ENTRADA CLIENTE        │
                  │   WhatsApp Oficial  ·  Instagram DM (Zernio) │
                  │  Teléfono Fijo / Voz IA  ·  Web Mobile-First │
                  └──────────────────────┬───────────────────────┘
                                         │
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │           CEREBRO CONVERSACIONAL IA          │
                  │    • Comprensión de carta y alérgenos        │
                  │    • Modificación de ingredientes/masas      │
                  │    • Selector de franja horaria de recogida  │
                  │    • Generación de link de pago seguro       │
                  └──────────────────────┬───────────────────────┘
                                         │
                   ┌─────────────────────┴─────────────────────┐
                   ▼                                           ▼
       ┌────────────────────────┐                 ┌────────────────────────┐
       │   PASARELA DE PAGO     │                 │   COMANDERA & COCINA   │
       │   Stripe Checkout      │                 │  Supabase en Coolify   │
       │   Apple Pay/Google Pay │                 │  Panel KDS para horno  │
       │   Confirmación al móvil│                 │  Historial & CRM local │
       └────────────────────────┘                 └────────────────────────┘
```

### Pilar 1: Chatbot Asistente de WhatsApp para Pedidos & Reservas (Zernio + IA)
- **Pedidos conversacionales en lenguaje natural:** El cliente puede escribir o mandar un audio: *"Hola, quiero dos pizzas medianas para recoger a las 21:45: una Barbacoa sin cebolla y una Carbonara con extra de queso"*.
- **Gestión inteligente de carta y extras:** El bot conoce la carta al milímetro, sugiere postres ("*¿Te apetece añadir un tiramisú casero por 5 €?*") y bebidas, aumentando el ticket medio un 15-20%.
- **Control de tiempos de cocina y slots de recogida:** El sistema reparte los pedidos en franjas (slots de 15 minutos) según la capacidad del horno de piedra para no saturar la cocina.
- **Módulo de Reservas de Mesa:** Permite agendar mesa indicando comensales, fecha y turno (primer turno 20:30h, segundo turno 22:15h), enviando confirmación y recordatorio automático 2 horas antes.

### Pilar 2: Pasarela de Pago Integrada con Stripe (Cobro Garantizado)
- **Enlace de pago instantáneo en WhatsApp:** Al confirmar la comanda, el bot genera un enlace seguro de Stripe compatible con **Apple Pay, Google Pay, Bizum y tarjeta de crédito/débito**.
- **Cero pedidos fantasma:** La comanda no se envía a pantalla de cocina hasta que el pago está confirmado (o bien se autoriza explícitamente el pago en caja para clientes habituales VIP).
- **Ahorro masivo en comisiones:** Frente al 30% que cobra Uber Eats, Stripe solo cobra la comisión interbancaria estándar (~1.4% + 0.25€), ahorrando al restaurante más de **400 € a 800 € netos mensuales** en comisiones.

### Pilar 3: Recepcionista Telefónica con Voz IA para Horas Punta (ElevenLabs + OpenRouter)
- **Desvío inteligente del teléfono fijo (`967 60 12 66`):** Cuando la línea comunica o tras 3 tonos sin respuesta en el restaurante, la IA descuelga inmediatamente con voz humana natural y tono amable.
- **Toma de pedidos y reservas telefónicas:** Atiende al cliente, anota la comanda o reserva de mesa, resuelve dudas ("*¿Lleva gluten la lasaña?*") y, al colgar, le remite un WhatsApp automático con el desglose de la comanda y el link de Stripe para pagar.
- **Atención fuera de horario comercial:** Si un cliente llama un lunes o a las 11:00 de la mañana, la recepcionista le informa de los horarios y le permite dejar reservada su mesa o pedido anticipado para el fin de semana.

### Pilar 4: Omnicanalidad Instagram Direct + WhatsApp vía Zernio
- **Monetización del Instagram gastronómico:** Pizzería Ángela tiene productos altamente fotogénicos (pizzas crujientes saliendo del horno de piedra). Toda persona que reaccione a una historia o envíe un mensaje directo a Instagram es atendida por Zernio y guiada a pedir o reservar sin salir del chat.
- **Unificación de bandeja de entrada:** El hostelero o encargado tiene en una única pantalla todas las conversaciones de WhatsApp e Instagram sin necesidad de cambiar de aplicación.

### Pilar 5: Rediseño Web Corporativa & Carta Interactiva (Skill Frontend Altera)
- **Sustitución de la web de Tappens:** Nueva web propia, mobile-first, diseñada con Tailwind CSS, micro-interacciones fluidas, fotografías de alta resolución y tiempos de carga inferiores a 0.8 segundos.
- **Carta integrada en el propio dominio:** Se eliminan los enlaces y redirecciones a dominios de terceros (`tappens.com`). La carta se visualiza con filtros por alérgenos, fotos sugerentes y botón directo de compra en 1 clic ("Pedir por WhatsApp" / "Pedir Online").
- **SEO Local para Albacete & AEO (AI Engine Optimization):**
  - Posicionamiento local en Google Maps y búsqueda orgánica para: *"pizzería imaginalia albacete"*, *"mejores pizzas albacete"*, *"pizzería horno de piedra albacete"*, *"pedir pizza a domicilio albacete"*.
  - Marcado estructurado Schema.org `Restaurant` y `Menu` para que motores de IA (ChatGPT Search, Perplexity, Gemini) recomienden Pizzería Ángela.

### Pilar 6: Panel TPV Comandera de Cocina (KDS), Stock 1-Clic & CRM Gastronómico Propio
- **Pantalla KDS (Kitchen Display System) para cocina:** Vista tipo Kanban en tablet de cocina con tarjetas de pedidos en curso, agrupados por hora de entrega o recogida:
  - *Columna 1: Recepción / Nuevos Pagados*.
  - *Columna 2: Montaje / Pendiente de Hornear*.
  - *Columna 3: En Elaboración / En Horno o Plancha*.
  - *Columna 4: Listos para Recoger / Servir en Mesa*.
- **Control Rápido de Stock ("Agotado en 1 Clic"):** Si en mitad del servicio se agota la *Masa Sin Gluten*, la *Mozzarella Di Bufala* o el *Tiramisú Casero*, el cocinero pulsa un botón en la tablet KDS y al instante el Bot de WhatsApp y la Recepcionista de Voz IA dejan de ofrecerlo y sugieren una alternativa.
- **Base de datos propia y marketing de fidelización:** Altera_FOOD almacena en Supabase el historial de pedidos y visitas de cada cliente con **Semáforo de Reputación CRM** (VIP, recurrente o alerta de plantones previos).

### Pilar 7: Gestión Integral de Sala, Reservas Anti No-Show & Cobro de Cuenta (Suite 360º vs Restoo)
Altera_FOOD incorpora todas las funciones de alto valor de plataformas de reservas como **Restoo** y las conecta nativamente con cocina y facturación para cubrir los **dos recorridos completos de principio a fin**:
1. **Recorrido Completo de Sala (De la Llamada/WhatsApp a Pagar la Cuenta):**
   - **Reserva por Voz IA o WhatsApp + Fianza Anti No-Show en 15s (Stripe Hold):** Para grupos grandes (>6 pax) o horas punta de fin de semana, el bot envía por WhatsApp un enlace seguro de validación con Apple Pay / Google Pay / tarjeta que retiene una fianza (ej. 10€/comensal) solo en caso de plantón sin avisar.
   - **Mapa Visual de Sala por Zonas y Doblaje Automático de Turnos:** Control interactivo de *Salón Interior* y *Terraza* con rotación inteligente en dos turnos (*Turno 1: 20:30h–22:00h* y *Turno 2: 22:15h–23:45h*) y **Alerta de Desperdicio de Cubiertos** (avisa si una reserva de 2 personas bloquea una mesa de 6 y sugiere reubicarla en 1 clic).
   - **Briefing Pre-Servicio Automático (30 min antes):** Resumen diario en la tablet de cocina y sala con alergias (celíacos), tronas de bebé, cumpleaños y clientes VIP.
   - **Lista de Espera Virtual & Derivación de Hora Punta:** Si las 21:30h están completas, el bot ofrece 20:30h o 22:30h o anota al cliente en la Lista de Espera para avisarle por WhatsApp en 1 clic en cuanto se libere una mesa.
   - **Cobro de Cuenta en Mesa (Pay-at-Table QR / Bizum / Stripe):** El comensal escanea el QR de su mesa, revisa su cuenta, la divide entre amigos si lo desea y paga en 10 segundos con Apple Pay o Bizum, liberando la mesa automáticamente para el segundo turno.
   - **Autopilot de Reseñas 5★ en Google Maps:** 60–90 minutos después de pagar la cuenta o recoger el pedido, el cliente recibe un WhatsApp automático. Si valora con 5★ va directo a publicar reseña en Google Maps; si puntúa ≤3★ se abre un canal privado con gerencia evitando reseñas negativas públicas.

---

## 4. Infraestructura Técnica & Aislamiento (Stack Altera)

Siguiendo la arquitectura robusta y probada de Altera en los proyectos previos (Dental, Fisio, Motor):

- **VPS dedicado (Contabo / Hetzner en Frankfurt / UE):** Entorno 100% aislado para Pizzería Ángela. Sus datos, pedidos y clientes no se comparten con ningún otro cliente.
- **Coolify como orquestador self-hosted:** Control total de contenedores Docker, despliegue continuo y mantenimiento sin cuotas de plataformas privativas.
- **Supabase Autoalojado (PostgreSQL + RLS + Auth + Storage):**
  - Almacena pedidos, productos de la carta, clientes, estados de cocina y reservas de mesas.
  - Coste de licencia Supabase: 0 € (Self-Hosted).
- **Zernio:** Pasarela oficial de integración para WhatsApp Business API e Instagram Messaging API.
- **ElevenLabs Conversational AI + OpenRouter:** Síntesis y reconocimiento de voz ultra-realista en castellano con latencia ultrabaja para telefonía.
- **Monitorización 24/7 (HetrixTools):** Supervisión continua del VPS y servicios para garantizar disponibilidad absoluta durante los servicios de cena.

---

## 5. El Gran Argumento Comercial: Subvención Junta de Castilla-La Mancha (Bono Crecimiento Pyme)

Este es el **catalizador de cierre indiscutible** para la reunión con los propietarios de Pizzería Ángela (y replicable en cualquier restaurante de Albacete como Vibra Burger):

### Ficha Técnica de la Subvención:
- **Programa:** Bono Crecimiento Pyme — Modalidad Transformación Digital & Inteligencia Artificial.
- **Organismo:** Junta de Comunidades de Castilla-La Mancha (Consejería de Economía, Empresas y Empleo).
- **Normativa:** Orden 116/2026 (DOCM 03/08/2026).
- **Código Trámite Sede Electrónica JCCM:** **1023976**.
- **Tipo de Procedimiento:** **Concesión directa / simplificada por orden de registro** (no concurrencia competitiva). Presupuesto dotado con 9.000.000 €.
- **Intensidad de la ayuda:** **80% a fondo perdido** de la inversión neta elegible (hasta un máximo de 12.000 €).

### La Ecuación Financiera Irresistible para el Cliente:
1. **Inversión total del proyecto (Fase 1 Suite 360º):** **4.000 €** (+ IVA deducible).
2. **Subvención neta JCCM (80% a fondo perdido):** **3.200 €**.
3. **Coste real inicial final asumido por el restaurante:** **800 € netos**.
4. **Mantenimiento Mensual Altera (Tarifa Plana Todo Integrado):** **200 € / mes (sin IVA)** (100% gasto deducible).
   - *Todo incluido sin parches de terceros:* Servidor VPS Cloud dedicado en Coolify 24/7, base de datos PostgreSQL en Supabase, Libro de Reservas y Mapa de Sala con Fianza Anti No-Show, Comandera Móvil Fullscreen (BYOD Camareros 0€ Hardware), Pantalla KDS de cocina con Stock en 1 clic, Bot de WhatsApp para pedidos y reservas, Recepcionista de Voz IA 24/7, Cobro de Cuenta en Mesa / TPV y Autopilot de Reseñas 5★ en Google.
   - *Comparativa demoledora frente al mercado fragmentado:* Contratar por separado **Restoo Premium (149 €/mes)** + **Last.app TPV/KDS (140 €/mes)** + **Bot de Voz IA Bookline (99 €/mes)** cuesta **~388 € / mes**. Con Altera_FOOD a **200 € / mes (sin IVA)** el restaurante ahorra **+188 € cada mes (+2.250 € al año)** teniendo todo integrado en una única plataforma propia.
5. **Costes Variables a Consumo Real (Facturados aparte directo por proveedor):**
   - **WhatsApp Business API (Meta Platforms):** Facturado a la tarjeta del cliente directamente en Meta Business Suite con conexión oficial a Meta Cloud API (sin márgenes ni markups de intermediarios BSP como Twilio o 360dialog, frente a los 0,088 €/SMS que cobran las plataformas tradicionales de reservas).
     - *Ventana de Servicio (Atención al cliente 24h):* **1.000 mensajes de servicio al mes GRATIS**; a partir del mensaje 1.001, tarificado al coste oficial de servicio de **0,0166 € por mensaje**.
     - *Plantillas de Utilidad (Avisos de Comanda / Estado en Cocina / Confirmación de Mesa / Fianza):* **0,0166 € por mensaje entregado (+34 España)**.
     - *Plantillas de Marketing (Reactivación en Días Flojos con Foto y Repetición en 1 Clic):* **0,0585 € por mensaje entregado (+34 España)**.
   - **Recepcionista de Voz IA Telefónica (ElevenLabs + Twilio/Zadarma):** Facturado por minuto hablado real (~**0,10 € / minuto**). Si un día no hay llamadas, coste 0€. El fin de semana en horas punta atiende 40 llamadas por ~4€ salvando más de 600€ en reservas y pedidos.
6. **Retorno de Inversión (ROI) en menos de 30 días:**
   - Una pizzería que facture 2.000 € al mes por Uber Eats paga ~600 € en comisiones solo en ese mes, más las mesas perdidas por plantones (No-Shows).
   - Con evitar un solo plantón de grupo el sábado noche (+120€) y pasar 25 pedidos de Uber al canal propio de WhatsApp (+150€), la cuota de 200€/mes queda pagada y multiplicada desde el primer mes.
7. **Diferenciación con el Kit Digital que ya tienen:**
   - La web actual de Tappens se acogió al Kit Digital estatal (solución básica de página web de 2023-2024).
   - El Bono Crecimiento Pyme de Castilla-La Mancha (2026) financia **herramientas de Inteligencia Artificial, automatización operativa, chatbots y CRM**, por lo que es 100% complementario y compatible.
8. **Cero burocracia para el hostelero:**
   - Al ser un contrato menor de 4.000 € (muy inferior al límite de 15.000 €), la normativa no exige presentar tres ofertas de proveedores distintos.
   - **Altera entrega la Memoria Técnica Oficial (Formulario III)** redactada al milímetro con cronograma, objetivos tecnológicos e impacto en la productividad del negocio, lista para presentar con firma digital.

---

## 6. Fases de Implantación de la Suite 360º (Fase 1 del Proyecto)

```
┌────────────────────────────────────────────────────────┐
│ ETAPA 1: PRESENTACIÓN AL CLIENTE & TRÁMITE JCCM (Sem 1)│
│ • Demo en vivo: Mapa de Sala, WhatsApp Bot, KDS y Voz  │
│ • Comparativa frente a Uber Eats + Last.app + Restoo   │
│ • Entrega de Formulario III cumplimentado + Presupuesto│
│ • Registro telemático en Sede Electrónica de la JCCM   │
└───────────────────────────┬────────────────────────────┘
                            │ (Efecto incentivador cubierto)
                            ▼
┌────────────────────────────────────────────────────────┐
│ ETAPA 2: SALA, RESERVAS & BOT DE WHATSAPP (Semanas 2-4)│
│ • Despliegue de VPS + Coolify + Supabase dedicado      │
│ • Mapa de Sala (Salón/Terraza), Doblaje Turnos y Fianza│
│ • Entrenamiento del bot de WhatsApp (pedidos y mesas)  │
│ • Pasarela Stripe (pre-pago pedidos + Pay-at-Table QR) │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ ETAPA 3: KDS COCINA, VOZ IA & RESEÑAS 5★ (Semanas 5-8) │
│ • Nueva landing web mobile-first ultrarrápida          │
│ • Puesta en marcha de Comandera KDS + Stock en 1 Clic  │
│ • Desvío inteligente a Recepcionista Voz IA ElevenLabs │
│ • Activación del Autopilot de Reseñas 5★ en Google     │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ ETAPA 4: JUSTIFICACIÓN DE LA AYUDA & SOPORTE (Mes 3-6) │
│ • Justificación técnica y económica ante la JCCM       │
│ • Cobro del 80% de la subvención por parte del cliente │
│ • Mantenimiento Todo Integrado (150 €/mes sin IVA)     │
└────────────────────────────────────────────────────────┘
```

---

## 7. Hoja de Ruta Modular: Módulos de Expansión para Fases 2 y 3

Una vez consolidada la **Fase 1** (desde que el cliente llama o escribe para reservar mesa o pedir comida hasta que paga la cuenta y deja reseña), la arquitectura de Altera_FOOD permite activar **5 módulos adicionales de gestión interna y redes sociales** en una segunda o tercera fase:

1. **📅 Sistema de Cuadrantes de Personal (Fase 2 · RRHH):**  
   Planificación visual de turnos de cocina, pizzeros/plancha y camareros de sala. Gestión de descansos semanales, vacaciones, cambios de turno entre empleados y alertas de cobertura según la previsión de reservas del fin de semana (conectable con el proyecto de gestión de turnos propio).
2. **⏱️ Sistema de Fichajes Digitales por Empleada (Fase 2 · Control Horario Legal):**  
   Aplicación integrada para que cada empleada fiche su entrada, pausas y salida desde su móvil o la tablet del local (con PIN o geolocalización), generando automáticamente los partes mensuales firmados para gestoría e Inspección de Trabajo.
3. **🧾 Sistema de Facturación Integrado & Verifactu (Fase 2/3 · Fiscal):**  
   Emisión de tickets de mesa, facturas simplificadas y facturas completas para comidas de empresa, arqueo y cierre de caja diario por turno, y cumplimiento con el reglamento antifraude Verifactu con exportación directa para contabilidad.
4. **📦 Sistema de Inventario y Escandallos para el Restaurante (Fase 3 · Stock & Food Cost):**  
   Descuento automático de materia prima en almacén por cada receta vendida (gramos de harina, mozzarella, bolas de carne smash, pan brioche, cajas de cartón), control de mermas, cálculo de rentabilidad exacta (*Food Cost*) por plato y alertas de pedido automático a proveedores.
5. **📸 Integración con Instagram para Programar Contenido (Fase 3 · Social Media Automation):**  
   Calendario visual y programador automático de Reels, Stories y publicaciones en Instagram conectado con Zernio, permitiendo dejar programado el contenido de toda la semana y convertir los comentarios o mensajes directos en reservas de mesa o pedidos de forma automática.

---

**Conclusión:**  
El brief de **Altera_FOOD 360º** ofrece una solución integral sin rival en el mercado: unifica lo mejor de la gestión de sala (mapa de mesas, doblaje de turnos, fianza anti-plantones, lista de espera y briefing), lo mejor de un **TPV/KDS moderno** (comandera móvil fullscreen 0€ hardware, stock en 1 clic y cobro de cuenta en mesa) y la **Inteligencia Artificial Conversacional** (Bot de WhatsApp + Recepcionista de Voz IA 24/7 + Autopilot de Reseñas 5★) por una tarifa plana de **200 € / mes (sin IVA) todo integrado**, financiada al **80% a fondo perdido (coste inicial neto de 800 € sobre 4.000 €)** gracias al Bono Crecimiento Pyme de Castilla-La Mancha.

