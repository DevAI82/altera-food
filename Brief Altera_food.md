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

### Pilar 6: Panel TPV Comandera de Cocina & CRM Gastronómico Propio
- **Pantalla KDS (Kitchen Display System) para cocina:** Vista tipo Kanban en tablet de cocina con tarjetas de pedidos en curso, agrupados por hora de entrega o recogida:
  - *Columna 1: Nuevos Pagados (Pendientes de horno)*.
  - *Columna 2: En Elaboración / En Horno*.
  - *Columna 3: Listos para Recoger*.
  - *Columna 4: Entregados*.
- **Base de datos propia y marketing de fidelización:** Altera_FOOD almacena en Supabase el historial de pedidos de cada cliente. Permite lanzar automatizaciones de reactivación autorizadas:
  - *"Hola Carlos, hace 2 semanas que no disfrutas de una pizza en horno de piedra. Este jueves tienes un postre casero de regalo con tu pedido"*.
  - Felicitación de cumpleaños automática con código promocional.

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
1. **Inversión total del proyecto:** **3.000 €** (+ IVA deducible).
2. **Subvención neta JCCM (80% a fondo perdido):** **2.400 €**.
3. **Coste real inicial final asumido por la pizzería:** **600 € netos**.
4. **Mantenimiento Mensual Altera (Tarifa Plana Base):** **99 € / mes** (100% gasto deducible).
   - *La cifra mágica:* Rompe la barrera psicológica de los 100€/mes.
   - *Qué incluye:* Servidor VPS Cloud dedicado en Coolify 24/7 (backups, monitorización, alta disponibilidad), base de datos PostgreSQL en Supabase, pantalla KDS de cocina, orquestación del bot de WhatsApp para pedidos ilimitados y soporte técnico continuo con cambios de carta en Albacete.
   - *Comparativa directa con Last.app (140-180€/mes):* El cliente ahorra más de **600 € al año en software** desde el primer mes, con el 100% de la propiedad tecnológica.
5. **Costes Variables a Consumo Real (Facturados aparte directo por proveedor):**
   - **WhatsApp Business API (Meta Platforms):** Facturado a la tarjeta del cliente en Meta Business Suite.
     - *Atención al cliente (ventana 24h):* **0,00 € (GRATIS)**.
     - *Plantillas de Utilidad (Avisos de Comanda):* ~**0,034 € por mensaje**.
     - *Plantillas de Marketing (Reactivación de Clientes):* ~**0,055 € - 0,060 € por mensaje entregado en España (+34)**. (Ej. 400 clientes = 22€ de coste para llenar el restaurante un jueves).
   - **Recepcionista de Voz IA Telefónica (ElevenLabs + Twilio/Zadarma):** Facturado por minuto hablado real (~**0,10 € / minuto**). Si un día no hay llamadas, coste 0€. El fin de semana en horas punta atiende 40 llamadas por ~4€ salvando 500€ en pedidos sin necesidad de contratar personal extra solo para descolgar el teléfono.
6. **Retorno de Inversión (ROI) en menos de 30 días:**
   - Una pizzería que facture 2.000 € al mes por Uber Eats paga ~600 € en comisiones solo en ese mes.
   - Con que solo **30 pizzas al mes** (1 al día) se pidan por WhatsApp para recoger en lugar de por Uber, se ahorran ~120 € en comisiones, cubriendo íntegramente la cuota mensual de Altera desde el primer mes.
7. **Diferenciación con el Kit Digital que ya tienen:**
   - La web actual de Tappens se acogió al Kit Digital estatal (solución básica de página web de 2023-2024).
   - El Bono Crecimiento Pyme de Castilla-La Mancha (2026) financia **herramientas de Inteligencia Artificial, automatización operativa, chatbots y CRM**, por lo que es 100% complementario y compatible.
8. **Cero burocracia para el hostelero:**
   - Al ser un contrato menor de 3.000 € (inferior al límite de 15.000 €), la normativa no exige presentar tres ofertas de proveedores distintos.
   - **Altera entrega la Memoria Técnica Oficial (Formulario III)** redactada al milímetro con cronograma, objetivos tecnológicos e impacto en la productividad del negocio, lista para presentar con firma digital.

---

## 6. Fases de Ejecución del Proyecto Altera_FOOD

```
┌────────────────────────────────────────────────────────┐
│ FASE 1: PRESENTACIÓN AL CLIENTE & TRÁMITE JCCM (Sem 1) │
│ • Demostración en vivo del bot de WhatsApp para pizzas │
│ • Presentación de la comparativa de ahorro frente a Uber│
│ • Entrega de Formulario III cumplimentado + Presupuesto│
│ • Registro telemático en Sede Electrónica de la JCCM   │
└───────────────────────────┬────────────────────────────┘
                            │ (Efecto incentivador cubierto)
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 2: INFRAESTRUCTURA & BOT DE WHATSAPP (Semanas 2-4)│
│ • Despliegue de VPS + Coolify + Supabase para Pizzería │
│ • Digitalización de la carta completa en base de datos │
│ • Entrenamiento del bot de WhatsApp para tomar pedidos │
│ • Conexión de Stripe para cobro online de comandas     │
│ • Configuración de Zernio para WhatsApp e Instagram    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 3: REDISEÑO WEB, VOZ IA & COMANDERA (Semanas 5-8) │
│ • Nueva landing web mobile-first ultrarrápida          │
│ • Puesta en marcha de la Comandera KDS para cocina     │
│ • Desvío de llamadas y Recepcionista de Voz ElevenLabs │
│ • Campaña de lanzamiento por código QR en cajas de pizza│
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ FASE 4: JUSTIFICACIÓN DE LA AYUDA & SOPORTE (Mes 3-6)  │
│ • Justificación técnica y económica ante la JCCM       │
│ • Cobro del 80% de la subvención por parte del cliente │
│ • Mantenimiento preventivo, backups y optimización     │
└────────────────────────────────────────────────────────┘
```

---

## 7. Estrategia Comercial de Entrada & Puntos Clave para la Reunión

1. **El impacto del "Coste 600 €" con la ayuda de CLM:**  
   Abrir la reunión explicando que Castilla-La Mancha ha publicado la Orden 116/2026 que financia el 80% de la implantación de Inteligencia Artificial para pymes hosteleras, y que Altera se encarga de todo el papeleo (Formulario III).
2. **El anzuelo de la "Prueba de WhatsApp en directo":**  
   Llevar al móvil del cliente una demo interactiva donde el propietario pueda enviar un WhatsApp pidiendo *"Una pizza cuatro quesos con jamón dulce para recoger a las 21:30"* y recibir en segundos la confirmación con el link de pago simulado.
3. **El dolor de Uber Eats vs. Canal Propio:**  
   Preguntar directamente: *"¿Cuánto os retiene Uber al mes en comisiones?"*. Poner la cifra sobre papel y demostrarles que ese dinero se lo están regalando a una multinacional cuando sus clientes viven a menos de 500 metros en el barrio de Imaginalia.
4. **La "Campaña del QR en la caja de pizza":**  
   Proponer una estrategia de transición sencilla: colocar una pegatina en cada caja de pizza que salga por Uber o teléfono que diga: *"Pide tu próxima pizza directamente por nuestro WhatsApp oficial y ahórrate el 10% de por vida [Código QR directo a WhatsApp]"*. Esto migra a los clientes cautivos de Uber al canal propio sin coste publicitario.
5. **Replicabilidad en otros negocios gastronómicos (Vibra Burger y otros):**  
   Este mismo brief y estructura técnica sirve para captar locales como Vibra Burger u otros restaurantes de Albacete, atacando la sustitución de cuotas caras de Last.app o la ausencia de pedidos por WhatsApp y recepción con Voz IA.

---

**Conclusión:**  
El brief de **Altera_FOOD** transforma una pizzería tradicional limitada por el teléfono fijo y dependiente del 30% de comisiones de Uber en un restaurante digitalizado de vanguardia con bot de pedidos 24/7, cobros automatizados por Stripe, recepcionista por voz IA y comandera propia, apalancado en el **Bono Crecimiento Pyme de Castilla-La Mancha (80% a fondo perdido: 3.000 € de proyecto por solo 600 € de coste neto real)**.
