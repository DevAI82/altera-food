#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador automático del FORMULARIO III oficial + ANEXO LEGAL (Bono Crecimiento Pyme - Orden 116/2026)
para PIZZERÍA ÁNGELA IMAGINALIA (Albacete) con presupuesto de 3.000 € (80% subvencionado = 2.400 €).
"""

import os
import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generar_formulario_iii_angela():
    base_dir = r"g:\Mi unidad\Altera_food"
    template_path = r"g:\Mi unidad\AYUDAS IA\Normativa ayudas\1023976_35310.DOCX"
    output_path = os.path.join(base_dir, "Formulario_III_Pizzeria_Angela.docx")
    
    if not os.path.exists(template_path):
        print(f"Error: No se encontró la plantilla en {template_path}")
        return False

    doc = docx.Document(template_path)

    # Insertar logos en la cabecera del documento si existen
    logo_altera = r"g:\Mi unidad\AYUDAS IA\app\logo-altera-header.png"

    if doc.paragraphs:
        first_p = doc.paragraphs[0]
        p_logos = first_p.insert_paragraph_before()
        p_logos.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        if os.path.exists(logo_altera):
            r_alt = p_logos.add_run()
            r_alt.add_picture(logo_altera, width=Inches(1.6))
            p_logos.add_run("   ")

        r_info = p_logos.add_run("\nAltera — Inteligencia REAL aplicada a tu negocio\ncontacto@altera-es.com · Tel.: +34 624 93 90 23 · www.altera-es.com\n")
        r_info.font.size = Pt(8.5)
        r_info.font.color.rgb = RGBColor(0x64, 0x74, 0x8b)

    servicios = [
        (
            "Modalidad 4",
            "Recepcionista de Voz Telefónica con IA 24/7 y Agente Omnicanal de Pedidos (WhatsApp / Instagram Direct)",
            "Implantación y entrenamiento de un agente de IA generativa conversacional de voz humana ultrarrealista (ElevenLabs) integrado en la línea telefónica fija del restaurante (967 60 12 66) junto con un chatbot omnicanal de pedidos en WhatsApp Business e Instagram Direct (mediante pasarela Zernio y servidor privado Coolify/Supabase). El sistema atiende el 100% de llamadas durante horas punta de servicio de cenas, gestiona reservas de mesas de salón/terraza, responde consultas de alérgenos y opciones sin gluten, y tramita pedidos de pizzas para recogida en local con cobro instantáneo por Stripe (Apple Pay, Google Pay y tarjeta bancaria), erradicando las comisiones abusivas del 30% de agregadores externos.",
            1500.00
        ),
        (
            "Modalidad 4",
            "Sistema KDS Inteligente de Cocina en 4 Fases, Control Dinámico de Tiempos de Horno y CRM de Fidelización",
            "Despliegue de un sistema digital de gestión de comandas en cocina (KDS - Kitchen Display System) táctil estructurado en 4 fases operativas: Recepción de comanda, Pendiente de estirar y elaborar, Horno de piedra en cocción y Listo para entrega en mostrador. Incluye motor de cálculo dinámico de tiempos de recogida en función del volumen en curso (limitando a 12 pizzas/horneada para evitar retrasos), módulo de impresión térmica de tickets de 80mm y automatizaciones CRM para reactivar clientes inactivos los jueves y domingos mediante promociones directas por WhatsApp.",
            1500.00
        )
    ]

    total = sum(s[3] for s in servicios)
    subvencion_80 = total * 0.80
    aportacion_20 = total - subvencion_80

    p_text_map = {
        "A) Breve presentación de la empresa solicitante": (
            "La entidad solicitante PIZZERÍA ÁNGELA IMAGINALIA, con establecimiento hostelero ubicado en Albacete capital, "
            "desarrolla su actividad comercial en el sector de la restauración y comidas preparadas (CNAE 5610). "
            "El restaurante es un referente gastronómico de barrio en la zona Imaginalia, especializado en pizzas artesanales "
            "al horno de piedra, pastas, entrantes y servicio de comida para recoger en tienda (Takeaway) y consumo en local. "
            "Para consolidar su crecimiento, erradicar la saturación telefónica durante los picos de demanda del fin de semana, "
            "acabar con los errores en comandas de papel y prescindir de las comisiones abusivas (hasta un 30%) de plataformas intermediarias, "
            "la empresa requiere acometer un proceso integral de modernización digital incorporando inteligencia artificial en recepción y cocina."
        ),
        "B) Localización del centro de trabajo": (
            "El proyecto se ejecuta íntegramente en las instalaciones operativas de PIZZERÍA ÁNGELA "
            "situadas en Calle Simone de Beauvoir, 3, 02006 Albacete (Castilla-La Mancha)."
        ),
        "C) Sector al que pertenece la empresa": (
            "Sector Hostelería / Restaurantes y puestos de comidas (CNAE I5610). Actividad plenamente subvencionable "
            "dentro de la Modalidad 4 (Transformación Digital) conforme a las bases de la Orden 116/2026 de la JCCM."
        ),
        "D) Productos o servicios que ofrece la empresa actualmente": (
            "Pizzería Ángela ofrece pizzas tradicionales y especiales de masa artesanal horneadas a la piedra, "
            "opciones adaptadas y pizzas sin gluten, ensaladas, platos de pasta italiana, bebidas y postres artesanos, "
            "disponibles para consumo en mesas de salón comedor y terraza, así como servicio de encargo y recogida rápida en mostrador."
        ),
        "A) Definición de los objetivos de crecimiento": (
            "1) Atender el 100% de las llamadas y mensajes entrantes sin esperas ni tonos de comunicación ocupada, "
            "capturando más de 40 pedidos y reservas semanales que anteriormente se perdían en horas punta de cocina.\n"
            "2) Fomentar el canal directo de recogida en tienda con pago anticipado por Stripe/Apple Pay, recuperando entre 600 € y 1.200 € "
            "mensuales que antes se fugaban en comisiones de plataformas externas como Uber Eats o Glovo.\n"
            "3) Optimizar el ritmo de trabajo de los maestros pizzeros mediante pantalla KDS táctil con avisos automáticos al móvil del cliente "
            "cuando su pizza entra al horno y cuando está recién empaquetada.\n"
            "4) Disponer de una base de datos propia de clientes (CRM en Supabase) para reactivación periódica con ofertas exclusivas por WhatsApp."
        ),
        "-B) Justificación, en su caso, del carácter innovador": (
            "El carácter innovador radica en la implantación pionera en la hostelería de Albacete de un agente de voz con Inteligencia Artificial "
            "ultrarrealista (ElevenLabs) capaz de sostener una conversación natural en español, resolver dudas de alérgenos y procesar comandas "
            "telefónicas conectadas en tiempo real a una base de datos relacional y a un KDS de cocina inteligente con cálculo de capacidades de horneado. "
            "Todo ello bajo una arquitectura de soberanía digital con servidor VPS privado europeo gestionado por Coolify, eliminando la dependencia "
            "de software cerrado de terceros con tarifas mensuales crecientes."
        ),
        "C) Alineación de la actuación con la estrategia regional de especialización inteligente s3": (
            "La actuación se alinea de forma directa con la prioridad transversal 'Digitalización, modernización y adopción de tecnologías "
            "disruptivas e inteligencia artificial en el tejido de pymes y micropymes' de la Estrategia de Especialización Inteligente S3 de Castilla-La Mancha 2021-2027."
        ),
        "A) Nº total de actuaciones propuestas conforme al art.8": (
            f"Se proponen 2 actuaciones técnicas integradas en la Modalidad 4 (Transformación Digital), "
            f"por un importe total presupuestado de {total:,.2f} € sin IVA.\n"
            f"• Subvención solicitada a la JCCM (80% a fondo perdido): {subvencion_80:,.2f} €.\n"
            f"• Aportación neta asumida por el establecimiento (20%): {aportacion_20:,.2f} €.\n\n"
            "Conforme al artículo 9.4 de la Orden 116/2026 y al artículo 118 de la Ley 9/2017 de Contratos del Sector Público, "
            "al ser el importe total del contrato inferior al umbral legal de contrato menor de servicios (15.000 €), "
            "no resulta exigible la presentación de tres ofertas de diferentes proveedores, bastando el presupuesto pro-forma aportado por Altera."
        ),
        "C) Justificación de la necesidad de las actuaciones propuestas": (
            "Durante los servicios de cenas de viernes a domingo, el teléfono de la pizzería llega a sonar más de 70 veces por hora, "
            "coincidiendo con el momento de mayor concentración en horno y barra. Atender el teléfono interrumpe la producción y genera "
            "errores en las notas de papel térmico, mientras que no atenderlo supone la pérdida directa de clientes fieles hacia la competencia. "
            "La digitalización integral mediante agente de voz IA, canal de WhatsApp y pantalla KDS resuelve de raíz este cuello de botella productivo."
        ),
        "A) Duración de las actuaciones propuestas. Cronograma": (
            "Plazo de ejecución previsto: 3 meses desde la fecha del resguardo telemático de solicitud de la ayuda en la JCCM "
            "(muy inferior al plazo reglamentario máximo de 6 meses establecido en el art. 10.1 de la Orden 116/2026).\n"
            "• Mes 1 (Semanas 1–3): Despliegue de infraestructura cloud dedicada (VPS Coolify + PostgreSQL/Supabase), configuración de pasarela "
            "de pagos Stripe y diseño de los árboles conversacionales de WhatsApp/Instagram en Zernio.\n"
            "• Mes 2 (Semanas 4–8): Entrenamiento del modelo de voz conversacional de ElevenLabs para recepción telefónica (desvío al fijo 967 60 12 66), "
            "desarrollo del software KDS táctil con 4 fases y pruebas de estrés con comanda térmica de 80mm.\n"
            "• Mes 3 (Semanas 9–12): Instalación de tablet/pantalla táctil en cocina, formación práctica del equipo de sala y obrador, "
            "lanzamiento en producción, acta de entrega técnica y elaboración de la justificación técnica final (Formulario V)."
        ),
        "B) Resultados esperados en la empresa y temporalización": (
            "Resultados cuantificables a los 6 meses de la implantación:\n"
            "- Cero llamadas perdidas en horario de servicio de cocina (100% de consultas y pedidos atendidos).\n"
            "- Aumento directo del 25% en pedidos de comida para llevar recogidos en mostrador gracias al QR de caja y al bot de WhatsApp.\n"
            "- Reducción de 8 minutos en el tiempo medio de entrega de pedidos gracias a la pantalla KDS sincronizada con el horno.\n"
            "- Retorno completo de la inversión en menos de 45 días mediante el ahorro de comisiones a plataformas intermediarias."
        )
    }

    # Recorrer párrafos e insertar los textos
    for p in list(doc.paragraphs):
        for key, text_content in p_text_map.items():
            if key in p.text:
                p_after = p._p.getnext()
                if p_after is not None:
                    target_p = doc.add_paragraph(text_content)
                    p._p.addnext(target_p._p)
                    target_p.style = doc.styles['Normal']
                    for r in target_p.runs:
                        r.font.size = Pt(10)
                        r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

    # Rellenar la tabla de actuaciones
    if doc.tables:
        tbl = doc.tables[0]
        for idx, (mod, act_tipo, act_desc, imp) in enumerate(servicios, start=1):
            if idx < len(tbl.rows) - 1:
                row = tbl.rows[idx]
                row.cells[0].text = mod
                row.cells[1].text = act_tipo
                row.cells[2].text = act_desc
                row.cells[3].text = "Altera Soluciones Tecnológicas\n(www.altera-es.com)"
                row.cells[4].text = "Presupuesto Pro-Forma ALT-2026-FOOD01"
                row.cells[5].text = f"{imp:,.2f} €"
                row.cells[6].text = "No aplica (Contrato menor < 15.000 € s/ Art. 9.4 Orden 116/2026)"

        # Fila TOTAL (última fila)
        last_row = tbl.rows[-1]
        if len(last_row.cells) >= 6:
            last_row.cells[5].text = f"{total:,.2f} €"

    # Salto de página y Anexo de Tramitación
    doc.add_page_break()
    p_anexo = doc.add_paragraph()
    r_anexo = p_anexo.add_run("ANEXO INFORMATIVO: GUÍA DE TRAMITACIÓN, DOCUMENTACIÓN Y MARCO LEGAL")
    r_anexo.bold = True
    r_anexo.font.size = Pt(13)
    r_anexo.font.color.rgb = RGBColor(0xDC, 0x26, 0x26)

    p_tram = doc.add_paragraph()
    p_tram.add_run("A) Procedimiento de Tramitación Integral (Llave en mano por Altera):\n").bold = True
    p_tram.add_run(
        "1. Presentación telemática oficial (Coste 0 €): Altera redacta íntegramente la Memoria Oficial (Formulario III) "
        "y acompaña a la pizzería en la presentación en la sede de la JCCM con certificado digital. Queda fijado el número de registro "
        "y asegurada la reserva de fondos de los 9.000.000 € de la convocatoria regional.\n"
        "2. Inicio inmediato del proyecto: Conforme al art. 10.2 de la Orden 116/2026, con el resguardo telemático de entrada ya se "
        "puede comenzar a ejecutar el proyecto legalmente sin esperar meses a la resolución administrativa.\n"
        f"3. Facturación e implantación: Altera despliega todas las soluciones y emite factura por 3.000,00 € + IVA. "
        "La pizzería abona la factura por transferencia bancaria (el IVA es deducible al 100% en la liquidación trimestral).\n"
        f"4. Reembolso directo de la Junta: Altera elabora la memoria final de justificación técnica (Formulario V). "
        f"La Junta transfiere directamente a la cuenta corriente del cliente el 80% ({subvencion_80:,.2f} €). "
        f"El coste neto definitivo asumido por Pizzería Ángela es de únicamente {aportacion_20:,.2f} €.\n"
    )

    p_docs = doc.add_paragraph()
    p_docs.add_run("B) Documentación Necesaria de la Pizzería Solicitante:\n").bold = True
    p_docs.add_run(
        "• NIF/DNI del titular o representante legal del establecimiento.\n"
        "• Certificado digital activo para firma telemática en sede electrónica de la JCCM.\n"
        "• Certificados tributarios de estar al corriente con AEAT, Seguridad Social y Tributos de CLM (o autorización de consulta telemática).\n"
        "• Certificado bancario acreditativo de la titularidad de la cuenta corriente (IBAN) para el abono de los 2.400 € de la subvención.\n"
    )

    p_ley = doc.add_paragraph()
    p_ley.add_run("C) Marco Normativo y Referencias Oficiales de la Convocatoria:\n").bold = True
    p_ley.add_run(
        "• Bases Reguladoras: Orden 116/2026, de 29 de julio (DOCM nº 149 de 03/08/2026).\n"
        "• Código SIACI oficial del trámite en la Junta de CLM: 1023976.\n"
        "• Procedimiento: Concesión directa y simplificada (NO competitiva) por riguroso orden de registro de entrada.\n"
        "• Enlace oficial de descarga del DOCM: https://docm.castillalamancha.es/portaldocm/descargarArchivo.do?ruta=2026/08/03/pdf/2026_5787.pdf&tipo=rutaDocm\n"
        "• Enlace oficial al trámite en Sede Electrónica JCCM: https://www.jccm.es/tramites/1023976\n"
    )

    doc.save(output_path)
    print(f"Documento oficial Formulario III generado con éxito en:\n{output_path}")
    return True

if __name__ == "__main__":
    generar_formulario_iii_angela()
