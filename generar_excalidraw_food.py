#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de diagrama de arquitectura Excalidraw para ALTERA FOOD
(Pizzería Ángela & Vibra Burger Albacete).
"""

import json
import os

def crear_rectangulo(id_elem, x, y, w, h, stroke="#0284c7", bg="#f0f9ff", stroke_w=2):
    return {
        "id": id_elem,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": "solid",
        "strokeWidth": stroke_w,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False
    }

def crear_texto(id_elem, x, y, w, h, texto, stroke="#0f172a", font_size=13, align="center"):
    return {
        "id": id_elem,
        "type": "text",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "text": texto,
        "fontSize": font_size,
        "fontFamily": 1,
        "textAlign": align,
        "verticalAlign": "top",
        "containerId": None,
        "originalText": texto,
        "lineHeight": 1.25
    }

def crear_flecha(id_elem, start_x, start_y, end_x, end_y, stroke="#64748b"):
    dx = end_x - start_x
    dy = end_y - start_y
    return {
        "id": id_elem,
        "type": "arrow",
        "x": start_x,
        "y": start_y,
        "width": abs(dx),
        "height": abs(dy),
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "boundElements": [],
        "updated": 1,
        "link": None,
        "locked": False,
        "points": [
            [0, 0],
            [dx, dy]
        ],
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow"
    }

def generar_excalidraw():
    elements = []

    # 1. Cabecera Principal
    elements.append(crear_texto(
        "title-main", 60, 25, 1200, 35,
        "ARQUITECTURA TECNOLÓGICA Y SISTEMA OPERATIVO — ALTERA FOOD",
        stroke="#0f172a", font_size=24, align="center"
    ))
    elements.append(crear_texto(
        "title-sub", 60, 65, 1200, 25,
        "Telefonía IA ElevenLabs (Ángela & Dino) + Zernio WhatsApp + KDS 4 Fases + Stripe + Supabase en VPS Coolify",
        stroke="#e11d48", font_size=15, align="center"
    ))

    # Definición de las 4 columnas
    cols = [
        {
            "id": "c1",
            "title": "1. CANALES DE CLIENTES",
            "x": 60, "stroke": "#0284c7", "bg": "#f0f9ff", "header_stroke": "#0369a1",
            "cards": [
                ("📞 Telefonía Entrante 24/7\nLlamadas a restaurante atendidas al instante\nGestión de reservas y pedidos takeaway\nSin líneas ocupadas ni esperas", "#0284c7"),
                ("💬 WhatsApp Bot (Zernio)\nConsulta interactiva de carta y alérgenos\nPedidos para recoger con confirmación\nRe-order en 2 clics para clientes fieles", "#0284c7"),
                ("🌐 Web App / Carta Digital\nPedido directo sin comisiones (0% vs 30% Glovo)\nDiseño mobile-first ultrarrápido\nSincronizada con cocina en tiempo real", "#0284c7"),
                ("💳 Stripe Checkout & Depósitos\nPago seguro con Apple Pay, Google Pay y tarjeta\nCobro anticipado takeaway antipedidos fantasma\nFianza antino-show para mesas numerosas", "#0284c7")
            ]
        },
        {
            "id": "c2",
            "title": "2. MOTOR IA & ORQUESTADOR (COOLIFY VPS)",
            "x": 360, "stroke": "#7c3aed", "bg": "#f5f3ff", "header_stroke": "#6d28d9",
            "cards": [
                ("🎙️ ElevenLabs Conversational Voice\nVoces ultranaturales en castellano peninsular\nÁngela (Pizzería) y Dino (Vibra Burger)\nLatencia ultra-baja (<700ms) y streaming", "#7c3aed"),
                ("⚡ Altera Food API Hub\nOrquestador central en VPS Hetzner/Contabo\nDesplegado con Coolify Open Source\nGestión de comandas, catálogo y stock", "#7c3aed"),
                ("⏱️ Estimador Dinámico de Cocina\nCálculo automático de tiempos de recogida\nAjuste dinámico según saturación de hornos\nNotifica al cliente tiempo exacto (ej. 25 min)", "#7c3aed"),
                ("🤖 Zernio Gateway & Webhooks\nConexión oficial con WhatsApp Cloud API\nEnvío de recibos térmicos en PDF y alertas\nAutomatización de confirmaciones inmediatas", "#7c3aed")
            ]
        },
        {
            "id": "c3",
            "title": "3. KDS & OPERACIONES EN RESTAURANTE",
            "x": 660, "stroke": "#d97706", "bg": "#fffbeb", "header_stroke": "#b45309",
            "cards": [
                ("📥 Fase 1: Recepción & Cola\nEntrada en directo de llamadas y WhatsApp\nNúmero de comanda y hora estimada\nAlerta de alérgenos (sin gluten, lácteos)", "#d97706"),
                ("👨‍🍳 Fase 2: En Preparación\nPantalla táctil para pizzaiolos / cocineros\nDetalle de ingredientes y personalizaciones\nAsignación por tiempos de cocción", "#d97706"),
                ("🔥 Fase 3: Horno / Plancha\nControl de aforo: máx 12 pizzas / 15 smash\nCronómetro visual por bandeja\nAlerta sonora al completar cocción", "#d97706"),
                ("🛍️ Fase 4: Listo & Impresión 80mm\nAviso automático por WhatsApp: '¡Listo para recoger!'\nTicket térmico ESC/POS con desglose IVA 10%\nReducción del 100% de errores en sala", "#d97706")
            ]
        },
        {
            "id": "c4",
            "title": "4. BASE DE DATOS & MARKETING CRM",
            "x": 960, "stroke": "#16a34a", "bg": "#f0fdf4", "header_stroke": "#15803d",
            "cards": [
                ("🗄️ Supabase PostgreSQL\nBase de datos relacional de pedidos y clientes\nControl de históricos, ticket medio y frecuencia\nCumplimiento RGPD y soberanía de datos pyme", "#16a34a"),
                ("📈 CRM WhatsApp & Fidelización\nCampañas segmentadas jueves/viernes tarde\nTasa de apertura > 92% (vs 18% email)\nReactivación de clientes sin consumo > 30 días", "#16a34a"),
                ("💼 Subvención JCCM Bono Crecimiento\nTotal Proyecto: 3.000 €\nSubvención 80%: 2.400 € a fondo perdido\nInversión Neta Cliente: sólo 600 € (+IVA)", "#16a34a"),
                ("🔄 Mantenimiento Continuo Altera\nRetainer 99 € / mes (soporte, backups, mejoras)\nConsumos ElevenLabs y WhatsApp al coste real\nSin ataduras ni comisiones por comanda", "#16a34a")
            ]
        }
    ]

    card_h = 100
    card_spacing = 15
    start_y = 175

    for c_idx, col in enumerate(cols):
        total_h = 4 * card_h + 3 * card_spacing + 70
        # Fondo columna
        elements.append(crear_rectangulo(
            f"col-{col['id']}", col["x"], 115, 270, total_h,
            stroke=col["stroke"], bg=col["bg"], stroke_w=2
        ))
        # Cabecera columna
        elements.append(crear_texto(
            f"t-head-{col['id']}", col["x"] + 10, 130, 250, 30,
            col["title"], stroke=col["header_stroke"], font_size=15, align="center"
        ))

        # Tarjetas dentro de la columna
        for i, (texto, st_col) in enumerate(col["cards"]):
            cy = start_y + i * (card_h + card_spacing)
            elements.append(crear_rectangulo(
                f"card-{col['id']}-{i}", col["x"] + 15, cy, 240, card_h,
                stroke=st_col, bg="#ffffff", stroke_w=1.5
            ))
            elements.append(crear_texto(
                f"t-card-{col['id']}-{i}", col["x"] + 20, cy + 8, 230, card_h - 16,
                texto, stroke="#0f172a", font_size=11, align="center"
            ))

    # Flechas conectivas entre fases (Columnas 1 -> 2 -> 3 -> 4)
    arrow_y_positions = [225, 340, 455, 570]
    for y_pos in arrow_y_positions:
        # Col 1 a Col 2
        elements.append(crear_flecha(f"arr-1-2-{y_pos}", 330, y_pos, 360, y_pos, stroke="#64748b"))
        # Col 2 a Col 3
        elements.append(crear_flecha(f"arr-2-3-{y_pos}", 630, y_pos, 660, y_pos, stroke="#64748b"))
        # Col 3 a Col 4
        elements.append(crear_flecha(f"arr-3-4-{y_pos}", 930, y_pos, 960, y_pos, stroke="#64748b"))

    # Banner inferior de impacto y valor diferencial
    banner_y = start_y + 4 * card_h + 3 * card_spacing + 35
    elements.append(crear_rectangulo(
        "banner-bottom", 60, banner_y, 1170, 75,
        stroke="#0f172a", bg="#0f172a", stroke_w=2
    ))
    elements.append(crear_texto(
        "t-banner-bottom", 70, banner_y + 12, 1150, 50,
        "✨ IMPACTO DIRECTO: Ahorro de un 30% en comisiones de plataformas (Glovo/Uber), 0 llamadas perdidas en hora punta de fin de semana,\n"
        "sincronización instantánea de comandas con cocina y fidelización automática por WhatsApp vía Altera Food.",
        stroke="#38bdf8", font_size=13, align="center"
    ))

    data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "gridSize": None
        },
        "files": {}
    }

    out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arquitectura-altera-food.excalidraw")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Diagrama Excalidraw generado con éxito: {out_file} ({len(elements)} elementos)")

if __name__ == "__main__":
    generar_excalidraw()
